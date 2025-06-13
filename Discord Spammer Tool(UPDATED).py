import discord
import asyncio
import time
import os
from colorama import *

os.system("title Discord Spammer - By SuperYOROX")

Banner = Fore.RED + """
                              ███████╗█████  █████╗  ███╗   ███╗███╗   ███╗███████╗██████╗ 
                              ██╔════╝██  ██ ██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                              ███████╗█████  ███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
                              ╚════██║██     ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                              ███████║██     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                              ╚══════╝╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
        
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                    Made By SuperYOROX // Discord Spammer Tool                                        ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
def print_animated_banner(text, delay=0.05):
    for line in text.splitlines():
        print(line)
        time.sleep(delay)

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

async def spam_channels(token, guild_id, message, repeat_count, delay):
    await client.login(token)
    guild = client.get_guild(guild_id)
    if guild is None:
        print(f"{Fore.RED}Guild not found.{Fore.RESET}")
        await client.close()
        return

    print(f"{Fore.GREEN}Connected to Guild:{Fore.RESET} {guild.name}")

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            print(f"{Fore.YELLOW}Spamming in channel:{Fore.RESET} #{channel.name}")
            for i in range(repeat_count):
                try:
                    await channel.send(f"{message} ({i+1})")
                    await asyncio.sleep(delay)
                except Exception as e:
                    print(f"{Fore.RED}Failed to send message in #{channel.name}:{Fore.RESET} {e}")
        else:
            print(f"{Fore.YELLOW}Skipping #{channel.name}, no permission.{Fore.RESET}")

    await client.close()

def main():
    print_animated_banner(Banner)
    token = input(f"{Fore.RED}[{Fore.WHITE}Insert Bot Token{Fore.RED}] {Fore.RED}->{Fore.RESET} ").strip()
    guild_id = (input(f"{Fore.RED}[{Fore.WHITE}Insert Guild ID{Fore.RED}] ->{Fore.RESET} ").strip())
    message = input(f"{Fore.RED}[{Fore.WHITE}Insert message to spam{Fore.RED}]:{Fore.RESET} ").strip()
    repeat_count = (input(f"{Fore.RED}[{Fore.WHITE}How many times to send the message per channel?{Fore.RED}]:{Fore.RESET} ").strip())
    delay = (input(f"{Fore.RED}[{Fore.WHITE}Delay between messages in seconds{Fore.RED}]:{Fore.RESET} ").strip())

    spam_channels(token, guild_id, message, repeat_count, delay)

if __name__ == "__main__":
    main()
    input ("[Press Enter to Exit...]")
    