from dataclasses import dataclass
@dataclass
class ticket():
    price : float = 0.0
    name : str = ''
    seat : str = ''
    movie : str = ''

tickets = [ticket() for i in range(5)]
ticket[0].price = 5.5
ticket[0].name = Anthony
ticket[0].seat = A23
ticket[0].movie = PussinBootsTheLastWish

print(tickets[0])
 