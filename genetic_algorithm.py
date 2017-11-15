from genetic_object import Genetic_Object
from generation import Generation
import datetime
import string
from random import randint

THRESHHOLD = 5
NUMBER_OF_SUCCESSORS = 1
POSSIBLE_CHARACTERS = string.printable

def make_random_string(string_length):
    """Return a random string of length string_length"""
    strn = ""
    while len(strn) < string_length:
        random_character_of_possible = randint(0, len(POSSIBLE_CHARACTERS)-1)
        strn = strn + POSSIBLE_CHARACTERS[random_character_of_possible]
    return strn

def run_genetic_algorithm(string_length):
    """
    Run the algorithm.
    string_length - the length of the strings we're working with
    RETURN
        The current/last generation
    """
    generation = list()
    generation_count = 0
    while len(generation) < THRESHHOLD:
        #Fill the generation with completely random strings alongside start_string
        random_object = Genetic_Object(make_random_string(string_length))
        generation.append(random_object)

    current_generation = Generation(generation,generation_count)
    start = datetime.datetime.now()
    TIME_LIMIT = datetime.timedelta(seconds=120)
    end = start + TIME_LIMIT
    while datetime.datetime.now() < end:
        #Run this for a certain amount of time specified by TIME_LIMIT
        current_generation,toprint = current_generation.get_new_generation(NUMBER_OF_SUCCESSORS)
        print(toprint)
        #Print the best of the newest generation
    return generation

if __name__ == "__main__":
    string_length = 500
    result = run_genetic_algorithm(string_length)
    input("Enter to exit")
