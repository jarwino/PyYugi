
from card import CardLogic

# Naming scheme of the card class must contain Card_<uid>
class Card_24224830(CardLogic):
    """Called by the Grave"""
    def summon(self):
        print("summoned")

