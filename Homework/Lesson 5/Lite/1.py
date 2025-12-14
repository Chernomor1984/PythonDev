"""
Напишите программу, которая будет:
- находить самое длинное слово в заданной строке.
- сколько вообще слов
- Получить индекс слова "сервер" и сколько раз оно встречается в строке
"""
text = """
Начнем с процесса регистрации. Перед вами форма с несколькими полями: Имя, Логин, Пароль, Кличка вашей собаки. 
Вы покорно заполняете все поля со звездочками, после чего жмякаете на кнопку 'Зарегистрироваться'. 
Ваши данные отправляются на сервер при помощи HTTP, сервер создает в базе данных новую запись, и если все проходит успешно, 
то вы зарегистрировались в системе. То есть процесс регистрации – это просто сохранение на сервере 'в определенном текстовом файле' 
данных, которые вы заполнили на сайте.
"""
import re

def makeListFrom(text: str) -> list[str]:
    # Replace all non letter, digit and _ symbols to whitespace
    modifiedText = re.sub(r"\W", " ", text)
    # Replace all long whitespaces to a single one + make it lowercased
    modifiedText = re.sub(r"\s+", " ", modifiedText).lower()
    return modifiedText.split()

textList = makeListFrom(text)
textList.sort(key=len)
word = "сервер"
index = -1
count = text.count(word)

try:
    index = text.index(word)
except ValueError:
    pass

print(f"1 - Самое длинное слово: {textList[-1]}")
print(f"2 - Количество слов в тексте: {len(textList)}")
print(f"3 - Индекс слова \"сервер\": {index}; Встречается в тексте: {count} раз.")