class NegativeNumberError(Exception):
    def __init__(self, value, errorMessage="Переданное число отрицательное"):
        super().__init__(errorMessage)
        self.value = value
        self.errorMessage = errorMessage
        
    def __str__(self):
        return f"Возникла ошибка! {self.errorMessage}: {self.value}"
    
def check_positive_number(number: int | float):
    if number > 0:
        print(f"Число {number} положительное")
    else:
        raise NegativeNumberError(number)
    
def validate_number(number: int | float):
    try:
        check_positive_number(num)
    except NegativeNumberError as nne:
        print(nne)
    
num = 5
validate_number(num)
num = -4
validate_number(num)
