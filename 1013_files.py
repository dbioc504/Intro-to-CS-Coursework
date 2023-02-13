"""Writing values to and reading values from files on a computer. """

import math
import random
import sys
import datetime




# TODO 01 - Randomly generate 50 integers in -111..111 and output the smallest and
# the largest of those random integers.
print("TODO 1:")
min_num = random.randint(-111,111)
max_num = random.randint(-111,111)
for i in range(1, 51):
	random_integer = random.randint(-111,111)
	print(f"{i}\t{random_integer}")
	if random_integer < min_num:
		min_num = random_integer
	if random_integer > max_num:
		max_num = random_integer
print(f"The smallest integer is {min_num} and the largest is {max_num}.")



# TODO 02* - Given a random integer #num# in 1..97, count its number of divisors.
# For example, 3 has 2 divisors (1, 3) and 12 has 6 divisors (1, 2, 3, 4, 6, 12)
print("\nTODO 2:")
random_integer_todo_2 = random.randint(1,97)
divisors = ""
divisor_count = 0
for i in range(1,random_integer_todo_2 + 1):
	if random_integer_todo_2 % i == 0:
		divisors = divisors + f"{i}, "
		divisor_count += 1
print(random_integer_todo_2)
print(f"{random_integer_todo_2} has {divisor_count} divisors ({divisors[:len(divisors)-2]}).")



# TODO 03 - A number is PRIME if its only divisors are 1 and the number itself.
# Given a random integer in 1..97, output 'prime' if it's prime, otherwise output 'not prime'.
print("\nTODO 3:")
random_integer_todo_3 = random.randint(1,97)
print(random_integer_todo_3)
divisor_count = 0
for i in range(1,random_integer_todo_3 + 1):
	if random_integer_todo_3 % i == 0:
		divisor_count += 1
if divisor_count == 2:
	print("prime")
else:
	print("not prime")


# TODO 04 - Output the prime numbers in 1..97.
print("\nTODO 4:")
for i in range(1, 98):
	count = 0
	for divisor in range(1, i+1):
		if i % divisor == 0:
			count += 1
	if count == 2:
		print(f"{i} is prime")


# TODO 05 - How many prime numbers in 1..97?
print("\nTODO 5:")
prime_number_count = 0
for i in range(1, 98):
	count = 0
	for divisor in range(1, 98):
		if i % divisor == 0:
			count += 1
	if count == 2:
		prime_number_count += 1
print(f"There are {prime_number_count} prime numbers in 1-97.")


# Use SEED to generate the same sequence of random integers.
# When generating a bunch of random integers, if you want to generate the exact same
# sequence, just seed the random number sequence by using this statement
# and using the same integer inside the parenthesis.
random.seed(999)
print(f'\nThe seed is 999:')
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)
print(f'The 1st three random integers are {n1}, {n2}, and {n3}')

random.seed(999)
n4 = random.randint(1, 100)
n5 = random.randint(1, 100)
n6 = random.randint(1, 100)
print(f'The 2nd three random integers are {n4}, {n5}, and {n6}')


# Change the seed so generate a different sequence of random integers
# to use with TODO 06 and TODO 07.
random.seed(101)




# TODO 06 - Randomly generate integers 1..97 until a prime number is generated.
# Output all the non-prime integers.
print("\nTODO 6:")
divisor_count = 0
while divisor_count != 2:
	random_integer_todo_6 = random.randint(1,97)
	divisor_count = 0
	for i in range(1,random_integer_todo_6 + 1):
		if random_integer_todo_6 % i == 0:
			divisor_count += 1
	# if divisor_count == 2:
	# 	print("prime")
	# else:
	print(random_integer_todo_6)



# Re-start the sequence of random integers to use the same random numbers as TODO 06.
random.seed(101)




