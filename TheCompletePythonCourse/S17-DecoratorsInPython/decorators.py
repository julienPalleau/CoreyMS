# import functools
#
# user = {'username': 'julien123', 'access_level': 'admin'}
#
#
# def user_has_permission(func):
#     @functools.wraps(func)  # <--- this wrapper is what allow us to get the right function name and the doc for the 3 prints below
#     def secure_func(*args, **kwargs):
#         if user.get('access_level') == 'admin':
#             return func(*args, **kwargs)
#     return secure_func
#
#
# @user_has_permission
# def my_function(panel):
#     """
#     Allowus to retrieve the password for the admin panel
#     """
#     return f'Password for {panel} panel is 1234.'
#
#
# @user_has_permission
# def another():
#     pass
#
#
# print(my_function.__name__)
# print(another.__name__)
# print(my_function.__doc__)
# print(my_function('movies'))
# print(another())


# --------------------------


"""
Implement a @access_control decorator that can be used like this:
@access_control(access_level)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))
Your decorator should meet the following requirements:
- It takes in an argument `access_level` and would compare the current user's role with the access level.
- You can get the current user's role, represented by an integer, by calling the `get_current_user_role()` function.
    You don't need to implement this function, we will take care of it for you.
- You may assume smaller access level value would have higher privilege. For example, 0 - admin, 1 - user, 2 - guest.
    So you can check if the user has proper access level like this:
if get_current_user_role() <= access_level:
    # do something
else:
    # forbid
- If the user has the proper access level, we allow the user to call the function (that has this decorator).
- If the user does not have a proper access level, we raise a `PermissionError` with the message:
    'You do not have the proper access level.'
- The decorator should be generic, which means it can be applied to any function that has any amount of
    arguments (or key word arguments).
- Your decorator should keep the original function's `__name__` and `__doc__` strings.
"""

from functools import wraps


# DO NOT CHANGE
def access_control(access_level: int):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            if get_user_role() <= access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError('You do not have the proper access level.')

        return inner_wrapper

    return outer_wrapper


def get_user_role() -> int:
    return 0


@access_control(0)
def delete_file(filename):
    # perform the deletion operation
    print(f'{filename} is deleted')


delete_file('file')

"""
Taken from our Complete Python Course: https://www.udemy.com/the-complete-python-course/?couponCode=REPLIT
Purely as an example, a function can have multiple decorators.
Decorators are applied from bottom to top, which means the top decorator is the first one to be evaluated when the function is executed.
In this example, we have two decorators. One checks the user's access_level, the other checks the user's username (must start with the letter 'j').
"""

import functools

# Try the various combinations below!
user = {'username': 'jose123', 'access_level': 'admin'}
# user = {'username': 'bob', 'access_level': 'admin'}
# user = {'username': 'jose123', 'access_level': 'user'}
# user = {'username': 'bob', 'access_level': 'user'}


def user_name_starts_with_j(func):
    """
    This decorator only runs the function passed if the user's username starts with a j.
    """

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('username').startswith('j'):
            return func(*args, **kwargs)
        else:
            print("User's username did not start with 'j'.")

    return secure_func


def user_has_permission(func):
    """
    This decorator only runs the function passed if the user's access_level is admin.
    """

    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
        else:
            print("User's access_level was not 'admin'.")

    return secure_func


@user_has_permission
@user_name_starts_with_j
def double_decorator():
    return 'I ran.'


print(double_decorator())

"""
When `double_decorator()` runs, this chain of "functions" runs:
user_has_permission -> user_name_starts_with_j -> double_decorator
That is because `user_name_starts_with_j` is the first decorator to be applied. It replaces `double_decorator` by the function it returns.
Then, `user_has_permission` is applied—and it replaces the function the other decorator returned by the function it returns.
"""
