# Tensor AQA Test Cases

## Функциональности
- Реализовано на Python 3.10+ с Selenium WebDriver
- Применен паттерн Page Object Model
- Использован pytest как тестовый фреймворк

## Шаги установки

```bash
# Клонируйте репозиторий
git clone https://github.com/sylaar/Tensor_AQA_TestCases.git
cd Tensor_AQA_TestCases

# Установите зависимости
pip install -r requirements.txt

# Запуск первого сценария
pytest -v src/Tests/test_case_01.py

# Запуск второго сценария
pytest -v src/Tests/test_case_02.py
