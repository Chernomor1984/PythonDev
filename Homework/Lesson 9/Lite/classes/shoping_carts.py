# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    __admin = None
    
    def __init__(self, owner):
        self.items = []
        self.__owner = owner
        
        """
        Геттер свойства 'владелец корзины'
        """
    @property
    def owner(self):
        return self.__owner

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total
    
    def register(self, administrator):
        self.__admin = administrator

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = f"Покупатель {self.__owner.username} приобрёл товары.\n"
        details += "Корзина покупок:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общее: {self.get_total()} руб"
        
        if self.__admin is not None:
            details += f"\nЗарегистировал покупки администратор {self.__admin.username}"
        return details