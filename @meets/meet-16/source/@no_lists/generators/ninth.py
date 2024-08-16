import customer.profile as profile

def generate():

    position_a = get_greate_odd()
    position_b = get_greate_even()

    if position_a > position_b:

        if position_a + 1 >= 9:
            return 0
        return position_a + 1
    
    if position_a < position_b:

        if position_a - 1 <= 0:
            return 9
        return position_a - 1
    
    return 0

def get_greate_odd():

    the_great_number = get_greater(
        profile.get_first(), 
        profile.get_third())
    
    the_great_number = get_greater(
        the_great_number,
        profile.get_fifth()
    )

    the_great_number = get_greater(
        the_great_number,
        profile.get_seventh()
    )

    return the_great_number

def get_greate_even():

    the_great_number = get_greater(
        profile.get_second(), 
        profile.get_forth())
    
    the_great_number = get_greater(
        the_great_number,
        profile.get_sixth()
    )

    the_great_number = get_greater(
        the_great_number,
        profile.get_eith()
    )

    return the_great_number

def get_greater(first_number, second_number):

    if first_number > second_number:
        return first_number
    return second_number

