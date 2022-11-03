# implement a Queue using 2 stacks
# from real interview

class Queue2Stacks():
    def __init__(self):
        
        # init two stacks
        self.s1 = [] 
        self.s2 = []
    
    def enqueue(self, element):
        self.s1.append(element)
        
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()