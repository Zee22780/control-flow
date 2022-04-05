# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

#Determine how python can take in 3 inputs
#After inputs are entered, program needs to compare the sides to each other to determine what kind of triangle it is
  #if a, b, and c are equal 
    #print message that says it's an equilateral
  #elif a, b, and c are uneaqual
    #print messages that says it's a scalene
  #else 
    #print message that says it's an isosceles


a, b, c = input('Enter the lengths of three sides of a triangle: ').split()

if a == b and b == c:
  print(f'A triangle with sides of {a}, {b} & {c} is an equilateral triangle')
elif a != b and b != c:
  print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
  print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')