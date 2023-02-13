"""Functions are blocks of reusable code.

To this point in the semester, we haven't done much to organize our code.
We organize our code with indentation because it's required by Python but
our only other organizing is by using whitespace (blank lines) to separate blocks
of code.

Organizing code is an important task as our programs grow longer and longer.
Functions are the primary method to organize code.

FUNCTIONS have 3 primary goals:
(1) To bundle code in REUSABLE blocks.  This is called MODULARITY.  Each bundle
is a block of code that should solve exactly 1 task.
(2) To make our code more READABLE.  Code is often written once but it is read
many many times.  We need to write code for the other humans who will read it.
(3) To LOCALIZE ERRORS.  Because functions solve only one task, whenever that task
isn't working, coders know exactly which block of code to review.

We've used many functions already.
    print('Hello, World!')
    name = input('Enter your name: ')
    year = int(input('Enter your birthyear: '))

Python knows these are functions.  How?  Because it's a word next to parenthesis.
Python knows print(), input(), and int() are  functions.
These are Python's builtin functions.

Now let's learn how to write our own functions.
We're learning to write USER-DEFINED FUNCTIONS.
"""


# How to organize your Python code
#
# The way we've been organizing our code is all wrong.
# We begin each statement against the left margin, what Python calls the
# GLOBAL SCOPE.  We shouldn't put everything in the global scope.  We should
# organize our code into bundles that solve only 1 task, that are easily reusable,
# that use descriptive names so our code is readable by other coders,
# and that make it easier for us to find errors in our code.
#
# Functions have two parts:  the function definition and the function call.
# The FUNCTION DEFINITION is the code we write to solve a task.
# The FUNCTION call is the code needed to use that function definition.
# The function definition is written once but this function can be called many times.
#
# print(), input(), and int() are Python builtin function calls.
# Each solves a single task and we've called these functions many times.
#

# Line 65 is our first function definition named main().
# Python knows it's a function definition because it begins with the #def# keyword
# followed by a word next to parenthesis.
# This function definition is defining a function named #main#.
# Our new function named #main# has a BODY that calls Python's builtin
# print() function.
#
# Now that we have this function definition named #main#, we can call it.
# Look at the Line 71 to see we're calling the function named #main#.
# Python knows it's a function call because it's a word next to parenthesis AND
# it's not prefixed with the #def# keyword.

# From now on, always organize your code as I've done in Lines 65 - 72.


def main():
    print('\n\n==========  WELCOME TO FUNCTIONS  ==========')
    # This is the body of your main() function.
    ages = read_column('titanic3.tsv', 4)
    survivors = read_column('titanic3.tsv', 1)
    names = read_column('titanic3.tsv', 2)
    pclass = read_column('titanic3.tsv', 0)
    fares = read_column('titanic3.tsv', 8)
    parchs = read_column('titanic3.tsv', 6)
    sibsps = read_column('titanic3.tsv', 5)
    print('\nTODO 1 & 2')
    welcome()
    print('\nTODO 3')
    welcome_3(input("Enter your name here: "))
    print('\nTODO 4:')
    print(welcome_4(input("\nEnter your name: ")))
    print("\nTODO 5:")
    print(name_char_return('Dominick', 'Louis', 'Bioc'))
    print('\nTODO 6 & 7:')
    print(min_and_max([5, 10, 15]))
    print('\nTODO 9:')
    print(dead_or_alive(read_column('titanic3.tsv', 1)))
    print('\nTODO 10:')
    print(survival_percentage(survivors))
    print('\nTODO 11:')
    print(pc_survival(survivors, pclass))
    print('\nTODO 12:')
    print(sexes(read_column('titanic3.tsv', 3)))
    print('\nTODO 13:')
    print(age_avg(read_column('titanic3.tsv', 3), ages))
    print('\nTODO 14:')
    print(destination_indexes(read_column('titanic3.tsv', 13), input("Enter a location provided within the Titanic database: ")))
    print('\nTODO 15:')
    print(no_family_survivors(sibsps, parchs, survivors))
    print('\nTODO 16:')
    print(avg_passenger_fare(fares))
    print('\nTODO 17:')
    print(survival_rate_embarkation(read_column('titanic3.tsv', 10), survivors))
    print('\nTODO 18:')
    print(age_bins(ages))
    print('\nTODO 19:')
    print(first_class_rates(pclass, survivors, fares))
    print('\nTODO 20:')
    print(titles(names))
    print('\nTODO 21:')
    print(diff_family_names(names))
    print('\n\n\nTODO 22:')
    print(familynamecount(names))
    
   

    


