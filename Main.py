class User():
    def __init__(self, id, name):
        self.__name = name
        self.__id = id
        self.__level = "User"

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_level(self):
        return self.__level
    def set_name(self, name):
        self.__name = name
    def set_level(self, level):
        self.__level = level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__admin_level = "Admin"
    def add_user(self, user_list, user):
        user_list.append(user)
        print(user_list)
    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(user_list)


user_list = []
admin = Admin("admin1", "Dima")
user = User("User1","Dasha")
user2 = User("user2","asdf")
print(user.get_name())
admin.add_user(user_list, user)
admin.add_user(user_list, user2)
admin.remove_user(user_list, user2)
print(user_list)