from node import Node

class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end = " ")
            node = node.pointer
        print()

    def _delete(self, prev, node):
        self.length -= 1
        if not prev:
            self.head = node.pointer
        else:
            prev.pointer = node.pointer

    def _add(self, value):
        self.length += 1
        self.head = Node(value, self.head)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        node, prev, i = self._find(index)
        if index == i:
            self._delete(prev, node)
        else:
            print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    def deleteNodeByValue(self, value):
        node, prev, found = self._find_by_value(value)
        if found:
            self._delete(prev, node)
        else:
            print(f"값 {value}에 해당하는 노드가 없습니다.")


if __name__ == "__main__":
    ll = LinkedListLIFO()
    for i in range(1, 5):
        ll._add(i)
    print("연결 리스트 출력:")
    ll._printList()
    print("인덱스가 2인 노드 삭제 후, 연결 리스트 출력:")
    ll.deleteNode(2)
    ll._printList()
    print("값이 3인 노드 삭제 후, 연결 리스트 출력:")
    ll.deleteNodeByValue(3)
    ll._printList()
    print("값이 15인 노드 추가 후, 연결 리스트 출력:")
    ll._add(15)
    ll._printList()
    print("모든 노드 모두 삭제 후, 연결 리스트 출력:")
    for i in range(ll.length-1, -1, -1):
        ll.deleteNode(i)
    ll._printList()