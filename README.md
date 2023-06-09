### Hexlet tests and linter status:
[![Actions Status](https://github.com/Gaben74/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/Gaben74/python-project-49/actions)

<a href="https://codeclimate.com/github/Gaben74/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/bf830954ff51ca9d5eb9/maintainability" /></a>

### Описание проекта:
«Brain Games» — набор из пяти консольных игр для прокачки мозга. 
Каждая игра задает вопросы, на которые нужно дать правильные ответы. 
После трех правильных ответов считается, что игра пройдена. 
Неправильные ответы завершают игру и предлагают пройти ее заново.

Список игр:
1. Brain Even - определение четного числа (Команда для запуска: brain-even)
2. Brain Calc - арифметические выражения, которые необходимо вычислить (Команда для запуска: brain-calc)
3. Brain Gcd - определение наибольшего общего делителя (Команда для запуска: brain-gcd)
4. Brain Progression - поиск пропущенных чисел в последовательности чисел (Команда для запуска: brain-progression)
5. Brain Prime - определение простого числа (Команда для запуска: brain-prime)

### Требования для установки:
1. Python - Версия 3.10 или выше
2. Poetry - Версия 1.4.0 или выше

### Установка:
Сборка пакета и его установка(инструкция для конечного пользователя):
1. poetry install(Makefile - make install) - первичная установка poetry и необходимых зависимостей;
2. poetry build(Makefile - make build) - сборка пакета в системе;
3. python3 -m pip install --user dist/*.whl(Makefile - make package-install) - установка пакета в систему;
4. poetry run flake8 brain_games(Makefile - make lint) - запуск линтера *из корневой папки проекта.

### Демонстрационные материалы:
1. Brain Even
https://asciinema.org/a/LYSyGQTH6Y1OtryZRsNOjFn2L

2. Brain Calc
https://asciinema.org/a/X5864U9QjfmyUyYz5VjAkiFIn

3. Brain Gcd
https://asciinema.org/a/xUZrPTzg6n26nZ8gRY32gt12e

4. Brain Progression
https://asciinema.org/a/FtA6YigTQkgT0sRfaqPJjDjP5

5. Brain Prime
https://asciinema.org/a/2PMNVU1XTl58HxKpIsa1p6sXo
