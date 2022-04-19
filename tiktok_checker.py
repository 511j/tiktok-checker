import requests
import random
import time
import os
from colorama import Fore
from tkinter import messagebox
from discord_webhook import DiscordWebhook, DiscordEmbed
os.system("clear")
logo = f'''

 ___  ___   ___                    ___  ___   ___                                    
`._|=|   |=|_.'   .'|   .'|   .'| `._|=|   |=|_.'   .'|=|`.     .'|   .'|            
     |   |    {Fore.GREEN}  .'  | .'  | .' .'      |   |      .'  | |  `. .'  | .' .'            
     |   |      |   | |   |=|.:      {Fore.WHITE}  |   |      |   | |   | |   |=|.:              
     `.  |      |   | |   |   |'.      `.  |      `.  | |  .' |   |   |'.            
       `.|      |___| {Fore.GREEN}|___|   |_|        `.|        `.|=|.'   |___|   |_|            
                                                                                     
             ___                    ___        ___                    ___        __  
        .'|=|_.'   .'| |`.     .'|=|_.'   .{Fore.WHITE}'|=|_.'   .'|   .'|   .'|=|_.'   .'|=|  | 
      .'  |      .'  | |  `. .'  |  ___ .'  |      .'  | .' .' .'  |  ___ .'  | |  | 
      |   |      |   |=|   | |   |=|_.' |   |      |   |=|.:   |   |=|_.' |   |=|.'  
      `.  |  ___ |   | |   | |   |  ___ `.  |  ___ |   |   |'. |   |  ___ |   |  |`. 
        `.|=|_.' |___| |___| |___|=|_.'   `.|=|_.' |___|   |_| |___|=|_.' |___|  |_| 
                   TikTok checker {Fore.GREEN}-{Fore.WHITE} By {Fore.GREEN}:{Fore.WHITE} @ilord4tb {Fore.GREEN}/{Fore.WHITE} Lord4tb .{Fore.GREEN}#{Fore.WHITE}0511                                                         
'''
print(logo)
webbb = input(f"[ {Fore.GREEN}+{Fore.WHITE} ] Enter your Discord webhook :{Fore.GREEN} ")
input(f"{Fore.WHITE}[ {Fore.GREEN}*{Fore.WHITE} ] Press Enter to start {Fore.GREEN}..{Fore.WHITE}")
while True:
    username = ""
    for char in random.choices(f"qwertyuiopasdfghjklzxcvbnm1234567890", k=4):
        username = username + char
    response = requests.get(f"https://www.tiktok.com/@{username}")

    if (response.status_code == 200):
        print(Fore.RED + f"Unavailable >>{Fore.WHITE} {username}")
    if (response.status_code == 301):
        print(Fore.RED + f"Banned >>{Fore.WHITE} {username}")
    elif (response.status_code == 404):
        print(Fore.GREEN + f"Available >>{Fore.WHITE} {username}")
        messagebox.showinfo("#lord4tb Tiktok Checker",f"Available user >> {username}")
        webhook = DiscordWebhook(url={webbb})
        embed = DiscordEmbed(title='#Lord4tb checker', color='2e2e2e')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/962419141892009994/966016990852546590/giphy_2.gif')
        embed.set_footer(text='#Lord4tb checker')
        embed.add_embed_field(name='TikTok username Checker', value=f'Available user >> {username}')
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        print(f"[ {Fore.RED}-{Fore.WHITE} ] Checker is Blocked {Fore.RED},{Fore.WHITE} try later")
        time.sleep(170)