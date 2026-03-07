# configuration database. This is just a python dictionary loaded on initialization.

config_db = {}
config_db["john_tan"] = {
    "name": "John Tan",
    "age": 65,
    "living_situation": "living with wife, emergency contact is wife",
    "emergency_contact_no": "+65 1234 5678",
    "emergency_contact_name": "Mrs. Emily Tan",
    "home_address": "Lost House, 55 Newton Rd, Singapore 307987",
    "preferred_language": "English",
    "get_me_home_lbl": "Get Me Home",
    "get_me_home_enabled": True,
    "get_me_home_template": "Please call me a Grab car. I am at address: 1010 Dover Rd, Singapore 139658 going to HOME_ADDRESS. Include  the pickup point (not the pickup address) and destination in your response. Respond in PREFERRED_LANGUAGE.",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
}

def update_template(user_info: dict) -> str:
    tmpl = user_info['get_me_home_template']
    tmpl = tmpl.replace('HOME_ADDRESS', user_info['home_address'])
    tmpl = tmpl.replace('PREFERRED_LANGUAGE', user_info['preferred_language'])
    return tmpl