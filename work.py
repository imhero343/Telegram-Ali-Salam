from telethon import TelegramClient, events
import asyncio

# CLIENT
api_id = 4922551
api_hash = '485a6c34eb2bb8772f4e183f90532686'
client = TelegramClient('session', api_id, api_hash)
client.start()

# HHHHHHIIIIIIIII
print('alsalam Alakom')


# FUNCTIONS
#FOR GROUP
@client.on(events.NewMessage(chats=['https://t.me/inainaiq',
                                                        'https://t.me/sabreenS1','https://t.me/rpnewsIRAQ',
                                                        'https://t.me/asdbaabil','https://t.me/AnbaaIraq',
                                                        'https://t.me/iraq29i','https://t.me/lFreeil',
                                                        'https://t.me/alahadch','https://t.me/alalamarabic','https://t.me/cnews98',
                                                        'https://t.me/MMFNEWS','https://t.me/teamsmediawar_1',
                                                        'https://t.me/jbt313','https://t.me/IraninArabic',
                                                        'https://t.me/todaylarq',
                                                        'https://t.me/KonoAnsarAllah','https://t.me/awla_bi_awal',
                                                        'https://t.me/alsyasehnews',
                                                        'https://t.me/Aletejahchanal','https://t.me/Tura313'
                                                        ,'https://t.me/almanarnews','https://t.me/ALWASATNEWSIRAQ','https://t.me/NJ_313',
                                                        'https://t.me/Iran_Bel_Arabi','https://t.me/HHHHNB','https://t.me/iran_military_capabilities'
                                                        ,'https://t.me/ElafNews',
                                                        'https://t.me/AQLAM_Almuqawama','https://t.me/khamenei_lb']))
async def wkalaAnba(event):
    print(event.message.message)
    await client.send_message('https://t.me/joinchat/foJG__93ORw4MDMy', event.message)



#FOR CHANNEL
@client.on(events.NewMessage(chats=['https://t.me/joinchat/nOLFBrWYZHo1NzEy']))
async def me(event):
    print(event.message.message)
    await client.send_message('https://t.me/alansarnews', event.message)

@client.on(events.NewMessage(chats=['https://t.me/almayadeen']))
async def meadeen(event):
    print(event.message.message)
    try:
        await client.send_message('https://t.me/alansarnews', event.message.message.split(':')[0] +':'+ event.message.message.split(':')[2])
    except:
        await client.send_message('https://t.me/alansarnews', event.message)


@client.on(events.NewMessage(chats=['https://t.me/haf_1998']))
async def joundieallh(event):
    print(event.message.message)
    await client.send_message('https://t.me/alansarnews', event.message)

client.run_until_disconnected()
