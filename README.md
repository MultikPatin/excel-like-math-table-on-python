# excel-like-math-table

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Uv](https://img.shields.io/badge/Uv-0.10.7-FFD43B?style=for-the-badge&logo=uv&logoColor=black)
![Ruff](https://img.shields.io/badge/Ruff-0.15.4-FB8B24?style=for-the-badge&logo=ruff&logoColor=white)
![Ty](https://img.shields.io/badge/Ty-0.0.21-2A6DB2?style=for-the-badge&logo=mypy&logoColor=white)
![Pre-commit](https://img.shields.io/badge/Pre--commit-4.5.1-FAB040?style=for-the-badge&logo=precommit&logoColor=white)

Простой Python-проект, имитирующий базовую функциональность электронных таблиц (как Excel) с поддержкой формул,
токенизацией, парсингом и вычислением выражений.

---

## 📦 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourname/excel-like-math-table.git cd excel-like-math-table
```

2. Создайте виртуальное окружение и установите зависимости:

```bash
uv sync --group dev
```

3. Установка хуков

```bash
pre-commit install
```

---

## 🧩 Структура проекта

```
src/
    ├── domains/ # Модели данных (Token, AST и т.д.)
    ├── services/ # Логика: токенизатор, парсер, вычислитель
    ├── main. py # Точка входа и пример использования 
    ├──tests/
```

---

## 📝 TODO

- [x] Реализовать парсер выражений (на основе токенов)
- [x] Добавить поддержку функций: `SUM`, `MAX`, `MIN`
- [ ] Поддержка ссылок на ячейки и диапазоны
- [ ] Вычисление формул по графу зависимостей

---

Создано с ❤️ для обучения архитектуре парсеров и работы с формулами.