import random

from data import *
from enums import *


def introduce_first_partner():
    gender = input("If you ever get a partner do you prefer male or female?(m/f): ")
    temp_partner_name = ""
    if gender == Gender.MALE.value:
        temp_partner_name = random.choice(male_partner_name_arr)
        print(male_partner_1_intro.format(partner_name=temp_partner_name,
                                          partner_hair=random.choice(partner_appearance_arr),
                                          partner_looks=random.choice(male_partner_accessories_arr),
                                          partner_height=random.choice(height_arr)))

    elif gender == Gender.FEMALE.value:
        temp_partner_name = random.choice(female_partner_name_arr)
        print(female_partner_1_intro.format(partner_name=temp_partner_name,
                                            partner_hair=random.choice(partner_appearance_arr),
                                            partner_looks=random.choice(female_partner_accessories_arr),
                                            partner_height=random.choice(height_arr)))
    return temp_partner_name


def introduce_second_partner():
    gender = input("If you ever get a partner do you prefer male or female?(m/f): ")
    temp_partner_name2 = ""
    if gender == Gender.MALE.value:
        temp_partner_name2 = random.choice(male_partner_name_arr)
        print(male_partner_2_intro.format(partner_name2=temp_partner_name2,
                                          partner_hair=random.choice(partner_appearance_arr),
                                          partner_looks=random.choice(male_partner_accessories_arr),
                                          partner_height=random.choice(height_arr)))

    elif gender == Gender.FEMALE.value:
        temp_partner_name2 = random.choice(female_partner_name_arr)
        print(female_partner_2_intro.format(partner_name2=temp_partner_name2,
                                            partner_hair=random.choice(partner_appearance_arr),
                                            partner_looks=random.choice(female_partner_accessories_arr),
                                            partner_height=random.choice(height_arr)))
    return temp_partner_name2


def escape_room1(partner_name):
    direction = input(question_where_to_look)
    while True:
        if direction == Direction.RIGHT.value:
            print("To your right is your partner " + partner_name + ",")
            print("and the bars and the cell door. On the door is a lock. A key may come in handy!")
            direction = input(question_where_to_look)
            continue
        elif direction == Direction.LEFT.value:
            print("To your left is a wooden bench and a metal stone wall.")
            print("The wall has been scratched with little writings.")
            closer_look = input("Would you like to take a closer look?(y/n): ")
            if closer_look == "y":
                print(scratched_writings_room1)
                direction = input(question_where_to_look)
                continue
            elif closer_look == "n":
                print("Ok. " + direction)
            else:
                print(invalid_input_text)
                direction = input(question_where_to_look)
                continue
        elif direction == Direction.FORWARD.value:
            print(direction_forward_room1)
            back_pack = input("Would you like to look in the backpack?(y/n): ")
            if back_pack == "y":
                print(inside_backpack_room1)
                tiny_bottle = input("Would you like to take the drug?(y/n): ")
                if tiny_bottle == "y":
                    print(take_tiny_bottle_room1.format(partner_name=partner_name))
                    exit()
                elif tiny_bottle == "n":
                    print("Ok.")
                else:
                    print("Invalid input.")
                open_safe = input("Would you like to open the safe?(y/n): ")
                if open_safe == "y":
                    num = input("Enter seven digits(Hint:Look at the message when you turn left): ")
                    if num == "4321191":
                        print("It pops open. Inside you find a box that needs")
                        print("a four digit code. There is also a letter.")
                        letter = input("Would you like to open the letter?(y/n): ")
                        if letter == "y":
                            print(letter_room1)
                        else:
                            print("Ok.")
                        open_box = input("Would you like to open the box?(y/n): ")
                        if open_box == "y":
                            num2 = input("Enter four digits: ")
                            if num2 == "1963":
                                print(open_box_room1.format(partner_name=partner_name))
                                exit()
                            elif num2 != "1963":
                                print("You punch it in. Beep. Beep. Beep.")
                                print("That code is incorrect.")
                                direction = input(question_where_to_look)
                                continue
                        elif open_box == "n":
                            print("Ok.")
                            direction = input(question_where_to_look)
                            continue
                    elif num != "4321191":
                        print("You punch it in. Beep. Beep. Beep.")
                        print("That code is incorrect. Hint: The 'ofs' and 'the' doesn't count.")
                        direction = input(question_where_to_look)
                        continue
            elif back_pack == "n":
                print("(Hint: There's clues in that backpack. You just missed it. Look forward again.)")
                direction = input(question_where_to_look)
                continue
        elif direction == Direction.DOWN.value:
            print("Below you is concrete floor.")
            direction = input(question_where_to_look)
            continue
        elif direction == Direction.UP.value:
            print("Above you is the ceiling.")
            direction = input(question_where_to_look)
            continue
        else:
            print("Invalid input.")
            direction = input(question_where_to_look)
            continue


