Web2
====

## Лекция

TODO

<!--
Часть 1: [pdf](https://github.com/xairy/mipt-ctf/raw/master/04-web/slides.pdf), [online](https://docs.google.com/presentation/d/1Zcc4av7v9B3ZGEShVkaVYCBy-NGMxFkN-6f2gbr_uCU/edit?usp=sharing).
-->


## Задачи

Задачки взяты с [Security Override](http://securityoverride.org/) (требует регистрации) и [picoCTF 2014](https://picoctf.com/).

В задачках без условия нужно тем или иным образом добыть спрятанный на сайте флаг.

<!--
### injection1

http://web2014.picoctf.com/injection1/

### injection2

http://web2014.picoctf.com/injection2/
-->

### sql0

http://securityoverride.org/challenges/basic/8/

Задачка для разминки, флаг отправлять не нужно.

### sql1

https://2013.picoctf.com/problems/php3/

### sql2

http://securityoverride.org/challenges/basic/12/index.php?id=1

### sql3

http://web2014.picoctf.com/injection3/

### sql4\*

http://web2014.picoctf.com/injection4/

### sql5\*

https://2013.picoctf.com/problems/php4/

### xss1

http://securityoverride.org/challenges/basic/14/

Флагом является первое\_второе\_и\_третье\_слово в тексте, который показывается после решения задачки.

### xss2

The bad guys have hidden their access codes on an [anonymous secure page service](http://sps.picoctf.com/). Our intelligence tells us that the codes was posted on a page with id 43440b22864b30a0098f034eaf940730ca211a55, but unfortunately it's protected by a password, and only site moderators can view the post without the password. Can you help us recover the codes?


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9994
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи

https://picoctf.com/problems

http://securityoverride.org/challenges/

https://xss-game.appspot.com/


## Материалы

https://github.com/vpavlenko/ctf-web-tasks

TODO: more.
