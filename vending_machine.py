personal_cash = 25
item_names = ['Mentos', 'Zero coke', 'Cheese', 'Latte Coffee']
item_costs = [4.5, 6, 7.5, 4]
item_counts = [2, 3, 5, 1]


def item_list():
    for item_name, item_cost, item_count in zip(item_names, item_costs, item_counts):
        print(f"Name: {item_name}, Cost: {item_cost}, Count: {item_count}")


def start_user():
    print("Welcome to Vending machine")
    print(f"you have got {personal_cash} cash.")
    item_list()
    input_item = input("Please choose an item:\n")
    choose_item(input_item)


def choose_item(input_item):
    global personal_cash
    try:
        item_index = item_names.index(input_item)
        if item_counts[item_index] > 0 and personal_cash > item_costs[item_index]:
            item_counts[item_index] = item_counts[item_index] - 1
            personal_cash -= item_costs[item_index]
        item_list()
        print(f"you have got {personal_cash} cash.")
        user_choose = input("Would you like to buy something else? 'Y' or 'N' \n")
        if user_choose == "Y":
            start_user()
        elif user_choose == "N":
            print("Thank you see you next time!")
        else:
            print("Incorrect answer!")
    except:
        print("Incorrect item, please try again!")


if __name__ == '__main__':
    start_user()
