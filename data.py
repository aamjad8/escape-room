room_dict = {"cell": "You have been transferred to a cell with a sleeping wolf",
             "nurses office": "You have been transferred to the nurses office in a school."}

male_partner_name_arr = ["Yousef", "Jonah", "Adam", "Umar", "Mike"]
female_partner_name_arr = ["Aa'isha", "Helena", "Hannah", "Jasmine", "Khadijah"]
partner_appearance_arr = ["brown eyes with straight black hair", "gray eyes with curly brown hair",
                          "blue eyes with smooth blond hair", "green eyes with straight red hair",
                          "black eyes with straight black hair", "brown eyes with wavy dark-brown hair"]
partner_accessories_dict = {
    "m": ["black round glasses", "a red baseball cap", "a kufi", "a turban", "a black top hat",
          "sun glasses"],
    "f": ["a pink hijab", "a purple scarf around her neck", "a pearl necklace",
          "big hoop earrings", "black round glasses", "green hijab"]
}

height_arr = ["tall", "short", "average(height)"]

direction_text = ("Directions: Welcome to Escape the Room. In this game you will be sent to a room and be given some "
                  "tools. The rest of you'll have to think wisely. Best of luck!")
room_intro_dic = {"cell": ("You're in a cell with a sleeping wolf."
                           " You might be wondering where exactly are you. Where is this cell?"
                           " This cell is in a building where animals are kept to be domesticated."
                           " You're also with you're partner {partner_name},"
                           " but they won't really help. It's up to you."
                           " You have to find the tools on you're own."
                           " You can look forward, right, left, up and down. You can also use items."
                           " Note that all responses should be lowercase."),
                  "nurses office": ("You're in a nurses office."
                                    " You might be wondering where exactly are you. Where is this office?"
                                    "This nurses office is in Discrete Elementary School, located in Montgomery, "
                                    "Alabama. Established in"
                                    " 1977. You're also with you're partner {partner_name},"
                                    " but they won't really help. It's up to you. "
                                    " You have to find the tools on you're own."
                                    " You can look forward, right, left, up and down. You can also use items."
                                    " Note that all responses should be lowercase.")}

room_partner_intro_dict = {
    "cell": {"m": ("You're partner's name is {partner_name}."
                   " You see {partner_name} quietly devoting his chocolate. He seems unaware"
                   " of the situation. But he is. And that's where you come in to help him."
                   " {partner_name} has {partner_hair}."
                   " He wears {partner_looks}. He's {partner_height}."
                   " He has been transferred from the game 'Open the fridge'."
                   " {partner_name} decided not to put his chocolate behind bars"
                   " which made him end up behind bars."
                   " Thus, he was offered to spin the wheel of fate. His fate brought him here. "),
             "f": ("You're partner's name is {partner_name}."
                   " You see {partner_name} quietly devoting her chocolate. She seems unaware"
                   " of the situation. But she is. And that's where you come in to help her. "
                   "{partner_name} has {partner_hair}."
                   " She wears {partner_looks}. She's {partner_height}."
                   " She has been transferred from the game 'Open the fridge'."
                   " {partner_name} decided not to put her chocolate behind bars"
                   " which made her end up behind bars."
                   " Thus, she was offered to spin the wheel of fate. Her fate brought her here. ")},
    "nurses office": {"m": ("You're partner's name is {partner_name}."
                            " You see {partner_name} sitting on the bed. He seems unaware"
                            " of the situation. But he is. And that's where you come in to help him."
                            " {partner_name} has partner_hair."
                            " He wears {partner_looks}. He's {partner_height}."
                            " He didn't feel well and got trapped in the nurses office."),
                      "f": ("You're partner's name is {partner_name}."
                            " You see {partner_name} sitting on the bed. She seems unaware"
                            " of the situation. But she is. And that's where you come in to help her."
                            " {partner_name} has {partner_hair}."
                            " She wears {partner_looks}. She's {partner_height}."
                            " She didn't feel well and got trapped in the nurses office.")}
}

direction_forward_room1 = ("In front of you is the sleeping wolf. There is a bag that says Dog Food."
                           " And a green backpack with a picture of the sleeping wolf."
                           " Underneath the picture is written Mowie.")
scratched_writings_room1 = ("It says..."
                            " Domestication Center of the United States of America"
                            " Established in 1963")

inside_backpack_room1 = ("Inside is a safe with a four digit code, there is also a tennis ball."
                         " The backpack also includes a knife, and a tiny bottle"
                         " that has one sentence clearly written and the next faded away."
                         " The bottle reads: This bottle contains a drug that will put animals to sleep.")

take_tiny_bottle_room1 = ("You take in the drug and immediately feel sick. You start to feel dizzy."
                          " Your partner {partner_name}, looks at you in horror."
                          " Apparently you didn't realize that this drug could poison you."
                          " Don't you recall me telling you that the second sentence had been faded away?"
                          " You have died.")

letter_room1 = ("Dear Dr. Felix Vir,"
                " Our wolf friend, Mowie, is doing great. He's"
                " just about tamed. He'll be like any dog in no time."
                " Mowie loves to play tennis.")

