
print("Welcome to the calorie counter\n")
print("Please enter your calories for the last 7 days")

week = [] 
for i in range(7):
    day = int(input("Day " + str(i+1) + ":")) 

total = sum(week) 
average = int(total / 7) 
print("Your total calorie intake for the week:", total)
print("Your average calorie intake for the week:", average)