# Your function definitions go here


# Functions have a distinct SIGNATURE.
# def function_name(parameter1, parameter2, ..., parameterN):
#     # BODY of the function are the statements Python will execute when
#     # the function is called.

import random

# TODO 01* - In main(), we are outputting the welcome message.  We are using
# Python's builtin print() function.  Change that function call to a user-defined 
# function call.  Your function must be named #welcome# and it has no parameters.
# Call your welcome() function.

def welcome():
    welcome_msg = input("Enter your name here: ")
    print(f'\n\n==========  WELCOME TO FUNCTIONS, {welcome_msg.upper()}  ==========')

 



# TODO 02 - Change your welcome() function to include the user's name in the
# welcome message.  Your function body must prompt for the user's name and this
# function has no parameters.





# TODO 03* - Create a new welcome message function that accepts the user's name
# as a PARAMETER and then outputs a personalized welcome message.

def welcome_3(user_name):
    print(f'Hello {user_name.upper()}, I hope you have a good day today.')





# TODO 04* - Create a new welcome message function that accepts the user's name
# and returns a personalized (string) message.

def welcome_4(user_name):
    personal_msg = f"Hello {user_name.capitalize()}, everything is going to be okay :)"
    return (personal_msg)
    




# TODO 05 - Create a function that given 3 names, returns the name with the
# middle number of characters.  For example, 'abc', 'abcde', 'a' will return 'abc'.
def name_char_return(name1, name2, name3):
    names = [name1, name2, name3]
    shortest_length = len(name1)
    longest_length = 0
    answer = []
    for name in names:
        if len(name) < shortest_length:
            shortest_length = len(name)
        if len(name) > longest_length:
            longest_length = len(name)
    for name in names:
        if len(name) > shortest_length and len(name) < longest_length:
            answer.append(name)
    return answer




# TODO 06 - Create a function that given a list of numbers, returns the average
# of those numbers.
def average_number(num_list):
    avg_num = sum(num_list) / len(num_list)
    return avg_num




# TODO 07 - Create a function that given a list of numbers, returns the minimum,
# maximum, and average of those numbers.  Your function must return a list with
# these three values.  Your function must use TODO 06 to calculate the average.
def min_and_max(num_list):
    min_of_list = min(num_list)
    max_of_list = max(num_list)
    list_three_nums = [min_of_list, max_of_list, average_number(num_list)]
    return list_three_nums




# Data Science is one of the hottest areas in Computer Science.
# It's a mixture of code and statistics.  It's a  mixture of AI, data mining, and
# machine learning.  Let's explore actual data from the Titanic disaster by
# using data science techniques.
#
# Kaggle is a website that has lots of free datasets.
# https://www.kaggle.com/competitions/titanic/overview
# The Titanic data is in the TAB-DELIMITED file 'titanic3.tsv'.
# If you're curious about the values, read the data dictionary at
# https://www.kaggle.com/competitions/titanic/data


# TODO 08* - Read the survived of all the passengers from the file.
# This function takes the file name and the column num (zero-indexed) and
# returns a list of values from that column in the file.
def read_column(file, column_num) -> list:
    """Gets the values from a particular column of a file.

    Args:
        file: The file name where the data can be found.
        column_num: The zero-based indexed column of the requested data.

    Returns:
        A list of data values from that particular column of the file.
        
    Notes:
        https://www.kaggle.com/competitions/titanic/data
        pclass = read_column('titanic3.tsv', 0)
        survived = read_column('titanic3.tsv', 1)
        names = read_column('titanic3.tsv', 2)
        sexes = read_column('titanic3.tsv', 3)
        ages = read_column('titanic3.tsv', 4)  # 263 missing
        sibsps = read_column('titanic3.tsv', 5)
        parchs = read_column('titanic3.tsv', 6)
        tickets = read_column('titanic3.tsv', 7)
        fares = read_column('titanic3.tsv', 8)  # 1 missing
        cabins = read_column('titanic3.tsv', 9)  # 1014 missing
        embarks = read_column('titanic3.tsv', 10)  # 2 missing
        boats = read_column('titanic3.tsv', 11)  # 823 missing
        bodies = read_column('titanic3.tsv', 12)  # 1188 missing
        destinations = read_column('titanic3.tsv', 13)  # 564 missing
    """
    valid_lines = []
    line_num = 1
    with open(file, 'r') as f:
        titles_line = f.readline()
        for line in f:
            line = line.strip()
            parts = line.split('\t')
            if len(parts) > column_num and parts[column_num] != '':
                if parts[column_num].isdigit():
                    valid_lines.append(int(parts[column_num]))
                else:
                    try:
                        valid_lines.append(float(parts[column_num]))
                    except ValueError:
                        valid_lines.append(parts[column_num])
            line_num = line_num + 1
    return valid_lines