open_box_room1 = ("It pops open. Inside you find a key. Just"
                  " what you need to open the door. You decide"
                  " to take Mowie with you. You take the backpack"
                  " and stuff in the dog food. You take the ball out"
                  " and grab Mowie's attention. The tamers"
                  " have tamed him well. He follows right along."
                  " You take the key and unlock the door. You,"
                  " {partner_name}, and Mowie run out."
                  "You and your party have escaped! Congratulations!")

direction_right_room2 = ("To your right is a 2ft by 3ft glass window. Adjacent to it is a door."
                         " However this door is locked, and there is no keyhole from the inside."
                         " You're locked in.")

direction_left_room2 = ("To your left is your partner {partner_name} and a bookshelf"
                        " filled with first aid supplies and little bottles. The ones closest"
                        " to you read: Valium sedative: Use in an emergency. The patient will"
                        " be asleep for four to six hours. Another bottle reads: Benadryl."
                        " Helps with coughing, sneezing, itchy or watery eyes, and itchy nose."
                        " Take the right amount of dose or drowsiness and other side effects"
                        " may occur. The last bottle reads: Beware! Don't open! This bottle"
                        " contains Leech saliva. If used improperly it can cause a "
                        " severe allergic reaction!")

direction_forward_room2 = ("In front of you is a sign about washing hands. On its right"
                           " is a sign about eating healthy. On its left is a sign about kindness."
                           " Below is a drawing of an entrance behind a bookshelf.")

take_valium_sedative_room2 = ("{partner_name} shakes their head at you but you take it in anyway."
                              " Once you take it in you start to feel drowsy. Your partner screams"
                              " for help but there is no one to help you. About 15 to 30 minutes"
                              " later you fall unconscious. You have died.")

drug_leech_saliva_room2 = ("You take off the bottle cap. When you rotate the opening"
                           " of the bottle toward your mouth you realize there is no"
                           " liquid, instead there are some pieces of paper. You take"
                           " it out, and start to read it. It reads: The bookshelf is"
                           " door. Press the right buttons to escape.")

riddle_game_intro_room2 = ("The bookshelf shifts open. You see a pitch dark passage."
                           " {partner_name} and you walk in. You feel your way through"
                           " when you bump right into a rock hard surface. You feel"
                           " the surface and find a locker. Thankfully it's open and"
                           " you find a flashlight and switch it on. You find the wall"
                           " you'd bumped into and turned to the left. On your left is"
                           " a clear passage way. You walk for a while."
                           " Out of nowhere a man dressed in clown's outfit with a"
                           " black curly mustache and a top hat, also holding a baton"
                           " jumps you and {partner_name} by his presence. He says:"
                           " 'Welcome to Escape the Riddle! You're about to reach the end"
                           " of this passage which will get you out of here. But in"
                           " order for that to happen. You must answer my riddle"
                           " CORRECTLY! If not you will be fed to my pets.' You see"
                           " a fierce lion beside the man. You and {partner_name}"
                           " agree to the challenge. 'Good. Good.' Says the man.")

heroin_riddle_room2 = ("Bingo! You're a smart one! Let's see if you can"
                       " get this last one. What will be your fate?"
                       " Try this: What word in the English language"
                       " does the following: the first two letters signify"
                       " a male, the first three letters signify a female,"
                       " the first four letters signify a great, while the"
                       " entire word signifies a great woman. What is the word?"
                       " (Hint: This word sounds like a drug but it's spelled differently).")

correct_answer_riddle_heroine_room2 = ("How perplexing! This was a really tricky one."
                                       " You have a really intelligent brain! You have earned"
                                       " your freedom. The man opens the door for you to"
                                       " escape. You and your party have escaped. Congrats!")

incorrect_answer_riddle_heroine_room2 = ("Was my hint not helpful?"
                                         " This was very difficult. It confuses you."
                                         " No? You've come this far. The man opens"
                                         " the door for you to escape. You and your"
                                         " party have escaped. Congrats!")
incorrect_answer_riddle_age_room2 = ("Nope! That's incorrect. This was a bit tricky."
                                     " It tries to play with your mind to think about"
                                     " something flying. No? You've come this far."
                                     " I'll give you my mercy. The man opens the door"
                                     " for you to escape. You and your party have escaped."
                                     " Congrats!")

incorrect_answer_riddle_incorrectly_room2 = ("Mmmm. Sorry but that's incorrect."
                                             " I know, I know. This riddle makes"
                                             " you think too hard when it's really easy. I know"
                                             " what you're thinking. You think I'll feed you to"
                                             " my pets. But since you answered the first one"
                                             " correctly I'll give you my mercy. You will be my"
                                             " servant. That is as much mercy as I can give you."
                                             " You and {partner_name} are now his servants.")

incorrect_answer_riddle_name_room2 = (" I'm sorry you're incorrect. I gave you a really easy one."
                                      " Sigh. You will be fed to my pets. The man watches as the"
                                      " lion eats you and your partner. You have died.")

question_are_you_ready = "Are you ready?(y/n): "
question_where_to_look = "Where do you want to look?(RIGHT[r]/LEFT[l]/FORWARD[f]/UP[u]/DOWN[d]): "
come_back_text = "Come back soon!"
invalid_input_text = "Invalid input."
incorrect_text = "That's incorrect!"
escape_room_display_text_dict={
    "cell": {
        "u": "Above you is the ceiling.",
        "d": "Below you is concrete floor.",
        "r": ""
    }
}
