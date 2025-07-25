class User:
    
    def __init__(self, name: str, birthyear):
        self.name = name
        self.birthyear = int(birthyear)

    def get_name(self):
        return self.name.upper()

    def age(self, current_year: int):
        return current_year - self.birthyear


user = User(name="John", birthyear=1999)
print(user.age(current_year=2023))
print(user.get_name())
