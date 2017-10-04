#Introduce: Determine if the odds of rolling a natural Yahtzee is really 1/1296
import random
print("What are the odds of rolling a Yahtzee?")
#Step 1: Create an “average number of rolls” variable and initialize it to 0.0
avg_num_rolls = 0.0
#Step 2: Create 5 dice variables (die_1, die_2, die_3, die_4, and die_5) and initialize each variable
#to a different integer value
die_1 = 1
die_2 = 2
die_3 = 3
die_4 = 4
die_5 = 5
#Step 3: Create a “test counter” variable and initialize it to 1
test_counter = 1
#Step 4: Create a “roll counter” variable and initialize it to 0

roll_counter = 0
#Step 5: Create a “total number of rolls” variable and initialize to 0
total_num_rolls = 0
#Step 6: While the “test counter” variable is less than 10000
while test_counter < 10001:
    #While the 5 dice do not show the same value
    while die_1 != die_2 and die_2 != die_3 and die_3 != die_4 and die_4 != die_5:
        #Roll all five dice
        die_1 = random.randint(1,6)
        die_2 = random.randint(1,6)
        die_3 = random.randint(1,6)
        die_4 = random.randint(1,6)
        die_5 = random.randint(1,6)
        #Increment the “roll counter” by 1
        roll_counter = roll_counter + 1
    #Increment the “test counter” by 1    
    test_counter = test_counter + 1
    #Add the “roll counter” to the “total number of rolls”
    total_num_rolls = total_num_rolls + roll_counter
    #Reset the “roll counter” to 0
    roll_counter = 0
    #Reset one die to some value other than 1 through 6 to make the inner-loop
    #test "false"
    die_1 = 7
    #Determine “average number of rolls” by dividing “total number of rolls” by “test
    #counter”

    avg_num_rolls = total_num_rolls / test_counter
    

print(die_1, die_2, die_3, die_4, die_5)
#Communicate/display the “average number of rolls”
print("The average number of rolls was:", avg_num_rolls)

#Terminate/Basta

#http://web.cs.sunyit.edu/~urbanc/CS_100_GHP_20_21_22_23.pdf

#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#THIS DOESN'T WORK CORRECTLY.  If I run the program I get "The average number of rolls was: 0.00019998000199980003"
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
