import discord
import os
from discord.ext import commands
from math import ceil, floor

client = commands.Bot(command_prefix='!tc ')
client.remove_command('help')

#hide token

reader = open('C:\\Users\\kwand\\OneDrive\\Desktop\\tccbot\\token.txt', 'r')
token = reader.read()

#array of possible items for input validation.
#there's probably a more elegant way
items = ['ruby', 'rubies', 'diamond', 'diamonds', 'sapphires',
		'sapphire', 'emeralds', 'emerald',
		'plate', 'plates', 'siglos', 'siglo',
		'darics', 'daric', 'talent', 'talents']

EMOJI = {'NO': '<:no:534529985210351677>', 'OLUL': '<:OMEGALUL:480157332945240066>',
		'RUBY': '<:ruby:533349001353756703>', 'SAPP': '<:sapphire:533349173349711903>',
		'EME': '<:emerald:533349173282734080>', 'DIA': '<:diamond:533349173206974480>',
		'GTAL': '<:gtalent:533386829253181461>', 'STAL': '<:stalent:533386829295255553>',
		'DAR': '<:daric:533386828913311759>', 'SIG': '<:siglo:533386829634863116>',
		'GPLATE': '<:gplate:533386829572079636>', 'SPLATE': '<:splate:533386829555040267>',
		'KIT': '<:kit:533354603115446275>', 'CURE': '<:cure:534558103987945472>'}


@client.event
async def on_message(message):
	if message.content.startswith('<:POGGERS:500039806143954964>'):
		await client.send_message(message.channel, '<:POGGERZ:533433324153208842>')
	if message.content == ('!fbi'):
		await client.send_message(message.channel, 'https://tenor.com/view/fbi-raid-swat-gif-11500735')
	await client.process_commands(message)



@client.command()
async def help():

	embed = discord.Embed(
		colour=discord.Colour.teal()
	)

	embed.set_author(name='Help')
	embed.add_field(name='!tc recipe <item_name>',
					value='`!tc recipe diamond`\nReturns <item> crafting requirements as well as crit results.',
					inline=False)
	embed.add_field(name='!tc craft <number> <item_name>',
					value='`!tc craft 10 emeralds`\nReturns exact materials needed for specified amount.',
					inline=False)
	embed.add_field(name='!tc use <number> <item_name> for <item2_name>',
					value='`!tc use 105 talents for plates`\nDisplays steps and total kits needed to go from lesser material to greater.',
					inline=False)
	embed.add_field(name='item names:',
					value='ruby/rubies, talent(s), sapphire(s), emerald(s), diamond(s), daric(s), siglo(s), plate(s)',
					inline=False)
	await client.say(embed=embed)


