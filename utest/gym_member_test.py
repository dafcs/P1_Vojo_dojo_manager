import unittest
from models.member import GymMember

class TestGymMember(unittest.TestCase):
    def setUp(self):
        self.gym_member = GymMember("Rafaela","Freitas","Standard")

    def test_gym_member_has_first_name(self):
        self.assertEqual("Rafaela",self.gym_member.first_name)
    
    def test_gym_member_has_last_name(self):
        self.assertEqual("Freitas",self.gym_member.last_name)
    
    def test_gym_member_has_membership_type(self):
        self.assertEqual("Standard",self.gym_member.membership_type)
    
    def test_gym_member_account_status(self):
        self.assertEqual(True,self.gym_member.account_status)

    def test_gym_member_id_none(self):
        self.assertEqual(None,self.gym_member.id)

    def test_gym_member_toggle_status(self):
        self.gym_member.toggle_status()
        self.assertEqual(False,self.gym_member.account_status)

    def test_gym_member_return_status(self):
        self.assertEqual(True,self.gym_member.account_status)

    def test_gym_member_change_to_premium(self):
        self.gym_member.change_membership_type_to_premium()
        self.assertEqual('Premium',self.gym_member.membership_type)

    def test_gym_member_change_to_standard(self):
        self.gym_member.change_membership_type_to_standard()
        self.assertEqual('Standard',self.gym_member.membership_type)

    def test_gym_member_return_membership_type(self):
        self.assertEqual('Standard',self.gym_member.return_membership_type())        
