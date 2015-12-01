Разбор [задачек по криптографии](https://github.com/xairy/mipt-ctf/tree/master/02-crypto/01-symmetric).

## simple

В условии задачки приведен список двоичных чисел. Судя по тому, что они 8-битные, логично предположить, что каждое число - это символ в ASCII кодировке.

```
$ python
>>> a = '01100010 01101001 01100111 01011111 01100010 01110010 01101111 01110100 01101000 01100101 01110010 01011111 01101001 01110011 01011111 01110111 01100001 01110100 01100011 01101000 01101001 01101110 01100111 01011111 01111001 01101111 01110101'
>>> ''.join(map(lambda x: chr(int(x, 2)), a.split()))
'big_brother_is_watching_you'
```

## 46esab

Название задачки - это перевернутая строка 'base64'.
Попробуем развернуть строку из условия и раскодировать с помощью base64.

```
$ echo 'Kw2bvN2X5JXZ29VeyVmdflnclZ3Xzl2X0YTZzFmY' | rev | base64 --decode
base64_is_very_very_very_cool
```

## steps

В условии дано длинное шестнадцатиричное число четной длины.
Если разбить его на группы по два символа, то каждая группа будет числом, кодирующим один байт.
Сделаем это и преобразуем каждый байт в символ, в соответствии с ASCII кодировкой.

```
$ python
>>> a = '5647686c636d56666257463558324a6c58323168626e6c666333526c63484d3d'
>>> a.decode('hex')
'VGhlcmVfbWF5X2JlX21hbnlfc3RlcHM='
```

Мы получили строку, которая заканчивается на символ '='.
Это типичная особенность base64.
Раскодируем.

```
>>> import base64
>>> base64.b64decode(a.decode('hex'))
'There_may_be_many_steps'
```

## caesar

Название задачки намекает, что строка была зашифрована шифром Цезаря.
Переберем все возможные сдвиги и для каждого из них выпишем результат дешифровки.

```
$ python
>>> a = 'Wkh_Txlfn_Eurzq_Ira_Mxpsv_Ryhu_Wkh_Odcb_Grj'
>>> import string
>>> def rotn(n):
...   from string import ascii_lowercase as lc, ascii_uppercase as uc
...   mapping = string.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
...   return mapping
... 
>>> for n in xrange(26):
...   a.translate(rotn(n))
... 
'Wkh_Txlfn_Eurzq_Ira_Mxpsv_Ryhu_Wkh_Odcb_Grj'
'Xli_Uymgo_Fvsar_Jsb_Nyqtw_Sziv_Xli_Pedc_Hsk'
'Ymj_Vznhp_Gwtbs_Ktc_Ozrux_Tajw_Ymj_Qfed_Itl'
'Znk_Waoiq_Hxuct_Lud_Pasvy_Ubkx_Znk_Rgfe_Jum'
'Aol_Xbpjr_Iyvdu_Mve_Qbtwz_Vcly_Aol_Shgf_Kvn'
'Bpm_Ycqks_Jzwev_Nwf_Rcuxa_Wdmz_Bpm_Tihg_Lwo'
'Cqn_Zdrlt_Kaxfw_Oxg_Sdvyb_Xena_Cqn_Ujih_Mxp'
'Dro_Aesmu_Lbygx_Pyh_Tewzc_Yfob_Dro_Vkji_Nyq'
'Esp_Bftnv_Mczhy_Qzi_Ufxad_Zgpc_Esp_Wlkj_Ozr'
'Ftq_Cguow_Ndaiz_Raj_Vgybe_Ahqd_Ftq_Xmlk_Pas'
'Gur_Dhvpx_Oebja_Sbk_Whzcf_Bire_Gur_Ynml_Qbt'
'Hvs_Eiwqy_Pfckb_Tcl_Xiadg_Cjsf_Hvs_Zonm_Rcu'
'Iwt_Fjxrz_Qgdlc_Udm_Yjbeh_Dktg_Iwt_Apon_Sdv'
'Jxu_Gkysa_Rhemd_Ven_Zkcfi_Eluh_Jxu_Bqpo_Tew'
'Kyv_Hlztb_Sifne_Wfo_Aldgj_Fmvi_Kyv_Crqp_Ufx'
'Lzw_Imauc_Tjgof_Xgp_Bmehk_Gnwj_Lzw_Dsrq_Vgy'
'Max_Jnbvd_Ukhpg_Yhq_Cnfil_Hoxk_Max_Etsr_Whz'
'Nby_Kocwe_Vliqh_Zir_Dogjm_Ipyl_Nby_Futs_Xia'
'Ocz_Lpdxf_Wmjri_Ajs_Ephkn_Jqzm_Ocz_Gvut_Yjb'
'Pda_Mqeyg_Xnksj_Bkt_Fqilo_Kran_Pda_Hwvu_Zkc'
'Qeb_Nrfzh_Yoltk_Clu_Grjmp_Lsbo_Qeb_Ixwv_Ald'
'Rfc_Osgai_Zpmul_Dmv_Hsknq_Mtcp_Rfc_Jyxw_Bme'
'Sgd_Pthbj_Aqnvm_Enw_Itlor_Nudq_Sgd_Kzyx_Cnf'
'The_Quick_Brown_Fox_Jumps_Over_The_Lazy_Dog'
'Uif_Rvjdl_Cspxo_Gpy_Kvnqt_Pwfs_Uif_Mbaz_Eph'
'Vjg_Swkem_Dtqyp_Hqz_Lworu_Qxgt_Vjg_Ncba_Fqi'
```

В глаза сразу бросается строка 'The_Quick_Brown_Fox_Jumps_Over_The_Lazy_Dog', она и является флагом.

## start

Если внимательно прочитать исходный код программы, которая использовалась для шифрования, то можно заметить, что текст шифруется только с помощью первого символа ключа 'key'.

Напишем программу, которая дешифрует текст с помощью каждой из букв английского алфавита.

```
$ python
>>> f = open('start.dat', 'r')
>>> a = f.read()
>>> f.close()
>>> import string
>>> for c in string.lowercase:
...   ''.join(map(lambda x: chr(ord(x) ^ ord(c)), a))
... 
'Vc"%eNbEpce0'
'U`!&fMaFs`f3'
"Ta 'gL`Grag2"
"Sf' `Kg@uf`5"
'Rg&!aJfAtga4'
'Qd%"bIeBwdb7'
'Pe$#cHdCvec6'
'_j+,lGkLyjl9'
'^k*-mFjMxkm8'
']h).nEiN{hn;'
'\\i(/oDhOzio:'
'[n/(hCoH}nh='
'Zo.)iBnI|oi<'
'Yl-*jAmJ\x7flj?'
'Xm,+k@lK~mk>'
'Gr34t_sTart!'
'Fs25u^rU`su '
'Ep16v]qVcpv#'
'Dq07w\\pWbqw"'
'Cv70p[wPevp%'
'Bw61qZvQdwq$'
"At52rYuRgtr'"
'@u43sXtSfus&'
'Oz;<|W{\\iz|)'
'N{:=}Vz]h{}('
'Mx9>~Uy^kx~+'
```

После внимательного просматривания всех этих строк, можно заметить строку 'Gr34t_sTart!', которая и является флагом.

## analyze

В условии задачи дается зашифрованный текст.
Предполагая, что он был зашифрован с помощью шифра простой замены, попробуем расшифровать его с помощью частотного анализа.

Вместо того, чтобы самим писать программу для осуществления частотного анализа, попробуем воспользоваться готовым автоматическим решением (http://quipqiup.com/).
Скопируем какой-нибудь осмысленный и достаточно длинный фрагмент текста, нажмем 'Solve' и получим расшифрованный текст.

Если поискать в интернете по фрагменту этого текста, то сразу найдется его автор, William Shakespeare.

## vigenere

В этой задачке текст зашифрован с помощью шифра Виженера. Способ шифрования немного отличается от того, что был рассмотрен на лекции. Вместо сложения букв по модулю 26 (количество букв в алфавите), здеcь происходит сложение ASCII кодов символов по модулю 256. Сути это не меняет, но взглянуть на зашифрованный текст глазами становится сложнее.

Посчитаем индекс совпадений для различных длин ключей.

``` python
def freq(data):
  f = {}
  for s in data:
    f[s] = f.get(s, 0) + 1
  return f

def coin(data):
  f = freq(data)
  n = len(data)
  c = 0.0
  for s in f:
    c += 1.0 * f[s] * (f[s] - 1) / n / (n - 1)
  return c

with open('vigenere.dat') as f:
  data = f.read()

for l in xrange(1, 20):
  print l, coin(data[::l])
```

Получим:

```
1 0.0283571391406
2 0.0283277761141
3 0.0283139576968
4 0.0284178783622
5 0.0284635187399
6 0.0282429568156
7 0.0543834340567
8 0.0284294318137
9 0.0277725390559
10 0.0276125790871
11 0.0288800996118
12 0.0291950492524
13 0.0287512517781
14 0.0537284649655
15 0.0282146662234
16 0.0282739763272
17 0.0278536601769
18 0.0274078699493
19 0.0276450359895
```

Видно, что индекс совпадений имеет высокое значение для длин ключа 7 и 14 (если будем смотреть и на более длинные ключи, индекс совпадений скорее всего будет высоким для всех длин кратных 7).

Предположим, что длина ключа равна 7.
Попробуем применить частотный анализ для поиска самого ключа.

Каждый 7-й символ текста был зашифрован с помощью одного и того же символа ключа.
Если вырезать каждый 7-й символ, составить из них текст и посчитать наиболее часто встречающийся там символ, то скорее всего будет зашифрованным символом 'e' (самая часто встречающаяся буква в английском языке).
Теперь можно перебрать все 256 различных возможных значений символа ключа, чтобы понять, какой именно из них был использован для шифрования.
Тот же самый процесс можно повторить для всех символов ключа.

``` python
l = 7

for i in xrange(l):
  f = freq(data[i::l])
  s = f.keys()
  s.sort(key=lambda x: f[x], reverse=True)
  s = s[0]

  for x in xrange(0, 256):
    if (ord(s) - x) % 256 == ord('e'):
      print x, chr(x)
```

Получим:
```
108 l
105 i
99 c
101 e
110 n
115 s
101 e
```

Получился ключ 'license' (ура, осмысленное слово!), который можно использовать для расшифровки зашифрованного текста.

## pad

В этой задачке необходимо взломать "многоразовый" одноразовый блокнот.
Даны несколько шифротекстов, которые шифровались с помощью `xor`а с одним и тем же ключом.

Давайте по`xor`им посимвольно все шифротексты с первым.
В результате получим:
```
_____________________________________________________________________________________________________
_?Es???_???MK???RI?E?_??L?N?E??????__?A???I?E??EA?????_A??_???_???T???U??T?R??T???????R?_H??_??_T???B
???_?????R???E??I??_????L_O?E?????DP?_S???YB???W??C????EO?U???I??_T???HO?OC???_??R????S_?ET?OI_?EP???
?__Nc???B?__??R?_??N?????U_????????GMSS???K???TA??C???_I??_??__???????N?J_???P???????YC??_??S?T?EP???
?H?I???_B?_??E??L?SN??_?L?OR???????N_?_???A????_??C????S?FT??ER?????R?NO?N???_?????????U?N?OT???E????
____???_B?_??????I?TW?????I??G_R???M_?DT??N?E??T??????X_??A???????????T??b?????????P??L??T??I??SA??B?
???E?O????E??_R?O??P??D??Yr??????E?M??R?H?H?E??I???????_??ST??M??S?_??K_?_??????????H?F??Ra??t???????
```
где `_` соответствует символу с кодом `0`, а `?` соответствует любому символу, не являющемся буквой английского алфавита или символом с кодом `0`.

Заметим, что если бы мы `xor`или открытые тексты, а не зашифрованные, то получили бы тот же самый результат, поскольку:
```
C1[i] ^ C2[i] ==
== (P1[i] ^ Key[i]) ^ (P2[i] ^ Key[i]) ==
== (P1[i] ^ P2[i]) ^ (Key[i] ^ Key[i]) ==
== P1[i] ^ P2[i]
```

Кроме того, заметим, что для любого символа английского алфавита `a`:
```
>>> chr(ord(' ') ^ ord('a')) == 'A'
True
>>> chr(ord(' ') ^ ord('A')) == 'a'
True
>>> ord(' ') ^ ord(' ') == 0
True
```

А значит, если `i`ый символ первого текста был пробелом,
то `i`ые символы по`xor`енных текстов будут либо иметь код `0`,
либо являться буквой английского алфавита (большой или маленькой).
Представим по`xor`енные тексты записанные друг под другом как таблицу.
Найдя все столбцы, в которых каждый символ либо имеет код `0` либо является буквой,
можно понять где в первом тексте стоят пробелы и определить,
что за символы стоят в других текстах на этих же местах.

В результате получим:
```
___ _______________ ______ ________ __ ___ ____ _______ __ ___________ __ _______________ ___________
___S_______________e______n________ __a___i____e_______a__ ___________u__t_______________h___________
___ _______________ ______o________p__s___y____w_______e__u___________h__o_______________e___________
___n_______________n______ ________g__s___k____a_______i__ ___________n__ _______________ ___________
___i_______________n______o________n__ ___a____ _______s__t___________n__n_______________n___________
___ _______________t______i________m__d___n____t_______ __a___________t__B_______________t___________
___e_______________p______R________m__r___h____i_______ __s___________k__ _______________r___________
```

Повторим эту операцию для остальных текстов кроме первого, получим:
```
_he Co__bre_ker__is w_d_l_ reg_r_ed _s th_ be_t a_c____ of t_e____t_r_ __ cr_____r_phy_u_ _______p___
_o Sch__ier_ pe__ rev_e_ _nd e_p_rt _naly_is _re _m____ant f_r____ _e_u__ty _____y_tog_a_h_______e___
_ou mi__t n_t t__nk t_a_ _ou c_u_d p_ssib_y a_swe_ ____e que_t____ _i_h__o l_____ _xpo_u_e_______ ___
_hen y__ le_rn __lang_a_e_ lis_e_ing_ spe_kin_ an_ ____ing a_e____o_t_n__ bu_____d_ng _a_ _______ ___
_ simp__ te_t f__e ne_d_ _o ad_i_ion_l me_ada_a t_ ____st th_ ____e_ _n__nte_____a_ion_ _n_______f___
_he fr__ ve_sio__ It _o_t_ins _ _omm_nd l_ne _nte_f____ flag_r____c_y_t__BiN_____R_ ep_o_t_______n___
_ater __th _he __laps_ _f_Russ_a_ Em_ire _he _niv_r____ was _a____D_n_k__ Un_____i_y a_t_r_______y___
```

Далее, угадывая недостающие буквы в каком-нибудь из текстов, и вычисляя буквы остальных, получим:
```
The Codebreakers is widely regarded as the best account of the history of cryptography up _______p___
To Schneier, peer review and expert analysis are important for the security of cryptograph_______e___
You might not think that you could possibly answer these questions with so little exposure_______ ___
When you learn a language, listening, speaking and writing are important, but reading can _______ ___
A simple text file needs no additional metadata to assist the reader in interpretation, an_______f___
The free version. It contains a command line interface, flag{r34l_crypt0_BiNg0_XOR} eploit_______n___
Later with the colapse of Russian Empire the university was named Donskoy University after_______y___
```

## mary

Смотреть [здесь](https://github.com/ctfs/write-ups-2014/tree/master/ructf-2014-quals/crypto-200).
