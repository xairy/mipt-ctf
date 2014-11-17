bash
====

## Задачи

Условия задач брать [здесь](https://andreyknvl.com/mipt-ctf/tasks/bash-tasks.tar.gz):
```
$ wget https://andreyknvl.com/mipt-ctf/tasks/bash-tasks.tar.gz
$ tar -xzf bash-tasks.tar.gz
$ cd bash-tasks/
$ ls
apart dense flip order path simple storage
```

Каждый файл - отдельная задача.
Для решения необходимо тем или иным образом извлечь из файла флаг вида flag{73c0487d1b4c9326bc4ec5ac09bf69eb}.
Для каждой из задачек рекомендуется для начала посмотреть на тип файла с помощью утилиты file.
Например:
```
$ file simple
simple: ASCII text
```

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9998
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).

## Материалы

[Презентация на паре](https://github.com/xairy/mipt-ctf/raw/master/01-bash/01-bash-presentation.pdf)

[Using Grep & Regular Expressions to Search for Text Patterns in Linux](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux)

[Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
