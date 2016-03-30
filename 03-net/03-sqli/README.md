SQL инъекции
============

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/tree/master/03-net/03-sqli/slides.pdf)

[Скринкаст](https://www.youtube.com/watch?v=vwHyycHIYrY)


## Задачи

В задачках без условия нужно тем или иным образом добыть спрятанный на сайте флаг.

### sql1

http://web2014.picoctf.com/injection1/

### sql2

https://2013.picoctf.com/problems/php3/

### sql3

http://web2014.picoctf.com/injection3/

[Hint 1.](http://web2014.picoctf.com/injection3/lookup_user.php?id=1)

[Hint 2.](http://web2014.picoctf.com/injection3/lookup_user.php?id=0 UNION SELECT 1,2,3,4,5,6,7 --)

[Hint 3.](http://www.mssqltips.com/sqlservertutorial/196/informationschematables/)

### sql4

http://web2014.picoctf.com/injection4/

[Hint 1.](http://web2014.picoctf.com/injection4/register.phps)

[Hint 2.] (http://www.w3schools.com/sql/sql_like.asp)

### sql5

https://2013.picoctf.com/problems/php4/

### sql6

https://wildwildweb.fluxfingers.net:1424/

https://wildwildweb.fluxfingers.net:1424/index.phps



## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9990
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Разбор задач

[Разбор задач](https://github.com/xairy/mipt-ctf/blob/master/03-net/03-sqli/WRITEUP.md)


## Дополнительные задачи

https://picoctf.com/problems

http://canyouhack.it/

http://securityoverride.org/challenges/


## Материалы

[Presentation on SQL injections by h34dump](https://docs.google.com/presentation/d/1Vks9AO7bA9OaABLBzyjNN0Z6wNKP_92JUoW28rYYAFY/edit#slide=id.p)

[SQL Injection от А до Я](http://www.ptsecurity.ru/download/PT-devteev-Advanced-SQL-Injection.pdf)

[Stacked queries](http://www.sqlinjection.net/stacked-queries/)

[Tactical Fuzzing - SQLi](https://github.com/jhaddix/tbhm/blob/master/6_SQLi.markdown)

[sqlmap](https://github.com/sqlmapproject/sqlmap)
