# Prints the string below to terminal
print "I will now count my chickens:"

# Prints the string "Hens" followed by the number 30
# 30 = (30/6) + 25
print "Hens", 25 + 30 / 6

# Prints the string "Roosters" followed by the number 97
# 97 = ((25*3) % 4) - 100
# NOTE % is the modulus operator. This returns the remainder (ex 6%2=0, 7%2=1)
print "Roosters", 100 - 25 * 3 % 4

# Prints the string below to terminal
print "Now I will count the eggs:"

# Prints 7 to the terminal
# 4%2=[0], 1/4=[0]
# 3 + 2 + 1 - 5 + [0] - [0] + 6
# NOTE 1/4 is 0 and not 0.25 because 1 & 4 are whole numbers, not floats
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

# Prints the string below to terminal
print "Is it true that 3 + 2 < 5 - 7?"

# Prints false to the screen
# 5 < -2  is false
# NOTE the < and > operators check whether something is truthy or falsey
print 3 + 2 < 5 - 7

# Prints the string below followed by the number 5
print "What is 3 + 2?", 3 + 2

# Prints the string below followed by the number -2
print "What is 5 - 7?", 5 - 7

# Prints the string below to terminal
print "Oh, that's why it's False."

# Prints the string below to terminal
print "How about some more."

# Prints the string below followed by 'true'
print "Is it greater?", 5 > -2

# Prints the string below followed by 'true'
print "Is it greater or equal?", 5 >= -2

# Prints the string below followed by 'false'
print "Is it less or equal?", 5 <= -2


# ================================
# ========= STUDY DRILLS =========
# ================================

#1 Above each line, use the # to write a comment to yourself explaining what the line does.
## DONE!

#2 Remember in Exercise 0 when you started Python? Start Python this way again and using the math operators, use Python as a calculator.
## DONE :)

#3 Find something you need to calculate and write a new .py file that does it.
## See calculator.py file

#4 Notice the math seems "wrong"? There are no fractions, only whole numbers. You need to use a "floating point" number, which is a number with a decimal point, as in 10.5, or 0.89, or even 3.0.
## Noted.

#5 Rewrite ex3.py to use floating point numbers so it's more accurate. 20.0 is floating point.
## Only rewrote line 20 because that's the only statement that would be affected by floating points. 
## Rewrote calculator.py as well :).