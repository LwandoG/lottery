# Lwando Gqobho Class 1
import project_functions


name = input("Enter name\n")
age = int(input("Enter your age\n"))


# Now we test if the user is old enough with age_test function from project_functions
if project_functions.age_test(age):  # if age_test returns true, the program continues
    user_numbers = []
    try:
        while len(user_numbers) < 6:  # Making sure we get six numbers from user.
            curr_num = int(input("Enter lotto number"))
            if curr_num not in user_numbers and curr_num in range(1, 49):  # Number validation
                user_numbers.append(curr_num)
    except ValueError:
        print("Invalid Value")
    project_functions.selection_sort(user_numbers)  # Sorting the user's numbers
    project_functions.write_to_file(name, age, user_numbers)  # Finally write to the file.


else:
    print("You are too young to play.")  # Print appropriate message and terminate if player underage.
