print("Welcome to the calorie counter\n")
print("Please enter your calories for the last 7 days")

week = [] #Create a list to store each day's value in.
for i in range(7):
    day = int(input("Day " + str(i+1) + ":")) # Dynamically generate the input using a for loop
    week.append(day) #add each day to the list

total = sum(week) #use the handy sum()  function to work out the total :-)
average = int(total / 7) #We use int again to clean the number up

print("Your total calorie intake for the week:", total)
print("Your average calorie intake for the week:", average)
