import asyncio
import aiohttp
import websockets
import aioconsole
import random
import json

token = input("\033[91m  > Enter token\033[33m ")
headers={"X-Debug-Options": "bugReporterEnabled", "X-Discord-Locale": "en-US","Authorization": token, "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjExMS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzExMS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTExLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTg1ODMyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9"}

created = []

async def create_hook(session, channel, hook_name):
    async with session.post(f"https://discord.com/api/v9/channels/{channel}/webhooks", headers=headers, json={"name": hook_name}) as creation:
        creation1 = await creation.json()
        try:
            created.append("https://discord.com/api/webhooks/{}/{}".format(creation1["id"], creation1["token"]))
            print("\033[92m  > Successful Creation!")
        except:
            print("\033[91m  > Creation Failed!")

async def setup_hooks(guild, hook_name):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False, keepalive_timeout=10000, ttl_dns_cache=10000, limit=0, limit_per_host=0), trust_env=False, skip_auto_headers=None, auto_decompress=True) as session:
        await asyncio.gather(*(asyncio.create_task(create_hook(session, channel, hook_name)) for channel in guild.channels)) # Deletes guilds
    
    # Checks if any urls were created before appending to webhooks.
    if len(created) > 0:
        with open("System/webhooks.txt", "a") as f:
            for url in created:
                f.write(url + '\n')

guild_ids = []
guilds = []
class Guild:

    def __init__(self, data):
        self.data = data
        self._update()

    def _update(self):
        self.id = self.data["id"]
        self.channels = []
        for channel in self.data["channels"]:
            if channel["type"] == 0:
                self.channels.append(channel["id"])

async def setup():
    servid = str(input("\033[91m  > Enter guild id\033[33m "))
    hook_name = input("\033[91m  > Enter hook name\033[33m ")
    ws = await websockets.connect("wss://gateway.discord.gg/?v=10&encoding=json")
    hello = json.loads(await ws.recv())
    await asyncio.sleep(1)

    identify = {
        "op": 2,
        "d": {
        "token": token,
        "properties": {
        "os": "linux",
        "browser": "Chrome",
        "device": "PC",
        },
        }}

    await ws.send(json.dumps(identify))
    identify = json.loads(await ws.recv())
    for i in identify["d"]["guilds"]:
        guild_obj = Guild(i)
        guilds.append(guild_obj)
        guild_ids.append(i["id"])
    
    if servid in guild_ids:
        for guild in guilds:
            if guild.id == servid:
                await setup_hooks(guild, hook_name)
    else:
        print("\033[91m  > Invalid guild provided \033[33m ")
    
    input("\033[91m  > Enter to continue\033[33m ")

