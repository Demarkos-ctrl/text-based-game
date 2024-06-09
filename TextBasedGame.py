# TextBasedGame.py
# Demarko Stephens
def show_instructions():
    print("Welcome to the Amusement Park Adventure Game!")
    print("Navigate the park, procure items, and outsmart the basket case to reclaim the Ferris")
    print("wheel before the attendees arrive.")
    print("Gather these essential items from the specified location to contain the basket case:")
    print("  - Lock Key: Found in Carousel Corner. Secure the basket case back into its place.")
    print("  - Special Sunglasses: Found in Haunted House. Subdue the basket case's unruly behavior")
    print("    with their unique lens.")
    print("  - Cash: Found in Main Street. Utilize it to negotiate or bribe the basket case.")
    print("  - Coffee Cup: Found in Food Court. Maintain your energy with a steaming cup of coffee.")
    print("  - Steel Toe Boots: Found in Gift Shop. Shield your feet from the basket case's antics.")
    print("  - iPhone: Found in Arcade Alley. Connect with allies and document your journey.")
    print("Commands: n, s, e, w for North, South, East, and West.")


def show_status(current_room, inventory, room_items):
    print("----------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if current_room in room_items:
        item = room_items.pop(current_room)
        inventory.append(item)
        print(f"You automatically picked up: {item}")
    if current_room == "Ferris Wheel":
        print("You see the Basket Case here!")
        print("Make sure you have collected all items before facing the Basket Case.")
    print("----------------------")
    print("Enter your move (n, s, e, w) or 'quit':")


def main():
    rooms = {
        "Entrance Plaza": {
            "N": {"room": "Food Court", "item": "Coffee Cup"},
            "E": {"room": "Haunted House", "item": "Special Sunglasses"},
            "S": {"room": "Gift Shop", "item": "Steel Toe Boots"},
            "W": {"room": "Main Street", "item": "Cash"}
        },
        "Main Street": {"E": {"room": "Entrance Plaza"}},
        "Food Court": {"S": {"room": "Entrance Plaza"}, "E": {"room": "Carousel Corner"}},
        "Carousel Corner": {"W": {"room": "Food Court"}},
        "Gift Shop": {"N": {"room": "Entrance Plaza"}, "E": {"room": "Ferris Wheel"}},
        "Haunted House": {"W": {"room": "Entrance Plaza"}, "N": {"room": "Arcade Alley"}},
        "Arcade Alley": {"S": {"room": "Haunted House"}},
        "Ferris Wheel": {"W": {"room": "Gift Shop"}}
    }
    inventory = []
    current_room = "Entrance Plaza"
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms[current_room])
        move = input().lower()
        if move in ['n', 's', 'e', 'w']:
            direction = move.upper()
            if direction in rooms[current_room]:
                next_room_info = rooms[current_room][direction]
                next_room = next_room_info["room"]

                if "item" in next_room_info:
                    item = next_room_info.pop("item")
                    inventory.append(item)
                    print(f"You automatically picked up: {item}")

                if next_room == "Ferris Wheel":
                    required_items = sorted(
                        ['Lock Key', 'Special Sunglasses', 'Cash', 'Coffee Cup', 'Steel Toe Boots', 'iPhone'])
                    if sorted(inventory) == required_items:
                        print(
                            "Congratulations! You have all items and have safely dealt with the Basket Case. You win!")
                        break
                    else:
                        print("AUHHHH! YOU'VE BEEN BASKETIZED. The Basket Case caught you before you were prepared! "
                              "GAME OVER.")
                        break
                else:
                    current_room = next_room
            else:
                print("You can't go that way!")
        elif move == 'quit':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
