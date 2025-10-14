import datetime

class GetSet:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        print(f"Accessing email on {datetime.datetime.now()}")
        return self._email

    def set_email(self, new_email):
        # Authentication / Validation is added within the class
        if "@" in new_email:
            print(f"Updating email on {datetime.datetime.now()}")
            self._email = new_email


user6 = GetSet("AB", "ab@gamil.com", "ab")
print(f"user6 email:", user6.get_email())
user6.set_email("abcduv@gmail.com")
print(f"Updated user6 email:", user6.get_email())
