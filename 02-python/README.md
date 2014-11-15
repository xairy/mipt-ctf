Python
======

## Задачи

### Simple

Флагом является ввод, при котором [программа](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/simple.py) печатает "Success!".

### Bitwise

Флагом является ввод, при котором [программа](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/bitwise.py) печатает "Success".

Задача взята из [picoCTF 2013](https://2013.picoctf.com).

### Eval

Набор задачек на эксплуатацию уязвимостей в сервисах, использующих функцию eval.

В задачах 1 и 2 нужно узнать значение переменной flag.
В задачах 3, 4 и 5 нужно получить доступ к консоли и прочитать флаг из файла.


Eval 1: [условие](https://2013.picoctf.com/problems/pyeval/stage1.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/eval1.py), флаг брать здесь:
```
nc python.picoctf.com 6361
```

Eval 2: [условие](https://2013.picoctf.com/problems/pyeval/stage2.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/eval2.py), флаг брать здесь:
```
nc python.picoctf.com 6362
```

Eval 3: [условие](https://2013.picoctf.com/problems/pyeval/stage3.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/eval3.py), флаг брать здесь:
```
nc python.picoctf.com 6363
```

Eval 4: [условие](https://2013.picoctf.com/problems/pyeval/stage4.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/eval4.py), флаг брать здесь:
```
nc python.picoctf.com 6364
```

Eval 5: [исходник](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/eval5.py), флаг брать здесь:
```
nc python.picoctf.com 6365
```

Задачи взяты из [picoCTF 2013](https://2013.picoctf.com).

### QR Code

Условие задачи qrcode будет раздаваться на занятии.


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9997
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи

1. Смотреть задачи [здесь](https://github.com/vpavlenko/startup-engineering/tree/gh-pages/python-bis)

2. Распаковать [архив](https://github.com/xairy/mipt-ctf/blob/master/02-python/tasks/brute.zip), пароль словарный.


## Материалы

https://github.com/vpavlenko/startup-engineering/tree/gh-pages/python-bis

http://www.slideshare.net/MattHarrison4/learn-90

https://en.wikipedia.org/wiki/Eval#Python
