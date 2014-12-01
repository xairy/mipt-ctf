Web
===

## Задачи

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

### inspection

On his computer, your father left open a browser with the [Thyrin Lab Website](https://picoctf.com/api/autogen/serve/index.html?static=false&pid=28baa70afa1967ff63b201f687b7533e). Can you find the hidden access code?

### contact

You notice that the indicator light near the robot’s antenna begins to blink. Perhaps the robot is connecting to a network? Using a wireless card and the network protocol analyzer Wireshark, you are able to create a PCAP file containing the packets sent over the network.

You suspect that the robot is communicating with the crashed ship. Your goal is to find the location of the ship by inspecting the network traffic.

You can perform the analysis online on [Cloudshark](http://www.cloudshark.org/captures/bc1c0a7fae2c) or you can download the [PCAP file](https://2013.picoctf.com/problems/first_contact.pcap).

### listed\*

http://canyouhack.it/Content/Challenges/Web/Web6.php

### path\*\*

The password is the full local path of the file.

http://canyouhack.it/Content/Challenges/Web/Web8.php


## Флаги

Отправлять флаги на сервер таким образом:
```
$ nc andreyknvl.com 9995
username taskname 73c0487d1b4c9326bc4ec5ac09bf69eb
```
где username - имя для таблицы результатов, а taskname - название задачи.

Доступна [таблица результатов](https://andreyknvl.com/mipt-ctf).


## Дополнительные задачи

http://canyouhack.it/

### ddos\*

It appears a SYN-flood style DDoS has been carried out on this system. Send us a list of the IP addresses of the attackers (in any order, separated by spaces), so we can track them down and stop them.

Pcap available to download [here](https://2013.picoctf.com/problems/syn_attack.pcap), or available to analyse online at [CloudShark](http://www.cloudshark.org/captures/88971318a309).

Hint: What's a defining pattern in a [syn flood attack](http://en.wikipedia.org/wiki/SYN_flood)?


## Материалы

TODO
