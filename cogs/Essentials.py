import discord
from discord.ext import commands
from time import strftime

class Essentials(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Initial startup confirmation
    @commands.Cog.listener()
    async def on_ready(self):
        print(strftime('\n%b %d, %Y'))
        print('Connected to %s servers\n' % (str(len(self.client.guilds))))
        print(strftime('%X    ') + 'Logged in as {0.user}'.format(self.client))

    # Error reporting
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        report = discord.Embed(colour=0xffffff)
        report.add_field(name='Command invoked incorrectly, run ..help for correct usage', value=error)
        await ctx.send(embed=report)

    # Kill command
    @commands.command(name='stop', aliases=['kill', 'exit', 'die'])
    async def kill_bot_command(self, ctx):
        print(strftime('%X    ') + 'User %s has killed Rumbot' % (ctx.author))
        await ctx.channel.send('ouch')
        await self.client.logout()

def setup(client):
    client.add_cog(Essentials(client))
