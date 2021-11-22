class Mobile:
    def __init__(self):
        self.model="Real me X"
    def set_model(self):
        self.model ="Real me 2"


x=Mobile()
print('before setting')
print(x.model)
print('After setting')
x.set_model()  
print(x.model)  