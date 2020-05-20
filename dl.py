#Download Music Program
#Support Me In My Github
#Thanks For Using My Program

import os, sys
os.system('pip install --upgrade pip')
os.system('pip install youtube-dl')
os.system('pip install termcolor')
from termcolor import colored
os.system('apt install mpv')

print(colored('_'*50,'yellow'))
os.system('clear')
baner= """

___  ___          _       ______                    _                 _
|  \/  |         (_)      |  _  \                  | |               | |
| .  . |_   _ ___ _  ___  | | | |_____      ___ __ | | ___   __ _  __| |
| |\/| | | | / __| |/ __| | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
| |  | | |_| \__ \ | (__  | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |
\_|  |_/\__,_|___/_|\___| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_| 0.1

         <•===============[Code By  : MR.C1M1N]===============•>"""

print(colored(baner,'green'))
print(colored('Options...','yellow'))
print(colored('1.Download Music','yellow'))
print(colored('2.Play Music','yellow'))
select=str(input(colored('Input Number: ','yellow')))
print(colored('_'*50,'yellow'))

if select == '1':
  link=str(input(colored('Input link Music: ','green')))
  os.system('youtube-dl -x --audio-format mp3 -o "/sdcard/YouTube/%(title)s.%(ext)s" '+link)
  print(colored('Download Succes!!','cyan'))
  print(colored('Check Your File in /sdcard/YouTube','blue'))
elif select == '2':
  folder=str(input(colored('Input Path Your File: ','yellow')))
  os.system('mpv '+folder)
else:
  print(colored('Number'+select+' Not Found In Options','red'))
