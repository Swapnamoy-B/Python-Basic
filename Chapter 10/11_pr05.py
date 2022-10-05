class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("****************")
        print(f"The name of the train is {self.name}")
        print(f"The no. of seats available are {self.seats}")
        print("****************")

    def fareInfo(self):
        print(f"The price of the ticket is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print("Your ticket is booked")
            self.seats=self.seats-1
        else:
            print("Train is booked, try in tatkal")

    def cancelTicket(self):
        pass

intercity = Train("Intercity Train", 50, 2)

intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()