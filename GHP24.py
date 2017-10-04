def main():
    import random
    count_2s = 0
    count_3s = 0
    count_4s = 0
    count_5s = 0
    count_6s = 0
    count_7s = 0
    count_8s = 0
    count_9s = 0
    count_10s = 0
    count_11s = 0
    count_12s = 0
    user_input = 0
    index = 0
    die_1 = 0
    die_2 = 0
    dice_total = 0
    user_input = userinput()

    
    while index < user_input:

    # Step 5b: Total the two dice
        dice_total = diceroll()

    # Step 5c: Test the dice total and increment the appropriate counter
        if dice_total == 2:
            count_2s = count_2s + 1
        elif dice_total == 3:
            count_3s = count_3s + 1
        elif dice_total == 4:
            count_4s = count_4s + 1
        elif dice_total == 5:
            count_5s = count_5s + 1
        elif dice_total == 6:
            count_6s = count_6s + 1
        elif dice_total == 7:
            count_7s = count_7s + 1
        elif dice_total == 8:
            count_8s = count_8s + 1
        elif dice_total == 9:
            count_9s = count_9s + 1
        elif dice_total == 10:
            count_10s = count_10s + 1
        elif dice_total == 11:
            count_11s = count_11s + 1
        else:
            count_12s = count_12s + 1

    # Step 5d: Increment index by 1
        index = index + 1

# Step 6: Print the results
    display(count_2s, count_3s, count_4s, count_5s, count_6s, count_7s, count_8s, count_9s, count_10s, count_11s, count_12s, user_input)
    return
    user_input = int(user_input)
    return(user_input)
def diceroll():
    import random
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    dice_total = die_1 + die_2
    return(dice_total)
def display(count_2s, count_3s, count_4s, count_5s, count_6s, count_7s, count_8s, count_9s, count_10s, count_11s, count_12s, user_input):
    print("2's rolled: " , count_2s, "or %5.2f percent" , count_2s/user_input * 100)
    print("3's rolled: " , count_3s, "or %5.2f percent" , count_3s/user_input * 100)
    print("4's rolled: " , count_4s, "or %5.2f percent" , count_4s/user_input * 100)
    print("5's rolled: " , count_5s, "or %5.2f percent" , count_5s/user_input * 100)
    print("6's rolled: " , count_6s, "or %5.2f percent" , count_6s/user_input * 100)
    print("7's rolled: " , count_7s, "or %5.2f percent" , count_7s/user_input * 100)
    print("8's rolled: " , count_8s, "or %5.2f percent" , count_8s/user_input * 100)
    print("9's rolled: " , count_9s, "or %5.2f percent" , count_9s/user_input * 100)
    print("10's rolled: " , count_10s, "or %5.2f percent" , count_10s/user_input * 100)
    print("11's rolled: " , count_11s, "or %5.2f percent" , count_11s/user_input * 100)
    print("12's rolled: " , count_12s, "or %5.2f percent" , count_12s/user_input * 100)
    return
main()

# Step 7: Terminate
