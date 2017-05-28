Python
======

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/slides.pdf),

[Скринкаст](https://www.youtube.com/watch?v=qUt1GRY8YD8)

Примеры:
[0](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/examples/eval_examples_0.py),
[1](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/examples/eval_examples_1.py),
[2](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/examples/eval_examples_2.py),
[3](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/examples/eval_examples_3.py),
[4](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/examples/eval_examples_4.py).

## Задачи

### Eval

Набор задачек на эксплуатацию уязвимостей в сервисах, использующих функцию `eval`.

В задачах 1 и 2 нужно узнать значение переменной flag.
В задачах 3, 4 и 5 нужно получить доступ к консоли и прочитать флаг из файла.


Eval 1: [условие](https://2013.picoctf.com/problems/pyeval/stage1.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/tasks/eval1.py), флаг брать здесь:
```
nc python.picoctf.com 6361
```

Eval 2: [условие](https://2013.picoctf.com/problems/pyeval/stage2.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/tasks/eval2.py), флаг брать здесь:
```
nc python.picoctf.com 6362
```

Eval 3: [условие](https://2013.picoctf.com/problems/pyeval/stage3.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/tasks/eval3.py), флаг брать здесь:
```
nc python.picoctf.com 6363
```

Eval 4: [условие](https://2013.picoctf.com/problems/pyeval/stage4.html), [исходник](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/tasks/eval4.py), флаг брать здесь:
```
nc python.picoctf.com 6364
```

Eval 5: [исходник](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/tasks/eval5.py), флаг брать здесь:
```
nc python.picoctf.com 6365
```

Задачи взяты из [picoCTF 2013](https://2013.picoctf.com).


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9997
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи

1. [Задачка](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/tasks/exec.py) с [CSAW CTF 2014](https://ctf.isis.poly.edu/).


## Разбор задач

[Разбор задач](https://github.com/xairy/mipt-ctf/blob/master/01-intro/03-eval/WRITEUP.md)


## Материалы

[Python Built-In Functions: eval](https://docs.python.org/2/library/functions.html#eval)

[Wikipedia: Eval in Python](https://en.wikipedia.org/wiki/Eval#Python)

[picoCTF: eval: stage 1](https://2013.picoctf.com/problems/pyeval/stage1.html)

[picoCTF: eval: stage 2](https://2013.picoctf.com/problems/pyeval/stage2.html)

[picoCTF: eval: stage 3](https://2013.picoctf.com/problems/pyeval/stage3.html)


## Всякое

[Разгадываем картинку из твиттера компании Intel](https://habrahabr.ru/post/257757/)

[Fuckpyjails Writeup](http://blog.germano.io/2014/fuckpyjails-writeup-9447-ctf/)

[PlaidCTF 2014 '\_\_nightmares\_\_' (Pwnables 375) Writeup](https://blog.mheistermann.de/2014/04/14/plaidctf-2014-nightmares-pwnables-375-writeup/)
