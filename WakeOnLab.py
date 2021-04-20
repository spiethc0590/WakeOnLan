#wakeonlan
#the purpose of this script is to create a script to use wake on lan  for Meraki Mini lab

import time
import sys
import os 


mac_list = [
"00:50:56:86:60:10",
"00:50:56:86:f8:dc",
"00:50:56:86:17:53",
"00:50:56:86:74:f"
]

for mac in mac_list:
	os.system(f"wakeonlan {mac}")


