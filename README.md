# Вычислитель отличий (gendiff)
***
![Hexlet Badge](https://img.shields.io/badge/Hexlet-116EF5?logo=hexlet&logoColor=fff&style=for-the-badge)
[![Actions Status](https://github.com/GrigoriyKruchinin/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/GrigoriyKruchinin/python-project-50/actions)
[![Check_my_Actions](https://github.com/GrigoriyKruchinin/python-project-50/actions/workflows/my_workflow.yml/badge.svg)](https://github.com/GrigoriyKruchinin/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/494bdd544175e66ad82b/maintainability)](https://codeclimate.com/github/GrigoriyKruchinin/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/494bdd544175e66ad82b/test_coverage)](https://codeclimate.com/github/GrigoriyKruchinin/python-project-50/test_coverage)


__"Вычислитель отличий" (gendiff)__ - второй проект, разработанный в рамках обучения на курсе Хекслет. Это инструмент командной строки для поиска различий между двумя файлами.

***

## Установка
Для установки и запуска проекта вам потребуется Python версии  3.10 и выше и инструмент для управления зависимостями Poetry.

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
```
git clone git@github.com:GrigoriyKruchinin/python-project-50.git
```
2. Перейдите в директорию проекта:
```
cd python-project-50
```
3. Установите необходимые зависимости с помощью Poetry:
```
poetry install
```
#### Поддерживаемые форматы файлов
Проект поддерживает следующие форматы файлов для поиска отличий:

- YAML (.yaml, .yml)
- JSON (.json)
***
## Как найти различия между двумя файлами

1. Поместите два файла, которые вы хотите сравнить, в папку tests/fixtures.
2. Выполните команду для поиска различий:
```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```
3. Замените file1.json и file2.json на названия ваших файлов
***
## Форматы вывода
Для выбора формата вывода различий, укажите флаг -f с названием форматтера. Возможные форматтеры:

- stylish (по умолчанию)
- plain
- json

#### Примеры команд для разных форматов вывода:


1. Вывод в стиле stylish
```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```

2. Вывод в формате plain
```
poetry run gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
```

3. Вывод в формате json
```
poetry run gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
```
***
## Контакты
- Автор: Grigoriy Kruchinin
- [GitHub](https://github.com/GrigoriyKruchinin)
- [Email](gkruchinin75@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/grigoriy-kruchinin/)
***
### Демонстрация работы программы:
[![asciicast](https://asciinema.org/a/597170.svg)](https://asciinema.org/a/597170)

[![asciicast](https://asciinema.org/a/598903.svg)](https://asciinema.org/a/598903)

[![asciicast](https://asciinema.org/a/599137.svg)](https://asciinema.org/a/599137)

[![asciicast](https://asciinema.org/a/599152.svg)](https://asciinema.org/a/599152)
***