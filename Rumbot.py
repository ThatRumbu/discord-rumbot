# Rumbot by Rumbu (@Rumbu#5277)
# Discord developer portal  - https://discordapp.com/developers/applications/
# Add Rumbot to your server - https://discordapp.com/oauth2/authorize?client_id=617989837500448788&scope=bot

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from time import strftime

load_dotenv()
cmd_prefix = '..'
client = commands.Bot(command_prefix=cmd_prefix)

# Default cogs
loaded_cogs = ['cogs.Essentials']

if __name__ == '__main__':
    for ext in loaded_cogs:
        client.load_extension(ext)

# Cog management group
@client.group(name='cogs', aliases=['cog', 'modules', 'ext', 'exts', 'extension', 'extensions'], invoke_without_command=True)
async def cog_mgmt(ctx):
    
    # List cogs
    unloaded_cogs = []
    for ext in os.listdir('./cogs'):
        if ext.endswith('.py') and 'cogs.' + ext[:-3] not in loaded_cogs:
            unloaded_cogs.append(ext[:-3])
    unloaded_cogs.sort()

    loaded_list = ''
    unloaded_list = ''
    if loaded_cogs == []:
        loaded_list = '—'
    if unloaded_cogs == []:
        unloaded_list = '—'

    for ext in loaded_cogs:
        loaded_list = loaded_list + str(ext)[5:] + '\n'
    for ext in unloaded_cogs:
        unloaded_list = unloaded_list + (ext + '\n')

    list_cogs = discord.Embed(title='Available Cogs', colour=0xfffffe)
    list_cogs.add_field(name='Loaded Cogs', value=loaded_list)
    list_cogs.add_field(name='Unloaded Cogs', value=unloaded_list)
    list_cogs.set_footer(text='Use %shelp to view correct usage and syntax for cogs' % cmd_prefix)
    await ctx.send(embed=list_cogs)

# Load cogs
@cog_mgmt.command(name='load', aliases=['enable', 'start', 'add'])
async def cog_mgmt_load(ctx, *extension):

    # Generate list
    unloaded_cogs = []
    for ext in os.listdir('./cogs'):
        ext = 'cogs.' + ext
        if ext.endswith('.py') and ext[:-3] not in loaded_cogs:
            unloaded_cogs.append(ext[:-3])
    
    # Validity check + load
    for ext in extension:
        ext = 'cogs.' + ext.replace(',', '')
        if ext not in loaded_cogs and ext not in unloaded_cogs:
            cog_load_info = discord.Embed(title=ext + ' does not exist', colour=0xffffff)
            cog_load_info.set_footer(text='Ensure capitalisation is correct, use %shelp for correct usage' % cmd_prefix)
            await ctx.send(embed=cog_load_info)
        elif ext in loaded_cogs:
            cog_load_info = discord.Embed(title=ext + ' is already loaded', colour=0xffffff)
            cog_load_info.set_footer(text='Use %scogs reload to update' % cmd_prefix)
            await ctx.send(embed=cog_load_info)
        else:
            client.load_extension(ext)
            loaded_cogs.append(ext)
            print('%s    %s has been enabled by %s in %s' % (strftime('%X'), ext, ctx.author, ctx.guild))
            cog_load_info = discord.Embed(title=ext + ' has been successfully loaded', colour=0xffffff)
            await ctx.send(embed=cog_load_info)

# Unload cogs
@cog_mgmt.command(name='unload', aliases=['disable', 'stop', 'remove'])
async def cog_mgmt_unload(ctx, *extension):

    # Generate list
    unloaded_cogs = []
    for ext in os.listdir('./cogs'):
        ext = 'cogs.' + ext
        if ext.endswith('.py') and ext[:-3] not in loaded_cogs:
            unloaded_cogs.append(ext[:-3])
    
    # Validity check + load
    for ext in extension:
        ext = 'cogs.' + ext.replace(',', '')
        if ext not in loaded_cogs and ext not in unloaded_cogs:
            cog_load_info = discord.Embed(title=ext + ' does not exist', colour=0xffffff)
            cog_load_info.set_footer(text='Ensure capitalisation is correct, use %shelp for correct usage' % cmd_prefix)
            await ctx.send(embed=cog_load_info)
        elif ext in unloaded_cogs:
            cog_load_info = discord.Embed(title=ext + ' is already unloaded', colour=0xffffff)
            await ctx.send(embed=cog_load_info)
        else:
            client.unload_extension(ext)
            loaded_cogs.remove(ext)
            print('%s    %s has been disabled by %s in %s' % (strftime('%X'), ext, ctx.author, ctx.guild))
            cog_load_info = discord.Embed(title=ext + ' has been successfully unloaded', colour=0xffffff)
            await ctx.send(embed=cog_load_info)

# Reload cogs
@cog_mgmt.command(name='reload', aliases=['update', 'restart'])
async def cog_mgmt_reload(ctx, *extension):

    # Generate list
    unloaded_cogs = []
    for ext in os.listdir('./cogs'):
        ext = 'cogs.' + ext
        if ext.endswith('.py') and ext[:-3] not in loaded_cogs:
            unloaded_cogs.append(ext[:-3])
    
    # Validity check + load
    for ext in extension:
        ext = 'cogs.' + ext.replace(',', '')
        if ext not in loaded_cogs and ext not in unloaded_cogs:
            cog_load_info = discord.Embed(title=ext + ' does not exist', colour=0xffffff)
            cog_load_info.set_footer(text='Ensure capitalisation is correct, use %shelp for correct usage' % cmd_prefix)
            await ctx.send(embed=cog_load_info)
        elif ext in unloaded_cogs:
            cog_load_info = discord.Embed(title=ext + ' is not loaded', colour=0xffffff)
            cog_load_info.set_footer(text='Use %scogs load to enable' % cmd_prefix)
            await ctx.send(embed=cog_load_info)
        else:
            client.reload_extension(ext)
            print('%s    %s has been reloaded by %s in %s' % (strftime('%X'), ext, ctx.author, ctx.guild))
            cog_load_info = discord.Embed(title=ext + ' has been successfully reloaded', colour=0xffffff)
            await ctx.send(embed=cog_load_info)

client.run(os.getenv('BOT_TOKEN'))

