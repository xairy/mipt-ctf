bash
====

## Лекция

TODO

## Задачи

### Bandit wargame

[Bandit](http://overthewire.org/wargames/bandit/) - одна из игр от [overthewire.org](http://overthewire.org/).

Для перехода на следующий уровень нужно узнать пароль от юзера следующего уровня (например bandit1 для уровня 1).
Игра начинается с [уровня 0](http://overthewire.org/wargames/bandit/bandit1.html):
```
ssh bandit0@bandit.labs.overthewire.org
# password: bandit0
```

Имеет смысл прорешать хотя бы до 12 уровня включительно.

### Bash мини-CTF

Условия задач брать [здесь](https://github.com/xairy/mipt-ctf/raw/master/01-intro/01-bash/tasks.tar.gz):
```
$ wget https://github.com/xairy/mipt-ctf/raw/master/01-intro/01-bash/tasks.tar.gz
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
$ nc andreyknvl.com 9999
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).

## Разбор задач

TODO

## Материалы

[The art of command line](https://github.com/jlevy/the-art-of-command-line)

[Give me that one command you wish you knew years ago](https://www.reddit.com/r/linux/comments/mi80x/give_me_that_one_command_you_wish_you_knew_years/)

[Using Grep & Regular Expressions to Search for Text Patterns in Linux](https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux)

[Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
