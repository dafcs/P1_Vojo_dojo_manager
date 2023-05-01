import unittest
from models.room import GymRoom

class TestGymRoom(unittest.TestCase):
    def setUp(self):
        self.gym_room = GymRoom('TheOneAndOnly',25)
    
    def test_room_has_name(self):
        self.assertEqual('TheOneAndOnly',self.gym_room.name)

    def test_room_has_set_capacity(self):
        self.assertEqual(25,self.gym_room.capacity)
    
    def test_room_id_none(self):
        self.assertEqual(None,self.gym_room.id)

    
    

