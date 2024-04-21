import dwarf
import elf
import archery
import fighting
import fire
import healing
import check_input

def main():

    print("Character Maker!")
    print("Choose your character: ")
    print("1. Dwarf")
    print("2. Elf")
    print("3. Halfling")
    char_choice = check_input.get_int_range("Enter choice: ", 1 ,3)
    print()
    c = None
    char_name = input("What is your character's name? ")
    if char_choice == 1:
        c = dwarf.Dwarf(char_name)
    elif char_choice == 2:
        c = elf.Elf(char_name)
    elif char_choice == 3:
        c = halfling.Halfling(char_name)
    print(c)
    ability = 0
    print("You have 5 points to spend on abilities: ")
    points = 5
    while points > 0 and ability !=5:
        print ("Add an ability:")
        print("1. Archery")
        print("2. Fighting")
        print("3. Fire Magic")
        print("4. Healing")
        ability = check_input.get_int_range("Enter ability: ", 1, 4)
        print()
        points -= 1
        if ability == 1:
            c = archery.Archery(c)
        elif ability == 2:
            c = fighting.Fighting(c)
        elif ability == 3:
            c = fire.Fire(c)
        elif ability == 4:
            c = healing.Healing(c)
        print(c)
    if c.constitution() > 0 and c.strength() > 0 and c.wisdom() > 0:
        print("Congratulations! you have creted your character")
    else:
        print("Sorry, your character has failed to survive. Try again")
        print(c)
main()