# bot.py
import feedparser
import discord
from dotenv import load_dotenv
import os
import pandas as pd

url = "https://www.reddit.com/r/valheim.rss"
feed = feedparser.parse (url)
client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

#entrEs = entry.title 

#hrefs = entry.href
    #print(entry.title)
    #print (entry.link)
    #print(entry.href)

data = {}
for entry in feed.entries[3:13]:
    data.setdefault('link',[])
    data.setdefault('title',[])
    #data.setdefault('hrefs',[])
    data['link'].append(entry.link)
    data['title'].append(entry.title)
    #data['hrefs'].append(entry.href)

df = pd.DataFrame(data)       
new_message = []

def listToString(x):
    str1 = ''
    for ele in x:
        str1 += ele + '\n'
    return str1


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith("~Odin's fresh shave?"):
        await message.channel.send('Baby smooth!')
        await message.channel.send(df.head(10))  
    elif message.content.startswith("~Odin's Beard!"):
        await message.channel.send('News from The Nine Relms!')
        for entry in feed.entries[3:13]:
            links = entry.link 
            #new_message.append(links)
            await message.channel.send(entry.link) 
            
client.run(TOKEN)
x=0
x = x + 1
print(x)


#feed and entrys
#keys
#print (feed.keys())
#print (feed.headers)
#print (len(feed.entries))


    






    