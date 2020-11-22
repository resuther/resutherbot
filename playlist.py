import discord
from discord.ext import commands
from discord.ext.commands import Bot
client = commands.Bot(command_prefix='=')
client.remove_command('help')

def Enquiry(lis1): 
    if not lis1: 
        return 1
    else: 
        return 0

@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

playlists = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot: return
    if message.content == '=playlist':
        if Enquiry(playlists):
            await message.channel.send('Playlist empty')
        else:
            for x in playlists:
                await message.channel.send(x)
    if message.content == '=playlistclear':
        playlists.clear()
        await message.channel.send('List cleared')
    if message.channel.name == 'playlist':
        playlists.append(message.content)
        await message.channel.send(f'Added:')
        await message.channel.send(f'`' + message.content + '`')
    if message.content == '<@!750589798468812850>':
        await message.channel.send('Try `=help` to get a list of commands.')
    

client.run('TOKEN')
