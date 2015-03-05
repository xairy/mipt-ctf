Web3
====

## Лекция

[Часть 1](https://github.com/xairy/mipt-ctf/tree/master/04-web).

[Часть 2](https://github.com/xairy/mipt-ctf/tree/master/05-web2).

Часть 2:
TODO.

<!--
[pdf](https://github.com/xairy/mipt-ctf/raw/master/05-web2/slides.pdf),
[online](https://docs.google.com/presentation/d/1yyzmHGmIHnEbWAK33q89TD6w77rNeeXTyEczSemNuT8/edit?usp=sharing).
-->

## Старые задачи

В задачках без условия нужно тем или иным образом добыть спрятанный на сайте флаг.

### sql1

https://2013.picoctf.com/problems/php3/

### sql2 \*

http://web2014.picoctf.com/injection3/

[Hint 1.](http://web2014.picoctf.com/injection3/lookup_user.php?id=1)

[Hint 2.](http://web2014.picoctf.com/injection3/lookup_user.php?id=0 UNION SELECT 1,2,3,4,5,6,7 --)

[Hint 3.](http://www.mssqltips.com/sqlservertutorial/196/informationschematables/)

### sql3 \*

http://web2014.picoctf.com/injection4/

[Hint 1.](http://web2014.picoctf.com/injection4/register.phps)

[Hint 2.] (http://www.w3schools.com/sql/sql_like.asp)

### sql4 \*\*

https://2013.picoctf.com/problems/php4/


## Новые задачи

### sql5

https://wildwildweb.fluxfingers.net:1424/

### sql6\*\*

http://asis-ctf.ir:12441/

### fpd

The flag is the full local path of the file.

http://canyouhack.it/Content/Challenges/Web/Web8.php?Page=Home


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9993
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи

https://picoctf.com/problems

http://canyouhack.it/

http://securityoverride.org/challenges/


## Материалы

https://github.com/vpavlenko/ctf-web-tasks

[Presentation on SQL injections by h34dump](https://docs.google.com/presentation/d/1Vks9AO7bA9OaABLBzyjNN0Z6wNKP_92JUoW28rYYAFY/edit#slide=id.g1284d550_1_15)

https://www.owasp.org/index.php/XPATH\_Injection
