# Lwando Gqobho Class 1
import random
from datetime import date


def winning_numbers():  # The function generates the six random numbers for the draw
    """
    >>> all([1 <= i <= 49 for i in winning_numbers()])
    True
    """
    random_list = []
    while len(random_list) < 6:
        ran_num = random.randint(1, 49)  # Specifying the range
        if ran_num not in random_list:  # Checking if the generated number is not already in the list, avoid duplicates.
            random_list.append(ran_num)

    return random_list


def age_test(age):  # This function returns True if age is 18 and above, else False.
    """
    >>> age_test(16)
    False
    >>> age_test(22)
    True
    """
    if age >= 18:
        return True
    else:
        return False


def selection_sort(my_list):  # This function accepts a list as a parameter and sorts it in ascending order.
    """
    >>> selection_sort([28, 21, 7, 16])
    [7, 16, 21, 28]
    """
    for i in range(len(my_list)):
        min_pos = i  # minimum position initialised to i, in case nothing is smaller than the value at index i
        for j in range(i+1, len(my_list)):
            if my_list[min_pos] > my_list[j]:  # finding the smallest value index of each iteration
                min_pos = j

        swap(my_list, i, min_pos)  # Minimum value index swapped with i
    return my_list  # return the sorted list


# This function takes a list and two indices as parameters and returns the list with values of the indices swapped.
def swap(my_list, i, j):
    """
    >>> swap([4, 8, 3, 5], 1, 3)
    [4, 5, 3, 8]
    """
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp
    return my_list


def count_matches(lotto_list, user_list):  # Counting the number of matching items between two lists
    """
    >>> count_matches([4, 15, 26, 38, 41, 47], [2, 4, 9, 15, 23, 39])
    2
    """
    count = 0
    for i in user_list:
        if i in lotto_list:  # If one item found in the other list, then increment count.
            count += 1
    return count


# Determining amount won by user according to the number of numbers guessed correctly.
def player_winnings(matches):
    """
    >>> player_winnings(4)
    2384.0
    """
    total = 0
    # defining a dict switcher mapping the number of correct guesses to the amount to be won.
    switcher = {
        0: 0.0,
        1: 0.0,
        2: 20.0,
        3: 100.50,
        4: 2384.0,
        5: 8584.0,
        6: 10000000.0
    }
    return switcher.get(matches)  # returning the amount.


def write_to_file(name, age, user_numbers):
    lotto_numbers = winning_numbers()
    selection_sort(lotto_numbers)
    f = open('results.txt', 'a')
    f.write("Today's winning numbers: " + str(lotto_numbers) + "\n")
    f.write("Date: " + str(date.today()) + "\n")
    f.write("Name: " + name + "\n")
    f.write("Age: " + str(age) + "\n")
    f.write("Number of numbers guessed correctly: " + str(count_matches(lotto_numbers, user_numbers)) + "\n")
    f.write("Amount won: R" + str(player_winnings(count_matches(lotto_numbers, user_numbers))) + "\n")
    f.write("\n")