def escape_room2(partner_name2):
    direction = input(question_where_to_look)
    while True:
        if direction == Direction.RIGHT.value:
            print(direction_right_room2)
            direction = input(question_where_to_look)
            continue
        elif direction == Direction.LEFT.value:
            print(direction_left_room2.format(partner_name2=partner_name2))
            drug = input("Would you like to take in one of the bottles?(y/n): ")
            if drug == "y":
                drug_to_take = input(
                            "Which drug would you like to take? Valium Sedative(v), Benadryl(b) or Leech saliva(ls)? ")
                if drug_to_take == DRUG.VALIUM_SEDATIVE.value:
                    print(take_valium_sedative_room2.format(partner_name2=partner_name2))
                    exit()
                elif drug_to_take == DRUG.BENADRYL.value:
                    print("You take in the pink cherry flavor fluid. Sometime later ")
                    print("you fall asleep. A few hours later you wake up. ")
                    direction = input(question_where_to_look)
                    continue
                elif drug_to_take == DRUG.LEECH_SALIVA.value:
                    print(drug_leech_saliva_room2)
                    door = input("Enter three letters to push the buttons you want: ")
                    if door == "lsb":
                        print(riddle_game_intro_room2.format(partner_name2=partner_name2))
                        print("Your first riddle: This belongs to you, but everyone uses it. ")
                        answer = input("Enter your answer in lowercase: ")
                        if answer == "your name" or answer == "name":
                            print("That was an easy one! Now try this: Which word in the ")
                            print("dictionary is always spelled incorrectly? ")
                            answer2 = input("Enter your answer in lowercase: ")
                            if answer2 == "incorrectly":
                                print("Also an easy one! Good job! You're getting the ")
                                print("hang of it. Now try this: What goes up but never goes down? ")
                                answer3 = input("Enter your answer in lowercase: ")
                                if answer3 == "age" or answer3 == "your age":
                                    print(heroin_riddle_room2)
                                    answer4 = input("Enter your answer in lowercase: ")
                                    if answer4 == "heroine":
                                        print(correct_answer_riddle_heroine_room2)
                                        exit()
                                    else:
                                        print(incorrect_answer_riddle_heroine_room2)
                                        exit()
                                else:
                                    print(incorrect_answer_riddle_age_room2)
                                    exit()
                            else:
                                print(incorrect_answer_riddle_incorrectly_room2.format(partner_name2=partner_name2))
                                exit()
                        else:
                            print(incorrect_answer_riddle_name_room2)
                            exit()
                    else:
                        print(incorrect_text)
                        direction = input(question_where_to_look)
                        continue
                else:
                    print(invalid_input_text)
                    direction = input(question_where_to_look)
                    continue
            else:
                print("OK!")
                direction = input(question_where_to_look)
                continue
        elif direction == Direction.UP.value:
            print("Above you is the ceiling. You see some graffiti that makes out ")
            print("the words 'YOU'LL NEVER ESCAPE!' My advice? Don't listen to that.")
            direction = input(question_where_to_look)
            continue
        elif direction == Direction.DOWN.value:
            print("Below you is the tiled floor. ")
            direction = input(question_where_to_look)
            continue
        elif direction == Direction.FORWARD.value:
            print(direction_forward_room2)
            direction = input(question_where_to_look)
            continue
        else:
            print("Invalid input.")
            direction = input(question_where_to_look)
            continue


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

            if your_room == Room.CELL.value:
                partner_name = introduce_first_partner()
                print(room_1_intro.format(partner_name=partner_name))
                escape_room1(partner_name)
            elif your_room == Room.NURSE_OFFICE.value:
                partner_name2 = introduce_second_partner()
                print(room_2_intro.format(partner_name2=partner_name2))
                escape_room2(partner_name2)
            break
        else:
            print(invalid_input_text)
