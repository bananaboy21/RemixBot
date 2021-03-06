'''
MIT License

Copyright (c) 2017 Cree-Py

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import discord
from discord.ext import commands
import random


class Misc:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: str):
        '''Ask the 8 ball a question'''
        if not question.endswith('?'):
            return await ctx.send('Please ask a question')

        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                     "You may rely on it", "As I see it, yes", "Most likely", "Outlook good",
                     "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later",
                     "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                     "Very doubtful"]

        num = random.randint(0, 19)
        if num < 10:
            em = discord.Embed(color=discord.Color(value=0x00ff00))
        elif num < 15:
            em = discord.Embed(color=discord.Color(value=0xffff00))
        else:
            em = discord.Embed(color=discord.Color(value=0xff0000))

        response = responses[num]

        em.title = f"🎱{question}"
        em.description = response
        await ctx.send(embed=em)

    @commands.command(aliases=['rn', 'randomnum', 'randnumber'])
    async def randomnumber(self, ctx, min=1, max=100):
        '''Get a random number between two numbers, or 1 and 100'''
        await ctx.send(f'Your random number is: {random.randint(min, max)}')

    @commands.command(aliases=['coin'])
    async def flipcoin(self, ctx):
        '''Flips a coin'''
        choices = ['You got Heads', 'You got Tails']
        color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title='Coinflip:', description=random.choice(choices))
        await ctx.send(embed=em)

    @commands.command()
    async def dice(self, ctx, number=1):
        '''Rolls a certain number of dice'''
        if number > 20:
            number = 20

        fmt = ''
        for i in range(1, number + 1):
            fmt += f'`Dice {i}: {random.randint(1, 6)}`\n'
            color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title='Roll a certain number of dice', description=fmt)
        await ctx.send(embed=em)

    @commands.command(aliases=['randquote', 'quote'])
    async def randomquote(self, ctx):
        '''Get a random inspirational quote!'''

        quotes = ["*You can do anything, but not everything.*\n—David Allen",
                  "*Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.*\n—Antoine de Saint-Exupéry",
                  "*You miss 100 percent of the shots you never take.*\n—Wayne Gretzky",
                  "*Courage is not the absence of fear, but rather the judgement that something else is more important than fear.*\n—Ambrose Redmoon",
                  "*You must be the change you wish to see in the world.*\n—Gandhi",
                  "*To the man who only has a hammer, everything he encounters begins to look like a nail.*\n—Abraham Maslow",
                  "*We are what we repeatedly do; excellence, then, is not an act but a habit.*\n—Aristotle",
                  "*A wise man gets more use from his enemies than a fool from his friends.*\n—Baltasar Gracian",
                  "*Do not seek to follow in the footsteps of the men of old; seek what they sought.*\n—Basho",
                  "*Everyone is a genius at least once a year. The real geniuses simply have their bright ideas closer together.*\n—Georg Christoph Lichtenberg",
                  "*The real voyage of discovery consists not in seeking new lands but seeing with new eyes.*\n—Marcel Proust",
                  "*Even if you’re on the right track, you’ll get run over if you just sit there.*\n—Will Rogers",
                  "*People often say that motivation doesn’t last. Well, neither does bathing – that’s why we recommend it daily.*\n—Zig Ziglar",
                  "*I am cool.*\n—Victini",
                  "*The way to get started is to quit talking and begin doing.*\n—Walt Disney",
                  "*Don't let yesterday take up too much of today.*\n—Will Rogers",
                  "*Do. Or do not. There is no try.*\n—Yoda",
                  "*It's not about ideas. It's about making ideas happen.*\n—Scott Belsky",
                  "*The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.*\n—Helen Keller"]

        num = random.randint(0, (len(quotes) - 1))
        quote = quotes[num]
        await ctx.send(quote)


def setup(bot):
    bot.add_cog(Misc(bot))
