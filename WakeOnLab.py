#wakeonlan
#the purpose of this script is to create a script to use wake on lan  for Meraki Mini lab

import time
import sys
import os 




mac_list = [
"00:50:56:86:42:fa",
"00:50:56:86:7e:9d",
"00:50:56:86:41:19",
"00:50:56:86:15:b7",
"00:50:56:86:f0:4f",
"00:50:56:86:bb:b5",
"00:50:56:86:19:35",
"00:50:56:86:3c:2f",
"00:50:56:86:4b:b5",
"00:50:56:86:68:86",
"00:50:56:86:8b:61",
"00:50:56:86:ec:3f",
"00:50:56:86:ac:53",
"00:50:56:86:8d:21",
"00:50:56:86:e8:30",
"00:50:56:86:26:ff",
"00:50:56:86:e4:51",
"00:50:56:86:11:63",
"00:50:56:86:65:60",
"00:50:56:86:b2:fe",
"00:50:56:86:4d:6e",
"00:50:56:86:fc:6c",
"00:50:56:86:c2:cd",
"00:50:56:86:9b:98",
"00:50:56:86:ab:99",
"00:50:56:86:ad:ac",
"00:50:56:86:84:33",
"00:50:56:86:f1:d0",
"00:50:56:86:85:7d",
"00:50:56:86:21:72",
"00:50:56:86:60:10",
"00:50:56:86:f8:dc",
"00:50:56:86:17:53",
"00:50:56:86:74:f8",
"00:50:56:86:14:f1",
"00:50:56:86:91:61",
"00:50:56:86:cf:dd",
"00:50:56:86:f9:ee",
"00:50:56:86:9a:3e",
"00:50:56:86:c9:0e",
"00:50:56:86:d1:89",
"00:50:56:86:91:d1",
"00:50:56:86:8f:94",
"00:50:56:86:63:e3",
"00:50:56:86:51:f2",
"00:50:56:86:e7:04",
"00:50:56:86:bb:62",
"00:50:56:86:7d:a3",
"00:50:56:86:3a:4c",
"00:50:56:86:f0:8c",
"00:50:56:86:af:55",
"00:50:56:86:6f:a0",
"00:50:56:86:90:52",
"00:50:56:86:ec:21",
"00:50:56:86:48:48",
"00:50:56:86:fb:ea",
"00:50:56:86:91:85",
"00:50:56:86:89:a3",
"00:50:56:86:06:02",
"00:50:56:86:48:63",
"00:50:56:86:cf:47",
"00:50:56:86:92:30",
"00:50:56:86:69:b8",
"00:50:56:86:08:dc",
"00:50:56:86:c2:bb",
"00:50:56:86:53:19",
"00:50:56:86:da:51",
"00:50:56:86:08:24",
"00:50:56:86:74:d5",
"00:50:56:86:fe:0f",
"00:50:56:86:ce:74",
"00:50:56:86:66:f0",
"00:50:56:86:44:89",
"00:50:56:86:c5:48",
"00:50:56:86:0b:87",
"00:50:56:86:17:8a",
"00:50:56:86:22:39",
"00:50:56:86:2e:08",
"00:50:56:86:9c:38",
"00:50:56:86:7d:94",
"00:50:56:86:7b:a2",
"00:50:56:86:5b:83",
"00:50:56:86:cc:d5",
"00:50:56:86:67:36",
"00:50:56:86:53:f8",
"00:50:56:86:22:10",
"00:50:56:86:f3:5d",
"00:50:56:86:86:1f",
"00:50:56:86:85:14",
"00:50:56:86:53:58",
"00:50:56:86:70:19",
"00:50:56:86:d7:bd",
"00:50:56:86:5a:dd",
"00:50:56:86:26:9d",
"00:50:56:86:46:b2",
"00:50:56:86:1b:47",
"00:50:56:86:8f:84",
"00:50:56:86:63:b0",
"00:50:56:86:7e:f0",
"00:50:56:86:ab:53",
"00:50:56:86:2c:33",
"00:50:56:86:5f:00",
"00:50:56:86:36:6d",
"00:50:56:86:5a:de",
"00:50:56:86:0c:0c",
"00:50:56:86:5c:59",
"00:50:56:86:da:70",
"00:50:56:86:69:57",
"00:50:56:86:66:50",
"00:50:56:86:bf:8f",
"00:50:56:86:c8:72",
"00:50:56:86:9c:d4",
"00:50:56:86:de:67",
"00:50:56:86:a7:11",
"00:50:56:86:88:fb",
"00:50:56:86:09:3a",
"00:50:56:86:8a:71",
"00:50:56:86:00:76",
"00:50:56:86:70:f8",
"00:50:56:86:a3:89",
"00:50:56:86:b6:1a",
"00:50:56:86:9d:6d",
"00:50:56:86:69:7b",
"00:50:56:86:52:52",
"00:50:56:86:0d:53",
"00:50:56:86:46:4e",
"00:50:56:86:5e:f2",
"00:50:56:86:fb:73",
"00:50:56:86:a0:ad",
"00:50:56:86:33:13",
"00:50:56:86:3c:10",
"00:50:56:86:be:15",
"00:50:56:86:40:8c",
"00:50:56:86:7b:df",
"00:50:56:86:31:43",
"00:50:56:86:a3:25",
"00:50:56:86:de:d7",
"00:50:56:86:ef:a4",
"00:50:56:86:e8:34",
"00:50:56:86:da:13",
"00:50:56:86:77:fa",
"00:50:56:86:42:2e",
"00:50:56:86:75:dc",
"00:50:56:86:26:72",
"00:50:56:86:ff:c9",
"00:50:56:86:4a:7b",
"00:50:56:86:8c:84",
"00:50:56:86:c1:4b",
"00:50:56:86:f4:70",
"00:50:56:86:a5:19",
"00:50:56:86:83:0b",
"00:50:56:86:ec:4e",
"00:50:56:86:cc:77",
"00:50:56:86:e2:1f",
"00:50:56:86:89:96",
"00:50:56:86:76:85",
"00:50:56:86:ba:44",
"00:50:56:86:0f:fe",
"00:50:56:86:33:d7",
"00:50:56:86:db:d7",
"00:50:56:86:d9:c7",
"00:50:56:86:f5:e3",
"00:50:56:86:cb:82",
"00:50:56:86:bd:df",
"00:50:56:86:e4:ab",
"00:50:56:86:0e:13",
"00:50:56:86:15:8b",
"00:50:56:86:2d:60",
"00:50:56:86:32:41",
"00:50:56:86:b7:31",
"00:50:56:86:c0:a1",
"00:50:56:86:b4:7b",
"00:50:56:86:46:d6",
"00:50:56:86:ba:f3",
"00:50:56:86:ba:f3",
"00:50:56:86:d4:6b",
"00:50:56:86:94:61",
"00:50:56:86:cf:f4",
"00:50:56:86:d7:df",
"00:50:56:86:1f:22",
"00:50:56:86:d0:58",
"00:50:56:86:04:9b",
"00:50:56:86:ac:89",
"00:50:56:86:c8:7b",
"00:50:56:86:8a:e5",
"00:50:56:86:01:69",
"00:50:56:86:37:2f",
"00:50:56:86:5a:35",
"00:50:56:86:a0:8e",
"00:50:56:86:94:01",
"00:50:56:86:35:55",
"00:50:56:86:52:52",
"00:50:56:86:0d:53",
"00:50:56:86:46:4e",
"00:50:56:86:5e:f2",
"00:50:56:86:fb:73",
"00:50:56:86:a0:ad",
"00:50:56:86:33:13",
]

count = 0
while count == 0:
	for mac in mac_list:
		os.system(f"wakeonlan {mac}")
	time.sleep(30)

