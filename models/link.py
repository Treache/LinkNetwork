from category import Category
from user import User
from review import Review
from datetime import datetime as dt

class Link:

    def __init__(self, name: str, desc: str, preview, category: Category, added_by: User, reviews: list(Review) = [], added_on: dt = dt.now, n_o_r: int = 0, rate: float = 0.0):
        pass