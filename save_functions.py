def init():
    pokemon_dict_list = []
    save_file = open("save.txt", "r")
    index_number = 1
    for line in save_file:
        info = line.split(",")
        pokemon_name = info[0]
        count = int(info[1])
        new_dict = {
            "Index": index_number,
            "Name": pokemon_name,
            "Count": count
        }
        pokemon_dict_list.append(new_dict)
        index_number += 1
    return pokemon_dict_list

    
def save(legendary_list):
    save_file = open("save.txt", "w")
    for dictionary in legendary_list:
        string = dictionary["Name"] + "," + str(dictionary["Count"]) + "\n"
        save_file.write(string)
    save_file.close()