class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__prev = None

    @property
    def player(self):
        return self.__player

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @next.setter
    def next(self, node):
        self.__next = node

    @prev.setter
    def prev(self, node):
        self.__prev = node

    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return f'Player Node: {self.key}, with Name: {self.__player.name}'