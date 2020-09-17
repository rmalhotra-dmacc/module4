"""""
Program: coupon_calculations.py
Author: Rajiv Malhotra
Last Modified Date: 09/17/2020
 
The program will accept the amount of purchase, the cash coupon, the percentage coupon and it will calculate the total
order price. 
"""""


def calculate_price(price, cash_coupon, percent_coupon):
    with_cashcoupon = price - cash_coupon
    with_percentcoupon = with_cashcoupon - (with_cashcoupon * percent_coupon/100)
    subtotal_tax = with_percentcoupon * 1.06
    if with_percentcoupon < 10:
        shipping = 5.95
    elif with_percentcoupon < 30:
        shipping = 7.95
    elif with_percentcoupon < 50:
        shipping = 11.95
    else:
        shipping = 0
    return subtotal_tax + shipping


if __name__ == '__main__':
    final_price = calculate_price(5.99, 5, 10)
