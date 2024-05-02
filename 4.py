# Write a program to implement a queue

class Queue:

    def __init__(self):
        self.L = []

    def enqueue(self, x):
        self.L.append(x)

    def dequeue(self):
        if len(self.L) == 0:
            print('Queue is empty')
        else:
            self.L.pop(0)

    def front(self):
        if len(self.L) == 0:
            print('Queue is empty')
        else:
            print('The front element is : {}'.format(self.L[0]))

    def display(self):
        if len(self.L) == 0:
            print('Queue is empty')
        else:
            print('The queue is : ', end='')
            for i in self.L:
                if i != self.L[len(self.L)-1]:
                    print(i, end=' -> ')
                else:
                    print(i)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.front()
q.display()
q.dequeue()
q.dequeue()
q.front()
q.display()
q.dequeue()
q.dequeue()
q.front()
q.display()
q.dequeue()


