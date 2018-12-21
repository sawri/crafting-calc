import discord
from discord.ext import commands
from math import ceil

client = commands.Bot(command_prefix='!')
client.remove_command('help')


@client.event
async def on_ready():
    print("Crafting Calc has logged in.\nCrafting Calc's message: crafting some diamonds.")
    await client.change_presence(game=discord.Game(name="crafting some diamonds"))


@client.command()
async def help():

    embed = discord.Embed(
        colour=discord.Colour.teal()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!<item_name>',
                    value='Returns <item> crafting requirements as well as crit results.',
                    inline=False)

    embed.add_field(name='!list <profession>',
                    value='Sends user a message listing all recipes of a specified profession.',
                    inline=False)

    embed.add_field(name='!craft <number> <item>',
                    value='Returns exact materials needed for specified amount.',
                    inline=False)

    embed.add_field(name='item names:',
                    value='sapphire, emerald, diamond, daric, siglo, plate',
                    inline=False)
    await client.say(embed=embed)


@client.command()
async def diamond():
    await client.say('1 Diamond requires:\n10 Emeralds, 1,000 Kits, and 500 PP.\nA crit will produce **3 Diamonds**.')


@client.command()
async def emerald():
    await client.say("1 Emerald requires:\n5 Sapphires, 60 Kits, and 85 PP.\nA crit will produce **5 Emeralds**.")


@client.command()
async def sapphire():
    await client.say('1 Sapphire requires:\n2 Rubies, 20 Kits, and 20 PP.\nA crit will produce **1 Emerald**.')


@client.command()
async def daric():
    await client.say('3 Darics require:\n5 Talents, 60 Kits, and 20 PP.\nA crit will produce **5 Darics**.')


@client.command()
async def siglo():
    await client.say('3 Siglos require:\n5 Talents, 60 Kits, and 20 PP.\nA crit will produce **5 Siglos**.')


@client.command()
async def plate():
    await client.say('3 Plates require:\n5 Darics, 240 Kits, and 80 PP.\nA crit will produce **5 Plates**.')


@client.command()
async def test(*args):
    await client.say('{} arguments: {}'.format(len(args), ', '.join(args)))


@client.command()
async def craft(num, item):
    num = int(num)
    if item == 'diamonds' or item == 'diamond':
        num2 = num * 10
        kits = num * 1000
        pp = num * 500
        await client.say('To craft {} Diamonds, you need {} Emeralds, {} Kits, and {} PP.'.format(num, num2, kits, pp))
    elif item == 'emeralds' or item == 'emerald':
        num2 = num * 5
        kits = num * 100
        pp = num * 85
        await client.say('To craft {} Emeralds, you need {} Sapphires, {} Kits, and {} PP.'.format(num, num2, kits, pp))
    elif item == 'sapphires' or item == 'sapphire':
        num2 = num * 2
        kits = num * 20
        pp = num * 20
        await client.say('To craft {} Sapphires, you need {} Rubies, {} Kits, and {} PP.'.format(num, num2, kits, pp))
    elif item == 'daric' or item == 'siglo' or item == 'darics' or item == 'siglos':
        item2 = item.capitalize()
        num2 = (num / 3) * 5
        kits = (num / 3) * 60
        pp = (num / 3) * 20
        await client.say('To craft {} {}, you need {} Talents, {} Kits, and {} PP.'.format(num, item2, num2, kits, pp))
    elif item == 'plate' or item == 'plates':
        num2 = ceil((num / 3) * 5)
        kits = ceil((num / 3) * 240)
        pp = ceil((num / 3) * 80)
        await client.say('To craft {} Plates, you need:'
                         '```\n{} Darics/Siglos,\n{} Kits,\n{} PP.```'.format(num,num2, kits, pp))

client.run('NTIyMzUyNDk1MzY0OTMxNTg0.DvfPVw.d_v8n2JrJEAUy3HyTdzDutVwRnk')
