from datetime import datetime as dt

class Review:

    @classmethod
    def new_review_instance(cls, context, rate, by):
        """
        This function creates and returns a new Review instance using the given values.
        ** This method uses current timestamp as the value for 'on' attribute.
        """
        return Review(context, rate, by, dt.now())


    def __init__(self, context, rate, by, on, likes=[]):
        self._context = context      # Review content
        self._rate = rate            # The rating
        self._written_by = by                # Review by
        self._written_on = on                # Review on (Datetime)
        self._likes = likes          # Likes on this review

    def get_rating(self):
        """Accessor for the rating"""
        return self._rate

    def get_context(self):
        """Accessor for the context"""
        return self._context

    def get_writer(self):
        """Accessor for the review writer"""
        return self._written_by

    def get_timestamp(self):
        """Accessor for the review's timestamp"""
        return self._written_on

    def print_review(self):
        print(f"'{self._context}' by '{self._written_by}' on '{self._written_on}'")
    
    def count_likes(self) -> int:
        """Returns the number of likes on this review"""
        return len(self._likes)
    
    def get_likes(self) -> list:
        """Returns the list of likes on this review"""
        return self._likes

    def edit_review(self, edit_by, context, rate):
        if(edit_by == self._written_by):
            self._context = context
            self._rate = rate
            return 
        raise ValueError("Hmm")
