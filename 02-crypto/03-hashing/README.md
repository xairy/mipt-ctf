Хеширование
===========

## Лекция

[Презентация](https://github.com/xairy/mipt-ctf/tree/master/02-crypto/03-hashing/slides.pdf)

[Скринкаст](https://www.youtube.com/watch?v=DyrV8-xWHBs)


## Задачи

Некоторые задачи взяты [отсюда](https://github.com/vpavlenko/ctf-crypto-tasks).
Для решения некоторых задачек вам могут пригодиться [словарь английских слов](http://downloads.skullsecurity.org/passwords/english.txt.bz2) и [словарь rockyou](http://downloads.skullsecurity.org/passwords/rockyou.txt.bz2).

### year

Гриша был зарегистрирован на одном сайте, базу паролей которого недавно взломали и выложили. Хэш его пароля: `3517c55f3ffdd3322ccbe12039e33758`. В каком году он родился?

### salt

Пароль был захеширован последующей схеме:

```
>>> salt = 'sI8dM1B9sWx'
>>> password = '...'
>>> print hashlib.sha256(salt + password).hexdigest()
0e5f530f5b00f812dd2aaa49bf023042cb13ca0582d301bae765d137214e6bcc
```

Какой это был пароль?

### mac

Сообщение подписывается ключом:

```
>>> key = '...'
>>> len(key)
15
>>> message = 'Hello world!'
>>> print hashlib.md5(key + message).hexdigest()
d8cecce59ccd894493717de77ff328a0
```

Подпишите ещё какое-нибудь сообщение тем же ключом. Пришлите его мне, и я выдам вам флаг.

### secret

Пароль был захеширован по следующей схеме:

```
>>> secret = 'PiIT7xSILB1he5ukuFU9HvtCbIh0Ae6vtS4RoIVY'
>>> salt = '8ksr5VNMegrVOPCB'
>>> password = '...'
>>> print hashlib.md5(secret + password + salt).hexdigest()
1183da1ecc1b8f13ae7307a3f026ace2
```

Какой это был пароль?

### rules\*

Пароль был захеширован с помощью обычного MD5.
Полученный хеш: `09c212ea86b841ed9a9fa80e09585b97`.
Какой это был пароль?

### bcrypt\*

Пароль был захеширован с помощью bcrypt.
Полученный хеш: `$2a$10$9fVGdOnRm8mox7vRc9FUV..tVvLoKX2b5g56LBe84rSF3pqgUhGTW`.
Какой это был пароль?

### gpu\*\*

Пароль был захеширован по следующей схеме:

```
>>> salt = '17732831'
>>> password = '...'
>>> print hashlib.md5(password + salt).hexdigest()
59b18904b1e912c10ee415934ad2bc0a
```

Какой это был пароль?

### elf\*\*

Создайте два исполняемых 32-битных ELF файла с совпадающим md5-хешем.
Один из файлов должен выводить при запуске строку `MD5 is insecure`, а второй - `Use SHA-3 whatever that means`.
Пришлите обе программы мне, и я выдам вам флаг.

## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9994
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).

## Разбор задач.

TODO

## Материалы

[MD5](https://en.wikipedia.org/wiki/MD5)

[SHA-1](https://en.wikipedia.org/wiki/SHA-1)

[SHA-2](https://en.wikipedia.org/wiki/SHA-2)

[SHA-3](https://en.wikipedia.org/wiki/SHA-3)

[bcrypt](https://en.wikipedia.org/wiki/Bcrypt)

[Message authentication code (MAC)](https://en.wikipedia.org/wiki/Message_authentication_code)

[Hash-based message authentication code (HMAC)](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)

[Length extension attack](https://en.wikipedia.org/wiki/Length_extension_attack)

[Hash Extender by Ron Bowes](https://github.com/iagox86/hash_extender)

[Everything you need to know about hash length extension attacks](https://blog.skullsecurity.org/2012/everything-you-need-to-know-about-hash-length-extension-attacks)

[MD5 Collision Demo](http://www.mathstat.dal.ca/~selinger/md5collision/)

[Why You Shouldn't be using SHA1 or MD5 to Store Passwords](https://www.bentasker.co.uk/blog/security/201-why-you-should-be-asking-how-your-passwords-are-stored)

[How To Safely Store A Password](https://codahale.com/how-to-safely-store-a-password/)

[Rainbow table](https://en.wikipedia.org/wiki/Rainbow_table)

[The Rainbow Table Is Dead](http://blog.ircmaxell.com/2011/08/rainbow-table-is-dead.html)

[Cracking Story – How I Cracked Over 122 Million SHA1 and MD5 Hashed Passwords](http://blog.thireus.com/cracking-story-how-i-cracked-over-122-million-sha1-and-md5-hashed-passwords)
