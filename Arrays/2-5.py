# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Calculates the total number of seats in the cinema
def seats_total(seats):
   total = 0
   for row in seats:
      total += len(row)  
   return total

def seats_available(seats):
   available = 0
   for row in seats:
      available += row.count('A')  
   return available

def seats_booked(seats):
   booked = 0
   for row in seats:
      booked += row.count('B') 

# Returns the status of the seat 
def seat_status(seats, row, place):
   if seats[row-1][place-1] == 'A':  
      return "Available"
   else:
      return "Booked"

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
