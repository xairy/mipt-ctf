Crypto
======

## Лекция

Часть 1: [слайды](https://github.com/xairy/mipt-ctf/raw/master/03-crypto/slides.pdf).

Часть 2: Not yet.

## Задачи

Многие задачи взяты [отсюда](https://github.com/vpavlenko/ctf-crypto-tasks).

### simple

```
01100010 01101001 01100111 01011111 01100010 01110010 01101111 01110100 01101000 01100101 01110010 01011111 01101001 01110011 01011111 01110111 01100001 01110100 01100011 01101000 01101001 01101110 01100111 01011111 01111001 01101111 01110101
```

### 46esab

```
Kw2bvN2X5JXZ29VeyVmdflnclZ3Xzl2X0YTZzFmY
```

### steps

```
5647686c636d56666257463558324a6c58323168626e6c666333526c63484d3d
```

### caesar

```
Wkh_Txlfn_Eurzq_Ira_Mxpsv_Ryhu_Wkh_Odcb_Grj
```

### start

После шифрования текста с помощью [программы](https://github.com/xairy/mipt-ctf/blob/master/03-crypto/tasks/start.py) был получен [файл](https://github.com/xairy/mipt-ctf/blob/master/03-crypto/tasks/start.dat). Расшифруйте.

Файл нужно скачать, нажав на кнопку Raw.
Просто скопировать не получится, поскольку часть данных не отображается браузером.

### analyze

Условие [тут](https://github.com/xairy/mipt-ctf/blob/master/03-crypto/tasks/analyze.txt).

Флагом является имя\_автора.

### vigenere\*

После шифрования текста с помощью [программы](https://github.com/xairy/mipt-ctf/blob/master/03-crypto/tasks/vigenere.py) был получен [файл](https://github.com/xairy/mipt-ctf/blob/master/03-crypto/tasks/vigenere.dat). Расшифруйте.

Файл нужно скачать, нажав на кнопку Raw.
Просто скопировать не получится, поскольку часть данных не отображается браузером.

Флагом являемся имя\_оригинального\_автора.

### mary\*\*

Условие [тут](https://github.com/xairy/mipt-ctf/blob/master/03-crypto/tasks/mary.txt).

Флагом является произведение года рождения и года смерти автора.


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9996
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи

Смотреть [здесь](https://github.com/vpavlenko/ctf-crypto-tasks).


## Материалы

https://github.com/vpavlenko/ctf-crypto-tasks

http://www.joelonsoftware.com/articles/Unicode.html

http://utf8everywhere.org/

https://en.wikipedia.org/wiki/Base64

https://en.wikipedia.org/wiki/Caesar_cipher

https://en.wikipedia.org/wiki/Vigenere_cipher
