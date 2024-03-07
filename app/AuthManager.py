import tink


class AuthManager:
    def __init__(self, database):
        self.database = database

    def register(self, username, password):
        """
        Register a new user
        args:
            username: str
            password: str
        """
        pass

    def login(self, username, password):
        """
        Login a user
        args:
            username: str
            password: str
        """
        pass

    def logout(self, session_token):
        """
        Logout a user
        args:
            session_token: str
        """
        pass

    def verify_password(self, username, password):
        """
        Verify a password for a given username
        args:
            username: str
            password: str
        """
        pass

    def check_session(self, session_token):
        """
        Check if a session token is valid
        args:
            session_token: str
        """
        pass

    def hash_password(self, password, salt=None):
        """
        Hash a password using a salt
        args:
            password: str
            salt: str
        """
        pass
