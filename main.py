from save_functions import save, init
from datetime import datetime
import time 

def main_menu(legendary_list):
    current_pokemon = None
    last_selected_menu = None
    while True:
        print("Here is a list of all Pokémon we are tracking currently and their count: \n")
        for dictionary in legendary_list:
            drop_chance_so_far = pow(99/100, dictionary["Count"])
            print(str(dictionary["Index"]) + ". " + dictionary["Name"] + ": " + str(dictionary["Count"]) + ".  Chance: {:.3%}".format(1 - drop_chance_so_far))
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("\nCurrent Time =", current_time)
        
        if current_pokemon == None:
            print("You have yet to select a Pokémon!")
        else:
            try:
                selected_pokemon_index = int(current_pokemon)
                for dictionary in legendary_list:
                    if selected_pokemon_index == dictionary["Index"]:
                        print("Current Pokémon: " + dictionary["Name"])
                        break
            except:
                print("Current Pokémon: " + current_pokemon)
    
        print("\nOperations: Save(S), Increase Pokémon(I), Decrease Pokémon(D), Select current hunt(P), Save and quit(Q)")
        main_menu_input = input("What would you like to do?: ").lower()
        if main_menu_input == "":
            main_menu_input = last_selected_menu

        if main_menu_input == "s":
            save(legendary_list)
            print("...\nSaved!\n")
        elif main_menu_input == "i":
            increase_count(legendary_list, current_pokemon)
            last_selected_menu = "i"
        elif main_menu_input == "d":
            decrease_count(legendary_list, current_pokemon)
            last_selected_menu = "d"
        elif main_menu_input == "p":
            current_pokemon = select_current_count(legendary_list)
            last_selected_menu = "p"
        elif main_menu_input == "q":
            save(legendary_list)
            exit()
        else:
            print("Incorrect input, please try again.")

def decrease_count(legendary_list, current_pokemon):
    if current_pokemon == None:
            print("You have to choose a Pokémon first.")
            return legendary_list

    for dictionary in legendary_list:
        if dictionary["Name"].lower() == current_pokemon.lower() or str(dictionary["Index"]) == current_pokemon:
            dictionary.update({"Count": dictionary["Count"] - 1})
            return legendary_list
            
    new_pokemon = {
        "Name": current_pokemon,
        "Count": 0,
        "Index": len(legendary_list) + 1
    }
    legendary_list.append(new_pokemon)

    return legendary_list

def increase_count(legendary_list, current_pokemon):
    if current_pokemon == None:
        print("You have to choose a Pokémon first.")
        return legendary_list

    for dictionary in legendary_list:
        if dictionary["Name"].lower() == current_pokemon.lower() or str(dictionary["Index"]) == current_pokemon:
            dictionary.update({"Count": dictionary["Count"] + 1})
            return legendary_list

    new_pokemon = {
        "Name": current_pokemon,
        "Count": 1,
        "Index": len(legendary_list) + 1
    }

    legendary_list.append(new_pokemon)
    return legendary_list

def select_current_count(legendary_list):
    for dictionary in legendary_list:
        print(str(dictionary["Index"]) + ". " + dictionary["Name"] + ": " + str(dictionary["Count"]))
    current_pokemon = input("Write the name of your current Pokémon or write a new name to create a new one: ")
    return current_pokemon

dict_list = init()
main_menu(dict_list)
