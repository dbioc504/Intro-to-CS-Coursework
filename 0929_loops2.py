"""Loops are helpful when we want to repeatedly do the same block of code.
We've learned to use for-loops and now we'll look at Python while-loops.

Use for-loops when you know exactly how many times a loop will be done.
In all other cases, use a while-loop.
"""

import random

xula_mission = "Xavier University of Louisiana, founded by Saint Katharine Drexel \
and the Sisters of the Blessed Sacrament, is Catholic and historically Black. \
The ultimate purpose of the University is to contribute to the promotion of a more \
just and humane society by preparing its students to assume roles of leadership and \
service in a global society. This preparation takes place in a diverse learning and \
teaching environment that incorporates all relevant educational means, including \
research and community service."


# TODO 01 - Output the indexes (positions) of the 1st, 2nd, 3rd, and 4rd spaces in Xavier's
# Mission Statement. You can assume the words are separated by at least 1 space.
# You can use index() and slicing to solve this problem but you cannot use Python's split()
# and you cannot use number literals.
#
# Xavier University of Louisiana, founded
# 012345678901234567890123456789012345678

index_count = -1
space_count = 0
print("TODO 1:")
for char in xula_mission:
    index_count += 1
    if char == " ":
        space_count += 1
        print(index_count)
        if space_count == 4:
            break



# TODO 02 - Output the 1st, 2nd, 3rd, and 4rd words in Xavier's Mission Statement.
# You can assume the words are separated by at least 1 space.
# Output the words in reverse order (which isn't the same as using Python's reverse().)
# Output each word on a separate line and each word must be enclosed inside apostrophes.
# You can use index() and slicing to solve this problem but you cannot use Python's split().

print("\nTODO 2:")
space_index_1 = xula_mission.index(' ')
word_1 = xula_mission[:space_index_1]
if ' ' in xula_mission[space_index_1:len(xula_mission)]:
    space_index_2 = xula_mission[space_index_1+1:].index(' ') + space_index_1 + 1
word_2 = xula_mission[space_index_1+1:space_index_2]
space_index_3 = xula_mission[space_index_2+1:].index(' ') + space_index_2 + 1
word_3 = xula_mission[space_index_2+1:space_index_3]
space_index_4 = xula_mission[space_index_3+1:].index(' ') + space_index_3 + 1
word_4 = xula_mission[space_index_3+1:space_index_4]
print(f"'{word_4}'\n'{word_3}'\n'{word_2}'\n'{word_1}'")



# Python has a nifty way to separate a string based on a given separator.
name = 'C. Reynold Verret'
num_chars = len(name)

split_name = name.split(' ')  # SPLIT the string at spaces
num_words = len(split_name)

first_name = split_name[0]
middle_name = split_name[1]
last_name = split_name[2]
print(f'\n{name}:\n\t {num_chars} characters\n\t {num_words} words\n\t {first_name}, {middle_name}, and {last_name}')

# Notice that we used Python's len() to calculate the number of characters in a string
# and we also used Python's len() after splitting the string into words.  The 2nd use
# of len() is calculating the number of split sections, or in this case, the number of
# words in the original string.
#
# Also, just as with strings, once we split(), the 1st split section is at index 0,
# the 2nd split section is at index 1, the 3rd split section is at index 3, etc.
#
# Just as we can find the first character of a string by using
first_char = name[len(name) - 1]
first_char = name[-1]
# We can find the first split section (or word) in our name by using
first_word = split_name[len(split_name) - 1]
first_word = split_name[-1]
#
# Just as we can find the last character of a string by using
last_char = name[len(name) - 1]
last_char = name[-1]
# We can find the last split section (or word) in our name by using
last_word = split_name[len(split_name) - 1]
last_word = split_name[-1]


print(f'\nXavier\'s Mission Statement has:')

# TODO 03 - How many characters in Xavier's Mission Statement?
print("\nTODO 3:")
print(f"Xavier's Mission Statement has {len(xula_mission)} characters.")


# TODO 04 - How many words in Xavier's Mission Statement?
# You can assume the words are separated by at least 1 space.
print("TODO 4:")
split_xula_mission = xula_mission.split(' ')
print(f"There are {len(split_xula_mission)} words in Xavier's Mission Statement.")


