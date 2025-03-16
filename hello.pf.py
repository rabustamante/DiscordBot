import discord
from discord.ext import commands
from discord import app_commands



class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

        try:
            guild= discord.Object(id=727013441021149245)   
            synced = await self.tree.sync(guild=guild)

            print(f'Synced {len(synced)} commands to guild {guild.id}') 

        except Exception as e:
            print(f'Error syncing commands: {e}')
   
   
   
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)



Guild_ID = discord.Object(id="token")

@client.tree.command(name="hello", description="Say Hello", guild=Guild_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")




@client.tree.command(name="printer", description="I wil print whatever you give me!", guild=Guild_ID)
async def sayHello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)


@client.tree.command(name="embed", description="Emdeb demo!", guild=Guild_ID)
async def sayHello(interaction: discord.Interaction):
    embed = discord.Embed(title="Aris",url="https://www.twitch.tv/avoidingthepuddle", description="I am the description", color=discord.Colour.purple())
    embed.set_thumbnail(url="https://www.twitch.tv/avoidingthepuddle" )
    embed.add_field(name="",value="", inline=False )
    embed.set_footer(text="")
    embed.set_author(name=interaction.user.name, url="https://www.twitch.tv/avoidingthepuddle")
    await interaction.response.send_message(embed=embed)


class View(discord.ui.View):
    @discord.ui.button(label="Click Me!",style=discord.ButtonStyle.red )
    async def button_callback(self, button,interaction):
        await button.response.send_message("click me!")


@client.tree.command(name="button", description="Dispalying a button", guild=Guild_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())




client.run('Token')
