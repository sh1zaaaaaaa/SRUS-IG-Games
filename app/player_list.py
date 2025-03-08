from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    @property
    def is_empty(self):
        if self.__head is None:
            return True
        else:
            return False

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
        new_player = PlayerNode(player)

        if self.is_empty:
            self.__head = new_player
            self.__tail = new_player
        else:
            new_player.next = self.__head
            self.__head.prev = new_player
            self.__head = new_player

    def append(self, player):
        new_player = PlayerNode(player)

        if self.is_empty:
            self.__head = new_player
            self.__tail = new_player
        else:
            self.__tail.next = new_player
            new_player.prev = self.__tail
            self.__tail = new_player

    def delete_tail(self):
        if self.is_empty:
            raise IndexError("Cannot delete from empty list.")

        if self.tail == self.head:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.tail.prev
            if self.tail:
                self.__tail.next = None

    def delete_head(self):
        if self.is_empty:
            raise IndexError("Cannot delete from empty list.")

        if self.head == self.tail:
            self.__tail = None
            self.__head = None
        else:
            self.__head = self.head.next
            self.__head.prev = None

    def delete(self, key):
        if self.is_empty:
            raise IndexError("Cannot delete from empty list.")

        key = str(key)

        current = self.head

        while current:
            if current.key == key:
                if current == self.head:
                    self.delete_head()
                elif current == self.tail:
                    self.delete_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

        raise IndexError(f"There is no Player with key {key}.")
