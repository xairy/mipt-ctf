Bash
====

### Задачи

Условия задач брать здесь:
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

Сдавать флаги вот так:
```
$ nc andreyknvl.com 9998
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```

Доступна таблица результатов TODO

### Материалы

[Презентация на паре](01-bash-presentation.pdf)
[Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
[DigitalOcean: Using Grep & Regular Expressions to Search for Text Patterns in Linux](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux)
