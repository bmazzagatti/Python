#!//usr/bin/env python3

def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} has boarded the ship")
        counter += 1
        
onboard_passengers(5)