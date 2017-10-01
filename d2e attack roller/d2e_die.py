import random
from d2e_mods import attack_mod

class base_stats:

    def __init__(self, side_range=0, heart=0, surge=0, shield=0):
        self.range = side_range
        self.heart = heart
        self.surge = surge
        self.shield = shield

    def __add__(self, other):
        self_plus_other = base_stats(self.range + other.range,
                                     self.heart + other.heart,
                                     self.surge + other.surge,
                                     self.shield + other.shield)

        return self_plus_other

    def __sub__(self, other):
        self_minus_other = base_stats(self.range - other.range,
                                      self.heart - other.heart,
                                      self.surge - other.surge,
                                      self.shield - other.shield)

        return self_minus_other

    def __iadd__(self, other):
        self.range += other.range
        self.heart += other.heart
        self.surge += other.surge
        self.shield += other.shield

        return self

    def __isub__(self, other):
        self.range -= other.range
        self.heart -= other.heart
        self.surge -= other.surge
        self.shield -= other.shield

        return self


class dieside(base_stats):
    """A class to define a side of a die"""

    def __init__(self, side_range=0, heart=0, surge=0, shield=0, miss=False):
        self.miss = miss
        base_stats.__init__(self, side_range, heart, surge, shield)

    def __add__(self, other):
        if type(other) is attack_mod:
            output = attack_mod.__add__(other, self)
            return output

        if (self.miss or other.miss):
            output = dieside(miss=True)
        else:
            output = base_stats.__add__(self, other)
            output.__class__ = dieside
            output.miss = False

        return output

    def __sub__(self, other):
        if (self.miss or other.miss):
            output = dieside(miss=True)
        else:
            output = base_stats.__sub__(self, other)
            output.__class__ = dieside
            output.miss = False

        return output

    def __iadd__(self, other):
        if (self.miss or other.miss):
            self.miss = True
            base_stats.__init__(self, side_range=0, heart=0, surge=0, shield=0)
        else:
            self.miss = False
            base_stats.__iadd__(self, other)

        return self

    def __isub__(self, other):
        if (self.miss or other.miss):
            self.miss = True
            base_stats.__init__(self, side_range=0, heart=0, surge=0, shield=0)
        else:
            self.miss = False
            base_stats.__isub__(self, other)

        return self

    def PrintDie(self):
        print('Range :', self.range)
        print('Heart :', self.heart)
        print('Surge :', self.surge)
        print('Shield :', self.shield)
        print('Miss :', self.miss)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class die:
    """A class to define a die object"""

    def __init__(self, color_string):

        random.seed()  # Initialize random seed
        self.side = []

        if color_string == 'red':
            self.color_string = 'red'
            self.side.append(dieside(0, 2, 0, 0, False))
            self.side.append(dieside(0, 2, 0, 0, False))
            self.side.append(dieside(0, 2, 0, 0, False))
            self.side.append(dieside(0, 1, 0, 0, False))
            self.side.append(dieside(0, 3, 1, 0, False))
            self.side.append(dieside(0, 3, 0, 0, False))

        elif color_string == 'black':
            self.color_string = 'black'
            self.side.append(dieside(0, 0, 0, 2, False))
            self.side.append(dieside(0, 0, 0, 2, False))
            self.side.append(dieside(0, 0, 0, 2, False))
            self.side.append(dieside(0, 0, 0, 3, False))
            self.side.append(dieside(0, 0, 0, 0, False))
            self.side.append(dieside(0, 0, 0, 4, False))

        elif color_string == 'gray':
            self.color_string = 'gray'
            self.side.append(dieside(0, 0, 0, 1, False))
            self.side.append(dieside(0, 0, 0, 1, False))
            self.side.append(dieside(0, 0, 0, 1, False))
            self.side.append(dieside(0, 0, 0, 0, False))
            self.side.append(dieside(0, 0, 0, 3, False))
            self.side.append(dieside(0, 0, 0, 2, False))

        elif color_string == 'brown':
            self.color_string = 'brown'
            self.side.append(dieside(0, 0, 0, 1, False))
            self.side.append(dieside(0, 0, 0, 1, False))
            self.side.append(dieside(0, 0, 0, 0, False))
            self.side.append(dieside(0, 0, 0, 0, False))
            self.side.append(dieside(0, 0, 0, 0, False))
            self.side.append(dieside(0, 0, 0, 2, False))

        elif color_string == 'green':
            self.color_string = 'green'
            self.side.append(dieside(1, 1, 1, 0, False))
            self.side.append(dieside(0, 0, 1, 0, False))
            self.side.append(dieside(1, 1, 0, 0, False))
            self.side.append(dieside(1, 0, 1, 0, False))
            self.side.append(dieside(0, 1, 1, 0, False))
            self.side.append(dieside(0, 1, 0, 0, False))

        elif color_string == 'yellow':
            self.color_string = 'yellow'
            self.side.append(dieside(1, 1, 0, 0, False))
            self.side.append(dieside(2, 1, 0, 0, False))
            self.side.append(dieside(0, 1, 1, 0, False))
            self.side.append(dieside(1, 0, 1, 0, False))
            self.side.append(dieside(0, 2, 1, 0, False))
            self.side.append(dieside(0, 2, 0, 0, False))

        elif color_string == 'blue':
            self.color_string = 'blue'
            self.side.append(dieside(0, 0, 0, 0, True))
            self.side.append(dieside(6, 1, 1, 0, False))
            self.side.append(dieside(4, 2, 0, 0, False))
            self.side.append(dieside(2, 2, 1, 0, False))
            self.side.append(dieside(3, 2, 0, 0, False))
            self.side.append(dieside(5, 1, 0, 0, False))
        else:
            raise ValueError('Unknown die color')

    def roll(self, side=None):
        """ Roll the die, provide a side otherwise random """
        if side is not None:
            return self.side[side]
        else:
            rand_side = random.randrange(0, 6, 1)
            return self.side[rand_side]
