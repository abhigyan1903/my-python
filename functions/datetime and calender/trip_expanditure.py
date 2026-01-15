#calculating the expense of trip
def hotel_cost(nights):
      return 200 * nights
def plane_ride(city):
      if city == "canada":
           return 1000
      elif city == "Switzerland":
           return 5000
      elif city == "russia":
           return 900
def rent_car(day):
    if day>=7:
        return (day*2000)-1000
    elif day>=3:
        return (day*2000)-400
    else:
        return day*2000-100
def trip_cost(city,day,spending_money):
    return hotel_cost(day)+plane_ride(city)+rent_car(day)+spending_money
print("the total cost of your trip is:",trip_cost("Switzerland",21,50000),"rupees")