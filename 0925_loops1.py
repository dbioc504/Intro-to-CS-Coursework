"""Before looking at loops, let's learn a few more string operations."""

import datetime
import random

college = 'Xavier'

# NEGATIVE INDEXES
# 654321  <-- negative indexes
# Xavier  <-- the string
# 012345  <-- positive indexes
first_char = college[0]
first_char = college[-6]
first_char = college[-len(college)]

last_char = college[len(college) - 1]
last_char = college[-1]



# TODO 01 - Swap the first and last characters in #college#
# and store the result in #school#.  Output both #college# and #school#.
print("TODO 01:")
school = last_char + college[1:-1] + first_char
print(f"college:{college} school: {school}")



# TODO 02 - If any two of the first, middle, and last characters
# of a string is 'x' (case sensitive), remove the middle 3 characters.
# For example, 'abxcx' should be changed to 'ax'
# Your code must work with every string.
print("\nTODO 02:")
str_var_td2 = input("Type any string here: ")
td2_mid_index = len(str_var_td2) // 2
td2_3_mid_indeces_start = td2_mid_index - 1
td2_3_mid_indeces_end = td2_mid_index + 2
count_for_x = 0
if str_var_td2[0] == "x":
    count_for_x += 1
if str_var_td2[td2_mid_index]:
    count_for_x += 1
if str_var_td2[-1] == "x":
    count_for_x += 1
if count_for_x >= 2:
	str_var_td2 =  str_var_td2[:td2_3_mid_indeces_start] + str_var_td2[td2_3_mid_indeces_end:]
print(str_var_td2)




# REVERSE a string
# reverse_college = college[::-1]
# print(f"\nThe reverse of '{college}' is '{reverse_college}'")



# TODO 03 - A PALINDROME is a string that is the same forward and backward.
# 'mom', 'noon', 'radar', and 'racecar' are palindromes.
# Give a string, output whether the string is a palindrome, or not a palindrome.
print("\nTODO 03:")
str_var_td3 = input("Enter a string here: ")
reverse_strvartd3 = str_var_td3[::-1]
if str_var_td3 == reverse_strvartd3:
    print(f"{str_var_td3} is a palindrome.")
else:
    print(f"{str_var_td3} is not a palindrome.")




# Python has a way to see if a string is contained within another string.
college = 'Xavier Univ'
print()
if 'ier' in college:
    print(f'Yes, "ier" is inside {college}')
else:
    print(f'"ier" is not inside {college}')
if 'ir' in college:
    print(f'Yes, "ir" is not inside {college}')
else:
    print(f'No, "ir" is not inside {college}')



# TODO 04 - Write Python code to determine if both 'i' and 'r' are in #college#?
print("\nTODO 4:")
if "i" in college and "r" in college:
    print(f"Yes, both 'i' and 'r' are in {college}.")
else:
    print(f"No, 'i' and 'r' are not in {college}.")
   


# TODO 05 - Given 3 strings, output if all of the first characters
# of the 3 strings are in #college#.  Use a case sensitive search.
# Otherwise output which of the 3 string(s) don't have their first character in #college#.
print("\nTODO 5:")
td5_str1 = "I think I'll watch a Pokemon movie this week."
td5_str2 = "The name of the movie is 'Pokemon 3000' I believe."
td5_str3 = "My certainty isn't 100% though."
if td5_str1[0] in college and td5_str2[0] in college and td5_str3[0] in college:
	print(f"All three of the strings have their first character in {college}.")
if td5_str1[0] not in college:
	print(f"The first character of '{td5_str1}' is not in {college}.")
if td5_str2[0] not in college:
	print(f"The first character of '{td5_str2}' is not in {college}.")
if td5_str1[0] not in college:
	print(f"The first character of '{td5_str3}' is not in {college}.")



# Python has a way to return the INDEX (position) of a string inside another string.
college = 'Xavier University'
index_of_i = college.index('i')
index_of_avi = college.index('avi')

# index_of_XU = college.index('XU')
# this crashes because 'xu' is not in #college#
# must first check if a string contains before using index()
if 'XU' in college:
    index_of_XU = college.index('XU')
else:
    print(f'\nXU is not in {college} so can not use index()')


