# This example requires the 'message_content' privileged intents

import os
import discord
import random
import json
import requests
from cosine import cosine, conv_vec

bot = discord.Bot(intents=discord.Intents.all())

@bot.slash_command(name="watup", description="Greet up yall homie!")
async def watup(ctx):
	watup_roasts = ['Gud to see u after ur prents seperated!', 'Someone pls speak to this peasant!', 'Nigga really is lonely!', 'Sry no change, cya later!']
	watup_roasts_gif = ['https://media.tenor.com/EGRAsWApsqUAAAAM/burn-oh-snaps.gif', 'https://media.tenor.com/TbYDWisEAKcAAAAM/shocked-burn.gif', 'https://media.tenor.com/3qgteD3kWrgAAAAM/el%C3%A7insangu-tea-time.gif']
	embed = discord.Embed(
		title=f"Yo nigga! {random.choice(watup_roasts)}",
		color=discord.Colour.blurple())

	embed.set_image(url=random.choice(watup_roasts_gif))
	message = await ctx.send(embed=embed)
	emojis = ['🥵', '🗿', '👀', '😂']
	for emoji in emojis:
		await message.add_reaction(emoji)


@bot.slash_command(name="ping", description="Check ma ping boi!")
async def ping(ctx):
	embed = discord.Embed(
		title=f"My ping is {round(bot.latency, 3)*1000}ms",
		color=discord.Colour.green())
	embed.set_image(url='https://i.makeagif.com/media/9-03-2017/Ij8D-4.gif')
	await ctx.respond(embed=embed)


meme = discord.SlashCommandGroup("meme", "Memes from ur home boi. dank memer is a scam!")
class SFWmemeView(discord.ui.View):
	@discord.ui.button(emoji="💾", label="Ask to Rate", style=discord.ButtonStyle.blurple)
	async def save_button_callback(self, button, interaction):
		embed = discord.Embed(
			title=f"{interaction.user} found this message funny!",
			description=f"pings: {interaction.message.guild.default_role} wanna react?")
		embed.set_image(url='https://media.tenor.com/lr8W5AadieAAAAAM/smile-laughing.gif')
		await interaction.response.send_message(embed=embed)
		emojis = ['🥵', '🗿', '👀', '😂']
		for emoji in emojis:
			await interaction.message.add_reaction(emoji)
	@discord.ui.button(emoji="➡️",label="Next", style=discord.ButtonStyle.green)
	async def next_button_callback(self, button, interaction):
		res = requests.get('https://meme-api.com/gimme').text
		memeData = json.loads(res)
		memeUrl = memeData['url']
		memeTitle = memeData['title']
		memeAuthor = memeData['author']
		memeSub = memeData['subreddit']
		memeLink = memeData['postLink']
		embed = discord.Embed(
			title=memeTitle,
			color=discord.Colour.orange())
		embed.set_image(url=memeUrl)
		embed.set_footer(text=f"Posted by {memeAuthor} | on {memeSub}!")
		await interaction.message.edit(embed=embed)
		await interaction.response.defer()

class NSFWmemeView(discord.ui.View):
	@discord.ui.button(emoji="💾", label="Ask to react", style=discord.ButtonStyle.blurple)
	async def save_button_callback(self, button, interaction):
		embed = discord.Embed(
			title=f"{interaction.user} found this message funny!",
			description=f"pings: {interaction.message.guild.default_role} wanna react??")
		embed.set_image(url='https://media.tenor.com/lr8W5AadieAAAAAM/smile-laughing.gif')
		await interaction.response.send_message(embed=embed)
		emojis = ['🥵', '🗿', '👀', '😂']
		for emoji in emojis:
			await interaction.message.add_reaction(emoji)
	@discord.ui.button(emoji="➡️",label="Next", style=discord.ButtonStyle.green)
	async def next_button_callback(self, button, interaction):
		res = requests.get('https://meme-api.com/gimme/NSFWMemes').text
		memeData = json.loads(res)
		memeUrl = memeData['url']
		memeTitle = memeData['title']
		memeAuthor = memeData['author']
		memeSub = memeData['subreddit']
		memeLink = memeData['postLink']
		embed = discord.Embed(
			title=memeTitle,
			color=discord.Colour.red())
		embed.set_image(url=memeUrl)
		embed.set_footer(text=f"Posted by {memeAuthor} | on {memeSub}!")
		await interaction.message.edit(embed=embed)
		await interaction.response.defer()

@meme.command(description="MEMES from ur home boi!")
async def sfw(ctx):
	res = requests.get('https://meme-api.com/gimme').text
	memeData = json.loads(res)
	memeUrl = memeData['url']
	memeTitle = memeData['title']
	memeAuthor = memeData['author']
	memeSub = memeData['subreddit']
	memeLink = memeData['postLink']
	embed = discord.Embed(
		title=memeTitle,
		color=discord.Colour.orange())
	embed.set_image(url=memeUrl)
	embed.set_footer(text=f"Posted by {memeAuthor} | on {memeSub}!")
	await ctx.respond(embed=embed, view=SFWmemeView())

