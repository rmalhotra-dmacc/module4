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
    average_score = average(1, 1, 1)
    print("Average score is {}".format(average_score))
