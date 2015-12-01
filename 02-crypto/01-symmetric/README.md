Crypto
======

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/slides.pdf)

[Скринкаст](https://www.youtube.com/watch?v=bbbtWLbEUe4)

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

После шифрования текста с помощью [программы](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/tasks/start.py) был получен [файл](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/tasks/start.dat). Расшифруйте.

Файл нужно скачать, нажав на кнопку Raw.
Просто скопировать не получится, поскольку часть данных не отображается браузером.

### analyze

Условие [тут](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/tasks/analyze.txt).

Флагом является имя\_автора.

### vigenere\*

После шифрования текста с помощью [программы](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/tasks/vigenere.py) был получен [файл](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/tasks/vigenere.dat). Расшифруйте.

Файл нужно скачать, нажав на кнопку Raw.
Просто скопировать не получится, поскольку часть данных не отображается браузером.

Флагом являемся имя\_оригинального\_автора.

### pad\*

Одноразовый блокнот.

```
2426d6c3ef1a29652be80311a82c031d3ba564992d2fbf1d3bb3bee6cb523187e64ecb1af636b0a492571de1ac693ca10483736ee37912ccf544233c5507f14a14a8da2877a2b0d16a8cb90ce91bc0192fe733b4b254e834b943bf41278cf922314c9f8433 
242193b0cf1d236520ff145ce339140b69ec65dc2c2fbe0f77abf0f08e502885e759db1af62bf1bc834154f0e97b3ae445897d71f965128df456232e5210f15615be8e3460b8e5cc65d8a35eff0d94153aec22b0b54aba20b90ba24d2796f4226559879571 
2921c6c3c11c2a683dba081fb769050672a27c992e2eba0c77b3f1e18e563f80ee4f8f4af836e3b9985e44a3a8743bf600923075fe721589ba53762d4e16b84d13a88e306caff89e7fc3fa12f91fc01a2db537bcaa42bb34bb06eb5a68c5f939741c87872b 
2726d68d8c0c227569f60311b127510f3ba076d73d33ba1f32e6bef8c7462490ec42c15dbb65e3a09f5356eaa77d68e00b843076e47e1285f44523294f07f14b10abc13571bafeca208cb80be44bc61329f13baabd0dab20a743aa42748aad33741c9c832d 
316ec08ac105216569ee0308b769170777a937d73f23bf0b77a4f1b4cf51349cf642c054f629b0bd9f465ce7a86e29a1118f3060e5640f9fee0277205842a3471cbfcb3525b2fe9e65c2ae1be21bc6133cf426adb543e461a80daf0e738de823745a85943a 
2426d6c3ca07286569ec0302b0201e0035ec5ecd7a25b41623abf7fadd1531d5e144c257f62bf4f0965b53e6e97326f500927660f5724accfc4e622f4610e2161184cd357cabe48e53eeb330f75beb2e07c72fe4bf5da42ea017aa5a6e8ae37170528ec632 
3c2fc786de553a693df24604ab2c510d74a076c92923fb1731eacce1dd463994ec0bea57e72ce2b5da4655e6e96f26e813856272ff631fcced4370685303bc4719fbea286ba8fbd1758c8f10f91dd1043bfc26bdfa4cae35ac11deb5a6f80ad23745b838931
```

### mary\*\*

Условие [тут](https://github.com/xairy/mipt-ctf/blob/master/02-crypto/01-symmetric/tasks/mary.txt).

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

## Разбор задач.

TODO

## Материалы

https://github.com/vpavlenko/ctf-crypto-tasks

[The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html)

[UTF-8 Everywhere](http://utf8everywhere.org/)

[Wikipedia: Base64](https://en.wikipedia.org/wiki/Base64)

[Wikipedia: Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

[Wikipedia: Vigenere cipher](https://en.wikipedia.org/wiki/Vigenere_cipher)

[Wikipedia: One time pad](https://en.wikipedia.org/wiki/One-time_pad)

TODO: DES, 3DES, AES
