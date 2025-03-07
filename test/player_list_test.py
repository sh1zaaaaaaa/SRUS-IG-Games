import unittest

from player import Player
from player_list import PlayerList


class PlayerListTest(unittest.TestCase):
    def test_push_to_empty_list(self):
        pl = PlayerList()
        self.assertEqual(True, pl.is_empty)
        player = Player(1, "Test Name")
        pl.push(player)
        self.assertEqual(pl.is_empty, False)
        self.assertEqual(len(pl), 1)

    def test_push_to_not_empty_list(self):
        pl = PlayerList()
        player = Player(1, "Test Name")
        pl.push(player)
        self.assertEqual(False, pl.is_empty)
        player1 = Player(2, "Another Name")
        pl.push(player1)
        self.assertEqual(len(pl),2)
        self.assertNotEqual(pl.head, pl.tail)

    def test_append_to_empty_list(self):
        pl = PlayerList()
        self.assertEqual(True, pl.is_empty)
        player = Player(1, "Test Name")
        pl.append(player)
        self.assertEqual(False, pl.is_empty)
        self.assertEqual(len(pl), 1)
        self.assertEqual(pl.head, pl.tail)

    def test_append_to_not_empty_list(self):
        pl = PlayerList()
        player = Player(1, "Test Name")
        pl.append(player)
        self.assertEqual(False, pl.is_empty)
        player1 = Player(2, "Another Name")
        pl.append(player1)
        self.assertEqual(len(pl), 2)
        self.assertNotEqual(pl.head, pl.tail)


if __name__ == '__main__':
    unittest.main()
