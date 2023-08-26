class instagram:
    def __init__(self, username, userid):
        self.username = username
        self.followers = 0
        self.userid = userid
        
    def follow(self, user):
        user.followers+=1
        self.following+=1

user1 = instagram("akash", "akash.dev.8092@gmail.com")
print(user1.userid)
print(user1.followers)
user2=instagram("rahul", "rahulsingh")

user2.follow(user1)
print()