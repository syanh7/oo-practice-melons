############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""


    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        #sets attributes to instance of MelonType object
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        #checks if a pairing is a list or str. If str, appends
        #to self.pairings list,
        #if list, extends the self.pairings list
        if type(pairing) == str:
            self.pairings.append(pairing)
        else:
            self.pairings.extend(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        #sets a new code for self.code
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


def print_pairing_info(all_melon_types):
    """Prints information about each melon type's pairings."""

    #iterate through list of MelonType objects
    #and prints the pairings list off
    for melon in all_melon_types:
        
        print(f"{melon.name} pairs with")
        
        for pairing in melon.pairings:
        
            print(f"\t- {pairing}")


def make_melon_type_lookup(all_melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #takes the list of MelonType object and creates a dict with
    #key as code, value as MelonType object
    melons_by_id = {}
    for melon in all_melon_types:
        melons_by_id[melon.code] = melon


    return melons_by_id
    #{'yw': <__main__.MelonType object at 0x7fb505802700>, 'cas': <__main__.MelonType object at 0x7fb505818550>}

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    #sets the attriubtes to melon object
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating 
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester 
    #melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')

    #check if the min rating of color and shape is greater than 5
    #check if melon isn't from field 3
    def is_sellable(self):
        min_rating = 5
        if self.color_rating > min_rating and self.shape_rating > min_rating and self.field != 3:
            return True
        
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    #get melontype dict
    melons_by_id = make_melon_type_lookup(melon_types)
    melons_harvested = []

    #create melon object, pass melontype object using key and dict
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    
    #use extend to add to list all at once
    melons_harvested.append(melon_1)
    melons_harvested.append(melon_2)
    melons_harvested.append(melon_3)
    melons_harvested.append(melon_4)
    melons_harvested.append(melon_5)
    melons_harvested.append(melon_6)
    melons_harvested.append(melon_7)
    melons_harvested.append(melon_8)
    melons_harvested.append(melon_9)

    return melons_harvested

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    #check if the melon is sellable or not, prints out the result
    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from field {melon.field} (can be sold)")
        else:
            print(f"Harvested by {melon.harvester} from field {melon.field} (not sellable)")

 
    
    

def create_melons_from_text(text_file, all_melon_types):
    open_file = open(text_file)
    melons_harvested = []
    melons_by_id = make_melon_type_lookup(all_melon_types)


    for line in open_file:
        line_list = line.split()
        #make melon object
        melon_type = line_list[5]
        shape_rating = int(line_list[1])
        color_rating = int(line_list[3])
        field = int(line_list[-1])
        harvester = line_list[8]

        melon = Melon(melons_by_id[melon_type],
                shape_rating,
                color_rating,
                field,
                harvester)
        
        melons_harvested.append(melon)

    return melons_harvested

    #{'yw': <__main__.MelonType object at 0x7fb505802700>, 'cas': <__main__.MelonType object at 0x7fb505818550>}
    #melon = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    #yellowwatermelon = MelonType('yw', 2013, 'yellow', False, True, 'yellow watermelon')

    #Shape 4 Color 6 Type musk Harvested By Sheila Field # 52
    # 0    1   2   3   4   5       6      7     8    9  10 11
#make the melon type list
all_melon_types = make_melon_types()
#sends the list to get the melons harvested
melons_harvested = make_melons(all_melon_types)
#prints if melons are sellable or not
get_sellability_report(melons_harvested)

melons_harvested = create_melons_from_text('harvest_log.txt', all_melon_types)
get_sellability_report(melons_harvested)

#Create a function that opens the file harvest_log.txt, 
#loops over the file and creates a melon object for each line of the file



