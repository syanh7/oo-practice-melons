############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        if type(pairing) == str:
            self.pairings.append(pairing)
        else:
            self.pairings.extend(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    #create muskmelon
    musk = MelonType('musk', 1998, 'green', True, True, 'muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    #casaba
    casaba = MelonType('cas', 2003, 'orange', False, False, 'casaba')
    casaba.add_pairing(['mint', 'strawberries'])
    all_melon_types.append(casaba)

    #crenshaw
    crenshaw = MelonType('cren', 1996, 'green', False, True, 'crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)
    

    #yellow watermelon
    yellowwatermelon = MelonType('yw', 2013, 'yellow', False, True, 'yellow watermelon')
    yellowwatermelon.add_pairing('ice cream')
    all_melon_types.append(yellowwatermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        
        print(f"{melon.name} pairs with")
        
        for pairing in melon.pairings:
        
            print(f"\t- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_objects = {}

    for melon in melon_types:
        melon_objects[melon.code] = melon
    

    return melon_objects
    #{'yw': yellowwatermelon, 'cas': casaba}

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



