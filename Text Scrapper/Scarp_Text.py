import asyncio
from telethon import TelegramClient
from telethon.tl import functions, types

api_id = ""
api_hash = ''
phone = ''
client = TelegramClient(phone, api_id, api_hash)
client.start()
channel = input('Enter Channel Link:') 
#specific = input('enter word which's you w')
async def main():
    
    
    await client.get_entity(channel)
    messages = await client.get_messages("-1956918522", limit= None) #pass your own args

    #then if you want to get all the messages text
    for x in messages:
        print(x.text)
        #return message.text
        await client.send_message(entity='https://t.me/', message=x.text.replace('traffic', ':'))





loop = asyncio.get_event_loop()
loop.run_until_complete(main())


#Licensed At 2023 By Amir 


#https://github.com/AmirHesam-Python/