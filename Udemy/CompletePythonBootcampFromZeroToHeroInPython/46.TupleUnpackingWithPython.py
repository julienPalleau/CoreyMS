"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20548632#search
Functions and Tuple Unpacking
"""
stock_prices = [('APPLE', 200), ('GOOGLE', 400), ('MICROSOFT', 100)]
for ticker, price in stock_prices:
    print(price + (0.1 * price))

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Return
    return (employee_of_month, current_max)


name, hours = employee_check(work_hours)
print(name, hours)
