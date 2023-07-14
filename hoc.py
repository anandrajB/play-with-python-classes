# Example 1: Squaring numbers using map()
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Example 2: Converting Celsius temperatures to Fahrenheit
celsius_temps = [23, 15, 30, 18, 27]
fahrenheit_temps = map(lambda c: (c * 9/5) + 32, celsius_temps)
print(list(fahrenheit_temps))  # Output: [73.4, 59.0, 86.0, 64.4, 80.6]



# Example 1: Filtering even numbers using filter()
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

# Example 2: Filtering names starting with 'J'
names = ['John', 'Jane', 'Mark', 'Jessica']
filtered_names = filter(lambda name: name.startswith('J'), names)
print(list(filtered_names))  # Output: ['John', 'Jane', 'Jessica']



from functools import reduce

# Example 1: Summing up a list of numbers using reduce()
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  

# Example 2: Finding the maximum number in a list using reduce()
numbers = [15, 8, 20, 12, 10]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  