# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

# My pseudocode
#request input from user - it will be a number but needs to be converted to an int
#take that int and
  #add 10 years to first 2 years
  #add 7 years for any remaining years
#test examples: user inputs 5
  #year 1 = 10
  #year 2 = 10
  #year 3 = 7
  #year 4 = 7
  #year 5 = 7
  #sum all integers = 41

  #or actually!

  #if int > 2 takes int and subtracts 2 and stores 2 in a variable
    #mult variable by 10
  #takes remainder and stores that in a separate variable
    #mult variable by 7
  #add var 1 + var 2 for total age
  #elif int < 2 multiply by 10
#prints a message to user and includes total age


human_age = input("Input a dog's age in human years: ")

if(int(human_age) > 2):
  a = 2
  b = int(human_age) - 2
  dog_age = (a*10) + (b*7)
  print(f"The dog's age in dog years is {dog_age}")
elif(int(human_age)<2):
  dog_age = int(human_age)*10
  print(f"The dog's age in dog years is {dog_age}")
