Стеганография
===========

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/tree/master/02-crypto/04-stego/slides.pdf)

TODO: Скринкаст


## Задачи

Для того, чтобы скачать файлы в задачках, необходимо нажать на кнопку Raw.

### rar

Добыть флаг из [изображения](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/rar.jpg).

### exif

Добыть флаг из [изображения](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/exif.jpg).

### lsb

Добыть флаг из [изображения](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/lsb.png).

### reverse

Добыть флаг из [аудио](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/reverse.wav).

### only

Добыть флаг из [изображения](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/only.png).

Подсказка: R <= 1, G <= 1, B <= 1.

### spectro

Добыть флаг из [аудио](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/spectro.wav).

### palette\*

Добыть флаг из [изображения](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/palette.png).

### filter\*

Добыть флаг из [изображения](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/filter.png).

### qr\*\*

Добыть флаг из [видео](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/04-stego/tasks/qr.mp4).


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9993
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Разбор задач.

TODO


## Материалы

[Стеганография](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D0%B3%D0%B0%D0%BD%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F)

[EXIF](https://ru.wikipedia.org/wiki/EXIF)

[PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)

[JPEG](https://en.wikipedia.org/wiki/JPEG)

[Стеганография. Скрытие информации в изображениях](http://xain.hackerdom.ru/zine/online/issue0/Steganography.html)

[Общие проверки для BMP/PNG/JMP и других](http://kmb.ufoctf.ru/stego/pic_stego/main.html)

[Stegsolve](http://kmb.ufoctf.ru/stego/stegsolve/main.html)
