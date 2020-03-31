# Rumbu's Rumbot for Discord

So I made this bot cause I was bored and in quarantine (thanks coronavirus), if you want to snag any parts of this bot that's fine as long as you don't claim it as yours (duh) and give credit where credit is due. 

Keep in mind everything is modular so theoretically you could just fork the whole thing and add your own cogs for an easy plug and play solution, would def appreciate a heads up though in case I fucked something up and didn't end up fixing it.

Speaking of modularity, the main `rumbot.py` is nothing more than an albeit overcomplicated and poorly designed cogs management system that will have no problem using third-party cogs. Just remember if you're using this you'll need to throw your bot's token in the `.env`. Anywho, with no futher ado I shall present to you my undeniably uneccessary documentation.

## Requirements

So you should be fine once you install `discord.py` and `python-dotenv` (tbh just put the token in the main file, this is overly fancy for no reason) but here's my `pip freeze` anyway. It may or may not be updated to the latest version of the bot, just check the modification dates I guess lol.
```
aiohttp==3.6.2
async-timeout==3.0.1
attrs==19.3.0
chardet==3.0.4
discord.py==1.3.2
idna==2.9
multidict==4.7.5
python-dotenv==0.12.0
websockets==8.1
yarl==1.4.2
```

## Usage

The layout's kinda wack already so I'll just chuck the basic commands here I s'pose, it's just cog management shit. The default command prefix is `..` so I'll be using that here, but it's easy asf to change so no stress if you think it's weird. I also put in way more aliases than I needed to so I'm not gonna put them in here but if it would make sense it'll probably work.

### cogs

`..cogs`

This'll just print a spicy looking list of loaded and unloaded cogs. Throw in whatever arguments you want cause they'll do *absolutely nothing*.

`..cogs load <extension> [*extension]`

Guess what? This one loads cogs :astonishment:

You can load more than one at once, and there's no need to worry about typos cause I *always* think of everything. Only a monster wouldn't use commas to separate them but hey, it'll work without 'em.

`..cogs unload <extension> [*extension]`

If you thought that last command was cool, check this bitch out! Same syntax so feel free to throw in more than one at once and it'll get those cogs working like a treat.

`..cogs reload <extension> [*extension]`

Dunno really what to say here, just more of the same stuff. Obviously unloaded cogs won't be reloaded, but tpyo consideration certainly isn't unique to this command. (lmao see what i did there?)

## Essentials

So this cog, *in my honest opinion* should not be removed unless you're dealing with all this shit already because—as the name suggests—I consider it to be essential to the functioning of a discord bot (technically it's not but they're all pretty standard features /shrug). Aside from error handling and `on_ready` confirmation among other useful behind-the-scenes functions, it has a command or two that you may find to be useful. Keep in mind that ease of use commands and other 'essentials' are in the [Base](https://github.com/ThatRumbu/discord-rumbot#Base) extension. I also consider that to be a necessity.

(it's a work in progress ok, there will be more than one command)

### stop

`..stop`

Yeah this doesn't take any arguments either, it's literally just stops the bot. No there's no start command cause that's not how this works.

I'mma fill out some space by letting you know that `..kill`, `..die` and `..exit` are all valid aliases. Yes, I know I said I wasn't going to list aliases. No, I don't care that this is blatant hypocrisy.

## Base

oops, this be empty. get to work, bud

## Help

a more detailed (and better looking) `..help` command. might do some other stuff, idk, I haven't written it yet

## Admin

ooh the useful shit! welp guess what, this is really low on my to do list so if you want it bug me

## Projects

create and manage channels for private discussion

## Overviewer

allows for integration with [Minecraft Overviewer](https://github.com/overviewer/Minecraft-Overviewer/); I also reckon it's super neat or something, you should check it out

## Dev

this has got a couple nonessential (crazy, right?) commands that I was using mostly during development, but if you feel like enabling it to do some testing feel free. I'll write some documentation on it at some point, can't be bothered rn even though I just wrote this entire document

## FAQs

No this isn't a cog you smartass, it's literally just a collection of frequently (not really, if I'm being honest they were arbitrarily decided by me with no purpose other than mentioning a couple of things I wanted to, and further expanding the comedic content of what could have been *extremely* boring documentation (ooh double parentheses—just felt like pointing out that the documentation itself was completely uneccesary, primarily because nobody, not one single person is going to read this. \*sigh\*)) asked questions. Here we go.

### Why do you keep referring to your bot as 'Rumbot`? Is this a subconscious reference to your alcohol addiction?

No, what the fuck. My name is Rumbu so I made a (possibly poor?) pun. I shouldn't have to be explaining this.

### So it's just humour that you use to mask your depression and resultant alcoholism?

1. How is this relevant to the bot?
2. At what point did I infer that I even drink alcohol?
3. Alcoholism isn't a joke, please take it seriously
4. That question doesn't even make sense

### Can I use your bot?

Finally a real question! Yes (I did mention this at the start but ok) you are more than welcome to take parts of Rumbot or snag the whole thing if you'd like, all I ask is you give me fair credit.

### It's not working. Fix your shitty ass-bot.

Well firstly, that's not even a question. Secondly, have you made sure you're using the right syntax? `..help` is your friend.

If your problem still persists feel free to ask me, just send me a message on discord (@Rumbu#5277)

### Do you cry youself to sleep because nobody finds you funny?

I'm actually done with this shit. No more questions. <sub><sub>Sometimes if I'm drunk and depressed</sub></sub>