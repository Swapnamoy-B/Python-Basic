class Railways:
    formtype= "Railwayform"
    def printData(self):
        print(f"name is {self.name}")
        print(f"Train is {self.train}")


myApplication = Railways()

myApplication.name= "Subai"
myApplication.train="Rajdhani"

myApplication.printData()