@client.command()
async def recipe(item, item2=""):
	if item == 'diamond':
		embed = discord.Embed(title="Diamond:\t500 PP", color=0xffffff)
		embed.set_thumbnail(url="https://teralore.com/items/icon_items/t_diamond_tex.png")
		embed.add_field(name='Profession:',
			value='800 (Master) Alchemy',
			inline=False)
		embed.add_field(name='Materials:',
			value='10 Emeralds\n1,000 Kits',
			inline=False)
		embed.add_field(name='Crit Reward:',
			value='3 Diamonds',
			inline=False)
		await client.say(embed=embed)

	elif item == 'emerald':
		embed = discord.Embed(title="Emerald:\t85 PP", color=0x0fbd1b)
		embed.set_thumbnail(url="https://teralore.com/items/icon_items/t_emerald_tex.png")
		embed.add_field(name='Profession:',
			value='500 (Artisan) Alchemy',
			inline=False)
		embed.add_field(name='Materials:',
			value='5 Sapphires\n60 Kits',
			inline=False)
		embed.add_field(name='Crit Reward:',
			value='5 Emeralds',
			inline=False)
		await client.say(embed=embed)

	elif item == 'sapphire':
		embed = discord.Embed(title="Sapphire:\t20 PP", color=0x1a3cc7)
		embed.set_thumbnail(url="https://teralore.com/items/icon_items/t_sapphire_tex.png")
		embed.add_field(name='Profession:',
			value='50 Alchemy',
			inline=False)
		embed.add_field(name='Materials:',
			value='2 Rubies\n20 Kits',
			inline=False)
		embed.add_field(name='Crit Reward:',
			value='1 Emerald',
			inline=False)
		await client.say(embed=embed)

	elif item == 'ruby':
		embed = discord.Embed(title="Ruby:\t5PP", color=0xc91c1c)
		embed.set_thumbnail(url="https://essentialmana.com/wp-content/tera/icons/icon_items/t_ruby_tex.png")
		embed.add_field(name='Profession:',
			value='0 Alchemy',
			inline=False)
		embed.add_field(name='Materials:',
			value='110 Kits',
			inline=False)
		embed.add_field(name='Crit Reward:',
			value='1 Sapphire',
			inline=False)
		await client.say(embed=embed)

	elif item == 'silver':
		if item2 == 'siglo':
			embed = discord.Embed(title="(3) Silver Siglo:\t20 PP", color=0xd2d4d9)
			embed.set_thumbnail(url="https://teralore.com/items/icon_items/corecolor1_2_tex.png")
			embed.add_field(name='Profession:',
				value='500 (Artisan) Processing',
				inline=False)
			embed.add_field(name='Materials:',
				value='5 Silver Talents\n60 Kits',
				inline=False)
			embed.add_field(name='Crit Reward:',
				value='5 Silver Siglos',
				inline=False)
			await client.say(embed=embed)

		elif item2 == 'plate':
			embed = discord.Embed(title="(3) Silver Plate:\t80 PP", color=0xd2d4d9)
			embed.set_thumbnail(url="https://teralore.com/items/icon_items/corecolor1_3_tex.png")
			embed.add_field(name='Profession:',
				value='800 (Master) Processing',
				inline=False)
			embed.add_field(name='Materials:',
				value='5 Silver Siglos\n240 Kits',
				inline=False)
			embed.add_field(name='Crit Reward:',
				value='5 Silver Plates',
				inline=False)
			await client.say(embed=embed)

		else:
			await client.say('Please specify either silver siglo or plate.')

	elif item == 'golden':
		if item2 == 'daric':
			embed = discord.Embed(title="(3) Golden Daric:\t20 PP", color=0xd9be36)
			embed.set_thumbnail(url="https://teralore.com/items/icon_items/corecolor2_2_tex.png")
			embed.add_field(name='Profession:',
				value='500 (Artisan) Smelting',
				inline=False)
			embed.add_field(name='Materials:',
				value='5 Golden Talents\n60 Kits',
				inline=False)
			embed.add_field(name='Crit Reward:',
				value='5 Golden Darics',
				inline=False)
			await client.say(embed=embed)

		elif item2 == 'plate':
			embed = discord.Embed(title="(3) Golden Plate:\t80 PP", color=0xd9be36)
			embed.set_thumbnail(url="https://teralore.com/items/icon_items/corecolor2_3_tex.png")
			embed.add_field(name='Profession:',
				value='800 (Master) Smelting',
				inline=False)
			embed.add_field(name='Materials:',
				value='5 Golden Darics\n240 Kits',
				inline=False)
			embed.add_field(name='Crit Reward:',
				value='5 Golden Plates',
				inline=False)
			await client.say(embed=embed)

		else:
			await client.say('Please specify either golden daric or plate.')
	else:
		await client.say(':no_entry_sign: Please enter a valid item.')


@client.command()
async def test(*args):
	await client.say('{} arguments: {}'.format(len(args), ', '.join(args)))