# TODO 07 - Randomly generate integers 1..97 until a prime number is generated.
# Output the number of integers that were generated before finally getting a prime.
# For example, if the generated random integers were 72, 100, 25, 5 then output 3
print("\nTODO 7:")
divisor_count = 0
non_prime_numbers = 0
while divisor_count != 2:
	random_integer_todo_7 = random.randint(1,97)
	divisor_count = 0
	for i in range(1,random_integer_todo_7 + 1):
		if random_integer_todo_7 % i == 0:
			divisor_count += 1
	non_prime_numbers += 1
print(f"There are {non_prime_numbers} non prime numbers.")




# TODO 08* - Write 1..10 to a new file named 'nums.txt'.
print("\nTODO 8:")
print('\nWriting 1..10 to nums.txt...', end="")
with open('nums.txt', 'w') as f:
    for i in range(1, 10 + 1, 1):
        # notice that write() requires us to attach our own '\n' unlike print().
        f.write(str(i) + '\n')
print(' done')


# Now that we know how to write to a file, we must be precise when asked to output
# values.  We must ask whether the output is to the terminal, called STDOUT, or
# to a file.  In my case, all output is to STDOUT unless I explicitly ask you to
# write to a file.



# TODO 09 - Write 10 random scores (0..100) to a new file named 'scores.txt'.
print("\nTODO 9: printed to scores.txt")
with open('scores.txt', 'w') as f:
	for i in range(1, 10 + 1, 1):
		num = random.randint(0,100)
		print(num)
		f.write(str(num) + '\n')




# TODO 10 - Generate 11 random integers (11..111) and output only the even numbers
# to a new file named 'evens.txt'.
print("\nTODO 10 printed to evens.txt")
with open('evens.txt', 'w') as f:
	for i in range(1, 11 + 1, 1):
		num = random.randint(11,111)
		if num % 2 == 0:
			print(f"This is an even number: {num}")
			f.write(str(num) + '\n')




# TODO 11 - Generate random integers (22..222) and output only the odd numbers
# to a new file named 'odds.txt'.  Keep generating numbers until exactly 12 numbers
# are output to the file.
print("\nTODO 11: printed to odds.txt")
with open('odds.txt', 'w') as f:
	odd_count = 0
	while odd_count < 13:
		num = random.randint(22,222)
		if num % 2 != 0:
			odd_count += 1
			f.write(str(num) + '\n')




# Seed the pseudorandom generator with the current time so we know this sequence
# is fairly unique each time this code is run.
random.seed(datetime.datetime.now())



# TODO 12 - Generate a random number of values (0..10) to output to a file and then
# generate that number of random floats (33..333) and output two of those floats
# on each line of a new file named 'two_per_line.dat'.
# For example, if the firs value is 7 then your program should output 4 rows of
# data to a file.  The first 3 rows have 2 numbers on them and the last row has only
# one number on it.
print("\nTODO 12:")
random_count = random.randint(0,10)
print(random_count)
with open('two_per_line.dat', 'w') as f:
	for i in range(random_count):
		random_float = random.uniform(33,333)
		f.write(str(random_float) + '\t')
		if (i - 1) % 2 == 0:
			f.write('\n') 




# Python has some nifty ways to read values from a file.



# TODO 13* - Read everything from the file into a string.
# Notice that it also reads the newlines at the end of each line.
print("\nTODO 13:")
with open('mission.txt', 'r') as f:
    message = f.read()
print(f'Mission Statement:\n{message}')



# TODO 14* - Read line-by-line from the file mission.txt and
# output to STDOUT with the line number next to that line from the file.
print('\nTODO 14: These are the lines from mission.txt:')
line_num = 1
with open('mission.txt', 'r') as f:
    for line in f:
        line = line.strip() # remove the newline
        print(f'({line_num})\t{line}')
        line_num = line_num + 1



# TODO 15 - Output the total of all the integers in nums.txt.
print("\nTODO 15:")
total_nums = 0
with open('nums.txt', 'r') as f:
	for line in f:
		line = line.strip()
		total_nums += int(line)
	print(total_nums)
	



# TODO 16 - What is the average of all the scores of at least 70
# in scores.txt?
print("\nTODO 16:")
total_16 = 0
todo_16_count = 0
with open('scores.txt', 'r') as f:
	for line in f:
		line = line.strip()
		if int(line) > 70:
			total_16 += int(line)
			todo_16_count += 1
