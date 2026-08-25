class ticket():
    def __init__(self):
        self.price = 0.0
        self.name = ''
        self.seat = ''
        self.movie = ''

    def setTicketData(self, thisname, thisprice, thisseat, thismovie):
        self.name = thisname
        self.price = thisprice
        self.seat = thisseat
        self.move = thismovie
    
    def getTicketData(self):
        return self.name, self.price, self.seat, self.move

tickets = [ticket() for i in range(5)]
tickets[0].setTicketData('Anthony',5.5,'A23','Spiderman: Brand New Day')
print(tickets[0].getTicketData())
 