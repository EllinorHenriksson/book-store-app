import bcrypt

class MemberModel:
    def is_email_unique(self, email):
        # Check if email is unique
        # OBS! Fortsätt här!
        is_email_unique = False
        return is_email_unique

    def create_member(self, member):
        # Hashes password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(member["password"].encode(), salt)

        # Create member
        print(member)