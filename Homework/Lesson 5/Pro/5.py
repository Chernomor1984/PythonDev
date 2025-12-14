"""
Напишите функцию, чтобы проверить, является ли строка действительным адресом электронной почты или нет.
Электронное письмо представляет собой символ (подмножество символов ASCII), разделенный на две части символом @, 
«personal_info» и доменом, то есть Personal_info@domain.
Примечание. В функции должно быть использоваться регулярное выражение
"""
import re

def isEmailValid(address: str) -> bool:
    pattern = r"\w+@\w+\.\w{2,}"
    return re.fullmatch(pattern, address)

validEmailAddress = "some_personal@domain.smp"
invalidEmailAddress = "some_personal@domain"

if isEmailValid(validEmailAddress):
    print(f"{validEmailAddress} is valid")
else:
    print(f"{validEmailAddress} is invalid")

if isEmailValid(invalidEmailAddress):
    print(f"{invalidEmailAddress} is valid")
else:
    print(f"{invalidEmailAddress} is invalid")