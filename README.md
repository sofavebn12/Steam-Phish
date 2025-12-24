# Steam-Phish

Набросок GUI-приложения с окном цвета `#212328` и сборкой `.exe` через PyInstaller.

## Запуск без сборки

1. Установите Python 3.11+.
2. Создайте окружение и поставьте зависимости:
	```bash
	python -m venv .venv
	source .venv/bin/activate  # Windows: .venv\Scripts\activate
	pip install --upgrade pip
	pip install -r requirements.txt
	```
3. Запустите приложение:
	```bash
	python src/main.py
	```

## Сборка `.exe` (Windows)

1. Убедитесь, что установлены Python 3.11+ и `pip`.
2. Запустите из корня репозитория:
	```bat
	build_windows.bat
	```
3. Готовый файл появится в `dist/SteamPhish.exe`.

Окно имеет фон `#212328`, фиксированный размер `800x500` и простой заголовок. Логику можно наращивать внутри `src/main.py`.