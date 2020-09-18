"""""
Program: validation_with_try.py
Author: Rajiv Malhotra
Last Modified Date: 09/187/2020
 
The program will accept the amount of purchase, the cash coupon, the percentage coupon and it will calculate the total
order price. 
"""""


def average(score1, score2, score3):
    NUMBER_TESTS = 3
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float((score1 + score2 + score3)/NUMBER_TESTS)


if __name__ == '__main__':
    lastName = input("Please enter your last name: ")
    firstName = input("Please enter your first name: ")
    age = input("Please enter your age: ")
    first_score = input("Enter your first score: ")
    second_score = input("Enter your second score: ")
    third_score = input("Enter your third score: ")
    try:
        average_score = average(int(first_score), int(second_score), int(third_score))
    except ValueError:
        print ("Please enter only positive scores!")
    else:
        print("{}, {}, age: {}, Average score is {}".format(lastName, first_score, age, average_score))
