from escape_room import *
from introduction import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(direction_text)

    loop_var = 0

    while loop_var != -1:
        ready = input(question_are_you_ready)
        if ready == "n":
            print(come_back_text)
            exit()
        if ready == "y":
            your_room = random.choice(list(room_dict.keys()))
            print(room_dict[your_room])
            partner_name = introduce_partner(your_room)
            print(room_intro_dic[your_room].format(partner_name=partner_name))
            play(your_room, partner_name)
            break
        else:
            print(invalid_input_text)
