HTTP
====

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/tree/master/03-net/01-http/slides.pdf)

[Скринкаст](https://www.youtube.com/watch?v=rHKRivpG3uI)


## Задачи

[Wargame по вебу](http://overthewire.org/wargames/natas/).
Начнем решать на занятии.


## Дополнительные задачи

Еще задачки, если вдруг wargame наскучит или покажется слишком сложным.

Задачки взяты с [CanYouHack.It](http://canyouhack.it/) и [picoCTF 2014](https://picoctf.com/).

В задачках без условия нужно тем или иным образом добыть спрятанный на сайте флаг.

### simple

http://canyouhack.it/Content/Challenges/Web/Web1.php?Page=Guest

### cookie

http://canyouhack.it/Content/Challenges/Web/Web2.php

### invasion

http://canyouhack.it/Content/Challenges/Web/Web3.php

### google

http://canyouhack.it/Content/Challenges/Web/Web4.php

### toaster

Daedalus Corp. uses a [web interface](http://web2014.picoctf.com/toaster-control-1040194/) to control some of their toaster bots. It looks like they removed the command 'Shutdown & Turn Off' from the control panel. Maybe the functionality is still there...

### inspection\*

_Эту задачку можно решать, но сдать не получится._

On his computer, your father left open a browser with the [Thyrin Lab Website](https://picoctf.com/api/autogen/serve/index.html?static=false&pid=28baa70afa1967ff63b201f687b7533e). Can you find the hidden access code?

### listed\*

http://canyouhack.it/Content/Challenges/Web/Web6.php


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9992
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи 2

http://canyouhack.it/

http://ahack.ru/contest/

http://securityoverride.org/

## Материалы

[Сетевая модель OSI](https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_OSI)

[IP](https://ru.wikipedia.org/wiki/IP)

[TCP](https://ru.wikipedia.org/wiki/TCP)

[UDP](https://ru.wikipedia.org/wiki/UDP)

[Порт](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%80%D1%82_(%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B5_%D1%81%D0%B5%D1%82%D0%B8))

[Стек TCP/IP](https://ru.wikipedia.org/wiki/TCP/IP)

[HTTP](https://ru.wikipedia.org/wiki/HTTP)

[URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator)

[URL encoding](https://en.wikipedia.org/wiki/Percent-encoding)

[DNS](https://ru.wikipedia.org/wiki/DNS)

[Коды состояния HTTP](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP)

[Заголовки HTTP](https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B8_HTTP)

[Basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication)

[Digest access authentication](https://en.wikipedia.org/wiki/Digest_access_authentication)

[HTTP cookie](https://ru.wikipedia.org/wiki/HTTP_cookie)

[Session hijacking](https://en.wikipedia.org/wiki/Session_hijacking)

[HTML](https://ru.wikipedia.org/wiki/HTML)
