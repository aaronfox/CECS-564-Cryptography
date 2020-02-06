# Aaron Fox
# Assignment 2 Problem 1
print('hi')
# Finds distribution permutations over Pn and how often their count
list_of_viable_perms = []


def permutation_distribution_solver_util(array, index, num, reduced_num):
    if reduced_num < 0:
        return

    # Then a combination was found
    if reduced_num == 0:
        # list_of_viable_perms.append(array)
        for i in range(index):
            potential_array = array[0:index]
            if potential_array not in list_of_viable_perms:
                list_of_viable_perms.append(potential_array)
            #     print(array[i], end=" ")
            # print("")
        return

   # Keep track of previous value to ensure potential new numbers are increasing or the same
    if index == 0:
        previous = 1
    else:
        previous = array[index - 1]

    # Only need numbers from 1 through 3 for Psub4, for example
    for i in range(previous, n + 1):
        array[index] = i

        # Recursively call util function
        permutation_distribution_solver_util(
            array, index + 1, num, reduced_num - i)


# JUST CHANGE N HERE FOR FIGURING OUT THE DISTRIBUTION AND COUNTS
# The main number to figure out the factorial from is n:
n = 12
arr = [0] * n
permutation_distribution_solver_util(arr, 0, n, n)
# print(str(list_of_viable_perms))
for l in list_of_viable_perms:
    print(l[::-1])
print("Length of viable combinations == " + str(len(list_of_viable_perms)))

running_value = 0
viable_perms_and_values = {}

for l in list_of_viable_perms:
    print("for l == " + str(l))
    this_l_mult = 1
    this_n = n
    # Must account for dividing by factorial amount of duplicate
    # cycle counts such as dividing by 2! for 2, 2, 1 in Psub5
    # and by 3! for 2, 2, 2, 1 in Psub7
    # TODO: Keep list of all the numbers to divide by in case there are multiple duplicates
    occurrences = {}
    for element in l:
        if element not in occurrences and element is not 1:
            occurrences[element] = 1
        elif element is not 1:
            occurrences[element] = occurrences[element] + 1
    print("occurrences == " + str(occurrences))
    number_to_divide_by = 1
    numbers_to_factorial_divide_by = []
    for value in occurrences.values():
        number_to_divide_by = number_to_divide_by * value
        if value > 1:
            numbers_to_factorial_divide_by.append(value)

    for i in l:
        temp_i = i
        this_i_mult = 1
        while temp_i > 1:
            for k in range(0, i):
                print("multiplying " + str(this_i_mult) + " * " +
                      str(this_n) + " to get " + str(this_i_mult * this_n))
                this_i_mult = this_i_mult * this_n
                # this_l_mult = this_l_mult * this_n * (this_n - 1)
                this_n = this_n - 1
                temp_i = temp_i - 1
            if temp_i != i:
                this_i_mult = this_i_mult / i
                print("!this_i_mult == " + str(this_i_mult) + " i == " + str(i))
            else: # identity combination
                this_i_mult = 1
                print("this_i_mult == 1")
        this_l_mult = this_l_mult * this_i_mult
        print("running total_l_mult == " + str(this_l_mult))


    # number_to_divide_by should actually be the factorial of the reoccurring numbers
    for i in range(number_to_divide_by - 1, 1, -1):
        number_to_divide_by = number_to_divide_by * i

    running_divide_by_num = 1
    for number_to_divide_byx in numbers_to_factorial_divide_by:
        for i in range(number_to_divide_byx - 1, 1, -1):
            number_to_divide_byx = number_to_divide_byx * i
        running_divide_by_num = running_divide_by_num * number_to_divide_byx
        

    running_value = running_value + this_l_mult / running_divide_by_num#number_to_divide_by
    viable_perms_and_values[str(l[::-1])] = this_l_mult / running_divide_by_num#number_to_divide_by
    print("running value == " + str(running_value))


print("running value == " + str(running_value))
print("viable_perms_and_values == " + str(viable_perms_and_values))
