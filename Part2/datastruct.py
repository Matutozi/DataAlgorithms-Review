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

user = User('aakash', 'Aakash Rai', 'aakash@example.com')

class UserDatabase:

    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i +=1

        self.users.insert(i, user)


    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        if target is not None:
            target.name, target.email = user.name, user.email
        else:
            print("NOT FOUND IN DATABASE")

    def list_all(self):
        return self.users

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', '@exasiddhantmple.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

database = UserDatabase()

database.insert(aakash)
database.insert(biraj)
database.insert(vishal)
database.insert(siddhant)

print(database)
user = database.find("siddhant")
print(user)

database.update(User(username="siddhant", name="Siddhant U", email = "sidd@eantsiddhantmple.com"))
user1 = database.find("siddhant")
print(user1)

all = database.list_all()
print(all)
#u can compare strings like numbers in python

""" COMPLEXITY
list - O(N)
insert - O(N)
update O(N)
find- O(N)
"""