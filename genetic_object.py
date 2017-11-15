from random import randint
import string

class Genetic_Object(object):
    """
    An object containing a string, and its closeness to the 'goal' string.
    """
    #All possible characters. Use is for mutations
    POSSIBLE_CHARACTERS = string.printable

    def get_fitness_factor(self,string):
        """
        Gets the completeness factor for the string the object contains
        RETURN:
        A float containing the closeness factor as a percentage (0-100)
        """
        k = len(string)
        sum = 0
        for i in range(0,k):
            sum += ord(string[i])
        return sum

    def __init__(self,string):
        self.string = string
        self.completeness_factor = self.get_fitness_factor(string)

    def splice(self,other_object):
        """
        Cut this string and other_object's string at a random location
        And add them together
        RETURN:
        A new genetic object containing the string we just created
        """
        cut = randint(0, len(other_object.string))
        new_string = self.string[cut:] + other_object.string[:cut]
        return Genetic_Object(new_string)

    def mutate(self):
        """
        If the chance variable containers a number greater than 95
        (5% chance of mutation)
        Then select a random character and change it to something completely different
        """
        chance = randint(0,100)
        if chance > 95:
            #Get the index of a random character in the string
            random_character_in_string = randint(0, len(self.string)-1)
            #Get the index of a random character in "POSSIBLE_CHARACTERS"
            random_character_of_possible = randint(0, len(self.POSSIBLE_CHARACTERS)-1)
            #Turn the string into a list of characters because STRINGS ARE IMMUTABLE!?
            strings_are_immutable = list(self.string)
            strings_are_immutable[random_character_in_string] = self.POSSIBLE_CHARACTERS[random_character_of_possible]
            self.string = "".join(strings_are_immutable)
