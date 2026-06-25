class MinStack:
    
    


    def __init__(self):
        self.stack=[]
        self.pointer=-1        
        
        

    def push(self, val: int) -> None:
        self.pointer=self.pointer+1
        self.stack.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop(self.pointer)
        self.pointer=self.pointer-1
        

    def top(self) -> int:
        return self.stack[self.pointer]
        

    def getMin(self) -> int:
        return min(self.stack)
        
