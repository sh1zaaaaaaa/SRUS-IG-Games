class Player:
    def __init__(self, uid, name):
        self.__uid = str(uid)
        self.__name = str(name)

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'Player: {self.__name} has an id: ({self.__uid})'