# TODO 05 - What are the first and last words in Xavier's Mission Statement?
print("\nTODO 5:")
first_word_xula_mission  = split_xula_mission[0]
last_word_xula_mission = split_xula_mission[-1]
print(f"The first word of Xavier's Mission Statement is '{first_word_xula_mission}', and the last word is '{last_word_xula_mission[:len(last_word_xula_mission)-1]}'")



# Remember that we can loop through the characters of a string.
college = 'Xavier'
print(f'\nThe characters in {college}:')
for char in college:
    print(char)

# We can also loop through the words in a split string.
name = 'C. Reynold Verret'
split_name = name.split(' ')  # SPLIT the string at spaces
print(f'\nThe words in {name}:')
for word in split_name:
    print(word)



# TODO 06 - Output all words of at least 10 characters in Xavier's Mission Statement.
print("\nTODO 6:")
for word in split_xula_mission:
    if len(word) >= 10:
        print(word)



# TODO 07 - How many words in Xavier's Mission Statement begin with a vowel?
print("\nTODO 7:")
words_beginning_with_vowels_in_xula_mission = 0
for word in split_xula_mission:
	if word[0].upper() in 'AEIOU':
		words_beginning_with_vowels_in_xula_mission += 1
print(words_beginning_with_vowels_in_xula_mission)

# TODO 08 - How many times is 'and' used in Xavier's Mission Statement?
print("\nTODO 8:")
count_of_and_in_xula_mission = 0
for word in split_xula_mission:
    if word.capitalize() == 'And':
        count_of_and_in_xula_mission += 1
print(count_of_and_in_xula_mission)



# TODO 09 - Does Xavier's Mission Statement have more 'a' or more 'l'?
# This is a case insensitive search so look for 'a', 'A', 'l', and 'L'.
print("\nTODO 9:")
letter_a_count = 0
letter_l_count = 0
for char in xula_mission:
    if char.upper() == 'A':
        letter_a_count += 1
    if char.upper() == 'L':
        letter_l_count += 1
if letter_a_count > letter_l_count:
    print("Xavier's Mission Statement has more 'a's than 'l's.")
else:
    print("Xavier's Mission Statement has more 'l's than 'a's.")



# TODO 09 - Which words in Xavier's Mission Statement have both 'a' and 'l'?
# This is a case insensitive search so look for 'a', 'A', 'l', and 'L'.
print("\nTODO 9 Pt. II:")
print("In the Xavier Mission Statement, these words have both 'a' and 'l'.")
for word in split_xula_mission:
    if 'a' in word and 'l' in word or 'A' in word and 'l' in word or 'A' in word and 'L' \
    in word or 'a' and 'L' in word:
        print(word)




# Python has a way to tell us if a character is uppercase or lowercase.
# Python has isupper() and islower().
college = 'Xavier'
if college[0].islower() == True:
    print(f'{college} begins with a lowercase letter')
else:
    print(f'{college} begins with an uppercase letter')

if college[0].isupper() == True:
    print(f'{college} begins with an uppercase letter')
else:
    print(f'{college} begins with a lowercase letter')



# TODO 10 - What percentage of words in Xavier's Mission Statement begins with a capital letter?
print("\nTODO 10:")
capital_letter_words = 0
word_count = len(split_xula_mission)
for word in split_xula_mission:
    if word[0].isupper() == True:
        capital_letter_words += 1
capital_letter_percentage = (capital_letter_words / word_count) * 100
print(f"{int(capital_letter_percentage)}% of words in Xavier's Mission Statement begins with a capital letter.")



# We've learned to use lots of for-loops.  Let's explore while-loops.
# Remember:
#    Use a for-loop when you know exactly how many times a loop will be done.
#    Use a while-loop for every other loop problem.



