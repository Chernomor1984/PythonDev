# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
# Удаляем заглушку, создаем переменную result:
# Используем subprocess.run для выполнения команды в переменной result
# Выводим результат выполнения команды result.stdout

import subprocess

def git_config_list():
    result = subprocess.run(
        ["git", "config", "--global", "--list"],
        capture_output=True,
        text=True,
        check=True
    )
    
    print(result.stdout)
    
git_config_list()
