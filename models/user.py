import uuid

class User:

    def __init__(self, display_name: str, email_address: str, profile_bio: str, points=0, reviews=[], uuid=uuid.uuid5()):
        self.email_address = email_address          # User's email address (Identifier)
        self._display_name = display_name           # User's display name
        self._profile_bio = profile_bio             # User's profile bio
        # self._profile_pic                         # User's profile picture -> NOT COMPLETE YET
        self._points = points                       # User's points
        self._reviews = reviews                     # User's reviews
        self._uuid = uuid                           # User's UUID