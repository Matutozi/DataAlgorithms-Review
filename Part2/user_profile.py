class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print("User created")
    
    def introduce_yourself(self, guest_name):
        print(f"Hi, i am {guest_name}!, contact me at {self.email}")

    def __repr__(self) -> str:
        return f"User(username={self.username}, name='{self.name}', email='{self.email}')"
    
    def __str__(self) -> str:
        return self.__repr__()
        
user1 = User("Emmanuel", "geebee", "so@gmail.com")
print(user1)
#user1.introduce_yourself("Matutozi")
