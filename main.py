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
                print("It says...")
                print("Domestication Center of the United States of America")
                print("Established in 1963")
                direction = input(question_where_to_look)
                continue
            elif closer_look == "n":
                print("Ok. " + direction)
            else:
                print(invalid_input_text)
                direction = input(question_where_to_look)
                continue
        elif direction == Direction.FORWARD.value:
            print("In front of you is the sleeping wolf. There is a bag that says Dog Food.")
            print("And a green backpack with a picture of the sleeping wolf.")
            print("Underneath the picture is written Mowie.")
            back_pack = input("Would you like to look in the backpack?(y/n): ")
            if back_pack == "y":
                print("Inside is a safe with a four digit code, there is also a tennis ball.")
                print("The backpack also includes a knife, and a tiny bottle")
                print("that has one sentence clearly written and the next faded away.")
                print("The bottle reads: This bottle contains a drug that will put animals to sleep.")
                tiny_bottle = input("Would you like to take the drug?(y/n): ")
                if tiny_bottle == "y":
                    print("You take in the drug and immediately feel sick. You start to feel dizzy.")
                    print("Your partner " + partner_name + ", looks at you in horror.")
                    print("Apparently you didn't realize that this drug could poison you.")
                    print("Don't you recall me telling you that the second sentence had been faded away?")
                    print("You have died.")
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
                            print("Dear Doctor Felix Vir,")
                            print("Our wolf friend, Mowie, is doing great. He's ")
                            print("just about tamed. He'll be like any dog in no time.")
                            print("Mowie loves to play tennis.")
                        else:
                            print("Ok.")
                        open_box = input("Would you like to open the box?(y/n): ")
                        if open_box == "y":
                            num2 = input("Enter four digits: ")
                            if num2 == "1963":
                                print("It pops open. Inside you find a key. Just ")
                                print("what you need to open the door. You decide ")
                                print("to take Mowie with you. You take the backpack ")
                                print("and stuff in the dog food. You take the ball out ")
                                print("and grab Mowie's attention. The domesticaters ")
                                print("have tamed him well. He follows right along. ")
                                print("You take the key and unlock the door. You, ")
                                print(partner_name + ", and Movie run out.")
                                print("You and your party have escaped! Congratulations!")
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
            print("To your right is a 2ft by 3ft glass window. Adjacent to it is a door.")
            print("However this door is locked, and there is no keyhole from the inside.")
            print("You're locked in. ")
            direction = input(question_where_to_look)
            continue
        elif direction == Direction.LEFT.value:
            print("To your left is your partner " + partner_name2 + " and a bookshelf ")
            print("filled with first aid supplies and little bottles. The ones closest ")
            print("to you read: Valium sedative: Use in an emergency. The patient will ")
            print("be asleep for four to six hours. Another bottle reads: Benadryl. ")
            print("Helps with coughing, sneezing, itchy or watery eyes, and itchy nose. ")
            print("Take the right amount of dose or drowsiness and other side effects ")
            print("may occur. The last bottle reads: Beware! Don't open! This bottle ")
            print("contains Leech saliva. If used improperly it can cause a ")
            print("severe allergic reaction! ")
            drug = input("Would you like to take in one of the bottles?(y/n): ")
            if drug == "y":
                identify = input(
                    "Which drug would you like to take? Valium Sedative(V), Benadryl(B) or Leech saliva(LS)? ")
                if identify == "V":
                    print(partner_name2 + " shakes her head at you but you take it in anyway. ")
                    print("Once you take it in you start to feel drowsy. Your partner screams ")
                    print("for help but there is no one to help you. About 15 to 30 minutes ")
                    print("later you fall unconscious. You have died. ")
                    exit()
                elif identify == "B":
                    print("You take in the pink cherry flavor fluid. Sometime later ")
                    print("you fall asleep. A few hours later you wake up. ")
                    direction = input(question_where_to_look)
                    continue
                elif identify == "LS":
                    print("You take off the bottle cap. When you rotate the opening ")
                    print("of the bottle toward your mouth you realize there is no ")
                    print("liquid, instead there are some pieces of paper. You take ")
                    print("it out, and start to read it. It reads: The bookshelf is ")
                    print("door. Press the right buttons to escape. ")
                    door = input("Enter three letters to push the buttons you want: ")
                    if door == "LSB":
                        print("The bookshelf shifts open. You see a pitch dark passage.")
                        print(partner_name2 + " and you walk in. You feel your way through ")
                        print("when you bump right into a rock hard surface. You feel ")
                        print("the surface and find a locker. Thankfully it's open and ")
                        print("you find a flashlight and switch it on. You find the wall ")
                        print("you'd bumped into and turned to the left. On your left is ")
                        print("a clear passage way. You walk for a while. ")
                        print("Out of nowhere a man dressed in clown's outfit with a ")
                        print("black curly mustache and a top hat, also holding a baton ")
                        print("jumps you and " + partner_name2 + " by his presence. He says: ")
                        print("Welcome to Escape the Riddle! You're about to reach the end ")
                        print("of this passage which will get you out of here. But in ")
                        print("order for that to happen. You must answer my riddle ")
                        print("CORRECTLY! If not you will be fed to my pets. You see ")
                        print("a fierce lion beside the man. You and " + partner_name2)
                        print(" agree to the challenge. Good. Good. Says the man. ")
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
                                    print("Bingo! You're a smart one! Let's see if you can ")
                                    print("get this last one. What will be your fate? ")
                                    print("Try this: What word in the English language ")
                                    print("does the following: the first two letters signify ")
                                    print("a male, the first three letters signify a female, ")
                                    print("the first four letters signify a great, while the ")
                                    print("entire word signifies a great woman. What is the word? ")
                                    print("(Hint: This word sounds like a drug but it's spelled differently). ")
                                    answer4 = input("Enter your answer in lowercase: ")
                                    if answer4 == "heroine":
                                        print("How perplexing! This was a really tricky one. ")
                                        print("You have a really intelligent brain! You have earned ")
                                        print("your freedom. The man opens the door for you to ")
                                        print("escape. You and your party have escaped. Congrats!")
                                        exit()
                                    else:
                                        print("Was my hint not helpful? ")
                                        print("You know I really wanted you to escape. But ")
                                        print("you didn't get the right answer. Your fate? ")
                                        print("You will be my servant. That is as much ")
                                        print("mercy as I can give you. You and " + partner_name2)
                                        print(" are now his servants.")
                                        exit()
                                else:
                                    print("Nope! That's incorrect. This was a bit tricky. ")
                                    print("It tries to play with your mind to think about ")
                                    print("Something flying. No? You've come this far.")
                                    print("I'll give you my mercy. The man opens the door ")
                                    print("for you to escape. You and your party have escaped ")
                                    print("Congrats!")
                                    exit()
                            else:
                                print("Mmmm. Sorry but that's incorrect.")
                                print("I know, I know. This riddle makes ")
                                print("you think too hard when it's really easy. I know ")
                                print("what you're thinking. You think I'll feed you to ")
                                print("my pets. But since you answered the first one ")
                                print("correctly I'll give you my mercy. The man opens ")
                                print("The door for you to escape. You and your party ")
                                print("have escaped. Congrats! ")
                                exit()
                        else:
                            print("I'm sorry you're incorrect. I gave you a really easy one. ")
                            print("Sigh. You will be fed to my pets. The man watches as the ")
                            print("lion eats you and your partner. You have died.")
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
            print("In front of you is a sign about washing hands. On its right ")
            print("is a sign about eating healthy. On its left is a sign about kindness. ")
            print("Below is a drawing of an entrance behind a bookshelf. ")
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
        # ready = input(question_are_you_ready)
        ready = "y"
        if ready == "n":
            print(come_back_text)
            exit()
        if ready == "y":
            your_room = "nurses office"  # random.choice(list(room_dict.keys()))
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
