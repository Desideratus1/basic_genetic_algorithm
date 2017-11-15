
class Generation:

    def __init__(self,gen=list(),gen_num=0):
        self.generation = gen
        #generation is a list of "Genetic_Object"
        self.generation_number = gen_num
        self.sort()

    def sort(self):
        """Sort the generation by its completeness factor."""
        self.generation.sort(key=lambda x: x.completeness_factor, reverse=True)

    def get_top(self,number=1):
        """Sort the generation by its completeness factor, then returns the top of the list

        Keyword arguments:
        number -- The number of genetic objects to return (default 1)
        """
        self.sort()
        return self.generation[:number]

    def get_new_generation(self,number_of_successors):
        """Get a new generation.

        Keyword arguments:
        number_of_successors -- the limit on how many successors we can have

        RETURN:
        tuple - 0th: a new Generation object containing the next generation.
              - 1st: A print statement for the new generation
        """
        new_gen = list()
        for genetic_object_1 in self.generation:
            genetic_object_1.mutate()
            for genetic_object_2 in self.generation:
                new_gen.append(genetic_object_1.splice(genetic_object_2))

        new_generation = Generation(new_gen,self.generation_number+1)
        #Create a new generation from new_gen
        new_generation.generation = new_generation.generation[:number_of_successors]
        generation_statement_string = list()
        generation_statement_string.append("TOP OF GENERATION %d\n" % new_generation.generation_number)
        for ob in new_generation.get_top(1):
            generation_statement_string.append("%.2f: %s\n" % (ob.completeness_factor, ob.string))
        return new_generation,"".join(generation_statement_string)