@meme.command(description="NSFW MEMES from ur home boi!")
async def nsfw(ctx):
	res = requests.get('https://meme-api.com/gimme/NSFWMemes').text
	memeData = json.loads(res)
	memeUrl = memeData['url']
	memeTitle = memeData['title']
	memeAuthor = memeData['author']
	memeSub = memeData['subreddit']
	memeLink = memeData['postLink']
	embed = discord.Embed(
		title=memeTitle,
		color=discord.Colour.red())
	embed.set_image(url=memeUrl)
	embed.set_footer(text=f"Posted by {memeAuthor} | on {memeSub}!")
	await ctx.send(embed=embed, view=NSFWmemeView())



@bot.slash_command(name="roast", description="Roast the fuck outta!")
async def roast(ctx, nigger: discord.Option(discord.SlashCommandOptionType.user)):
	roasts_file = open('roasts.txt', encoding="utf-8")
	roasts = roasts_file.readlines()
	roasts = [roast.strip() for roast in roasts]
	roast_gifs = ['https://media.tenor.com/KJVlOt5r1pkAAAAj/discord-discordgifemoji.gif', 'https://media.tenor.com/cmwedILasMIAAAAM/boom-roasted.gif', 'https://media.tenor.com/f8YmpuCCXJcAAAAM/roasted-oh.gif', 'https://media.tenor.com/CZoZV7amWI8AAAAM/roast-turkey-turkey.gif', 'https://media.tenor.com/uecw2PP2wJsAAAAM/roasted-oh.gif', 'https://media.tenor.com/Zm_jDUcRffcAAAAM/roasting-roast.gif']
	roast = random.choice(roasts)
	embed = discord.Embed(
		title=f'@{nigger.name}',
		description=roast,
		color=discord.Colour.yellow()
		)
	embed.set_image(url=random.choice(roast_gifs))
	embed.set_footer(text=f"Roasted by {ctx.author}| using chad bot")
	message = await ctx.send(embed=embed)
	emojis = ['🥵', '🗿', '👀', '🫡']
	for emoji in emojis:
		await message.add_reaction(emoji)

@bot.slash_command(title='say', description='repeats what u say!')
async def say(ctx, text = discord.Option(str)):
	await ctx.respond(text)



### EVENTS ->

@bot.event
async def on_ready():
	print("Yo nigga im in!")

@bot.event
async def on_message(message):
	
	# print(message.content)
	if message.author != bot.user and message.author != discord.Member.bot:
		message_vec = conv_vec(message.content)
		# Ohio meme		
		results_ohio = []
		Ohio_sent_list = ["only in ohio", "ohio moment", "bro is born in ohio", 'ohio', 'what', 'bruh', 'bro skipped']
		for ohio_sentence in Ohio_sent_list:
			ohio_vec = conv_vec(ohio_sentence)
			results_ohio.append(cosine(message_vec, ohio_vec))

		total_ohio = 0
		for results_num in results_ohio:
			total_ohio += results_num

		if total_ohio >= 0.5:
			embed = discord.Embed(
				title="Ohio moment 💀!",
				color=discord.Colour.red())
			ohio_gif = ['https://media.tenor.com/NT09SttCWNMAAAAC/ohio-unfunny.gif', 'https://i.imgflip.com/6zl05b.gif', 'https://i.imgflip.com/71li7e.gif']
			embed.set_image(url=random.choice(ohio_gif))
			embed.set_footer(text="if wrong moment pls ignore! Programmed by a dumb dev")
			await message.channel.send(embed=embed)

		# Bye message
		results_bye = []
		bye_message_list = ['by', 'bye', 'byee', 'byei', 'byie', 'goodbye', 'cya', 'enough for today', 'buy']
		for bye_sentence in bye_message_list:
			bye_vec = conv_vec(bye_sentence)
			results_bye.append(cosine(message_vec, bye_vec))

		total_bye = 0
		for results_num in results_bye:
			total_bye += results_num

		if total_bye >= 0.5:
			embed = discord.Embed(
				title=f"Say bye to {message.author}",
				color=discord.Colour.blurple())
			bye_gifs = ['https://media.tenor.com/cv7t69yhNYwAAAAM/peace-out-bye.gif', 'https://media.tenor.com/qYbjnr7Y2S8AAAAM/simpson-bye.gif', 'https://banter.so/wp-content/uploads/2022/06/see-you-later-bye-felicia.gif', 'https://banter.so/wp-content/uploads/2022/06/see-you-later-bye-felicia.gif']
			embed.set_image(url=random.choice(bye_gifs))
			await message.channel.send(embed=embed)

bot.add_application_command(meme)
bot.run(os.environ["DISCORD_TOKEN"])
