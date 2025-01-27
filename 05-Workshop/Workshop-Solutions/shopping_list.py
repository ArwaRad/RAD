#----------------------------------------------------------------
#
# Shopping list
#
# Develop an interactive program which repeatedly prompts the
# user to enter a grocery item (as text) to be added to a shopping
# list.
#
# The procedure should stop when string 'stop' is entered,
# and a complete, alphabetically sorted list of grocery items
# should be then printed to the screen, one item per line.
#


#---------------------------------------------------------
#
# A suggested problem solving strategy:
#
# 1. Initialise a list variable to hold the shopping list
# 2. Get the first input from the user
# 3. As long as the user's input is not 'stop':
#    a. Add the item entered by the user to the shopping list
#    b. Get the next input from the user
# 4. Sort the shopping list
# 5. Print the shopping list, one item per line
#

# An interactive process which repeatedly prompts the
# user to enter a grocery item 

# 1. Initialise a list variable to hold the shopping list
shopping_list = []

# 2. Get the first input from the user
response = input('Please enter a grocery item or "stop": ')

# 3. As long as the user's input is not 'stop':
while response != 'stop':
    # a. Add the item entered by the user to the shopping list
    shopping_list.append(response)
    # b. Get the next input from the user
    response = input('Please enter a grocery item or "stop": ')

# 4. Sort the shopping list
sorted_list = sorted(shopping_list)

# 5. Print the shopping list, one item per line
for item in sorted_list:
    print(item)
