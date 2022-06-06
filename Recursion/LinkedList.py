
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def print_data(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def add_to_start(self, data):
        node = Node(data)
        if(not self.head):
            self.head = node 
        else:
            tmp = self.head
            self.head = node
            self.head.next = tmp


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.add_to_start(8)
    linked_list.add_to_start(3)
    linked_list.add_to_start(3)
    linked_list.add_to_start(2)

    linked_list.print_data()