class LinkedList:
    def __init__(self):
        self._A = None

    def __str__(self):
        p = self._A
        while p:
            print(p[0])
            p = p[1]

    def push_front(self, data):
        self._A = [self._A, data]  # unappropriate to use "A = [data, A]"

    def empty(self):
        return self._A == None

    # удаляет 1-е звено и возвращает его data
    def pop_front(self):
        if self.empty():
            raise IndexError()
        data = self._A[0]
        self._A = self._A[1]
        print(self._A)
        return data