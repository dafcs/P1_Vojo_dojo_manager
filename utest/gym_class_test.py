import unittest
from models.gym_class import GymClass


class TestGymClass(unittest.TestCase):
    def setUp(self):
        self.gym_class_1 = GymClass("Pilates")


    def test_gym_class_has_name(self):
        self.assertEqual('Pilates',self.gym_class_1.name)
    
    def test_gym_class_has_duration(self):
        self.assertEqual(1,self.gym_class_1.duration)
    
    def test_gym_class_id_none(self):
        self.assertEqual(None,self.gym_class_1.id)
    
