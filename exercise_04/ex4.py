# The whole number 100 is assigned to the variable cars
cars = 100

# The floating point number 4.0 is assigned to the variable space_in_a_car
space_in_a_car = 4.0

# The whole number 30 is assigned to the variable drivers
drivers = 30

# The whole number 90 is assigned to the variable passengers
passengers = 90

# The result of the value 100-30 is assigned to the variable cars_not_driver
cars_not_driven = cars - drivers

# The value of drivers (30) is assigned to the variable cars_driven
cars_driven = drivers

# The result of the value 30*4.0 is assigned to the variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car

# The result of the value 90/30 is assigned to the variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars avaialble."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# ================================
# ========= STUDY DRILLS =========
# ================================

# Explain the error below:
# --------------------------------
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#      average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# --------------------------------
### This error is thrown because one of the variables used in the code was not defined
### Specifically, the variable 'car_pool_capacity' is not defined
### This was a typo, it should've been 'carpool_capacity'
### The user can find this error on line 8 of his/her code

#1 I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
### I would argue that in this case, floats (ex 4.0) are unnecesssary because well, would you ever have 4.25 or 4.5 spaces available in a car? Arguably, yes - you could have a backpack take up half a seat. ALthough, I'm not sure if it's safe to offer up half a seat for a person to sit in.
### If we used a whole number (ex 4), the return value of carpool_capacity would be a whole number as well.

#2 Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
### Noted.

#3 Write comments above each of the variable assignments.
### Done

#4 Make sure you know what = is called (equals) and that it's making names for things.
### Noted :).

#5 Remember that _ is an underscore character.
### Done. Stored in memory.

#6 Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
### Done. This is what I ran in Terminal:
### oprah_net_worth = 3000000000.0
### my_net_worth = 25498.32
### difference = oprah_net_worth - my_net_worth
### print difference