avg_16 = total_16 / todo_16_count
print(avg_16)




# Sometimes it's helpful to know your computer's minimum and maximum values.
print(f'\nThe largest  integer (on this computer) is  {sys.maxsize:,d}')
print(f'The smallest integer (on this computer) is {-sys.maxsize - 1:,d}')
print(f'{2**(63):,d} has {math.ceil(math.log10(2**(63)))} digits')



# TODO 17* - What is the largest value in evens.txt?
print("\nTODO 17:")
largest = -sys.maxsize - 1
with open('evens.txt', 'r') as f:
    for line in f:
        line = line.strip() # remove the newline
        num = int(line)
        if num > largest:
            largest = num
print(f'The largest integer in evens.txt is {largest}')



# TODO 18 - What is the smallest value in odds.txt?
print("\nTODO 18:")
smallest = sys.maxsize
with open('odds.txt', 'r') as f:
	for line in f:
		line = line.strip()
		num = int(line)
		if num < smallest:
			smallest = num
print(f"The smallest integer in odds.txt is {smallest}")



# TODO 19 - What is the longest word in mission.txt?  If more than
# one word has the same longest length, output all of those words.
print("\nTODO 19:")
longest_word_len = -sys.maxsize - 1
longest_word = ""
with open('mission.txt', 'r') as f:
	mission_statement = f.read()
	mission_no_newline = mission_statement.replace('\n', ' ')
	mission_noperiods = mission_no_newline.replace('.','')
	mission_nocommas = mission_noperiods.replace(',', '')
	mission_split = mission_nocommas.split(' ')
for word in mission_split:
	if len(word) > longest_word_len:
		longest_word_len = len(word)
		longest_word = word
print(longest_word)
for word in mission_split[mission_split.index(longest_word) + 1:]:
	if len(word) == longest_word_len:
		print(word)




# TODO 20 - Count the number of times the pairs of floats in
# two_per_line.dat are in increasing order.  Be careful since
# the file may not have an even number of values.
print("\nTODO 20:")
order_count = 0
with open('two_per_line.dat', 'r') as f:
	for line in f:
		line = line.strip()
		line_split = line.split('\t')
		print(line_split)
		if len(line_split) > 1:
			if float(line_split[0]) < float(line_split[1]):
				order_count += 1
print(order_count)




# TODO 21 - Generate a random integer (33..333) and count the number
# of times that value is between the pair of floats in a line from
# two_per_line.dat.
# For example, 50 is between the floats 33.3 and 333.3.
# 50 is also between the floats 333.3 and 33.3.
# You decide what your code should do if a line doesn't have 2 numbers.
print("\nTODO 21:")
random_integer_todo_21 = random.randint(33,333)
int_in_between_count = 0
print(random_integer_todo_21)
with open('two_per_line.dat', 'r') as f:
	for line in f:
		line = line.strip()
		line_split = line.split('\t')
		num_1 = float(line_split[0])
		if len(line_split) > 1:
			num_2 = float(line_split[1])
			if len(line_split) > 1 and num_1 > random_integer_todo_21 and random_integer_todo_21 > num_2\
		or num_1 < random_integer_todo_21 and random_integer_todo_21 < num_2:
				int_in_between_count += 1
print(int_in_between_count)



# TODO 22 - Which of the 3 files evens.txt, two_per_line.dat, and/or odds.txt
# has the integer with the largest value?  Output the largest value and also
# the name(s) of the file(s) that have that largest value.
print("\nTODO 22:")
#syntax for odds largest
biggest = -sys.maxsize - 1
with open('odds.txt', 'r') as f:
    for line in f:
        line = line.strip() # remove the newline
        num = int(line)
        if num > biggest:
            biggest = num
#syntax for two_per_line largest
hugest = -sys.maxsize - 1
with open('two_per_line.dat', 'r') as f:
	for line in f:
		line = line.strip()
		line_split = line.split('\t')
		num_1 = float(line_split[0])
		if num_1 > hugest:
			hugest = num_1
		if len(line_split) > 1:
			num_2 = float(line_split[1])
			if num_2 > hugest:
				hugest = num_2
