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

class Bsboxsim:
    def __init__(self, bot):
        self.bot = bot
        
    def getResult():
        num = random.randint(0, 100)
        
        if num < 35:
            return "1 Elixir"
        elif num < 40:
            return "2 Elixir"
        elif num < 44:
            return "3 Elixir"
        elif num < 47:
            return "5 Elixir"
        elif num < 49:
            return "7 Elixir"
        elif num < 50:
            return "10 Elixir"
        elif num < 85:
            return "Common Brawler"
        elif num < 85:
            return "Rare Brawler"
        elif num < 94:
            return "Super Rare Brawler"
        elif num < 97:
            return "Epic Brawler"
        elif num < 99:
            return "Mythic Brawler"
        else:
            return "Legendary Brawler"
        
    @commands.command(aliases=['open', 'box']
    async def boxsim(self, ctx):
        
        result = getResult()
        
        await ctx.send("Tap! Tap!")
        await ctx.send(result)