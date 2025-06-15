class PasswordHasher:
    def hash(self, password: str) -> str:
        return password

    def compare(self, password: str, hashed_password: str) -> bool:
        return password == hashed_password
