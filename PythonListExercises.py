fruits = ['mango', 'banana', 'apple', 'grape', 'orange']
print(fruits)

colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0], colors[2], colors[4])

numbers = [10, 20, 30, 40, 50]
numbers[1]= 25
numbers.append(60)
print(numbers)

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = [names[0], names[1], names[2]]
print(subset)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    squared = numbers[0] ** 2
    print(squared)
    numbers[0] += 1
    if numbers[0] == 11: 
        break

shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('egg')
shopping_cart2 = ['butter', 'cheese']
shopping_cart.extend(shopping_cart2)
print(shopping_cart)

numbers = [45, 22, 88, 56, 92, 33]
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = letters.count('a')
print("The amount of times a shows up in the list is:", count_of_a)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [square ** 2 for square in numbers if square % 2 == 0]
print(even_numbers)

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = (set(nums))
print(unique_nums)