from random import shuffle

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def_init_(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def_lt_(self, c2):
        if self.value < c2.valule:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def_gt_(self,, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def_repr_(self):
        v = self.values[self.value] + " of " \
         + self.suits[self.suit]
        return v
