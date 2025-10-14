class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def send_msg(self, user):
        print(
            f"Sending msg to {user.username}: Hi {user.username} , sent by {self.username}"
        )


user1 = User("Yuva", "uva@gmail.com", "uva1")
user2 = User("Sri", "sri@gmail.com", "sri1")
user1.send_msg(user2)
print(f"user1 email:", user1.email)

# we can update the fields directly
user1.email = "yuva@gmail.com"
print(f"Updated user1 email:", user1.email)