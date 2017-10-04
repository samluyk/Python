
#Introduce - This will find the largest and smallest number inputted, and average them all.

#the below are constants:
#1. total = 0
num_of_inputs = 0 
max_number = 0
min_number = 0
a = 0

#2.
while (a>=0):
    a = int(input("Input a positive integer please (or negitive if you want to stop) "))
#3
    if (a<0):
        break
#4
    num_of_inputs = num_of_inputs + 1
    totat = total
    if(a>max_number):
        max_number = a
    if(a<min_number):
        min_number = a
#5
#6
print("Total numbers entered: " + str(num_of_inputs))
print("Largest number: " + str(max_number))
print("Smallest number: " + str(min_number))
print("The average of the inputs: " + str(total/num_of_inputs))
#7
#Terminate (pasta)
