import tink
from tink import daead


class AuthManager:
    def __init__(self, key_path):
        """Create a new AuthManager with the given key path."""