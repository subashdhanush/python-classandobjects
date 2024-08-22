class laptop:
    def __init__(self):
        self.price="0"
        self.ram=""
        self.processor=""
        # print("demo")
    def display(self):
        print("Display")
hp=laptop()
hp.price=50000
hp.ram="8gb"
hp.processor="i5"
print(hp.ram)
hp.display()        