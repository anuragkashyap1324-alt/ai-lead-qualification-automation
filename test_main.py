
import unittest
from main import validate_lead

class TestValidateLead(unittest.TestCase):

    def test_valid_lead(self):
        lead = {
            "name": "Rahul",
            "email": "rahul@example.com",
            "interest": "AI automation",
            "budget": 65000,
            "requirement": "Lead automation",
            "urgency": "high"
        }

        self.assertTrue(validate_lead(lead))


    
    def test_empty_name(self):
        lead = {
            "name": "",
            "email": "rahul@example.com",
            "interest": "AI automation",
            "budget": 65000,
            "requirement": "Lead automation",
            "urgency": "high"
        }

        self.assertFalse(validate_lead(lead))

    
    def test_zero_budget(self):
        lead = {
            "name": "Rahul",
            "email": "rahul@example.com",
            "interest": "AI automation",
            "budget": 0,
            "requirement": "Lead automation",
            "urgency": "high"
        }

        self.assertFalse(validate_lead(lead))

    
    def test_invalid_urgency(self):
        lead = {
            "name": "Rahul",
            "email": "rahul@example.com",
            "interest": "AI automation",
            "budget": 65000,
            "requirement": "Lead automation",
            "urgency": "urgent"
        }

        self.assertFalse(validate_lead(lead))


    def test_invalid_ai_priority(self):
        ai_response = {
            "priority": "urgent",
            "confidence": 90,
            "reason": "Urgent lead",
            "recommended_action": "Contact immediately"
        }

        from main import validate_ai_response
        self.assertFalse(validate_ai_response(ai_response))



if __name__ == "__main__":
    unittest.main()
