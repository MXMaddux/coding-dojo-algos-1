

def sum_nums(start_num):
    if start_num > 0:
        return start_num + sum_nums(start_num - 1)
    return 0
print(sum_nums(4))

def r_factor(num):
    if num > 1:
        return r_factor(num - 1) * num
    return 1

print(r_factor(6))


# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

# def mults():
#     for i in range(-300, 0):
#         if i % 3 == 0 and i != -3 and i != -6:
#             print(i)
#
# mults()

# Print integers from 2000 to 5280, using a WHILE.

# def ints():
#     i = 2000
#     while i < 5281:
#         print(i)
#         i += 1
#
# ints()

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

# def print_ints():
#     for i in range(1,101):
#         if i % 5 == 0 and i % 10 == 0:
#             print("Coding Dojo")
#         elif i % 5 == 0:
#             print("Coding")
#         else:
#             print(i)
#
# print_ints()
#
# # Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
#
# def num(hi_num, low_num, mult):
#     i = hi_num
#     for i in range(hi_num, low_num, -1):
#         if i % mult == 0:
#             print(i)
#
# num(666, 1, 4)

# def val_paren(str):
#     left_par = 0
#     right_par = 0
#     for i in str:
#         if i == "(":
#             left_par += 1
#         if i == ")":
#             right_par += 1
#     if left_par == right_par:
#         return True
#     else:
#         return False

# val_paren("N(0(p)3")
# val_paren("Y(3(p)p(3)r)s")

# def val_braces(str):
#     l_par = 0
#     r_par = 0
#     l_curl = 0
#     r_curl = 0
#     l_sq = 0
#     r_sq = 0
#     for i in str:
#         if i == "(" or i == "{" or i == "[":
#             l_par += 1
#             l_curl += 1
#             l_sq += 1
#         if i == ")" or i == "}" or i == "]":
#             r_par += 1
#             r_curl += 1
#             r_sq += 1
#     if l_par == r_par and l_curl == r_curl and l_sq == r_sq:
#         return True
#     else:
#         return False

# val_braces("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!")



# def reverse(arr):
#     arr = arr[::-1]
#     print(arr)

# reverse([1,2,3,4,5])

# def rotate(arr, shift_by):
#     shift_by = shift_by % len(arr)
#     shift_by = -shift_by
#     return arr[shift_by:] + arr[:shift_by]

# rotate([1,2,3], 1)

# def rotate_left(arr, shift_by):
#     arr = arr[shift_by:] + arr[:shift_by]
#     return arr

# rotate_left([1,2,3,4,5], 1)

# def filter_range(arr):
#     min = arr[0]
#     max = 0
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#         if arr[i] > arr[i-1]:
#             max = arr[i]
#     arr = [i for i in arr if i > min and i < max]
#     print(arr)

# filter_range([1,2,3,4,5])

# def concat(arr1, arr2):
#     new_arr = arr1 + arr2
#     print(new_arr)

# concat(['a', 'b'], [1, 2])

# Generate Coin Change
# Change is inevitable (especially when breaking a twenty).
# Make generateCoinChange(cents). Accept a number of American cents,
# compute and print how to represent that amount with the smallest number of coins.
# Common American coins are pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents).

# Example output, given (94):

# def generateCoinChange(amount):
#     dollar = 0
#     quarter = 0
#     dime = 0
#     nickel = 0


#     while amount > 100:
#         dollar += 1
#         amount -= 100
#     while amount > 25:
#         quarter += 1
#         amount -= 25
#     while amount > 10:
#         dime += 1
#         amount -= 10
#     while amount > 5:
#         nickel += 1
#         amount -= 5
#     penny = amount
#     print(f"Dollars: {dollar}, Quarters: {quarter}, Dimes: {dime}, Nickels: {nickel}, Pennies {penny}")

# generateCoinChange(267)

# def palindrome(n):
#     if str(n) == str(n)[::-1]:
#         print("It's a palindrome")
#     else:
#         print("It's not a palindrome")