#largest number variables
evens_largest = largest
odds_largest = biggest
two_per_line_largest = hugest
largest_numbers = [evens_largest, odds_largest, two_per_line_largest]
king_large = -sys.maxsize - 1
for num in largest_numbers:
	if num > king_large:
		king_large = num
if num == evens_largest:
	print(f"evens.txt has the largest number:{num}")
if num == odds_largest:
	print(f"odds.txt has the large number: {num}")
if num == two_per_line_largest:
	print(f"two_per_line.dat has the largest number: {num}")




# TODO 23 - A Mad Lib is a way to form silly sentences.  The sentences your
# 7-year old self would have found hilarious.  Scroll down to the Format
# section of https://en.wikipedia.org/wiki/Mad_Libs to see an example.
# Given the words listed in each of the following 4 categories,
# build 5 RANDOM Mad Libs using the template
#     #who capitalized# #verb# #pronoun# #adjective# #noun#.
whos = 'she, he, they'
verbs = 'caught, jumped, hugged, cleaned'
adjectives = 'blue, green, yellow, messy'
nouns = 'cat, dog, car, apartment'
# The pronoun is based on which #whos# is selected.  If #whos# is 'she'
# then the pronoun is 'her'.  If #whos# is 'he' then the pronoun is
# 'his'.  If #whos# is 'they' then the pronoun is 'their'.
# For example, a Mad Lib for that template with these categories could be
# She jumped her green dog.

print("\nTODO 23:")

#converting the strings to lists
whos_split = whos.split(', ')
verbs_split = verbs.split(', ')
adjectives_split = adjectives.split(', ')
nouns_split = nouns.split(', ')

#randomizing word selction
for i in range(5):
	who = random.choice(whos_split)
	verb = random.choice(verbs_split)
	# pronoun = ''
	if who == 'she':
		pronoun = 'her'
	elif who == 'he':
		pronoun = 'his'
	else:
		pronoun = 'their'
	adjective = random.choice(adjectives_split)
	noun = random.choice(nouns_split)
	print(f"{who.capitalize()} {verb} {pronoun} {adjective} {noun}.")




# TODO 24 - Store the words in XULA's mission statement in a single string
# but replace all 4-letter words with '####' and all 3-letter words (except 'and')
# with '***'.  You can assume all words are separated by a space.  I've included
# the file 'mission.txt' that has XULA's mission statement.
print("\nTODO 24:")
with open('mission.txt', 'r') as f:
	mission_statement = f.read()
	mission_no_newline = mission_statement.replace('\n', ' ')
	mission_noperiods = mission_no_newline.replace('.','')
	mission_nocommas = mission_noperiods.replace(',', '')
	mission_split = mission_nocommas.split(' ')
new_string = ""
for word in mission_split:
	if len(word) == 4:
		word = '####'
	elif len(word) == 3 and word != 'and':
		word = '***'
	new_string = new_string + word + " "
print(new_string)




# We already know a quick way to reverse the characters in a string
college = 'Xavier University of Louisiana'
college_reversed = college[::-1]
print(f'\nThe reversed words in "{college}" is "{college_reversed}"')

# We also know how to split a string based on some separator like a space.
college_split = college.split(' ')

# Python also knows how to reverse the order of the parts of a split.
college_temp = college_split
college_temp.reverse()

message = ''
for word in college_temp:
    message = message + ' ' + word
print(f'The words reversed in "{college}" is "{message}".')



# TODO 25 - Reverse both the order of the words in the mission statement
# and also reverse the characters of every other word in the mission statement.
# Output this wacky version of the mission statement.
print("\nTODO 25:")
wacky_xms = ''
word_count = -1
mission_split.reverse()
for word in mission_split:
	word_count += 1
	if word_count % 2 == 0:
		word = word[::-1]
	wacky_xms = wacky_xms + ' ' + word
print(wacky_xms)