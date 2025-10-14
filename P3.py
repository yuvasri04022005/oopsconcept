# Consenting Adult Philosophy -- making most effective private data with a leading underscore ( double underscore __ )
# Mangled - variables are not access through outside the class
# so protected variables can access outside the class
# but in private variables in double underscore cannot access outside the class because the python changes the attribute name into others


class Sample:
    def __init__(self, username, email, password):
        self.username = username
        # even if we try to access it outside the class it will give error
        self.__email = email
        self.password = password

    # def get_email(self):
    #     return self._email
    def clean_email(self):
        return self.__email.lower().strip()


user4 = Sample("Uva", " YUVA@gmail.com ", "yuva")
# AttributeError: 'Sample' object has no attribute '__email' because it is private
print(f"user4:", user4.__email)
print(f"Cleaned mail:", user4.clean_email())