@client.command(pass_context=True)
#what you need to craft a specified amount of items
async def craft(ctx, num : int, item : str):
	auth = ctx.message.author.id
	if await idiot_check(auth):
		return
	item = item.lower()
	if item not in items:
		await client.say('Sorry! I don\'t recognize that item. For help, use !tc help.')
	elif num <= 0:
		await client.say('Please enter a number greater than 0.')
	else:
		if num == 1 and item.endswith('s') and not item == 'plates':
			item = item[:len(item)-1]
		if num > 1 and not item.endswith('s'):
			item = item + 's'
		msg = ':hammer_pick: | To craft `{}` {}, you need:\n\n'.format(num, item)

		if item == 'diamonds' or item == 'diamond':
			num2 = format((num * 10), ',')
			kits = format((num * 1000), ',')
			pp = format((num * 500), ',')

			msg += '{} x `{}`\n{} x `{}`\n{}: `{} PP`'.format(EMOJI['EME'], num2, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			await client.say(msg)

		elif item == 'emeralds' or item == 'emerald':
			num2 = format((num * 5), ',')
			kits = format((num * 100), ',')
			pp = format((num * 85), ',')

			msg  += '{} x `{}`\n{} x `{}`\n{}: `{} PP`'.format(EMOJI['SAPP'], num2, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			await client.say(msg)

		elif item == 'sapphires' or item == 'sapphire':
			num2 = format((num * 2), ',')
			kits = format((num * 20), ',')
			pp = format((num * 20), ',')

			msg += '{} x `{}`\n{} x `{}`\n{}: `{} PP`'.format(EMOJI['RUBY'], num2, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			await client.say(msg)

		elif item == 'daric' or item == 'siglo' or item == 'darics' or item == 'siglos':
			if (num % 3 != 0):
				while (num % 3 != 0):
					num += 1
				msg = ':warning: | Darics and siglos are crafted in multiples of 3. Rounding up to {}!'.format(num)
				msg += '\nTo craft `{}` {}, you need:\n\n'.format(num, item)

			num2 = format(ceil((num / 3) * 5), ',')
			kits = format(ceil((num / 3) * 60), ',')
			pp = format(ceil((num / 3) * 20), ',')

			msg += '{}/{} x `{}`\n{} x `{}`\n{}: `{} PP`'.format(EMOJI['GTAL'], EMOJI['STAL'], num2, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			await client.say(msg)

		elif item == 'plate' or item == 'plates':
			if (num % 3 != 0):
				while (num % 3 != 0):
					num += 1
				msg = ':warning: | Plates are crafted in multiples of 3. Rounding up to {}!'.format(num)
				msg += '\nTo craft `{}` {}, you need:\n\n'.format(num, item)
			num2 = int(format(ceil((num / 3) * 5), ','))
			if (num2 % 3 != 0):
				while (num2 % 3 != 0):
					num2 += 1
			kits = format(int(((num2 * 60)/3) + ((num * 240)/3)), ',')
			pp = format(ceil((num / 3) * 80) + ceil((num2 / 3) * 20), ',')
			
					
			tals = format(ceil((num2 / 3) * 5), ',')
			#pp2 = format(ceil((num2 / 3) * 20), ',')

			msg += '**Starting supplies**\n{}/{} x `{}`\n{} x `{}`\n{} x `{}`'.format(EMOJI['GTAL'], EMOJI['STAL'], tals, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			msg += '\n**Intermediate step**\n{}/{} x `{}`\n**Final product**\n{}/{} x `{}`'.format(EMOJI['DAR'], EMOJI['SIG'], num2, EMOJI['GPLATE'], EMOJI['SPLATE'], num)
			
			await client.say(msg)
			

@client.command(pass_context=True)
async def use(ctx, num : int, item : str, poop = '', item2 = ''):
	auth = ctx.message.author.id
	if await idiot_check(auth):
		return
		
	# item = what they have, item2 = what they want. poop = whatever they write
	item = item.lower()

	item2 = item2.lower()
	if item not in items or (item2 not in items and item2 != ''):
		await client.say('{} | Sorry! I don\'t recognize that item. For help, use !tc help.'.format(EMOJI['NO']))
		return
	if num < 0:
		await client.say('{} | Please enter a non-negative number.'.format(EMOJI['NO']))
		return
	if num == 0:
		await client.say('{} | Lol you can\'t make anything {}'.format(EMOJI['NO'], EMOJI['OLUL']))
		return

	if item == 'rubies' or item == 'ruby':
		if item2 == 'diamonds' or item2 == 'diamond':
			if num < 100:
				await client.say('{} | You do not have enough rubies to make a diamond.\n\t\t1 diamond is 100 rubies.'.format(EMOJI['NO']))
			else:
				msg = ''
				if (num % 100 != 0):
					r = num % 100
					num = num // 100 * 100
					msg += ':warning: | Rounding down to `{}` rubies. `{}` left over.\n\n'.format(num, r)
				dia = floor(num / 100)
				eme = dia * 10
				sapp = eme * 5
				kits = format((dia * 1000) + (eme * 100) + (sapp * 20), ',')
				msg += '**Starting supplies**\n{} x `{}`\n{} x `{}`'.format(EMOJI['RUBY'], num, EMOJI['KIT'], kits)
				msg += '\n**Intermediate steps**\n{} x `{}`\n{} x `{}`'.format(EMOJI['SAPP'], sapp, EMOJI['EME'], eme)
				msg += '\n**Final product**\n{} x `{}`'.format(EMOJI['DIA'], dia)
				await client.say(msg)
		elif item2 == 'emeralds' or item2 == 'emerald':
			if num < 10:
				await client.say('{} | You do not have enough rubies to make an emerald.\n1 emerald is 10 rubies.'.format(EMOJI['NO']))
			else:
				msg = ''
				if (num % 10 != 0):
					r = num % 10
					num = num // 10 * 10
					msg += ':warning: | Rounding down to `{}` rubies. `{}` left over.\n\n'.format(num, r)
				eme = floor(num / 10)
				sapp = eme * 5
				kits = format((eme * 100) + (sapp * 20), ',')
				msg += '**Starting supplies**\n{} x `{}`\n{} x `{}`'.format(EMOJI['RUBY'], num, EMOJI['KIT'], kits)
				msg += '\n**Intermediate step**\n{} x `{}`'.format(EMOJI['SAPP'], sapp)
				msg += '\n**Final product**\n{} x `{}`'.format(EMOJI['EME'], eme)
				await client.say(msg)
		elif item2 == 'sapphires' or item2 == 'sapphire' or item2 == '':
			msg = ''
			warned = False
			if item2 == '':
				msg += ':warning: | Item2 not specified. Defaulting to next tier up.\n'
				warned = True
			if (num % 2 != 0):
				r = num % 2
				num = num // 2 * 2
				if warned:
					msg += '\t\t'
				else:
					msg += ':warning: | '
				msg += 'Rounding down to `{}` rubies. `{}` left over.\n\n'.format(num, r)
			sapp = floor(num / 2)
			kits = format(sapp * 20, ',')
			msg += '**Starting supplies**\n{} x `{}`\n{} x `{}`'.format(EMOJI['RUBY'], num, EMOJI['KIT'], kits)
			msg += '\n**Final product**\n{} x `{}`'.format(EMOJI['SAPP'], sapp)
			await client.say(msg)
		else:
			await client.say('I\'m not working for some reason. <@145322874805157889>')
	if item == 'sapphires':
		if item2 == 'emeralds' or item2 == 'emerald' or item2 == '':
			msg = ''
			if (num % 5 != 0):
				r = num % 5
				num = num // 5 * 5
				msg += ':warning: | Rounding down to `{}` sapphires. `{}` left over.\n\n'.format(num, r)
			eme = floor(num / 5)
			kits = format(eme * 100, ',')
			msg += '**Starting supplies**\n{} x `{}`\n{} x `{}`'.format(EMOJI['SAPP'], num, EMOJI['KIT'], kits)
			msg += '\n**Final product**\n{} x `{}`'.format(EMOJI['EME'], eme)
			await client.say(msg)
		if item2 == 'diamonds' or item2 == 'diamond':
			msg = ''
			if (num % 50 != 0):
				r = num % 50
				num = num // 50 * 50
				msg += ':warning: | Rounding down to `{}` sapphires. `{}` left over.\n\n'.format(num, r)
			dia = floor(num / 50)
			eme = dia * 10
			kits = format((dia * 1000) + (eme * 100), ',')
			msg += '**Starting supplies**\n{} x `{}`\n{} x `{}`'.format(EMOJI['SAPP'], num, EMOJI['KIT'], kits)
			msg += '\n**Intermediate steps**\n{} x `{}`'.format(EMOJI['EME'], eme)
			msg += '\n**Final product**\n{} x `{}`'.format(EMOJI['DIA'], dia)
			await client.say(msg)
	if item == 'emeralds':
		if item2 != 'diamonds' and item2 != 'diamond' and item2 != '':
			await client.say('{} | You can only make diamonds with emeralds. No item2 needs to be specified.'.format(EMOJI['NO']))
		else:
			msg = ''
			if (num % 10 != 0):
				r = num % 10
				num = num // 10 * 10
				msg += ':warning: | Rounding down to `{}` emeralds. `{}` left over.\n\n'.format(num, r)
			dia = floor(num / 10)
			kits = format((dia * 1000), ',')
			msg += '**Starting supplies**\n{} x `{}`\n{} x `{}`'.format(EMOJI['EME'], num, EMOJI['KIT'], kits)
			msg += '\n**Final product**\n{} x `{}`'.format(EMOJI['DIA'], dia)
			await client.say(msg)

	if item == 'talents':
		if item2 == 'daric' or item2 == 'darics' or item2 == '' or item2 == 'siglo' or item2 == 'siglos':
			msg = ''
			if (num % 5 != 0):
				r = num % 5
				num = num // 5 * 5
				msg += ':warning: | Rounding down to `{}` talents. `{}` left over.\n\n'.format(num, r)
			daric = floor(num / 5)
			kits = format((daric * 60), ',')
			pp = int(((num / 5) * 20) / 1000)
			msg += '**Starting supplies**\n{}/{} x `{}`\n{} x `{}`\n{} x `{}`'.format(EMOJI['GTAL'], EMOJI['STAL'], num, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			msg += '\n**Final product**\n{}/{} x `{}`'.format(EMOJI['DAR'], EMOJI['SIG'], daric * 3)
			await client.say(msg)
		elif item2 == 'plates' or item2 == 'plate':
			msg = ''
			if (num % 5 != 0):
				r = num % 5
				num = num // 5 * 5
				msg += ':warning: | Rounding down to `{}` talents. `{}` left over.\n\n'.format(num, r)
			daric = int(num / (5/3))
			plate = int((daric // 5 * 5) / (5/3))
			kits = format(int(((daric * 60)/3) + ((plate * 240)/3)), ',')
			pp = int((((num / 5) * 20) + ((daric / 5) * 80)) / 1000)
			msg += '**Starting supplies**\n{}/{} x `{}`\n{} x `{}`\n{} x `{}`'.format(EMOJI['GTAL'], EMOJI['STAL'], num, EMOJI['KIT'], kits, EMOJI['CURE'], pp)
			msg += '\n**Intermediate step**\n{}/{} x `{}`'.format(EMOJI['DAR'], EMOJI['SIG'], daric)
			if (daric % 5 != 0):
				rd = daric % 5
				msg += '\n**Final product**\n{}/{} x `{}`\n{}/{} x `{}` (left over)'.format(EMOJI['GPLATE'], EMOJI['SPLATE'], plate, EMOJI['DAR'], EMOJI['SIG'], rd)
			else:
				msg += '\n**Final product**\n{}/{} x `{}`'.format(EMOJI['GPLATE'], EMOJI['SPLATE'], plate)

			await client.say(msg)
		else:
			await client.say('{} | Please enter a valid item name for item #2. For talents, this is darics, siglos, or plates.'.format(EMOJI['NO']))
			return
	if item == 'darics' or item == 'siglos':
		if item2 != 'plates' and item2 != 'plate' and item2 != '':
			await client.say('{} | You can only make diamonds with emeralds. No item2 needs to be specified.'.format(EMOJI['NO']))
		else:
			msg = ''
			if (num % 5 != 0):
				r = num % 5
				num = num // 5 * 5
				msg += ':warning: | Rounding down to `{}` darics. `{}` left over.\n\n'.format(num, r)
			plate = floor(num / 5)
			kits = format((plate * 240), ',')
			pp = int(((num / 5) * 80) / 1000)
			msg += '**Starting supplies**\n{}/{} x `{}`\n{} x `{}`\n{} x `{}`'.format(EMOJI['DAR'], EMOJI['SIG'], num, EMOJI['KIT'], kits, EMOJI['CURE'], pp


			)
			msg += '\n**Final product**\n{}/{} x `{}`'.format(EMOJI['GPLATE'], EMOJI['SPLATE'], plate * 3)
			await client.say(msg)

@client.command(pass_context=True)
async def post(ctx, channel, *msg):
	#make so command only works in bunana_chat

	gen = client.get_channel('499830030717812737')
	bun = client.get_channel('328327931824832514')
	craf = client.get_channel('532999570024693760')
	if ctx.message.channel.id != '328327931824832514':
		return
	else:
		output = ' '.join(msg)
		if channel == 'b':
			await client.send_message(bun, output)
		if channel == 'g':
			await client.send_message(gen, output)
		if channel == 'c':
			await client.send_message(craf, output)


client.run(token)
