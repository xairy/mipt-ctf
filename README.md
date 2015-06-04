CTF на Физтехе
==============

Курс по подготовке к соревнованиям по компьютерной безопасности CTF.
Читался в 2014-2015 учебном году, в 2015-2016 будет прочитан еще раз.
Начало занятий планируется в конце октября 2015, следите за новостями в [группе](https://vk.com/mipt_ctf).

Каждое занятие состоит из небольшой лекции и практики в виде решения задачек на определенную тему.
Предварительная подготовка не требуется.
Желательно наличие собственного компьютера, но пользоваться компьютерами в аудитории тоже возможно.

[Группа ВКонтакте](https://vk.com/mipt_ctf).

**Реклама.**
Ещё на Физтехе читается [курс по веб-программированию](https://vk.com/mipt_web).

## План на 2015-2016

Предварительный план того, что будет в следующем году.

* Intro
    * Что такое CTF. Введение в bash, полезные команды.
    * Введение в Python. Основной синтаксис, регулярные выражения.
    * Escaping python sandboxes. TODO.
* Crypto
    * Кодировки (ASCII, ANSI Code Pages, Unicode, UTF-8/16/32). base64. Симметричные шифры. Шифры Цезаря, простой замены, Вижинера. Частотный анализ, индекс совпадений. Одноразовый блокнот. AES, 3DES, Blowfish.
    * Ассиметричные шифры. Протокол Диффи-Хеллмана, RSA. Электронная цифровая подпись, сертификат открытого ключа. SSL, TLS. Как работает HTTPS.
    * Криптографические хеш-функции (MD5, SHA*, ГОСТ*). Реализация MD5. Коллизии. Length extension attack. Storing passwords, salt. Cracking passwords. John the Ripper, hashcat. Словари. Радужные таблицы.
    * Стеганография. TODO.
* Net
    * Введение в Веб. ip, port, DNS, netcat (-l), ping (of death), nmap. HTTP, HTTPS, HTTP headers, GET/POST/…, cookies. curl, python requests. Browser dev tools, plugins.
    * Анализ трафика. tcpdump. Wireshark. TODO.
    * SQL-инъекции. TODO.
    * Остальные типы инъекций (XPATH, Command, LDAP). XSS, CSRF. robots.txt, FPD. LFI, RFI, .htaccess, .htpasswd, .svn, .git. Dirbuster. MITM, DDOS.
* Binary
    * Ассемблер. Intel и AT&T синтаксисы. Регистры x86, x64. Основные команды. Flags register. Calling conventions. Inline gcc asm. NASM. Контест по NASM’у.
    * Дисассемблирование. Во что компилируется Hello world. Как работают кряки. Binary patching tools (bsdiff, bspatch, …). Утиные истории.
    * Инструменты для реверса. file, strings, readelf, objdump, strace, gdb. IDA Pro, Hopper. Qira. Как устроен ELF. C++, Go и Rust бинарники. Обфускация, деобфускация. Пакеры. Anti debugger. Visual RE.
    * Buffer overflow. Shellcode. Non-executable stack, stack canaries, ASLR, RELRO. checksec.sh. String format exploit. Overwriting PLT. Controlling gdb environment, keeping stdin open.
    * ROP. return-to-libc. gadgets, gadget finders. python struct, zio. Bypassing ASLR on x32. Heap buffer overflow.

## Программа 2014-2015

### Осенний семестр

**29 октября.**
[Что такое CTF. Какие бывают задачки. Командная оболочка bash. Полезные команды.]
(https://github.com/xairy/mipt-ctf/tree/master/01-bash)

**11 и 18 ноября.**
[Введение в язык Python. Escaping Python sandboxes.]
(https://github.com/xairy/mipt-ctf/tree/master/02-python)

**25 ноября.**
[Криптография, часть 1. Кодировки (ASCII, Unicode, base64). Шифры Цезаря, простой подстановки и Виженера. Частотный анализ. Индекс совпадений.]
(https://github.com/xairy/mipt-ctf/tree/master/03-crypto)

**2 декабря.**
[Веб, часть 1. nmap, HTTP/HTTPS, cookies, Python requests, curl, robots.txt. ]
(https://github.com/xairy/mipt-ctf/tree/master/04-web)

### Весенний семестр

**26 февраля**
[Веб, часть 2. Инъекции. SQLi, XSS, LFI, RFI.]
(https://github.com/xairy/mipt-ctf/tree/master/05-web2)

**5 марта**
[Веб, часть 3. Command Injection, CSRF, XPATH Injection, MITM, DDOS.]
(https://github.com/xairy/mipt-ctf/tree/master/06-web3)

**12 марта**
[Криптография, часть 2. Асимметричное шифрование, протокол Диффи-Хеллмана, RSA, электронная цифровая подпись, сертификат открытого ключа. Криптографические хеш-функции, Length Extension Attack.]
(https://github.com/xairy/mipt-ctf/tree/master/07-crypto2)

**19 марта**
[Реверс, часть 1. Ассемблер. Синтаксисы Intel и AT&T.]
(https://github.com/xairy/mipt-ctf/tree/master/08-reverse)

**26 марта**
[Реверс, часть 2. Ассемблер. NASM.]
(https://github.com/xairy/mipt-ctf/tree/master/09-reverse2)

**2 апреля**
[Реверс, часть 3. Binary patching. ]
(https://github.com/xairy/mipt-ctf/tree/master/10-reverse3)

**16 апреля**
[Реверс, часть 4. Инструменты для реверса. gdb, strace. ]
(https://github.com/xairy/mipt-ctf/tree/master/11-reverse4)

**23 апреля**
[Реверс, часть 5. Buffer overflow и format string exploit'ы. ]
(https://github.com/xairy/mipt-ctf/tree/master/12-reverse5)

**7 мая**
[Реверс, часть 6. Return-Oriented-Programming. Гаджеты, ROPgadget. zio. ]
(https://github.com/xairy/mipt-ctf/tree/master/13-reverse6)

**21 мая**
[Advanced. Эксплуатация уязвимостей беспроводных сетей. airmon-ng, airodump-ng, aircrack-ng. wifite. reaver. ]
(https://github.com/xairy/mipt-ctf/tree/master/14-advanced)
