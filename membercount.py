@client.command(aliases=["members", "mc"])
async def member_count(ctx):
    channel = client.get_channel(779840341011726397)
    a=ctx.guild.member_count
    b=discord.Embed(title=f"Members in {ctx.guild.name}",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)
    await channel.edit(name=a)
