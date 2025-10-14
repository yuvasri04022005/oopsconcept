class Sample:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    # def get_email(self):
    #     return self._email
    def clean_email(self):
        return self._email.lower().strip()


user4 = Sample("Uva", " YUVA@gmail.com ", "yuva")

print(f"user4:", user4._email)

print(f"Cleaned mail:", user4.clean_email())