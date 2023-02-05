<h1 style="text-align: center;">
	<a href='https://intranet.alxswe.com/projects/290'>
		0x04. AirBnB clone - Web framework
	</a>
</h1>


## Resources
* [name_1](link)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
* [name_3](link)


## Project Overview

- [**Mandatory Task**](#mandatory-task)
	- [0. Hello Flask!](0-hello_route.py)
	- [1. HBNB](1-hbnb_route.py)
	- [2. C is fun!](2-c_route.py)
	- [3. Python is cool!](3-python_route.py)
	- [4. Is it a number?](4-number_route.py)
	- [Task_1](link_to_file)
- [**Advanced Task**](#advanced-task)
	- [Task_013](link_to_file)
	- [Task_013](link_to_file)
	- [Task_014](link_to_file)

---



<h2 style="text-align: center;">Tasks</h2>

### Mandatory Task
#### 0. Hello Flask!

**Problem:** Write a script that starts a Flask web application:

**Requirements:**
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
	* `/`: display “Hello HBNB!”
* You must use the option `strict_slashes=False` in your route definition

```
AirBnB_clone_v2(master)➜ python3 -m web_flask.0-hello_route
 * Serving Flask app '0-hello_route'
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

-------------------------------- Terminal 2 --------------------------------
imitor＠excalibur:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
```
- [x] *File:* [0-hello_route.py](0-hello_route.py)

---

#### 1. HBNB

**Problem:** Write a script that starts a Flask web application:

**Requirements:**
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
	* `/`: display “Hello HBNB!”
	* `/hbnb`: display “HBNB”
* You must use the option `strict_slashes=False` in your route definition

```
AirBnB_clone_v2(master)➜ python3 -m web_flask.1-hbnb_route
 * Serving Flask app '1-hbnb_route'
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

-------------------------------- Terminal 2 --------------------------------
imitor＠excalibur:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
```
- [x] *File:* [1-hbnb_route.py](1-hbnb_route.py

---
#### 2. C is fun!

**Problem:** Write a script that starts a Flask web application:

**Requirements:**
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
	* `/`: display “Hello HBNB!”
	* `/hbnb`: display “HBNB”
	* `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
* You must use the option `strict_slashes=False` in your route definition
```
AirBnB_clone_v2(master)➜ python3 -m web_flask.2-c_route.py
 * Serving Flask app '2-c_route.py'
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

-------------------------------- Terminal 2 --------------------------------
imitor＠excalibur:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$

```
- [x] *File:* [2-c_route.py](2-c_route.py)

---

#### 3. Python is cool!
**Problem:** Write a script that starts a Flask web application:

**Requirements:**
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
	* `/`: display “Hello HBNB!”
	* `/hbnb`: display “HBNB”
	* `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
	* `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
		* The default value of `text` is “is cool”
* You must use the option `strict_slashes=False` in your route definition
```
AirBnB_clone_v2(master)➜ python3 -m web_flask.3-python_route
 * Serving Flask app '3-python_route'
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

-------------------------------- Terminal 2 --------------------------------
imitor＠excalibur:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
imitor＠excalibur:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e 
Python is cool$
imitor＠excalibur:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e 
Python is cool$
```
- [x] *File:* [3-python_route](3-python_route)

---

#### 4. Is it a number?
**Problem:** Write a script that starts a Flask web application:

**Requirements:**
* Your web application must be listening on `0.0.0.0`, port `5000`
* Routes:
	* `/`: display “Hello HBNB!”
	* `/hbnb`: display “HBNB”
	* `/c/<text>`: display “C ” followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
	* `/python/(<text>)`: display “Python ”, followed by the value of the `text` variable (replace underscore `_` symbols with a space ` `)
		* The default value of `text` is “is cool”
	* `/number/<n>`: display “n is a number” only if `n` is an integer
* You must use the option `strict_slashes=False` in your route definition
```
AirBnB_clone_v2(master)➜ python3 -m web_flask.4-number_route.py
 * Serving Flask app '4-number_route.py'
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

-------------------------------- Terminal 2 --------------------------------
imitor＠excalibur:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$

imitor＠excalibur:~$ curl 0.0.0.0:5000/number/8.9
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

imitor＠excalibur:~$ curl 0.0.0.0:5000/number/emiwest
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```
- [x] *File:* [4-number_route.py](4-number_route.py)

---

### Advanced Task

---
#### Task_013
**Problem:** lorem_ipsum

**Requirements:**
* lorem_ipsum
* lorem_ipsum

```
code sample
```
- [ ] *File:* [Task_13](link_to_file)

---

#### Task_014

**Problem:** lorem_ipsum

**Requirements:**
* lorem_ipsum
* lorem_ipsum

```
code sample
```
- [ ] *File:* [Task_14](link_to_file)

---

<h2 style="text-align: center;">Collaborative Author(s)</h2>

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