# TODO 09 - How many people survived and how many died?  This is a function
# that takes a list and returns two results.
def dead_or_alive(valid_lines):
    dead_count = 0
    alive_count = 0
    for i in valid_lines:
        if i == 1:
            alive_count += 1
        else:
            dead_count += 1
    doa_list = [dead_count, alive_count]
    return doa_list
    



# TODO 10 - What percentage of people survived?  This is a function that takes
# a list and returns the (float) percentage of people who survived.
def survival_percentage(valid_lines):
    alive_count = valid_lines.count(1)
    s_percent = alive_count / len(valid_lines)
    return s_percent * 100




# TODO 11 - What percentage of people survived in each pclass?
# Should you write a function?  Yes, everything is a function.
def pc_survival(survival_list, pclass_list):
    pclass_sums = pclass_list
    diff_classes = set(pclass_list)
    diff_classes_list = []
    pclass_counts = []
    survival_rates = []
    survival_count = 0
    for i in diff_classes:
        pclass_counts.append(pclass_list.count(i))
        diff_classes_list.append(i)

    for i in range(len(diff_classes_list)):
        for j in range(len(survival_list)):
            if pclass_list[j] == diff_classes_list[i] and survival_list[j] == 1:
                survival_count += 1
                survival_rates.append(survival_count)



    return diff_classes_list




# TODO 12 - How many females and how many males?  Your function should take a list
# of sexes and return a single result that has the number of females separate from
# the number of males.
def sexes(sex_list):
    women = sex_list.count('female')
    men = sex_list.count('male')
    m_and_f_counts = [men, women]
    return m_and_f_counts




# TODO 13 - What is the average age of the females and the average age of males?
def age_avg(sex_list, age_list):
    men_ages = []
    women_ages = []
    for i in range(len(age_list)):
        if sex_list[i] == 'male':
            men_ages.append(age_list[i])
        if sex_list[i] == 'female':
            women_ages.append(age_list[i])
    avg_male_age = sum(men_ages) / len(men_ages)
    avg_female_age = sum(women_ages) / len(women_ages)
    avg_ages_list = [avg_male_age, avg_female_age]
    return 




# TODO 14 - Pass a (string) destination and return the indexes to all passengers
# with that destination.
def destination_indexes(destination_list, user_location):
    new_destinations = []
    for i in range(len(destination_list)):
        new_destinations.append(destination_list[i].replace("\"", ""))
    location_indexes = []
    for i in range(len(new_destinations)):
        if new_destinations[i] == user_location:
            location_indexes.append(i)
    return location_indexes




# TODO 15 - Did people with no other family aboard the Titanic survive more than others?
def no_family_survivors(siblings, parents, survival_list):
    survived_overall = survival_list.count(1)
    with_family_survived = 0
    for i in range(len(survival_list)):
        if siblings[i] == 1 or parents[i] == 1 or parents[i] == 2:
            if survival_list[i] == 1:
                with_family_survived += 1
    no_family_survived = survived_overall - with_family_survived
    if no_family_survived > with_family_survived:
        return True
    else:
        return False



# TODO 16 - What was the average passenger fare?
def avg_passenger_fare(fare_list):
    avg_fee = average_number(fare_list)
    return avg_fee




# TODO 17 - How does the survival rate differ between the 3 ports of embarkation?
def survival_rate_embarkation(embark_list, survival_list):
    ports = []
    port1_survived = 0
    port2_survived = 0
    port3_survived = 0
    for i in range(len(embark_list)):
        if i != len(embark_list) - 1 and embark_list[i] != embark_list[i + 1] and embark_list[i] \
        not in ports:
            ports.append(embark_list[i])
    for i in range(len(survival_list) - 2):
        if embark_list[i] == ports[0] and survival_list[i] == 1:
            port1_survived += 1
        if embark_list[i] == ports[1] and survival_list[i] == 1:
            port2_survived += 1
        if embark_list[i] == ports[2] and survival_list[i] == 1:
            port3_survived += 1
    port_population = [embark_list.count(ports[0]), embark_list.count(ports[1]), embark_list.count(ports[2])]
    p1_survival_rate = port1_survived / port_population[0]
    p2_survival_rate = port2_survived / port_population[1]
    p3_survival_rate = port3_survived / port_population[2]
    survival_rates = [p1_survival_rate, p2_survival_rate, p3_survival_rate]
    return survival_rates




