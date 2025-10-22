# Tensor AQA Test Cases

## Описание
- Выполнено на Python 3.10+ с Selenium WebDriver
- Применен паттерн Page Object Model
- Использован pytest как тестовый фреймворк

## Шаги установки

```bash
# Клонировать репозиторий
git clone https://github.com/sylaar/Tensor_AQA_TestCases.git

# Перейти в папку с заданием
cd Tensor_AQA_TestCases

# Создать и активировать виртуальное окружение
python3 -m venv venv

# для Linux/macOS
source venv/bin/activate
# для Windows
venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt

# Запуск первого сценария
pytest -v src/Tests/test_case_01.py

# Запуск второго сценария
pytest -v src/Tests/test_case_02.py
