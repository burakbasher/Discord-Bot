import discord
import responses
import os
from http_server import keep_alive
from discord import app_commands
from slash_commands import slash_command


async def send_message(message, user_message, client, is_private):
  try:
    #change to lower letters, get username, and choose true response
    p_message = user_message.lower()
    username = str(message.author.display_name)
    response = responses.handle_response(user_message, username)

    moderator = '<@&moderatorID>'
    help_channel = client.get_channel(helpChannelID)
    await message.author.send(
      response) if is_private else await message.channel.send(response)
    if p_message == "!help":
      #Send a message to help channel
      await help_channel.send(
        f"Message here..."
      )
  except Exception as e:
    print(e)


class aclient(discord.Client):

  def __init__(self):
    #Bot initialize
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    super().__init__(intents=intents)
    self.synced = False
    self.tree = app_commands.CommandTree(self)

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await self.tree.sync()
      self.synced = True
    print('log report here, bot is on'.format(self))


def run_discord_bot():
  client = aclient()

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    #Log records
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"{username} said: '{user_message}' ({channel})")

    await send_message(message, user_message, client, is_private=False)

  @client.event
  async def on_member_join(member):
    #Channel, role and the message
    moderator = '<@&moderatorID>'
    channel = client.get_channel(registerChannelID)
    message = f'Message here...'

    #Create message as an Embed message
    embed = discord.Embed(title="Title here...",
                          description=message,
                          color=0xFF5733)
    embed.set_thumbnail(
      url=
      thumbnailURL
    )
    embed.set_image(
      url=
      imageURL
    )

    #The role object for every new member
    guild = client.get_guild(ServerId)
    role = guild.get_role(RoleId)

    #Give the role
    await member.add_roles(role)

    #Send the message
    await channel.send(embed=embed)

  slash_command(client)

  my_secret = os.environ['MY_KEY']
  keep_alive()
  client.run(my_secret)
