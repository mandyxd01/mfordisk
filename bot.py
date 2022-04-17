import re
from time import sleep
import requests
from telethon import TelegramClient , events
import os


id= 11002107
hash = "2132509c0fda48eb2b16125992352b75"

print("Starting Deployment..!")

client = TelegramClient("main_session"  , api_id=id , api_hash=hash)

#mdisk_api
mdisk_api = 'SQUCMKJxGO5CLccne6qe'

#footer
footer = '''\n🌀 For VIP Content :- @VipContentService
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
⭐️JOIN OUR BACKUP CHANNEL
➡️https://t.me/+S4m4SxWBsss0NGYx'''


#indian variables
indchats = [-1001562499878,-1001316413287,-1001184354892,-1001213151009,-1001493682832,-1001493682832,-1001562499878,-1001741213557]
indsend_to = -1001384606870

#webseries var 
webchat = [-1001226710408,-1001663135966,-1001755571010,-1001398939317,-1001350448575,-1001615897915,-1001480308591]
websend_to = -1001188182423

#desi vars
deschat = [-1001711248489,-1001541608805,-1001186092691,-1001372777220,-1001660835958,-1001685545707,-1001350183964,-1001183555683]
dessend_to = -1001595706785

#tango vars
tanchat = [-1001755055372,-1001198221154,-1001620385630]
tansend_to = -1001580258829

#onlyfans vars 
onchat = [-1001581007387,-1001660122872,-1001717214543,-1001523206841,-1001342011276,-1001765382005]
onsend_to = -1001682123828


#forward here
source = deschat
frzz = [-1001656381315,-1001773024200]


@client.on(events.NewMessage(chats=indchats))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(indsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(indsend_to , caption)


#################webseries############

@client.on(events.NewMessage(chats=webchat))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(websend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(websend_to , caption)


############# DESI #################
@client.on(events.NewMessage(chats=deschat))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(dessend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(dessend_to , caption)

############ TANGO ###############

@client.on(events.NewMessage(chats=tanchat))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(tansend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(tansend_to , caption)

########### ONLYFANS #####################
@client.on(events.NewMessage(chats=onchat))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(onsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(onsend_to , caption)


            
            
 ############ FORWARDER #################
@client.on(events.NewMessage(chats=source))
async def hello(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)

        caption = re.sub("@.*" , "" , caption)
        caption = re.sub("https://t.me/.*" , "" , caption)
        caption = re.sub("t.me/.*" , "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link
                }
            res = requests.post(url, json = param)
            shareLink = res.json()['sharelink']
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(frzz[0] ,file=media , caption=caption)
            await client.send_file(frzz[1] ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(frzz[0] , caption)
            await client.send_message(frzz[1] , caption)

    
print("Bot has been deployed.!")

client.start()
client.run_until_disconnected()





