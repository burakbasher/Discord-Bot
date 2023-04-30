import discord


def slash_command(client):
  moderator = '<@&moderatorID>'

  @client.tree.command(
    name="help",
    description=
    "Description here..."
  )
  async def help(interaction: discord.Interaction, helpneeded: str):
    help_channel = client.get_channel(helpChannelID)
    #Send a message to the help channel
    await help_channel.send(
      f"Message for moderators..."
    )
    #Send a message to the user who used this command
    await interaction.response.send_message(
      f"Message for users to inform request has been taken."
    )
    print("log record...")


  @client.tree.command(
    name="signup",
    description="Description here..."
  )
  async def signup(interaction: discord.Interaction, name: str, num: str, faculty: str, departmant: str):
    channel = client.get_channel(channelID)

    #Check if the command was used in the correct channel
    if interaction.channel_id != channel.id:
      print(channel)
      await interaction.response.send_message(
          f"Wrong channel message...")
      return

    #Get the member object of the author of the command
    member = interaction.guild.get_member(interaction.user.id)
    #Change member nick on server
    await member.edit(nick=name)
    await interaction.response.send_message(
      f"Successful message")

    role = discord.utils.get(interaction.guild.roles, id=roleID)
    await member.add_roles(role)
    print("log report, signup is completed")

    signup_channel = client.get_channel(channelID)
    # Send a message to the sign-up channel
    await signup_channel.send(f"Moderation report")
