Reverse
=======

## Лекция

TODO


## Материалы

[Introduction to return oriented programming (ROP)](https://web.archive.org/web/20141130082019/http://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html)

[Introduction to format string exploits](https://web.archive.org/web/20130925222312/http://codearcana.com/posts/2013/05/02/introduction-to-format-string-exploits.html)

[Shellcodes database](http://shell-storm.org/shellcode/)

[Linux x86 Program Start Up](http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html)


## Инструменты

http://www.trapkit.de/tools/checksec.html

http://shell-storm.org/project/ROPgadget/

https://github.com/zTrix/zio


## ASLR

Перед решением задачек нужно выключить [ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization):
```
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```

Чтобы его включить обратно:
```
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
```


## Задачи

Задачи взяты с [picoCTF 2013](https://2013.picoctf.com).
Кто там зарегистрирован, можете решать задачки на их серверах.
Кто нет, можете зарегистрироваться, но для того, чтобы открылись все задачки нужно сначала прорешать несколько первых.

В каждой задаче нужно найти уязвимость и с ее помощью запустить шелл.

## overflow1

[Исходник](https://2013.picoctf.com/problems/overflow1-3948d17028101c40.c),
[бинарник](https://2013.picoctf.com/problems/overflow1-3948d17028101c40).

## overflow2

[Исходник](https://2013.picoctf.com/problems/overflow2-44e63640e033ff2b.c),
[бинарник](https://2013.picoctf.com/problems/overflow2-44e63640e033ff2b).

## overflow3

[Исходник](https://2013.picoctf.com/problems/overflow3-28d8a442fb232c0c.c),
[бинарник](https://2013.picoctf.com/problems/overflow3-28d8a442fb232c0c).

## overflow4

[Исходник](https://2013.picoctf.com/problems/overflow4-4834efeff17abdfb.c),
[бинарник](https://2013.picoctf.com/problems/overflow4-4834efeff17abdfb).

## rop1

[Исходник](https://2013.picoctf.com/problems/rop1-fa6168f4d8eba0eb.c),
[бинарник](https://2013.picoctf.com/problems/rop1-fa6168f4d8eba0eb).

## rop2

[Исходник](https://2013.picoctf.com/problems/rop2-20f65dd0bcbe267d.c),
[бинарник](https://2013.picoctf.com/problems/rop2-20f65dd0bcbe267d).

## rop3

[Исходник](https://2013.picoctf.com/problems/rop3-7f3312fe43c46d26.c),
[бинарник](https://2013.picoctf.com/problems/rop3-7f3312fe43c46d26).

## format1

[Исходник](https://2013.picoctf.com/problems/format1.c),
[бинарник](https://2013.picoctf.com/problems/format1).

## format2

[Исходник](https://2013.picoctf.com/problems/format2.c),
[бинарник](https://2013.picoctf.com/problems/format2).


## Дополнительные задачи

http://overthewire.org/wargames/

https://exploit-exercises.com/
