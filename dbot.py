import discord
import sys
import os

if os.getenv('TOKEN') is not None:
    token = os.environ.get('TOKEN')
else:
    token = sys.argv[1]
print(f'Set token as {token}')

join_greeting = '''Welcome to the DevOps Journey Discord! We are a new community that embraces everything DevOps related.

The community is still new so sometimes our channel can be quiet but please feel free to ask questions are bring up a topic in our <#devops> channel.

Don't forget to check out our #test channel for plenty of free learning resources!
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