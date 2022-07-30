# mvc-vanilla-python

## About

User can register using this app (maybe, for the event). User gets QR-code with link to the page after registration. And there's a table of all registered users.
  
Summary:
* Using embedded Python http-server for getting requests, sending responses and routing  
* Using pyqrcode to generate QR-code  
* SQLite as database  
* Model contains methods for executing SQL statements  
* Jinja as template engine  

## Setup  
0. Clone repository
```
git clone https://github.com/bee-joo/mvc-vanilla-python.git
```
1. Install dependencies from [`requirements.txt`](./requirments.txt)
```
pip3 install -r requirements.txt
```
>You can also use [venv](https://docs.python.org/3/library/venv.html) 
2. Run it
```
python3 app.py
```
