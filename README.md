CTF на Физтехе
==============

Курс по подготовке к соревнованиям по компьютерной безопасности формата CTF.
Занятия проходят по средам в 20:00 в 324б ЛК.

Каждое занятие состоит из небольшой лекции и практики в виде решения задачек на определенную тему.
Предварительная подготовка не требуется.
Желательно наличие собственного компьютера, но пользоваться компьютерами в аудитории тоже возможно.

[Группа ВКонтакте](https://vk.com/mipt_ctf).

## Программа

**28 октября.** [Компьютерная безопасность. Что такое CTF. Attack-defence, jeopardy (task-based). УК РФ. Командная оболочка bash. Полезные команды и утилиты.](https://github.com/xairy/mipt-ctf/tree/master/01-intro/01-bash)

## План на 2015-2016

Предварительный план того, что будет в этом году.

* Intro
    * Что такое CTF. Введение в bash, полезные команды.
    * Введение в Python. Основной синтаксис, регулярные выражения.
    * Escaping python sandboxes. TODO.
* Crypto
    * Кодировки (ASCII, ANSI Code Pages, Unicode, UTF-8/16/32). base64. Симметричные шифры. Шифры Цезаря, простой замены, Вижинера. Частотный анализ, индекс совпадений. Одноразовый блокнот. AES, 3DES, Blowfish.
    * Ассиметричные шифры. Протокол Диффи-Хеллмана, RSA. Электронная цифровая подпись, сертификат открытого ключа. SSL, TLS. Как работает HTTPS.
    * Криптографические хеш-функции (MD5, SHA\*, ГОСТ\*). Реализация MD5. Коллизии. Length extension attack. Storing passwords, salt. Cracking passwords. John the Ripper, hashcat. Словари. Радужные таблицы.
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
