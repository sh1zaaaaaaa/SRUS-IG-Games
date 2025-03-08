from player import Player
from player_list import PlayerList

if __name__ == '__main__':
    pl = PlayerList()
    player = Player(1, "Test Name")
    player1 = Player(2, "Another Name")
    player2 = Player(3, "Another Name")
    pl.push(player)
    pl.push(player1)
    pl.push(player2)
    pl.display()
    pl.display(forward=False)