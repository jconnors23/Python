class User:
    pass
    # init function
    def __init__(self, user_id, speed):
        print("we initialize this print when we create the user objects")
        self.id = user_id
        self.speed = speed
        # default value
        self.followers = 0
        self.following = 0
    # methods always have to have self parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 1000)

# snake_case, PascalCase, camelCase
user_2 = User('12', 10000)

# constrctor: used to initialize starting values for attritbutes of class objects
# def __init__(self): initialize attribuites

user_1.follow(user_2)