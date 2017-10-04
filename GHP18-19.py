
def main():
 
#1. Introduce the program
    Intro()
 
#2. Get user inputted scores
    (first_score, second_score, third_score, fourth_score, fifth_score)= get_score()
 
#3. Find the average
    average= calc_average(first_score, second_score, third_score, fourth_score, fifth_score)
 
#4. Convert grade to a letter
    first_grade= determine_grade(first_score)
    second_grade= determine_grade(second_score)
    third_grade= determine_grade(third_score)
    fourth_grade= determine_grade(fourth_score)
    fifth_grade= determine_grade(fifth_score)
    average_grade= determine_grade(average)
 
 
#5. Display the scores and average, with letter grades
    print("First test:")
    display_grade(first_score,first_grade)
    print("Second test:")
    display_grade(second_score,second_grade)
    print("Third test:")
    display_grade(third_score,third_grade)
    print("Fourth test:")
    display_grade(fourth_score,fourth_grade)
    print("Fifth test:")
    display_grade(fifth_score,fifth_grade)
    print("The final grade and the average:")
    display_grade(average,average_grade)
    print()
 
    quit
 
def Intro():
    
    print("We're going to take 5 inputs, display them as a letter, average them, and print all that info. ")
    print()
    return
 
def get_score():
    for pasta in range(1,6):
        score= int(input("Please enter a score: "))
        if pasta == 1:
            first_score= score
        elif pasta ==2:
            second_score= score
        elif pasta ==3:
            third_score= score
        elif pasta ==4:
            fourth_score= score
        elif pasta ==5:
            fifth_score= score
    return(first_score, second_score, third_score, fourth_score, fifth_score)
 
def calc_average(first_score, second_score, third_score, fourth_score, fifth_score):
    #This is where we calculate the average and such
    average = 0
    score_sum = first_score + second_score + third_score + fourth_score + fifth_score
    average = score_sum / 5
    return (average)
 
def determine_grade(score):
    #Determine the letter grade
    if score >= 90:
        grade = "A"
    elif score < 90 and score >= 80:
        grade = "B"
    elif score < 80 and score >= 70:
        grade = "C"
    elif score < 70 and score >= 65:
        grade = "D"
    else:
        grade = "D--"
    return (grade)
 
def display_grade(score, grade):
    #Display the letter grade and score
    print("You earned:", score)
    print("and the letter grade is:", grade)
    return
   
 
 main()
