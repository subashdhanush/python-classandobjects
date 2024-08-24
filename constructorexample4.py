class Calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        c=self.a+self.b
        print(c)
    def sub(self):
        c=self.a-self.b
        print(c) 
    def mul(self):
        c=self.a*self.b
        print(c)   
    def div(self):
        c=self.a//self.b
        print(c)
obj1=Calculator(5,5)
obj1.add()                        