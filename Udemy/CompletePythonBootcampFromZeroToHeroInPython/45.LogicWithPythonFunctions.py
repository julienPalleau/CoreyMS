"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/20548624#search
Functions with logic
"""
def even_check(number: int):
    return number % 2 == 0


print("event_check")
print(even_check(20))
print(even_check(21))


# Return True if any number is even inside a list
def check_even_list(num_list: list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            # return False # WRONG !!!
            pass
    return False


# it is important to understand that, when return is executed it breaks the loop.
# As a consequence if you put return False, as soon as a number is not even it will exit the loop and if a number is
# even after it won't be detected and the result of our function will be wrong! To overcome this problem, the retrun False
# must be outside the loop. Because in this case the return True won't break the loop and return will return False.


print("")
print("event_check list")
print(check_even_list([1, 3, 5]))
print(check_even_list([2, 4, 5]))
print(check_even_list([2, 1, 1, 1]))
print(check_even_list([1, 1, 1, 2]))

print("")
print("Now I want to return all the even numbers in a list")


# Now I want to return all the even numbers in a list
def check_even_list_2(num_list: list):
    # return all the even numbers in a list

    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


print(check_even_list_2([1, 2, 3, 4, 5]))
print(check_even_list_2([1, 3, 5]))
