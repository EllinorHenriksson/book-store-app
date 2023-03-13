import bcrypt

# Hashes password
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)