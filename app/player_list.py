from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def __len__(self):
        count = 0

        current = self.__head
        while current:
            count += 1
            current = current.next
        return count

    def push(self, player):
        if self.is_empty:
            new_player = PlayerNode(player)
            self.__head = new_player
            self.__tail = new_player
        else:
            new_player = PlayerNode(player)
            new_player.next = self.__head
            self.__head = new_player

    @property
    def is_empty(self):
        if self.__head is None:
            return True
        else:
            return False