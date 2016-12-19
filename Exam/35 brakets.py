class LinkedList:
    def __init__(self):
        self._A = []

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
        return data

    def correct_braces_sequence(self, expr):
        stack = LinkedList()
        left = ['{', '[', '(']
        right = ['}', '[', ')']
        other_brace = dict(zip (left, right))
        for brace in expr:
            if brace in left:
                stack.push_front(brace)
            elif brace in right:
                if stack.empty():
                    return False
                if brace != other_brace[stack.pop_front()]:
                    return False
        return stack.empty()


B = ['[','{','}',']']
obj_1 = LinkedList()
obj_1.push_front(B)
#print(obj_1.empty())
print(obj_1.pop_front())
obj_1.correct_braces_sequence(B)

""" Cтек- это LIFO-очередь; last in - first out
Очередь - это LIFO-очередь first in - first out
Кольцевая очередь
"""