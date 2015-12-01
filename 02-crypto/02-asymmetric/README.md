Crypto
======

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/tree/master/02-crypto/02-asymmetric/slides.pdf)


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

### fermat

Моя веселая ФЕРМА.

Играя в свою любимую игру, я наткнулся на данные ниже. Помогите разобраться с этим! Я хочу купить новый хвост для коровы.

```
{
  "n":55730048063717018374316281207573259125944928596988375563008761242928555444475159973323697033529485947694144334157841984089222608221659443869403243311377775287940043976050079897679344195429140671152006335092107296007295641129810127120597697958505609557108821553087048650668127879505133240481364133955404508724801433652620134539765901833015644832323224073360418288546329260222548709056388931692867087156683666545959017505300012887342748040633895056662119255382438961050252741419077501234468618586586761527436899702065013210399451488547753808782146177428317609036251342347553017178247158741715583011215815698806579497027,
  "e":65537,
  "enc_data":25234514147851501650928728210405740434891970671488428405196440434538180451319426356822060051035053769070087646943825115802785624107829588035763512660763770355863470442359006751937231446693677756587159506517057107545904847781133985450962418304405156723626987851757046221296000186129919558271304842917074255645894198513219579694940888303668954853572211412406774298397963087228995608199961416160365961933944487096937024121738220372895375686782970385612792024930159117151472088279156003279742341584430863692287750584160827079689586790181031407137862737274577936446435723045268025310178271959285118689249074803904304795181
}
```

### prime

```
Алиса и Боб сидят в чате.

Алиса: Боб, давай я тебе скажу кое-что секретное?
Боб: Алиса, окей. Только все остальные же узнают, если ты прямо здесь это напишешь.
Алиса: Давай использовать Диффи-Хеллмана для генерации секретного ключа. Я зашифрую на нём сообщение алгоритмом Rijndael-256 в режиме CBC. Расшифруешь вот тут: http://www.tools4noobs.com/online_tools/decrypt/
Боб: Окей.
Алиса: g = 5, g ** a = 3552713678800500929355621337890625.
Боб: g ** b = 100974195868289511092701256356196637398170423693954944610595703125.
Алиса: Зашифровала: 0M2lm0nZFN4kWuagdb6Azsk1fPs9O1P+AA2N6BMdRnKXMVoOlCcfvhlz2jIdbKzZZOuDc9Q+KYtnb5FjrKlj5A==
Боб: А нам точно не нужен простой модуль p?
```

### short

```
Боб: Боюсь, предыдущее сообщение легко расшифровали. Давай заново, и теперь с простым модулем. Смотри не накосячь!
Алиса: Постараюсь. g = 5, p = 19208302915743920857294037403209473409509, pow(g, a, p) = 10986351755751103712777758371696540996168
Боб: pow(g, b, p) = 4737807098550297950358929203191827188641
Алиса: Gq7qV1a7aHWQLa5GA43W8Qi4D23LbRI9xlNeDt/Cdra0nV+HcUyUPs1SGJvoNmGsmV90UC9gLI8fmnOqpj4WXA==
```

### broken\*\*

[This RSA service](https://github.com/xairy/mipt-ctf/tree/master/02-crypto/02-asymmetric/broken_rsa_source.py) seems to be broken.
They encrypt the flag and send it to you each time... but they throw out the private key and you never get to see it.
Any ideas on how to recover the flag?

Connect from the shell with 'nc vuln.picoctf.com 6666'.

### mistakes\*\*

Daedalus Corp seems to have had a very weird way of broadcasting some secret data.
We managed to find [the server code that broadcasted it, and one of our routers caught some of their traffic](https://picoctf.com/problem-static/crypto/rsa-mistakes/handout.zip) - can you find the secret data?
We think someone may have requested the secret using someone else's user id by accident, but we're not sure.


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9995
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Разбор задач.

TODO


## Материалы

[Wikipedia: Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)

[Weak Diffie-Hellman and the Logjam Attack](https://weakdh.org/)

[Wikipedia: RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

[Wikipedia: HTTPS](https://en.wikipedia.org/wiki/HTTPS)

[How does HTTPS actually work?](http://robertheaton.com/2014/03/27/how-does-https-actually-work/)

[SSL/TLS & Perfect Forward Secrecy](http://vincent.bernat.im/en/blog/2011-ssl-perfect-forward-secrecy.html)