# TODO 06 - Read two strings from the user and then output
# True if the first input value occurs before the second
# input value in #college#.  Otherwise output False.
# Notice no quotes around True and none around False.
# Hint:  use index() and slicing.
print("\nTODO 6:")
college = 'Xavier University'
message1 = input("Enter a string here: ")
message2 = input("Enter a string here again: ")
if message1 in college:
	index_of_msg1 = college.index(message1)
else:
    print(f"{message1} doesn't exist in {college}.")
if message2 in college:
	index_of_msg2 = college.index(message2)
else:
    print(f"{message2} doesn't exist in {college}.")

if message1 in college and message2 in college:
    print(index_of_msg1 < index_of_msg2)
else:
    print(f"{message1} & {message2} don't exist in {college}.")

# TODO 07 - Write Python code to determine if #college# has
# two 'i' characters in it.  Hint:  use index() and slicing.
print("\nTODO 7:")
if 'i' in college:
    index_i = college.index('i')
    slice = college[index_i+1:]
    if 'i' in slice:
        index_i_2 = slice.index('i')
        print(f"Yes, there are two 'i' characters in {college} at index {index_i} and {index_i_2} after the first 'i' is identified.")


# TODO 08 - Write Python code to determine whether
# two 'v' characters in #college# occur before a string
# input by the user.  Hint:  use index() and slicing.
# For example, in 'avail' the two a's occur before i and l
# but not before v.
print("\nTODO 8:")
message3 = "Uni"
if message3 in college:
    index_of_msg3 = college.index(message3)
if 'v' in college:
    index_of_v = college.index('v')
if 'v' in college[index_of_v + 1:]:
    index_of_v_2 = college[index_of_v + 1:].index('v')
if index_of_msg3 > index_of_v and index_of_msg3 > index_of_v_2:
	print(f"Two 'v' characters occur in {college} with the first at {index_of_v}, the user string at {index_of_msg3}, and the second 'v' at {index_of_v_2} after the first 'v' is identified.")




"""Loops make it easy to execute the same statements repeatedly.

For example,we know how to output the integers 1..5
but how can we easily output the integers 1..500?
Or, how can we continually prompt the user until they input a valid pin?

In those cases, we need a way to continuously execute a block of statements.
We need a way to tell Python where the loop begins and we need a Boolean
condition to tell Python when to stop executing that block of code.

For example, we could prompt the user for their pin, if the user input is a valid pin,
we'll output "Welcome" and leave the loop block but if the user input
is an invalid pin, output "Try again' and prompt them to input their pin again.

Python has 2 loop structures: a for-loop and a while-loop.
"""


# Use a FOR-LOOP when you know the exact number of times a block of
# code should be executed.

print('\nThe integers from 1 to 10:')
for num in range(1, 10+1, 1):
    print(num)

print('\nEvery other integer from 1 to 10:')
for num in range(1, 10+1, 2):
    print(num)

print('\nEvery third integer from 1 to 10:')
for num in range(1, 10+1, 3):
    print(num)


# TODO 09 - Output the integers from 19 to 25.
print("\nTODO 9:")
for num in range(19, 25+1, 1):
    print(num)

# TODO 10 - Output the integers from -3 to 3
print("\nTODO 10:")
for num in range(-3, 3+1, 1):
    print(num)


today = datetime.date.today()
current_year = today.year


# # TODO 11 - Output the years from 2015 to the current year.
print("\nTODO 11:")
for num in range(2015, current_year+1, 1):
    print(num)


# TODO 12 - Generate a random integer in 1999..2019.
# Generate another random integer in 2020..2022.
# Output the years from the first value to the last value inclusive.
print("\nTODO 12:")
year_1 = random.randint(1999,2019)
year_2 = random.randint(2020,2022)
print(f"{year_1} and {year_2}")
for num in range(year_1, year_2+1, 1):
    print(num)



# TODO 13 - Using the random years from TODO 12, output the
# years that are divisible by 10.
print("\nTODO 13:")
for num in range(year_1, year_2+1, 1):
    if num % 10 == 0:
        print(num)



# TODO 14 - Using the random years from TODO 12, count the
# number of years that are divisible by 10.
print("\nTODO 14:")
mult_of_10 = 0
for num in range(year_1, year_2+1, 1):
    if num % 10 == 0:
        mult_of_10 += 1
print(f"There are {mult_of_10} year(s) that are divisible by 10.")



