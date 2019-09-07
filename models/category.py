from datetime import datetime as dt

class Category:

    def __init__(self, name: str, desc: str, created_by, n_o_r=0, created_on=dt.now()):
        self._name = name                       # Name of the category
        self._desc = desc                       # Category description
        self._n_o_r = n_o_r                     # Number of redirects
        self._created_on = created_on           # Category creation timestamp
        self._created_by = created_by           # Category creation suggestion by
        self._suggestion_votes = []             # Votes for this category's suggestion -> NOT COMPLETE

    