# TODO 18 - Draw a horizontal histogram of survival based on age bins 10.  For example,
# if the data is 9, 33, 22, 55, 8, 52, 65, 55, 0, 50 then
# the 00-09 bin is ***
# the 10-19 bin is 
# the 20-29 bin is *
# the 30-39 bin is *
# the 40-49 bin is 
# the 50-59 bin is ****
# the 60-69 bin is *
def age_bins(age_list):
    histogram = ''

    bins = [0] * 15
    for age in age_list:
        bins[int(age) // 10] += 1
    print(f'bins: {bins}')

    # Dominick:  build your histogram that will be returned
        
        # if 0 < a < 9:
        #     count += 1
        #     histogram = histogram + f"\n{len(asterict_counts) * '*'}"
        # if 10 < a < 19:
        #     asterict_counts = []
        #     asterict_counts.append(a)
        #     histogram = histogram + f"\n{len(asterict_counts) * '*'}"
        # if 20 < a < 29:
        #     asterict_counts.append(a)
        #     return len(asterict_counts)
        # if 30 < a < 39:
        #     asterict_counts.append(a)
        #     return len(asterict_counts)
        # if 40 < a < 49:
        #     asterict_counts.append(a)
        #     return len(asterict_counts)
        # if 50 < a < 59:
        #     asterict_counts.append(a)
        #     return len(asterict_counts)
        # if 60 < a < 69:
        #     asterict_counts.append(a)
        #     return len(asterict_counts)
    # histogram = f"{_10_19_bin * '*'}\n{_20_29_bin * '*'}\n{_30_39_bin * '*'}\n{_40_49_bin * '*'}\n{_50_59_bin * '*'}\n{_60_69_bin * '*'}"
    return histogram




# TODO 19 - (8 points) How does the survival rate differ between the fares of
# the 1st class passengers?
def first_class_rates(pclass_list, survival_list, fare_list):
	first_class_survivors = 0
	first_class_death = 0
	for i in range(len(pclass_list)):
		if pclass_list[i] == 1:
			if survival_list[i] == 1:
				first_class_survivors += 1
			else:
				first_class_death += 1



# TODO 20 - How many Mr./Master., Mrs./Miss./Mme, and Other titles?  Group Mr. and Master.
# Group Mrs., Miss., and Mme.  Group everything else together in one group.
def titles(name_list):
    mister_and_master = 0
    miss_and_mrs = 0
    everything_else = 0
    listed_names = []
    for name in name_list:
        if 'Mr.' in name or 'Master.' in name:
            mister_and_master += 1
            listed_names.append(name)
        elif 'Mrs.' in name or 'Miss' in name:
            miss_and_mrs += 1
            listed_names.append(name)
        else:
            everything_else += 1
    title_list = [mister_and_master, miss_and_mrs, everything_else] 
    return title_list
        



# TODO 21 - How many different family names?  Your function should return a list
# that has no duplicates.
def diff_family_names(name_list):
    families = []
    for i in range(len(name_list)):
        split = name_list[i].split(',')
        name_list[i] = split[0][1:]
        families.append(name_list[i])
    lastnames = len(set(families))
    return lastnames




# TODO 22 - (12 points) How many people are in each family name?
# Your function should return a 2D list like
#     [ ['Verret', 5], ['McCall', 2], ['Sunda-Meya', 3]]
# meaning the Verret family has 5 members, the McCall's 2, and the Sunda-Meya's 3.
def familynamecount(name_list):
    lastnames_here = []
    answer_list = []
    for i in range(len(name_list)):
        split = name_list[i].split(',')
        name_list[i] = split[0][1:]
        lastnames_here.append(name_list[i])
    lastnames = set(lastnames_here)
    for name in lastnames:
        answer_list.append([name, name_list.count(name)])
    
    return sorted(answer_list)




if __name__ == "__main__":
    main()