# palindrome("racecar")

# def reverse(arr):
#     reverse_arr = arr[::-1]

#     print(reverse_arr)


# reverse('creature')


# def remove_even(arr):
#     new_arr = []
#     for i in range(0, len(arr)):
#         if len(arr[i]) % 2 != 0:
#             new_arr.append(arr[i])
#     print(new_arr)


# remove_even(["Nope!", "Its", "Kris", "starting", "with", "K!",
#             "(instead", "of", "Chris", "with", "C)", "."])





# def num2roman(num):
#     num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

#     roman = ''

#     while num > 0 and num < 4000:
#         for i, r in num_map:
#             while num >= i:
#                 roman += r
#                 num -= i

#     return roman

# num2roman(55)

# def remove_blanks(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         if arr[i] != " ":
#             new_arr.append(arr[i])
#     new_arr_no_commas = ''.join(new_arr)
#     print(new_arr_no_commas)


# remove_blanks(" Pl ayTha tF u nkyM usi c ")

# def get_digits(arr):
#     digits = []
#     for i in arr:
#         if i.isdigit():
#             digits.append(i)
#     print(''.join(digits))


# get_digits("0s1a3y5w7h9a2t4?6!8?0")

# def acronyms():
#     answer = [s[0].upper() for s in "Live from New York, it's Saturday Night!".split()]
#     final_answer = ''.join(answer)
#     print(final_answer)

# acronyms()

# def zip_map():
#     arr1 = ["abc", 3, "yo"]
#     arr2 = [42, "wassup", True]
#     arr3 = []
#     for i in range(0, len(arr1)):
#         arr3.append(arr1[i])
#         arr3.append(arr2[i])
#     print(arr3)

# zip_map()

# def invert_hash():
#     my_dict = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
#     my_dict2 = {y:x for x,y in my_dict.items()}
#     print(my_dict2)

# invert_hash()

# 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255
# def from_1_to_255():
#     nums = []
#     for num in range(1, 256):
#         nums.append(num)
#     print(nums)

# from_1_to_255()

# 2. Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise
# def get_evens():
#     even_nums = []
#     for num in range(1,1001):
#         if num % 2 == 0:
#             even_nums.append(num)
#     print(sum(even_nums))

# get_evens()

# 3. Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999)
# def get_odds():
#     odd_nums = []
#     for num in range(1,5001):
#         if num % 2 == 1:
#             odd_nums.append(num)
#     print(sum(odd_nums))

# get_odds()

# 4. Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14)
# my_list = [45, 87, 98, 76, 976]
# def sum_em():
#     print(sum(my_list))

# sum_em()

# 5. Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)
# my_list = [45, 87, 98, 76, 976]
# def find_max(arr):
#     print(max(arr))

# find_max(my_list)

# 6. Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)
# my_list = [45, 87, 98, 76, 976]
# def find_avg(arr):
#     avg = sum(arr) / len(arr)
#     print(avg)

# find_avg(my_list)

# 7. Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method
# def odds():
#     odd_nums = []
#     for num in range(1, 51):
#         if num % 2 == 1 and num > 0 and num < 51:
#             odd_nums.append(num)
#     print(odd_nums)

# odds()

# 8. Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7)

# def find_greater_nums():
#     y = 40
#     total = 0
#     my_list = [34, 45, 21, 87, 9, 8, 687]
#     for i in my_list:
#         if i > 40:
#             total += 1
#     print(total)

# find_greater_nums()

# 9. Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])
# def squares():
#     my_list = [34, 45, 21, 87, 9, 8, 687]
#     my_list_squared = []
#     for i in my_list:
#         my_list_squared.append(i*i)
#     print(my_list_squared)

# squares()

# 10. Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])
# def no_negs():
#     my_list = [34, 45, -21, 87, 9, -8, -687]
#     for i in range(len(my_list)):
#         if my_list[i] < 0:
#             my_list[i] = 0
#     print(my_list)

# no_negs()

