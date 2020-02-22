class Cal:
    def setdata(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result=self.first+self.second
        return result
a=Cal()
a.setdata(3,2)
print(a.add())
# -----------------------------another way---------------------------
class Cal:
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result=self.first+self.second
        return result

a=Cal(3,2)
print(a.add())
