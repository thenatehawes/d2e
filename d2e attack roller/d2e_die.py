import random


class dieside:
    """A class to define a side of a die"""

    def __init__(self, side_range=0, heart=0, surge=0, shield=0, miss=False):
        self.range = side_range
        self.heart = heart
        self.surge = surge
        self.shield = shield
        self.miss = miss

    def __add__(self, other):
        if (self.miss or other.miss):
            output = dieside(0, 0, 0, 0, True)
        else:
            output = dieside(self.range + other.range,
                            self.heart + other.heart,
                            self.surge + other.surge,
                            self.shield + other.shield,
                            False)
        return output

    def __sub__(self, other):
        if (self.miss or other.miss):
            output = dieside(0, 0, 0, 0, True)
        else:
            output = dieside(self.range - other.range,
                            self.heart - other.heart,
                            self.surge - other.surge,
                            self.shield - other.shield,
                            False)
        return output

    def PrintDie(self):
        print('Range :', self.range)
        print('Heart :', self.heart)
        print('Surge :', self.surge)
        print('Shield :', self.shield)
        print('Miss :', self.miss)


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

    def roll(self, side='rand'):
        """ Roll the die, provide a side otherwise random """
        if side == 'rand':
            rand_side = random.randrange(0, 5, 1)
            return self.side[rand_side]
        else:
            return self.side[side]