"""
11. Max/Min/Avg - Given an array with multiple values,
write a function that returns a new array that only contains the
maximum, minimum, and average values of the original array.
(e.g. [1,5,10,-2] will return [10,-2,3.5])

"""

# def max_min_avg(arr):
#     maximum = max(arr)
#     minimum = min(arr)
#     avg = sum(arr) / len(arr)
#     new_arr = [maximum, minimum, avg]
#     print(new_arr)
#     return new_arr

# max_min_avg([12, -4, 78, 65])

"""
12. Swap Values - Write a function that will swap the first and last
values of any given array. The default minimum length of the array
is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1])
"""

# def swap_values(arr):
#     arr[0], arr[-1] = arr[-1], arr[0]
#     print(arr)

# swap_values([3,5,7,9])

"""
13. Number to String - Write a function that takes an array of numbers
and replaces any negative values within the array with the string 'Dojo'.
For example if array = [-1,-3,2], your function will return
['Dojo','Dojo',2]
"""

# def num_to_string(arr):
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             arr[i]= "Dojo"
#     print(arr)
#     return arr

# num_to_string([2,-6,4,5])

"""
14. Biggie Size - Given an array, write a function that changes all positive
numbers in the array to the string "big".  Example: makeItBig([-1,3,5,-5])
returns that same array, changed to [-1, "big", "big", -5]

"""
# my_list = [-1, -2, -3, 4, 5, 6]
# def biggie():
#     for i in range(len(my_list)):
#         if my_list[i] > 0:
#             my_list[i] = "big"
#     print(my_list)

# biggie()

"""
15. Print Low, Return High - Create a function that takes in an array of numbers.
    The function should print the lowest value in the array, and return the highest
    value in the array

"""

# my_list = [-1, -2, -3, 4, 5, 6]
# def low_high():
#     print(min(my_list))
#     return max(my_list)

# low_high()

"""
16. Print One, Return Another - Build a function that takes in an array of numbers.
    The function should print the second-to-last value in the array, and return the
    first odd value in the array

"""

# my_list = [1, 2, 3, 4, 5, 6]
# def print_one():
#     print(my_list[-2])
#     for i in range(len(my_list)):
#         if i % 2 == 1:
#             return i
# print_one()

"""
17. Double Vision - Given an array (similar to saying 'takes in an array'),
    create a function that returns a new array where each value in the original
    array has been doubled.  Calling double([1,2,3]) should return [2,4,6] without
    changing the original array

"""

# my_list = [2, 4, 6, 8, 9]
# my_list_squared = []
# def squared():
#     for i in range(len(my_list)):
#         my_list_squared.append(my_list[i] * my_list[i])
#     print(my_list_squared)

# squared()

"""
18. Count Positives - Given an array of numbers, create a function to
    replace the last value with the number of positive values found in the
    array.  Example, countPositives([-1,1,1,1]) changes the original array
    to [-1,1,1,3] and returns it

"""
# my_list = [-1, 5, 6, 7]
# def replace_value():
#     tot = 0
#     for i in my_list:
#         if i > 0:
#             tot += 1
#     my_list[-1] = tot
#     print(my_list)

# replace_value()

"""
19. Evens and Odds - Create a function that accepts an array.
    Every time that array has three odd values in a row, print "That's odd!".
    Every time the array has three evens in a row, print "Even more so!"

"""

# my_list = [1,3,5,2, 7, 5,6,8,10, 11, 12, 13,14,16,18, 19, 20, 21,23,25]
# def evens_and_odds():
#     odds = 0
#     evens = 0
#     for i in range(len(my_list)):
#         if my_list[i] % 2 == 1:
#             odds += 1
#             evens = 0
#             if odds == 3:
#                 my_list[i] = "That's odd!"
#         elif my_list[i] % 2 == 0:
#             evens += 1
#             odds = 0
#             if evens == 3:
#                 my_list[i] = "Even more so!"
#     print(my_list)

# evens_and_odds()

