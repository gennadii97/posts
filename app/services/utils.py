from passlib.context import CryptContext

passwd_context = CryptContext(
    schemes=['bcrypt']
)


def generate_passwd_hash(password: str) -> str:
    hash = passwd_context.hash(password)
    return hash
