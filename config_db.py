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

config_db["manikam"] = {
    "name": "Manikam",
    "age": 75,
    "living_situation": "Has mild dementia, lives alone, office-hours social worker contact Sofia",
    "emergency_contact_no": "+65 0873 3452",
    "emergency_contact_name": "Sofia (office hour only)",
    "home_address": "15 South Buona Vista Rd, Singapore 118146",
    "preferred_language": "Tamil",
    "get_me_home_lbl": "வீடு",
    "get_me_home_enabled": True,
    "get_me_home_template": "Please call me a Grab car. I am at address: 11 Eunos Rd 8, Singapore 408601 going to HOME_ADDRESS. Include  the pickup point (not the pickup address) and destination in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
}

config_db["hafiz_salleh"] = {
    "name": "Hafiz Salleh",
    "age": 11,
    "living_situation": "Goes to Special Needs School, both parents working, no social worker",
    "emergency_contact_no": "+65 3243 6544,+65 0982 1239",
    "emergency_contact_name": "Abu Salleh and Monica",
    "home_address": "88 Geylang Bahru, Singapore 339696",
    "preferred_language": "Malay",
    "get_me_home_lbl": "Pulang Rumah",
    "get_me_home_enabled": True,
    "get_me_home_template": "I am an 11 year old special needs student and i am lost. Please call my parents: EMERGENCY_CONTACT_NAME their phone numbers are EMERGENCY_CONTACT_NO so they can pick me up. I am at address: 11 Eunos Rd 8, Singapore 408601 going to HOME_ADDRESS. Be sure to inlcude the parents reply in your response. Respond in PREFERRED_LANGUAGE then repeat in English.",
    "talk_to_someone_lbl": "I need to talk to someone",
    "talk_to_someone_enabled": True,
}


def update_template(user_info: dict) -> str:
    tmpl = user_info['get_me_home_template']
    tmpl = tmpl.replace('HOME_ADDRESS', user_info['home_address'])
    tmpl = tmpl.replace('PREFERRED_LANGUAGE', user_info['preferred_language'])
    tmpl = tmpl.replace('EMERGENCY_CONTACT_NAME', user_info['emergency_contact_name'])
    tmpl = tmpl.replace('EMERGENCY_CONTACT_NO', user_info['emergency_contact_no'])
    return tmpl