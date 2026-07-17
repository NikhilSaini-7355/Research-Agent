from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

pw = "sir"
hashed = pwd_context.hash(pw)
hashed2 = pwd_context.hash(hashed)
print(hashed)
print(pwd_context.verify(hashed, "$2b$12$FjkBO6vszk/2gg8gCk9osOuX5KdLMhO67ftTDaxvBQr0RbVDlZU4a"))  # should print True
print(len("$2b$12$O.H8/evxdvz0VetR4JUxauVwij6M2PCBPD.5eABZ.GVLCJsrBHz46"))