# TODO 11* - Read and write integers from the user until they input a zero.
# Once zero is input, stop reading values.  The zero should not be output.
# Pause before coding this and consider why we cannot use a for-loop to solve this.
# Note:  In this problem, zero is called the SENTINEL because it's a guard that
# knows if we should keep looping.
# num = int(input('\nEnter an integer (zero to quit):  '))
# while num != 0:
#     print(num)
#     num = int(input('Enter another integer (zero to quit):  '))
print("\nTODO 11:")
integer_until_zero = int(input("\nEnter an integer: (zero to quit): "))
while  integer_until_zero != 0:
	print(integer_until_zero)
	integer_until_zero = int(input("Enter an integer (zero to quit): "))



# TODO 12* - Read integers from the user until they input a negative integer.
# Once a negative integer is input, output the number of integers that were input.
# Should you solve this using a for-loop or a while-loop?
# count = 0
# num = int(input('\nEnter an integer (negative to quit):  '))
# while num >= 0:
#     count = count + 1
#     num = int(input('Enter another integer (negative to quit):  '))
# print(f'You entered {count} non-negative integer(s)')
print("\nTODO 12:")
count_of_user_integers = 0
integer_until_negative = int(input("\nEnter an integer (negative to quit): "))
while integer_until_negative >= 0:
    count_of_user_integers += 1
    integer_until_negative = int(input("Enter another integer (negative to quit): "))
print(f"You entered {count_of_user_integers} non-negative integer(s)")



# TODO 13 - Loop through the words in Xavier's Mission Statement and output
# the words of even length that have more than 7 characters.
# Should you solve this using a for-loop or a while-loop?
print("\nTODO 13:")
for word in split_xula_mission:
    if len(word) % 2 == 0 and len(word) > 7 and word[7] != '.' and word[7] != ',':
        print(word)




# TODO 14* - Loop through the name and output the index next to each word.
# name = 'C. Reynold Verret'
# split_name = name.split(' ')  # SPLIT the string at spaces
# print(f'\nIndex and words in {name}:')
# for index in range(0, len(split_name)):
#     print(f'{index} \t {split_name[index]}')

# print(f'\nAnother way to output index and words in {name}:')
# index = 0
# for word in split_name:
#     print(f'{index} \t {word}')
#     index = index + 1
print("\nTODO 14:")
name_for_TODO14 = 'D. Louis Bioc'
split_name_for_TODO14 = name_for_TODO14.split(' ')
index_for_TODO14 = 0
print(f"\nIndex and words in {split_name_for_TODO14}.")
for word in split_name_for_TODO14:
    print(f"{index_for_TODO14}\t{word}")
    index_for_TODO14 += 1



# TODO 14* - Loop through the words in Xavier's Mission Statement and output
# the words until the word 'Saint' is found.  Once the word 'Saint' is found,
# output the average length of the previous (non-sentinel) words.
# count = 0
# len_words = 0
# index = 0
# while words_in_mission[index] != 'Saint':
#     count = count + 1

#     word = words_in_mission[index]
#     len_words = len_words + len(word)

#     index = index + 1
# print(f'\nThe average length up to Saint is {len_words / count:.1f} characters')
# print(f'{len_words} {count}')
print("\nTODO 14 Part II:")
count_of_words_until_Saint = 0
len_words_until_Saint = 0
index_for_words_until_Saint = 0
while split_xula_mission[index_for_words_until_Saint] != 'Saint':
    count_of_words_until_Saint += 1
    word = split_xula_mission[index_for_words_until_Saint]
    len_words_until_Saint += len(word)
    index_for_words_until_Saint += 1
print(f"\nThe average length up to Saint is {len_words_until_Saint / count_of_words_until_Saint:.1f} characters")
print(f"{len_words_until_Saint} {count_of_words_until_Saint}")

# TODO 15 - Build a string of all the words in Xavier's Mission Statement that
# have more than 10 characters.
print("\nTODO 15:")
string_of_10_character_words = ""
for word in split_xula_mission:
    if len(word) > 10:
        string_of_10_character_words += ' ' + word
print(string_of_10_character_words)



# TODO 16 - Build a string of every 10th word in Xavier's Mission Statement.
print("\nTODO 16:")
new_word_count = 0
every_10th_word = 0
string_for_every_10th_word = ''
for word in split_xula_mission:
    new_word_count += 1
    if new_word_count % 10 == 0:
        string_for_every_10th_word += word + ' '
