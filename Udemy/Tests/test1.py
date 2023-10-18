# List comprehension
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]


def get_price(price):
    return price if price > 0 else 0


prices = [get_price(i) for i in original_prices]
print(prices)


# Set and Dictionary Comprehensions
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

squares = {i: i * i for i in range(10)}
print(squares)

# using the Warlus Operator
import random
def get_weather_data():
    return random.randrange(90, 110)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(hot_temps)

# Choose Generators for large Datasets
sum(i * i for i in range(1000000000))