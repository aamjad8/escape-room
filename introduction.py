import random

from data import *
from enums import *


def introduce_partner(room):
    gender_input = input("If you ever get a partner do you prefer male or female?(m/f): ")
    temp_partner_name = ""
    gender = ""
    if gender_input == Gender.MALE.value:
        gender = Gender.MALE
        temp_partner_name = random.choice(male_partner_name_arr)
    elif gender_input == Gender.FEMALE.value:
        gender = Gender.FEMALE
        temp_partner_name = random.choice(female_partner_name_arr)

    print(room_partner_intro_dict[room][gender.value].format(partner_name=temp_partner_name,
                                                             partner_hair=random.choice(partner_appearance_arr),
                                                             partner_looks=random.choice(
                                                                 partner_accessories_dict[gender.value]),
                                                             partner_height=random.choice(height_arr)))
    return temp_partner_name
