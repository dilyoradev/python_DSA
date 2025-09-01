"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return  EXPECTED_BAKE_TIME - elapsed_bake_time
    



# You might also consider defining a 'PREPARATION_TIME' constant.
PREPARATION_TIME = 2
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(number_of_layer):
    """Calculate the preparation_time_in_minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param : minutes spent for each layer int * 2.
    :return: preparation_time_in_minutes.

    This function takes one integer representing the number of lasagna layers and calculates the total minutes to be spent to make each layer (2)lasagna.
    """
    return number_of_layer * PREPARATION_TIME
    



def elapsed_time_in_minutes(number_of_layer, elapsed_baked_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layer) + elapsed_baked_time
