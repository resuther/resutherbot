@client.command(aliases = ['calct'])
async def calcx(ctx, num1: int, num2: int):
    sum = num1*num2
    await ctx.send('The multiplication of {0} and {1} is {2}'.format(num1, num2, sum))

@client.command(aliases = ['calc+'])
async def calcp(ctx, num1: int, num2: int):
    sum = num1 + num2
    await ctx.send('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

@client.command()
async def calcd(ctx, num1: int, num2: int):
    sum = num1/num2
    await ctx.send('The division of {0} and {1} is {2}'.format(num1, num2, sum))

@client.command()
async def calcm(ctx, num1: int, num2: int):
    sum = num1-num2
    await ctx.send('The subtraction of {0} and {1} is {2}'.format(num1, num2, sum))
