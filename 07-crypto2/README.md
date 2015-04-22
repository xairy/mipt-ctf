Crypto
======

## Лекция

[Часть 1](https://github.com/xairy/mipt-ctf/tree/master/03-crypto).

Часть 2:
[pdf](https://github.com/xairy/mipt-ctf/raw/master/07-crypto2/slides.pdf),
[онлайн](https://docs.google.com/presentation/d/1_wH9fFyCnPiZYMvVxsbkYfV4_jmHBCRgE8CT3rVTBGw/edit?usp=sharing),
[скринкаст](https://www.youtube.com/watch?v=g-IfMANVBdg).


## Асимметричное шифрование

Задачи взяты [отсюда](https://github.com/vpavlenko/ctf-crypto-tasks) и с [picoCTF 2014](https://picoctf.com/).

### rsa

A Daedalus Corp spy sent an RSA-encrypted message.
We got their key data, but we're not very good at math.
Can you decrypt it?
[Here](https://picoctf.com/problem-static/crypto/RSA/handout.tgz)'s the data.
Note that the flag is not a number but a number decoded as ASCII text.

### hexy

```
{"c": 2151755227352155628689133334816, "e": 7, "n": 4698616511411820332781170272631, "hint_for_last_step": "hex"}
```

### fermat \*

Моя веселая ФЕРМА.

Играя в свою любимую игру, я наткнулся на данные ниже. Помогите разобраться с этим! Я хочу купить новый хвост для коровы.

```
{
  "n":55730048063717018374316281207573259125944928596988375563008761242928555444475159973323697033529485947694144334157841984089222608221659443869403243311377775287940043976050079897679344195429140671152006335092107296007295641129810127120597697958505609557108821553087048650668127879505133240481364133955404508724801433652620134539765901833015644832323224073360418288546329260222548709056388931692867087156683666545959017505300012887342748040633895056662119255382438961050252741419077501234468618586586761527436899702065013210399451488547753808782146177428317609036251342347553017178247158741715583011215815698806579497027,
  "e":65537,
  "enc_data":25234514147851501650928728210405740434891970671488428405196440434538180451319426356822060051035053769070087646943825115802785624107829588035763512660763770355863470442359006751937231446693677756587159506517057107545904847781133985450962418304405156723626987851757046221296000186129919558271304842917074255645894198513219579694940888303668954853572211412406774298397963087228995608199961416160365961933944487096937024121738220372895375686782970385612792024930159117151472088279156003279742341584430863692287750584160827079689586790181031407137862737274577936446435723045268025310178271959285118689249074803904304795181
}
```

### broken\*\*

[This RSA service](https://github.com/xairy/mipt-ctf/tree/master/07-crypto2/broken_rsa_source.py) seems to be broken.
They encrypt the flag and send it to you each time... but they throw out the private key and you never get to see it.
Any ideas on how to recover the flag?

Running on vuln.picoctf.com

Hint: Connect from the shell with 'nc vuln.picoctf.com 6666'.
Read up on RSA and try to figure out why this might be bad...
Good luck!


## Хеширование

Задачи взяты [отсюда](https://github.com/vpavlenko/ctf-crypto-tasks).

### year

Гриша был зарегистрирован на одном сайте, базу паролей которого недавно взломали и выложили. Хэш его пароля: 3517c55f3ffdd3322ccbe12039e33758. В каком году он родился?

### salt

Пароль был зашифрован с использованием соли:

```
>>> salt = 'sI8dM1B9sWx'
>>> password = '...'
>>> print(hashlib.sha256((salt + password).encode('ascii')).hexdigest())
0e5f530f5b00f812dd2aaa49bf023042cb13ca0582d301bae765d137214e6bcc
```

Какой это был пароль?

### sign\*

Сообщение подписывается ключом:

```
>>> key = '...'
>>> len(key)
15
>>> message = 'Hello world!'
>>> print(hashlib.md5((key + message).encode('ascii')).hexdigest())
d8cecce59ccd894493717de77ff328a0
```

Подпишите ещё какое-нибудь сообщение тем же ключом. Пришлите его мне, и я выдам вам флаг.

### elf\*\*

Создайте два исполняемых файла ELF для 32-битного Линукса с совпадающим md5-хешем.
Один из файлов должен выводить при запуске строку `MD5 is insecure`, а второй - `Use SHA-3 whatever that means`.
Пришлите обе программы мне, и я выдам вам флаг

## Дополнительные задачи

Смотреть [здесь](https://github.com/vpavlenko/ctf-crypto-tasks).

### mistakes\*\*

Daedalus Corp seems to have had a very weird way of broadcasting some secret data.
We managed to find [the server code that broadcasted it, and one of our routers caught some of their traffic](https://picoctf.com/problem-static/crypto/rsa-mistakes/handout.zip) - can you find the secret data?
We think someone may have requested the secret using someone else's user id by accident, but we're not sure.


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9992
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

TODO
