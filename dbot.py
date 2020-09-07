import discord
import sys
import os
import logging
logging.basicConfig(level=logging.DEBUG)

logging.debug('Starting Application')

if os.getenv('TOKEN') is not None:
    token = os.environ.get('TOKEN')
else:
    token = sys.argv[1]
print(f'Set token as {token}')

join_greeting = '''Welcome to the DevOps Journey Discord! We are a new community that embraces everything DevOps related.

#Resources Channel has plenty of free learning resources.

#Devops Channel to spark up any devops related questions or conversations.

YouTube Channel: https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg
'''

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author == client.user: return
        if message.content == '!stop': await client.logout()
        #if message.content.startswith('!ping'): await message.channel.send('Pong!')
    
    async def on_member_join(self, member):
        await member.send(join_greeting)

client = MyClient()
client.run(token)