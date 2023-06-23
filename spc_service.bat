@echo off
echo "Uruchamianie serwera SPC"
cd /d c:\Users\karol\PycharmProjects\SubiektProductChecker\
call myvenv\Scripts\activate
python manage.py runserver 10.0.0.10:8080
pause