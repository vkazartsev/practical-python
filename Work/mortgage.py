# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

total_paid = 0.0
current_month = 1

while principal > 0:
    monthly_payment = payment + extra_payment * ((current_month >= extra_payment_start_month) and (current_month <= extra_payment_end_month))
    principal = principal * (1+rate/12)
    monthly_payment = min(monthly_payment, principal)
    principal = principal - monthly_payment
    total_paid = total_paid + monthly_payment
    current_month += 1
    print(f'{current_month}, {total_paid}, {principal}')

print(f'Total paid: {total_paid}')