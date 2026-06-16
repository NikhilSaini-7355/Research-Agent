import bcrypt

class SecurityUtils:
    """
    Utility class for handling cryptographic operations within the application.
    Using native bcrypt to avoid passlib compatibility issues.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Takes a plain text password and returns a secure, salted bcrypt hash.
        """
        # Bcrypt requires bytes, so we encode the python string to utf-8
        pwd_bytes = password.encode('utf-8')
        
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(pwd_bytes, salt)
        
        # Decode back to a string so SQLAlchemy can save it in the database
        return hashed_bytes.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Compares a plain text password against an existing database hash.
        Returns True if they match, False otherwise.
        """
        # Convert both strings back to bytes for comparison
        plain_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        
        return bcrypt.checkpw(plain_bytes, hashed_bytes)