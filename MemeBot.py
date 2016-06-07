from groupy import Member, Bot, Group
from random import randint

group = Group.list()[0]
bot = Bot.list().first
members = group.members()

rating = ['I rate your meme: shitpost', 'I rate your meme: 0/10 fuck you', 'I rate your meme: God tier', 'I rate your meme: perfect 5/7', 'I rate your meme: gr8 8/8', 'I rate your meme: 2/10, 6/10 with rice']

def MemeBot(message):
	if "Try these commands:" in message:
		return
	elif "Damn straight I'm Canadian" in message:
		return
	elif "!ratememe" in message:
		ind = randint(0,5)
		bot.post(rating[ind])
	elif "lol" in message:
		bot.post("That wasn't funny you asshole")
	elif "!help" in message:
		bot.post("There's no help for you, anon")
	elif "!actualhelp" in message:
		bot.post("Try these commands: '!help', '!roll', '!ratememe', !pickasshole")
	elif "!roll" in message:
		bot.post( ("Rolled: %d") % (randint(1,6)) )
	elif "A sig" in message:
		bot.post("Alpha Sigma Phi is Butler's freshest meme")
	elif "a sig" in message:
                bot.post("Alpha Sigma Phi is Butler's freshest meme")
	elif "A Sig" in message:
                bot.post("Alpha Sigma Phi is Butler's freshest meme")
	elif "Lol" in message:
		bot.post("That wasn't funny you asshole")
	elif "memebot" in message:
		bot.post("Fuck you, eh!")
	elif "Canadian" in message:
		bot.post("Damn straight I'm Canadian!")
	elif "canadian" in message:
                bot.post("Damn straight I'm Canadian!")
	elif "MemeBot" in message:
                bot.post("Fuck you, eh!")
	elif "Memebot" in message:
                bot.post("Fuck you, eh!")
	elif "!pickasshole" in message:
		pickedMem = members[randint(0,len(members)-1)].nickname
		bot.post("Selected asshole is %s" % pickedMem)
		
