class Mobile:
    def __init__(self):
        self.model="Real me"
    def get_model(self):
        return self.model 


x=Mobile()
y=x.get_model()  
print(y)      