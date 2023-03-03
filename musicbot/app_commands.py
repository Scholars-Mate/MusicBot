import asyncio
import discord
from .bot import MusicBot

def initialize_slash_commands(bot: MusicBot):

    test_guild = [bot.config.test_guild]

    # Media controls
    @bot.slash_command(name = "play", description = "play a song", guild_ids = test_guild)
    async def play(ctx, song: discord.Option(str, "song name or youtube/spotify url")):
        await ctx.defer()
        response = await ctx.bot.cmd_play(
            message = "",
            _player = ctx.bot.players.get(ctx.guild_id),
            channel = ctx.channel,
            author = ctx.author,
            permissions = ctx.bot.permissions.for_user(ctx.author),
            leftover_args = [song],
            song_url = ""
        )
        await ctx.respond(response.content)

    async def stream(ctx):
        pass

    async def pause(ctx):
        pass

    async def resume(ctx):
        pass

    async def volume(ctx, volume: discord.Option(int, "new volume")):
        pass

    # Playlist Manipulation
    @bot.slash_command(name = "queue", description = "display the current queue", guild_ids = test_guild)
    async def queue(ctx):
        await ctx.defer()
        response = await ctx.bot.cmd_queue(
            channel = ctx.channel,
            player = ctx.bot.get_player_in(ctx.guild)
        )
        await ctx.respond(embed = discord.Embed(title = "Queue", description = response.content))

    async def np(ctx):
        pass

    @bot.slash_command(name = "skip", description = "skip the current song", guild_ids = test_guild)
    async def skip(ctx):
        await ctx.defer()
        response = await ctx.bot.cmd_skip(
            player = ctx.bot.get_player_in(ctx.guild),
            channel = ctx.channel,
            author = ctx.author,
            message = ctx.message,
            permissions = ctx.bot.permissions.for_user(ctx.author),
            voice_channel = None,
            param = "force"
        )
        await ctx.respond(response.content)

    @bot.slash_command(name = "remove", description = "remove a song from the queue", guild_ids = test_guild)
    async def remove(ctx, position: discord.Option(int, "the number of the song in queue to remove")):
        await ctx.defer()
        response = await ctx.bot.cmd_remove(
            user_mentions = None,
            message = ctx.message,
            author = ctx.author,
            permissions = ctx.bot.permissions.for_user(ctx.author),
            channel = ctx.channel,
            player = ctx.bot.get_player_in(ctx.guild),
            index = position
        )
        await ctx.respond(response.content)

    async def search(ctx, search: discord.Option(str, "search string")):
        pass

    async def save(ctx):
        pass

    async def clear(ctx):
        pass

    async def resetplaylist(ctx):
        pass

    async def playnext(ctx, song: discord.Option(str, "song name or youtube/spotify url")):
        pass

    async def shuffle(ctx):
        pass

    async def karaoke(ctx):
        pass

    # Bot Administration
    @bot.slash_command(name = "summon", description = "summon the bot the current voice channel", guild_ids = test_guild)
    async def summon(ctx):
        await ctx.defer()
        response = await ctx.bot.cmd_summon(
            channel = ctx.channel,
            guild = ctx.guild,
            author = ctx.author,
            voice_channel = None
        )
        await ctx.respond(embed = discord.Embed(title = "Summon", description = response.content))

    @bot.slash_command(name = "disconnect", description = "force the bot to leave the current voice channel", guild_ids = test_guild)
    async def disconnect(ctx):
        await ctx.defer()
        await ctx.bot.disconnect_voice_client(ctx.guild)
        await ctx.respond("Disconnected from {}".format(ctx.guild.name))

    @bot.slash_command(name = "restart", description = "restart the bot", guild_ids = test_guild)
    async def restart(ctx):
        await ctx.respond("Restarting...");
        await ctx.bot.cmd_restart(ctx.channel)

    async def shutdown(ctx):
        pass

    async def blacklist(ctx):
        pass

    async def joinserver(ctx):
        pass

    async def leaveserver(ctx):
        pass

    async def setname(ctx, name: discord.Option(str, "new name")):
        pass

    async def setnick(ctx, name: discord.Option(str, "new name")):
        pass

    async def setavatar(ctx, url: discord.Option(str, "url of the new avatar")):
        pass

    async def option(ctx):
        pass

    # Utilities
    async def help(ctx):
        pass

    async def clean(ctx, search_range: discord.Option(int, "the number of songs to remove")):
        pass

    async def id(ctx):
        pass

    async def listids(ctx):
        pass

    async def perms(ctx):
        pass

    async def pldump(ctx):
        pass
