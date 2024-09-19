# Тест автоматизации покупки товара на saucedemo.com

## Описание
Проект представляет собой автоматический e2e тест, который проверяет процесс покупки товара на сайте saucedemo.com. 

## Требования
- Python 3.8+
- Google Chrome

## Установка зависимостей
1. Клонируйте репозиторий:
```bash
git clone https://github.com/Wizardass/saucedemo-qa-test.git
```
2. Перейдите в папку проекта:
```bash
cd saucedemo-qa-test
```

3. Создайте виртуальную среду:
```bash
python -m venv saucedemo-test
```

4. Активируйте виртуальную среду:
* на Windows (PowerShell):
```bash
.\saucedemo-test\Scripts\Activate.ps1
```
* на macOS/Linux
```bash
source saucedemo-test/bin/activate
```

5. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск теста
1. Убедитесь, что у вас установлен Google Chrome.
2. Запустите тест:
```bash
python test_purchase.py
```

## Ожидаемый результат
После успешного выполнения теста в консоли будет выведено сообщение:
```
Test passed successfully!
```

