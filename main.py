import json
import os
lead = {
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "interest": "AI automation",
    "budget": 65000,
    "requirement": "Need customer lead automation",
    "urgency": "high"
}
with open("fields.json", "w") as file:
    json.dump(lead, file, indent=4)

def validate_lead(lead):
    if lead["name"]=="":
        return False
    if lead["email"]=="":
        return False
    if lead["interest"]=="":
        return False
    if lead["budget"]<=0:
        return False
    if lead["requirement"]=="":
        return False
    if lead["urgency"] not in ["high", "low", "medium"]:
        return False
    return True
result=validate_lead(lead)


prompt=f'''
You are an AI lead qualification assistant.
Analyze the following customer lead and determine its priority.

Lead:
Name: {lead["name"]}
Email: {lead["email"]}
Interest: {lead["interest"]}
Budget: {lead["budget"]}
Requirement: {lead["requirement"]}
Urgency: {lead["urgency"]}

Determine:
- priority
- confidence
- reason
- recommended_action

Rules:
- priority must be exactly one of: high, medium, low
- confidence must be a number from 0 to 100
- reason must briefly explain the priority
- recommended_action should tell the sales team what to do

Return json only.
Do not include any additional text.


Expected format:
{{
    "priority": "high",
    "confidence": 90,
    "reason": "reason for the priority",
    "recommended_action": "recommended action" 
}}
'''

def validate_ai_response(response):
    required_fields=[
        "priority",
        "confidence",
        "reason",
        "recommended_action"
    ]
    for field in required_fields:
        if field not in response:
            return False
    if response["priority"] not in ["high", "medium", "low"]:
        return False
    if not isinstance(response["confidence"], (int,float)):
        return False
    if not 0<=response["confidence"]<=100:
        return False
    if response["reason"]=="":
        return False
    if response["recommended_action"]=="":
        return False
    return True
valid_response = {
    "priority": "high",
    "confidence": 92,
    "reason": "High budget and urgent requirement.",
    "recommended_action": "Contact the customer immediately."
}
invalid_response = {
    "priority": "urgent",
    "confidence": 150,
    "reason": "",
    "recommended_action": ""
}
final=validate_ai_response(response=invalid_response)


def determine_action(ai_result):
    if ai_result["priority"]=="high" and ai_result["confidence"]>=80:
        action="Notify sales immediately"
    elif ai_result["priority"]=="medium" and ai_result["confidence"]>=80:
        action="Add to follow-up list"
    elif ai_result["priority"]=="low" and ai_result["confidence"]>=80:
        action="Add to marketing list"
    else:
        action="Send for human review"
    return action
ai_result_1 = {
    "priority": "high",
    "confidence": 92,
    "reason": "High budget and urgent requirement.",
    "recommended_action": "Contact the customer immediately."
}
medium_result = {
    "priority": "medium",
    "confidence": 85
}
low_confidence_result = {
    "priority": "high",
    "confidence": 65
}
outcome=determine_action(ai_result_1)
outcome2=determine_action(medium_result)
outcome3=determine_action(low_confidence_result)



def process_lead(lead, ai_result):
    if not validate_lead(lead):
        print("Invalid lead")
        return None
    if not validate_ai_response(ai_result):
        print("Invalid AI response")
        return None
    action=determine_action(ai_result)
    final={
    "name": lead["name"],
    "email": lead["email"],
    "priority": ai_result["priority"],
    "confidence": ai_result["confidence"],
    "action": action
    }
    return final
result=process_lead(lead, invalid_response)

def send_to_crm(lead, max_retries=3):
    attempt=0
    while attempt < max_retries:
        attempt += 1
        print(f"CRM attempt {attempt}")
        if attempt == 3:
            print("CRM update successful")
            return True
        print("CRM request failed")

    print("CRM failed after all retries")
    return False
result=send_to_crm(lead, max_retries=2)

def save_failed_lead(lead, filename="failed_leads.json"):
    try:
        failed_lead=lead.copy()

        failed_lead["status"] = "pending_retry"
        failed_lead["reason"] = "CRM update failed"

        if os.path.exists(filename):
            with open(filename, "r") as file:
                failed_leads = json.load(file)
        else:
            failed_leads=[]
        failed_leads.append(failed_lead)

        with open(filename, "w") as file:
            json.dump(failed_leads, file, indent=4)
            return True
    except (OSError, TypeError, ValueError) as e:
            return False
result=save_failed_lead(lead)
print(result)

result=save_failed_lead(lead)
print(result)

def run_automation(lead, ai_result):
    if not validate_lead(lead):
        print("Invalid lead")
        return None
    if not validate_ai_response(ai_result):
        print("Invalid AI response")
        return None
    action=determine_action(ai_result)
    result=send_to_crm(lead, max_retries=3)
    if result:
        final={
            "name": lead["name"],
            "email": lead["email"],
            "priority": ai_result["priority"],
            "confidence": ai_result["confidence"],
            "action": action,
            "crm_status": "success"
            }
        return final
    else:
        save_failed_lead(lead)
        failed={
            "name": lead["name"],
            "email": lead["email"],
            "priority": ai_result["priority"],
            "confidence": ai_result["confidence"],
            "action": action,
            "crm_status": "failed",
            }
        return failed
result = run_automation(lead, valid_response)
print(result)

    



    
