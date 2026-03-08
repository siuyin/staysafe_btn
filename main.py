# This is a fastAPI app.
# The main endpoints are "/" to provide static html, css and javascript.
# and /ws/userId/sessionId which is the main conduit to ADK's bidirectional API.

import asyncio

from dotenv import load_dotenv
from pathlib import Path

from datastar_py.fastapi import DatastarResponse, ServerSentEventGenerator as sse
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from google.adk.agents.live_request_queue import LiveRequestQueue
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from datetime import datetime

from config_db import config_db, update_template
from sensors_simulation import sensors_report_db

from websocket_funcs import (
    audio_run_config,
    websocket_to_liverequestqueue,
    run_live_to_websocket,
)

# Load environment variables from .env file BEFORE importing agent
load_dotenv(Path(__file__).parent / ".env")

# Import agent after loading environment variables
# pylint: disable=wrong-import-position
from google_search_agent.agent import agent  # noqa: E402

APP_NAME = "audio_output"
app = FastAPI()

# Mount static files
# static_dir = Path(__file__).parent / "static"
# app.mount("/static", StaticFiles(directory=static_dir), name="static")

session_service = InMemorySessionService()
runner = Runner(app_name=APP_NAME, agent=agent, session_service=session_service)


async def patch_response_div(prompt):
    yield sse.patch_elements(f"""<div id="response">{prompt}</div>""")


@app.websocket("/ws/{user_id}/{session_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: str,
    session_id: str,
    proactivity: bool = False,
    affective_dialog: bool = False,
) -> None:
    """WebSocket endpoint for bidirectional streaming with ADK.

    Args:
        websocket: The WebSocket connection
        user_id: User identifier
        session_id: Session identifier
        proactivity: Enable proactive audio (native audio models only)
        affective_dialog: Enable affective dialog (native audio models only)
    """
    await websocket.accept()
    print(f"Connection accepted: affective dialog: {affective_dialog}")
    run_config = audio_run_config(proactivity, affective_dialog)

    # Get or create session (handles both new sessions and reconnections)
    session = await session_service.get_session(
        app_name=APP_NAME, user_id=user_id, session_id=session_id
    )
    if not session:
        await session_service.create_session(
            app_name=APP_NAME, user_id=user_id, session_id=session_id
        )

    live_request_queue = LiveRequestQueue()

    t1 = asyncio.create_task(
        websocket_to_liverequestqueue(websocket, live_request_queue)
    )
    t2 = asyncio.create_task(
        run_live_to_websocket(
            websocket, runner, run_config, user_id, session_id, live_request_queue
        )
    )
    try:
        done, pending = await asyncio.wait(
            [t1, t2], return_when=asyncio.FIRST_COMPLETED
        )
        for task in pending:
            task.cancel()
    except WebSocketDisconnect:
        print("WebSocket Disconnected")
    except Exception as e:
        print(f"Unexpected error in streaming tasks: {e}")
    finally:
        live_request_queue.close()


async def getConfig(user_id: str):
    if user_id not in config_db:
        yield sse.patch_elements(
            f"""<div id="{user_id}_config">{user_id} not found</div>"""
        )
        print(f"{user_id} not found")
        
    config = config_db[user_id]

    display_keys = ["name", "age", "living_situation", "emergency_contact_name", "emergency_contact_no", "home_address", "preferred_language", "blood_type"]
    rows = "".join(f"<tr><td><b>{k}</b></td><td>{config[k]}</td></tr>" for k in display_keys if k in config)
    
    yield sse.patch_elements(
        f"""<div id="{user_id}_config"><table style="border-collapse:collapse;"><tbody>{rows}</tbody></table></div>"""
    )
    
    button_labels = ["get_me_home", "medical_emergency", "no_motion_detected", "continuous_charging", "continuous_discharging"]
    
    for label in button_labels:
        tmpl = update_template(config, label)
        if label == "get_me_home":
            yield sse.patch_elements(f"""
                                     <button id="get_me_home_btn" class="action" data-on:click="sendMessage('{tmpl}')">{config['get_me_home_label']}</button>
                             """)
        if label == "medical_emergency":
            yield sse.patch_elements(f"""
                                     <button id="medical_emergency_btn" class="action_emergency" data-on:click="sendMessage('{tmpl}')">{config['medical_emergency_label']}</button>
                             """)
        if label == "no_motion_detected":
            yield sse.patch_elements(f"""
                                     <button id="no_motion_detected_btn" data-on:click="sendMessage('{tmpl}')">{config['no_motion_detected_label']}</button>
                             """)
        if label == "continuous_charging":
            yield sse.patch_elements(f"""
                                     <button id="continuous_charging_btn" data-on:click="sendMessage('{tmpl}')">{config['continuous_charging_label']}</button>
                             """)
        if label == "continuous_discharging":
            yield sse.patch_elements(f"""
                                     <button id="continuous_discharging_btn" data-on:click="sendMessage('{tmpl}')">{config['continuous_discharging_label']}</button>
                             """)
            
        print(tmpl)
        print(f"configuration for {user_id}: {config}")


@app.get("/config/{user_id}", response_class=StreamingResponse)
async def show_config(user_id: str):
    return DatastarResponse(getConfig(user_id))


async def sensors_simulation(report_id: str):
    report = sensors_report_db[report_id]
    last_key = f"last_{report_id}_timestamp"
    report[last_key] = report["current_timestamp"]
    report["current_timestamp"] = datetime.now()

    current = report["current_timestamp"]
    last = report[last_key]
    current_str = current.strftime("%Y-%m-%d %H:%M:%S")

    if last:
        last_str = last.strftime("%Y-%m-%d %H:%M:%S")
        interval_str = f"{int((current - last).total_seconds())}s"
    else:
        last_str = "-"
        interval_str = "-"

    yield sse.patch_elements(f"""<div id="{report_id}_report">
        current: {current_str}<br>
        last: {last_str}<br>
        interval: {interval_str}
    </div>""")


@app.post("/sensors/{report_id}")
async def show_sensors_simulation_report(report_id: str):
    return DatastarResponse(sensors_simulation(report_id))


static_dir = Path(__file__).parent / "static"
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
