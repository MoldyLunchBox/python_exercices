cookbook = {
            "sandwich": 
                {
                    "ingredients":
                        {
                            "ham", "bread","cheese", "tomatoes"
                        },
                    "meal": "lunch", 
                    "prep_time": "10 minutes"
                },
            "Cake": 
                {
                    "ingredients":
                        {
                            "flour", "sugar","eggs"
                        },
                    "meal": "dessert", 
                    "prep_time": "60 minutes"
                },
            "Salad": 
                {
                    "ingredients":
                        {
                            "avocado", "arugula", "tomatoes", "spinach"
                        },
                    "meal": "lunch", 
                    "prep_time": "15 minutes"
                },
            }


def print_func(meal):
    print(meal)
    for  key in cookbook:
        if (key == meal):
            print (cookbook[key]["ingredients"])

def main():
    choice = 0
    while (int(choice) < 1 or int(choice) > 5):
        choice = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
    if (int(choice) == 3):
        choice = input("Please enter the recipe's name to get its details:\n")
        print_func(choice)
    if (int(choice) == 1):
        choice = input("Please enter the recipe's name to get its details:\n")
        print_func(choice)
if __name__ == '__main__':
    main()