# TODO 15 - Using the random years from TODO 12, calculate the
# sum (total) of those years.
print("\nTODO 15:")
sum_total = 0
for num in range(year_1, year_2+1, 1):
	sum_total += num
print(sum_total)
    



# TODO 16 - Using the random years from TODO 12, calculate the
# average of those years.
print("\nTODO 16:")
amount_of_yrs = 0
for num in range(year_1, year_2+1, 1):
    amount_of_yrs += 1
avg = sum_total // amount_of_yrs
print(avg)



# The Pythonic way to SWAP or exchange the values stored in 2 variables:
#    var1, var2 = var2, var1
#
# We should also know the typical way to SWAP.
#    temp = var1
#    var1 = var2
#    var2 = temp



# TODO 17 - Randomly generate an integer in 1..10 and store in #num1#.
# Randomly generate another integer in 1..10 and store it in #num2#.
# Make sure the smaller of the two values is in #num1# and the
# larger of the two values is in #num2#
print("\nTODO 17:")
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
if num1 > num2:
	num1, num2 = num2, num1
print(f"Num1: {num1}\tNum2: {num2}")



# TODO 18 - Randomly generate two integers in 1999..2022
# and count the even years within that range.
print("\nTODO 18:")
even_years = 0
int_1 = random.randint(1999, 2022)
int_2 = random.randint(1999, 2022)
if int_1 > int_2:
	int_1, int_2 = int_2, int_1
for num in range(int_1, int_2, 1):
    if num % 2 == 0:
        even_years += 1
print(f"There are {even_years} even year(s) within {int_1} and {int_2}")

# TODO 19 - Output the years from 1999 to the current year but only
# print the years that are divisible by either 3 or 5 but not divisible by 10.
print("\nTODO 19:")
for num in range(1999, current_year+1, 1):
    if num % 3 == 0 or num % 5 == 0: 
        if num % 10 != 0:
            print(num)


# TODO 20 - Which years from 1991 to the current year have the same
# first and last digits?
print("\nTODO 20:")
for num in range(1991, current_year+1, 1):
    if num // 1000 == num % 10:
        print(num)



# TODO 21 - Output the integers from 10 down to 1
# and then output 'BLASTOFF!'
print("\nTODO 21:")
for num in range(10, -1+1, -1):
    print(num)
print("BLASTOFF!")




# TODO 22 - Is this a countdown?  Why or why not?
print("\nTODO 22:")
print('\n1..10 Blastoff:')
for num in range(1, 10, -1):
    print(num)
print('BLASTOFF2!')
print(f'This is not a countdown because the third parameter of the ', end="")
print(f'functions asking the for loop to print the numbers from 1-10 ', end="")
print(f"in a negative order, and that's impossible because 1 is less than 10.")



# Here is how to output the characters in #college#.
print(f'\nThe characters in the string \'{college}\':')
for char in college:
    print(char)



# TODO 23 - Output the number of vowels in #college#.
print("\nTODO 23:")
vowel_count = 0
for char in college:
    # if char == 'a' or char == 'i' or char == 'e' or char == 'o' or char == 'u':
    if 'a' in college or 'i' in college or 'e' in college or 'o' in college or 'u' in college:
        vowel_count += 1
print(vowel_count)



# Python's print() outputs a '\n' but sometimes we want to continue
# writing in a subsequent print() statement.  To retain our position in
# the output without moving to the next line, we can use
#     print(f'Your first name is {firstname} and your', end="")
#     print(f' last name is {lastname}.')
#
# But what if we want to do this without using end="" at the end of our
# print statement?
#     message = f'Your first name is {firstname} and your'
#     message = message + f' last name is {lastname}.'
#     print(message)


# TODO 24 - Replace a string's 'a' and 'i' characters in college with '#' and
# store this result in a string named #message#.
print("\nTODO 24:")
# FINDING THE A AND I 
message = ''
for char in college:
    if char == 'a' or char == 'i':
        char = '#'
        message += char
    else:
        message += char
print(message)



# TODO 25 - Output the indexes next to the character at that index.
# For example, if the string is 'XU of' then the output format is:
# 0    X
# 1    U
# 2
# 3    o
# 4    f
print("\nTODO 25:")
character_count = 0
for char in college:
    print(f"{character_count}\t{char}")
    character_count += 1