"""
20. Increment the Seconds - Given an array of numbers arr, add 1
    to every other element, specifically those whose index is odd
    (arr[1], arr[3], arr[5], etc).  Afterward, console.log each array
    value and return arr

"""

# my_list = [1, 2, 3, 4, 5, 6]
# def increment_the_seconds():
#     for i in range(len(my_list)):
#         if my_list[i] % 2 == 0:
#             pass
#         else:
#             my_list[i] += 1
#     print(my_list)
#     return my_list

# increment_the_seconds()

"""
21. Previous Lengths - You are passed an array
 (   similar to saying 'takes in an array' or 'given an array')
    containing strings.  Working within that same array, replace
    each string with a number - the length of the string at the
    previous array index - and return the array.  For example,
    previousLengths(["hello", "dojo", "awesome"]) should return
    ["hello", 5, 4]. Hint: Can for loops only go forward?

"""

# my_array = ["Hello Chris", "Happy Kitty", "Be nice", "Purrrr"]
# def previous_lengths(list):
#     for i in range(len(my_array) + 1):
#         if i > 1:
#             my_array[i - 1] = len(my_array[i - 1])
#     print(my_array)

# previous_lengths(my_array)

"""
22. Add Seven - Build a function that accepts an array.
    Return a new array with all the values of the original,
    but add 7 to each. Do not alter the original array.
    Example, addSeven([1,2,3]) should return [8,9,10] in a new array

"""
# my_array = [1,2,3]
# new_array = []
# def add_seven(list):
#     for i in list:
#         new_array.append(i + 7)
#     print(new_array)
#     return new_array

# add_seven(my_array)

"""
23. Reverse Array - Given an array, write a function that reverses its values,
    in-place.  Example: reverse([3,1,6,4,2]) returns the same array,
    but now contains values reversed like so... [2,4,6,1,3].
    Do this without creating an empty temporary array.  (Hint: you'll need to swap values)

"""
# my_array = [1,2,3]
# def reverse(list):
#     print(list[::-1])
#     return list[::-1]

# reverse(my_array)

"""
24. Outlook: Negative - Given an array, create and return a new one
    containing all the values of the original array, but make them all
    negative (negative values should remain negative). Given [1,-3,5],
    return [-1,-3,-5]

"""
# my_array = [2, 3, -1, 7]
# def outlook_negative(list):
#     for i in range(len(list)):
#         if list[i] > 0:
#             list[i] *= -1
#     print(list)

# outlook_negative(my_array)

"""
25. Always Hungry - Create a function that accepts an array,
    and prints "yummy" each time one of the values is equal to "food".
    If no array values are "food", then print "I'm hungry" once

"""
# my_array = [2, "food", 3, -1, "food", 7]
# my_array2 = [1, 2, 3]
# def always_hungry(list):
#     found_in_list = 0
#     for i in range(len(list)):
#         if list[i] == "food":
#             # list[i] = "yummy"
#             print("Yummy")
#             found_in_list += 1
#     if found_in_list == 0:
#         print("I'm hungry")


# always_hungry(my_array)
# always_hungry(my_array2)

"""
26. Swap Toward the Center - Given an array, swap the first and last values,
    third and third-to-last values, etc.  Example: swapTowardCenter([true,42,"Ada",2,"pizza"])
    turns the array into ["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns
    the array into [6,2,4,3,5,1].  No need to return the array this time

"""

# my_list = [1,2,3,4,5,6]
# def toward_center(list):
#     list[0], list[-1] = list[-1], list[0]
#     list[2], list[-3] = list[-3], list[2]
#     print(list)

# toward_center(my_list)

"""
27. Scale the Array - Given an array arr and a number num,
multiply all values in the array arr by the number num,
and return the changed array arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9]
"""
# def scale_array(arr, num):
#     for i in range(len(arr)):
#         arr[i] = arr[i] * num
#     print(arr)
#     return arr

# scale_array([3,4,5,6], 7)
