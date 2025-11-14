import discord
import time
import random
import os
import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix = "!")

############
# Settings #
############
token = "" # OBTAIN THROUGH ENV
bypassedUsers = ["", ""] # User IDs of Bypassed
footer = "Admin Bot"
footerImage = "<INSERT FOOTER IMAGE URL>"
botId = "<INSERT BOT ID>" # OR OBTAIN THROUGH ENV
verifyArrray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n" ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
youtubeChannelImage = ""
vouchers = []

@client.event
async def on_ready():
    #########
    # Setup #
    #########

    # Boot #
    ########
    print("Bot is ready.")
        
    
    
@client.event
async def on_message(msg):
    #########
    # Setup #
    #########

    # Basic #
    #########
    userId = msg.author.id
    contents = msg.content.split(" ")
    server = msg.channel.server
    
    # Roles #
    #########
    mutedRole = discord.utils.get(msg.server.roles, name = "Muted")
    developerRole = discord.utils.get(msg.server.roles, name = "Developer")
    ownerRole = discord.utils.get(msg.server.roles, name = "Owner")
    adminRole = discord.utils.get(msg.server.roles, name = "Administrator")
    buyerRole = discord.utils.get(msg.server.roles, name = "Buyer")
    

    # Channels #
    ############
    serverLogsChannel = discord.utils.get(msg.server.channels, name = "〖server-logs〗")
    rulesChannel = discord.utils.get(msg.server.channels, name = "〖rules〗")
    howToPurchaseChannel = discord.utils.get(msg.server.channels, name = "〖how-to-purchase〗")
    donationsChannel = discord.utils.get(msg.server.channels, name = "〖donations〗")
    helpDeskChannel = discord.utils.get(msg.server.channels, name = "〖help-desk〗")
    vouchesChannel = discord.utils.get(msg.server.channels, name = "〖vouches〗")
    
    
        
    # Commands that can be used by anyone in any channel #
    ######################################################
    
    if msg.content.lower().startswith("!display"):
        channel = msg.channel
        chooseUser = contents[1]
        chooseUser = chooseUser[2:len(chooseUser) - 1]
        specificId = chooseUser
        userAvatar = ""
        userAccountCreationDate = ""
        userRoles = []
        userStatus = ""
        userVouched = False
        try:
            chooseUser = server.get_member(chooseUser)
            userAvatar = chooseUser.avatar_url
            userAccountCreationDate = chooseUser.created_at
            userRoles = chooseUser.roles
            userStatus = chooseUser.status
        except:
            chooseUser = contents[1]
            chooseUser = chooseUser[3:len(chooseUser) - 1]
            specificId = chooseUser
            chooseUser = server.get_member(chooseUser)
            userAvatar = chooseUser.avatar_url
            userAccountCreationDate = chooseUser.created_at
            userRoles = chooseUser.roles
            userStatus = chooseUser.status
        userRolesString = ""
        for x in range(1, len(userRoles)):
            userRolesString = userRolesString + "**" + str(userRoles[x]) + "**"
            if x == len(userRoles) - 1:
                pass
            else:
                userRolesString = userRolesString + ", "

        if str(chooseUser.id) in vouchers:
            userVouched = True
        userAccountCreationDate = str(userAccountCreationDate)
        userAccountCreationDate = userAccountCreationDate[0:10]
        userAccountCreationDate = userAccountCreationDate[8:10] + userAccountCreationDate[7] + userAccountCreationDate[5:8] + userAccountCreationDate[0:4]
        if str(userStatus) == "dnd":
            userStatus = "do not disturb"
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_footer(text = footer)
        embed.add_field(name = "User", value = contents[1])
        embed.set_thumbnail(url = userAvatar)
        embed.add_field(name = "Creation Date", value = userAccountCreationDate)
        embed.add_field(name = "Roles", value = userRolesString)
        if userVouched == True:
            embed.add_field(name = "Vouched", value = "True")
        else:
            embed.add_field(name = "Vouched", value = "False")
        embed.add_field(name = "User ID", value = str(specificId))
        embed.add_field(name = "Status", value = str(userStatus))
        await client.send_message(channel, embed = embed)

    if msg.content.lower().startswith("!youtube"):
        channel = msg.channel
        embed = discord.Embed(colour = discord.Colour.red())
        embed.set_footer(text = footer)
        embed.add_field(name = "Youtube Channel", value = "[Link]: **<INSERT LINK HERE>**")
        embed.set_thumbnail(url = youtubeChannelImage)
        embed.add_field(name = "Description", value = "<INSERT QUICK DESCRIPTION HERE>")
        await client.send_message(channel, embed = embed)

    if msg.content.lower().startswith("!vouch"):
        channel = msg.channel
        if str(userId) in vouchers:
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Server Vouch", value = "<@%s> you can not vouch more than once" % (userId))
            await client.send_message(channel, embed = embed)
        else:
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            userVouchMessage = ""
            for x in range(1, len(contents)):
                userVouchMessage = userVouchMessage + contents[x] + " "
                
            embed.add_field(name = "Server Vouch", value = "```diff\n+ " + userVouchMessage + "```" + "\nfrom <@%s>" % (userId))
            vouchers.append(str(userId))
            await client.send_message(vouchesChannel, embed = embed)
        
        

        

    
    # Commands that can be used only by high ranks #
    ################################################
    if userId in bypassedUsers or ownerRole in msg.author.roles or developerRole in msg.author.roles or adminRole in msg.author.roles:
        if msg.content.lower().startswith("*kick"):
            channel = msg.channel
            embed = discord.Embed(colour = discord.Colour.red())
            kickUser = contents[1]
            kickUser = kickUser[2 : len(kickUser) - 1]
            kickUser = server.get_member(kickUser)
            embed.add_field(name = "Server Kick", value = contents[1] + " has been kicked by <@%s>" % (userId))
            embed.set_footer(text = footer)
            await client.kick(kickUser)
            await client.send_message(serverLogsChannel, embed = embed)

        if msg.content.lower().startswith("*ban"):
            channel = msg.channel
            embed = discord.Embed(colour = discord.Colour.red())
            banUser = contents[1]
            banUser = banUser[2:len(banUser) - 1]
            banUser = server.get_member(banUser)
            embed.add_field(name = "Server Ban", value = contents[1] + " has been banned by <@%s>" % (userId))
            embed.set_footer(text = footer)
            await client.ban(banUser)
            await client.send_message(serverLogsChannel, embed = embed)

        if msg.content.lower().startswith("*mute"):
            channel = msg.channel
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            muteUser = contents[1]
            muteUser = muteUser[2:len(muteUser) - 1]
            muteUser = server.get_member(muteUser)
            
            if mutedRole in muteUser.roles:
                embed.add_field(name = "Server Mute", value = contents[1] + " has already been muted")
                await client.send_message(serverLogsChannel, embed = embed)
            else:
                await client.add_roles(muteUser, mutedRole)
                embed.add_field(name = "Server Mute", value = contents[1] + " has been muted by <@%s>" % (userId))
                await client.send_message(serverLogsChannel, embed = embed)
                

        if msg.content.lower().startswith("*unmute"):
            channel = msg.channel
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            unmuteUser = contents[1]
            unmuteUser = unmuteUser[2:len(unmuteUser) - 1]
            unmuteUser = server.get_member(unmuteUser)

            if not mutedRole in unmuteUser.roles:
                embed.add_field(name = "Server Unmute", value = contents[1] + " is already not muted")
                await client.send_message(serverLogsChannel, embed = embed)
            else:
                await client.remove_roles(unmuteUser, mutedRole)
                embed.add_field(name = "Server Unmute", value = contents[1] + " has been unmuted by <@%s>" % (userId))
                await client.send_message(serverLogsChannel, embed = embed)


        if msg.content.lower().startswith("*purge"):
            channel = msg.channel
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            deleteAmount = 0
            try:
                deleteAmount = int(contents[1]) + 1
            except:
                deleteAmount = 100
            messagesTemp = []
            async for message in client.logs_from(channel, limit = deleteAmount):
                messagesTemp.append(message)
            embed.add_field(name = "Server Purge", value = channel.name + " has been purged by <@%s>" % (userId))
            await client.delete_messages(messagesTemp)
            await client.send_message(serverLogsChannel, embed = embed)

        if msg.content.lower().startswith("*welcome"):
            channel = msg.channel
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Welcome", value = "Hello reader, you are welcomed whether you are old or new. Go to #〖rules〗for the rules and simple help.")
            embed.set_image(url = footerImage)
            await client.send_message(channel, embed = embed)

        if msg.content.lower().startswith("*rules"):
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.set_image(url = footerImage)
            embed.add_field(name = "Overview", value = "These are the rules for the server. You are obliged to follow these rules or you will consequently face the punishments.")
            embed.add_field(name = "Rules", value = "\n<INSERT RULE HERE>")
            await client.send_message(rulesChannel, embed = embed)

        if msg.content.lower().startswith("*purchase"):
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Purchase", value = "There are 2 methods below on ways you can purchase our product.")
            embed.add_field(name = "Auto-Buy", value = "[Link]: <PURCHASE LINK>")
            embed.add_field(name = "Manual-Buy", value = "<INSERT DISCORD USER HERE> (DM me)")
            embed.set_image(url = footerImage)

            await client.send_message(howToPurchaseChannel, embed = embed)

        if msg.content.lower().startswith("*donation"):
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Donation", value = "To help support us you can donate via the links below.")
            embed.add_field(name = "Link", value = "[Paypal]: **<INSERT PAYPAL LINK>**\n\n[Note]:Please notify me via Discord of the Donation.")
            embed.add_field(name = "Rewards", value = "\n\n**£1** - Bronze Donator\n\n**£3** - Silver Donator\n\n**£5** - Gold Donator\n\n**£10** - Platinum Donator")
            embed.set_image(url = footerImage)

            await client.send_message(donationsChannel, embed = embed)
            
            
        if msg.content.lower().startswith("*helpdesk"):
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Help Desk", value = "Hello reader! The help desk's commands are listed below. Just type them into this channel and you should receive a reply instantly!")
            embed.add_field(name = "Commands", value = "\n\n**!Apply** - Apply for a rank within the server\n\n**!Shop** - Go to the Auto-buy area\n\n**!Info** - Get information on our product.")
            await client.send_message(helpDeskChannel, embed = embed)
        
       
    # Help Desk Only Commands #
    ###########################
    if msg.channel == helpDeskChannel:
        if msg.content.lower().startswith("!apply"):
            applyUser = await client.get_user_info(userId)
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Apply", value = "To apply please click the application form link below")
            embed.add_field(name = "Application Form", value = "[Link]: <INSERT FORM APP LINK HERE>")
            await client.send_message(applyUser, embed = embed)
            await client.add_reaction(msg, u"\u2709")

        if msg.content.lower().startswith("!shop"):
            shopUser = await client.get_user_info(userId)
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Shop", value = "To access the auto-buy shop click the link below")
            embed.add_field(name = "Selly.gg Shop", value = "[Link]: <INSERT SHOP LINK HERE>")
            await client.send_message(shopUser, embed = embed)
            await client.add_reaction(msg, u"\u2709")

        if msg.content.lower().startswith("!info"):
            infoUser = await client.get_user_info(userId)
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_footer(text = footer)
            embed.add_field(name = "Server Information", value = "This server is a community of discord users all in support of our product!")
            embed.add_field(name = "Product Information", value = "<INSERT PRODUCT INFORMATION HERE>")
            embed.set_image(url = footerImage)
            await client.send_message(infoUser, embed = embed)
            await client.add_reaction(msg, u"\u2709")

        if userId == botId:
            pass
        else:
            time.sleep(1)
            await client.delete_message(msg)
            
                
            
client.run(token)
