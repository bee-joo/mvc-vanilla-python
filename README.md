# mvc-vanilla-python

## About

Simple MVC app using vanilla Python  
  
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
1. Install dependencies from [`requirements.txt`](./requirements.txt)
```
pip3 install -r requirements.txt
```
>You can also use [venv](https://docs.python.org/3/library/venv.html) 
2. Run it
```
python3 app.py
```

## Project structure
```
-\
 |-- images                ## generated qr-codes
 |   \-- images            ## just file
 |
 |-- models                
 |   |-- __init__.py
 |   |-- client   
 |       \-- __init__.py   ## model and db methods
 |
 |-- templates
 |   |-- 404.html          ## template for 404 error
 |   |-- allusers.html     ## table of users
 |   |-- form.html         ## main form of app
 |   |-- layout.html       ## base layout of all templates
 |   |-- post.html         ## template for POST method
 |   \-- user.html         ## user page
 |
 |-- views                
 |   |-- __init__.py
 |   |-- client   
 |       \-- __init__.py   ## methods to render templates
 |
 |-- .gitattributes
 |-- .gitignore 
 |-- LICENSE
 |-- README.md
 |-- app.py                ## main app file with routing and controllers
 \-- requirements.txt      ## dependencies
```
