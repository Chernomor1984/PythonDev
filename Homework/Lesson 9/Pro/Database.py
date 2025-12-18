class Database:
    """
    База данных пользователей
    """
    users = []
    
    @staticmethod
    def add_user(user):
        Database.users.append(user)
        
    @staticmethod
    def remove_user(user):
        if user in Database.users:
            Database.users.remove(user)