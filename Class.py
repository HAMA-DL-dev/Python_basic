class Ballet:
    def __init__(self,name,sex,age,height):
        self.name=name
        self.sex=sex
        self.age=age
        self.height=height

    def showMyProfile(self):
        print ("Name : %s"%self.name)
        print ("Sex : %s"%self.sex)
        print ("Age : %s"%self.age)
        print ("Height : %s"%self.height)

Hayeon=Ballet("Hayeon","F","22","155")
Hayeon.showMyProfile()