print(string_for_every_10th_word)



# TODO 17* - The only valid pin for an ATM has an odd number of characters
# and has at least one of $, @, or _ symbols and the pin cannot have a space.
# Continually prompt the user until they input a valid pin.
# pin = input('\nEnter your pin: ')
# valid = len(pin) % 2 != 0 and ('$' in pin or '@' in pin or '_' in pin) and (' ' not in pin)
# while not valid:
#     pin = input('Try again:  ')
#     valid = len(pin) % 2 != 0 and ('$' in pin or '@' in pin or '_' in pin) and (' ' not in pin)
# print(f'Your valid pin is {pin}')
print("\nTODO 17:")
pin_number = input("\nEnter your pin: ")
valid = len(pin_number) % 2 != 0 and ('$' in pin_number or '@' in pin_number or '_' in pin_number) and (' ' not in pin_number)
while not valid:
    pin_number = input("Try again: ")
    valid = len(pin_number) % 2 != 0 and ('$' in pin_number or '@' in pin_number or '_' in pin_number) and (' ' not in pin_number)
print(f"Your valid pin is {pin_number}.")


# TODO 18 - Let's play the High-Low Game.  Here's how it works.
# Randomly select an integer in 1..100.  This is the #target#.
# The user guesses any integer.  If their guess is the #target#, they win
# and the game is over.  If the user's guess is below the #target#, output
# 'HIGHER' and give the user another chance to guess.  If the user's guess is
# above the #target#, output 'LOWER' and give the user another change to guess.
# The gam is over when the user guesses the #target# or the user guesses 5 times.
# When the game ends, output either "You won!" or "You lost, the target was #target#."

print("\nTODO 18:")
target = random.randint(0,100)
player_tries = 1
player_guess = int(input("Enter a number between 1 and 100: "))
while player_tries < 5 and player_guess != target:
    if player_guess > target:
        player_tries += 1
        print("LOWER")
        player_guess = int(input("Try again. "))
    elif player_guess < target:
        player_tries += 1
        print("HIGHER")
        player_guess = int(input("Try again. "))
if player_guess == target:
    print("You won!")
else:
    print(f"You lost, the target was {target}.")


# TODO 19 - Loop through the words in Xavier's Mission Statement and output
# the indexes of the words but only when the word is 'and'.
print("\nTODO 19:")
for word in split_xula_mission:
    word_count += 1
    if word.capitalize() == 'And':
        print(word_count)


# TODO 20 - Loop through the words in Xavier's Mission Statement and output
# the words until the second time the word 'and' is found.
print("\nTODO 20:")
count_of_and_in_xula_mission = 0
for word in split_xula_mission:
    print(word)
    if word.capitalize() == 'And':
        count_of_and_in_xula_mission += 1
        if count_of_and_in_xula_mission == 2:
            break




# TODO BONUS (up to +10 points) - The only valid pin for an ATM has an even number
# of characters, begins with an 'X', ends with 'r', has 'avie' in the middle, and
# has at least one of $ or _ symbols, exactly 2 '@' symbols, and the pin must have a space.
# Continually prompt the user to input a pin until they input a valid pin.
bonus_pin = input("Enter your pin here (X$avie@@ r):   ")
valid_bonus = len(bonus_pin) % 2 == 0 and ('avie' in bonus_pin) and ('$' in bonus_pin or '_' in bonus_pin) and ('@' in bonus_pin and \
'@' in bonus_pin[bonus_pin.index('@'):]) and (' ' in bonus_pin) and (bonus_pin[0] == 'X' and bonus_pin[len(bonus_pin) - 1] == 'r')
while not valid_bonus:
    bonus_pin = input("Enter another pin here (X$avie@@ r):  ")
    valid_bonus = len(bonus_pin) % 2 == 0 and ('avie' in bonus_pin) and ('$' in bonus_pin or '_' in bonus_pin) and ('@' in bonus_pin and \
    '@' in bonus_pin[bonus_pin.index('@'):]) and (' ' in bonus_pin) and (bonus_pin[0] == 'X' and bonus_pin[len(bonus_pin) - 1] == 'r')
print(f"Your valid pin is {bonus_pin}.")
