# WeatherAppDjango — Setup Guide

## Prerequisites
- Python 3.12+
- Git

---

## 1. Clone the repo

```powershell
git clone https://github.com/metalRudge/WeatherAppDjango.git
cd WeatherAppDjango
```

---

## 2. Create & activate virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

> If PowerShell blocks the script, run this first:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Copy the example file and fill in your keys:

```powershell
copy .env.example .env
```

Edit `.env`:

```
SECRET_KEY=your_django_secret_key
OPENWEATHER_API_KEY=your_openweathermap_api_key
DEBUG=True
```

Get a free API key at [openweathermap.org](https://openweathermap.org/) → Account → API Keys.

---

## 5. Run migrations

```powershell
python manage.py makemigrations -->
python manage.py migrate
```

---

## 6. Start the server

```powershell
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Project structure

```
WeatherAppDjango/
├── .venv/                  # virtual environment (not committed)
├── .env                    # your local secrets (not committed)
├── manage.py
├── requirements.txt
├── config/                 # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── main/                   # app logic
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── migrations/
    └── templates/
        └── main/
            └── index.html
```
