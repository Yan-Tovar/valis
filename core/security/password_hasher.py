import bcrypt


class PasswordHasher:


    @staticmethod
    def hash_password(password):

        password_bytes = password.encode("utf-8")

        salt = bcrypt.gensalt()

        hashed = bcrypt.hashpw(
            password_bytes,
            salt
        )

        return hashed.decode("utf-8")


    @staticmethod
    def verify_password(
        plain_password,
        hashed_password
    ):

        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )