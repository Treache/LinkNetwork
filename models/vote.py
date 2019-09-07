from user import User
class Vote:

    def __init__(self, vote_by: User, vote_direction: bool=True):
        self._vote_by = vote_by
        self._vote_direction = vote_direction