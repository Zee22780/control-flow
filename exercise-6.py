# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

# request 2 pieces of input from user - month (using 3 letters) and day of the month
# based on that input evaluates the season of the year
  #if month == dec or month == jan or month == feb or month == mar
    # and day >= 21 for dec or day == 1-30 for Jan, etc.
      #i think we need either tuples or to zip or both? research tuples 
  #print a message including month and day telling user the season



month = input('Enter the month of the year as three characters (Jan - Dec): ')
day = int(input('Enter the day of the month: '))


if month in ('Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif month in ('Apr', 'May', 'Jun'):
  season = 'Spring'
elif month in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
else: 
  season = 'Fall'

if (month == 'Mar') and (day >=20):
  season = 'Spring'
elif (month == 'Jun') and (day >=21):
  season = 'Summer'
elif (month == 'Sep') and (day >= 22):
  season = 'Fall'
elif (month == 'Dec') and (day >= 21):
  season = 'Winter'
  
print(f'{month} {day} is in {season}')

