class Queue():
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def Enqueue(self, item):
        self.items.insert(0, item)
        
    def Dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)