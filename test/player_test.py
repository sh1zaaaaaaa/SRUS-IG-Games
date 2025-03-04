import unittest
from player import Player

class PlayerClassTest(unittest.TestCase):
    def test_player_data_input_is_string(self):
        player = Player("0001", "Someone")
        self.assertEqual(player.name, "Someone")
        self.assertEqual(player.uid, "0001")

    def test_player_data_input_is_not_string(self):
        player = Player(1, "Someone")
        self.assertEqual(player.name, "Someone")
        self.assertEqual(player.uid, "1")


if __name__ == '__main__':
    unittest.main()
