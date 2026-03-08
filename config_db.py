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
    "get_me_home_label": "Get Me Home",
    "get_me_home_enabled": True,
    "get_me_home_template": "Please call me a Grab car. I am at address: 1010 Dover Rd, Singapore 139658 going to HOME_ADDRESS. Include the pickup point (not the pickup address) and destination in your response. Respond in PREFERRED_LANGUAGE.",
    "medical_emergency_label": "Ambulance",
    "medical_emergency_enable": True,
    "medical_emergency_template": "Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me.",
    "blood_type": "B+",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
    "no_motion_detected_label": "No Motion Detected",
    "no_motion_detected_enabled": True,
    "no_motion_detected_template": "Your phone has reported no motion for the last 12 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [no motion detected for 12 hours] in your response.",
    "continuous_charging_label": "Continuous Charging",
    "continuous_charging_enabled": True,
    "continuous_charging_template": "Your phone has reported continuous charging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous charging detected for 18 hours] in your response.",
    "continuous_discharging_label": "Continuous Discharging",
    "continuous_discharging_enabled": True,
    "continuous_discharging_template": "Your phone has reported continuous discharging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous discharging detected for 12 hours] in your response."
}

config_db["manikam"] = {
    "name": "Manikam",
    "age": 75,
    "living_situation": "Has mild dementia, lives alone, office-hours social worker contact Sofia",
    "emergency_contact_no": "+65 0873 3452",
    "emergency_contact_name": "Sofia (office hour only)",
    "home_address": "15 South Buona Vista Rd, Singapore 118146",
    "preferred_language": "Tamil",
    "get_me_home_label": "வீடு",
    "get_me_home_enabled": True,
    "get_me_home_template": "Please call me a Grab car. I am at address: 11 Eunos Rd 8, Singapore 408601 going to HOME_ADDRESS. Include  the pickup point (not the pickup address) and destination in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "medical_emergency_label": "அவசர ஊர்தி",
    "medical_emergency_enable": True,
    "medical_emergency_template": "Call Ambulance on Phone number 995 let them know my current location at 910 Upper Thomson Rd, Singapore 787112 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "blood_type": "A+",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
    "no_motion_detected_label": "No Motion Detected",
    "no_motion_detected_enabled": True,
    "no_motion_detected_template": "Your phone has reported no motion for the last 12 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [no motion detected for 12 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "continuous_charging_label": "Continuous Charging",
    "continuous_charging_enabled": True,
    "continuous_charging_template": "Your phone has reported continuous charging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous charging detected for 18 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "continuous_discharging_label": "Continuous Discharging",
    "continuous_discharging_enabled": True,
    "continuous_discharging_template": "Your phone has reported continuous discharging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous discharging detected for 12 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English."
}

config_db["hafiz_salleh"] = {
    "name": "Hafiz Salleh",
    "age": 11,
    "living_situation": "Goes to Special Needs School, both parents working, no social worker",
    "emergency_contact_no": "+65 3243 6544,+65 0982 1239",
    "emergency_contact_name": "Abu Salleh and Monica",
    "home_address": "88 Geylang Bahru, Singapore 339696",
    "preferred_language": "Malay",
    "get_me_home_label": "Pulang Rumah",
    "get_me_home_enabled": True,
    "get_me_home_template": "I am an 11 year old special needs student and i am lost. Please call my emergency contacts: EMERGENCY_CONTACT_NAME their phone numbers are EMERGENCY_CONTACT_NO so they can pick me up. I am at address: 11 Eunos Rd 8, Singapore 408601 going to HOME_ADDRESS. Be sure to inlcude the parents reply in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "medical_emergency_label": "Ambulans",
    "medical_emergency_enable": True,
    "medical_emergency_template": "Call Ambulance on Phone number 995 let them know my current location at 80 Mandai Lake Rd, Mandai Wildlife Reserve, Singapore 729826 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contacts: EMERGENCY_CONTACT_NAME and their numbers: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "blood_type": "O+",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
    "no_motion_detected_label": "No Motion Detected",
    "no_motion_detected_enabled": True,
    "no_motion_detected_template": "Your phone has reported no motion for the last 12 hours, Please Call Ambulance on Phone number 995 let them know my current location at 80 Mandai Lake Rd, Mandai Wildlife Reserve, Singapore 729826 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contacts: EMERGENCY_CONTACT_NAME and their numbers: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Respond in PREFERRED_LANGUAGE then repeat in English. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "continuous_charging_label": "Continuous Charging",
    "continuous_charging_enabled": True,
    "continuous_charging_template": "Your phone has reported continuous charging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous charging detected for 18 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "continuous_discharging_label": "Continuous Discharging",
    "continuous_discharging_enabled": True,
    "continuous_discharging_template": "Your phone has reported continuous discharging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous discharging detected for 12 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English."
}

config_db["chen_ah_niu"] = {
    "name": "Chen Ah Niu",
    "age": 70,
    "living_situation": "Living independently and alone, no caretaker, no social worker",
    "emergency_contact_no": "+65 6457 1089",
    "emergency_contact_name": "Jia En",
    "home_address": "6 Ubi Rd 1, Singapore 408726",
    "preferred_language": "Mandarin",
    "get_me_home_label": "送我回家",
    "get_me_home_enabled": True,
    "get_me_home_template": "Please call me a Grab car. I am at address: 13 Serangoon Avenue 3, 556123 going to HOME_ADDRESS. Include the pickup point (not the pickup address) and destination in your response. Respond in PREFERRED_LANGUAGE. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "medical_emergency_label": "救护",
    "medical_emergency_enable": True,
    "medical_emergency_template": "Call Ambulance on Phone number 995 let them know my current location at 910 Upper Thomson Rd, Singapore 787112 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "blood_type": "AB+",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
    "no_motion_detected_label": "No Motion Detected",
    "no_motion_detected_enabled": True,
    "no_motion_detected_template": "Your phone has reported no motion for the last 12 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [no motion detected for 12 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "continuous_charging_label": "Continuous Charging",
    "continuous_charging_enabled": True,
    "continuous_charging_template": "Your phone has reported continuous charging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous charging detected for 18 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "continuous_discharging_label": "Continuous Discharging",
    "continuous_discharging_enabled": True,
    "continuous_discharging_template": "Your phone has reported continuous discharging for the last 18 hours, Please call Call Ambulance on Phone number 995 let them know my current location at 930 Yishun Ave 2, Singapore 769098 and my blood type: BLOOD_TYPE, also let them know i am: LIVING_SITUATION. Secondly also call my emergency contact: EMERGENCY_CONTACT_NAME and their phone number: EMERGENCY_CONTACT_NO and let them know where the ambulance is taking me. Be sure to include [continuous discharging for 12 hours] in your response. Respond in PREFERRED_LANGUAGE then repeat in English."
}


def update_template(user_info: dict, button_lbl: str) -> str:
    key = button_lbl + "_template"
    tmpl = user_info[key]
    
    tmpl = tmpl.replace('HOME_ADDRESS', user_info['home_address'])
    tmpl = tmpl.replace('PREFERRED_LANGUAGE', user_info['preferred_language'])
    tmpl = tmpl.replace('EMERGENCY_CONTACT_NAME', user_info['emergency_contact_name'])
    tmpl = tmpl.replace('EMERGENCY_CONTACT_NO', user_info['emergency_contact_no'])
    tmpl = tmpl.replace('BLOOD_TYPE', user_info['blood_type'])
    tmpl = tmpl.replace('LIVING_SITUATION', user_info['living_situation'])

    return tmpl