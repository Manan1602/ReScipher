import discord
import os
import csv
import time
ctf=[
  915500826791915520, #test
  915548589411950622,
  915548842584342529,
  915496956212686878, #citadel
  773227034981826580,
  915457967862722620,
  915458171043201094,
  915458629799407616,
  915458814462025758,
  915458902609494026,
  915459110684749834,
  915459193048297542,
  915459351282589726,
  915459462796574720,
  915459587858116668,
  915459676777365524,
  915459936639680603,
  915460022589329488,
  915460143716651028,
  915460420469424160,
  915460495044149310,
  915460580482105344,
  915460665144143913,
  915460798636240916,
  915460878097317930,
  915490478147911701,
  915490535874134077,
  915490725943210034,
  915490776740421662,
  915490947750563850,
  915491127149338624
]
client = discord.Client()
current_round=1
team_pos = {
  915500826791915520: 1,#test
  915548589411950622: 1,
  915548842584342529: 1,#/test
  915457967862722620: 1,
  915458171043201094: 1,
  915458629799407616: 1,
  915458814462025758: 1,
  915458902609494026: 1,
  915459110684749834: 1,
  915459193048297542: 1,
  915459351282589726: 1,
  915459462796574720: 1,
  915459587858116668: 1,
  915459676777365524: 1,
  915459936639680603: 1,
  915460022589329488: 1,
  915460143716651028: 1,
  915460420469424160: 1,
  915460495044149310: 1,
  915460580482105344: 1,
  915460665144143913: 1,
  915460798636240916: 1,
  915460878097317930: 1,
  915490478147911701: 1,
  915490535874134077: 1,
  915490725943210034: 1,
  915490776740421662: 1,
  915490947750563850: 1,
  915491127149338624: 1
}

answers = {
  1: '.andromeda',
  2: '.golden record',
  3: '.afronaut nkoloso',
  4: '.geminids meteor shower',
  5: '.pale blue dot',
  6: '.soyuz 9',
  7: '.note it down',
  8: '.dread it run from it destiny still arrives'
}

class MyClient(discord.Client):

  async def on_ready(self):
    print(f"We have logged in as {client.user}!")

  async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))
    # for channel in ctf.text_channels: # Get text channel
    #   text_channel_list.append(channel.name) # Append them to the list
    msg = message.content

    if message.channel.category_id in ctf:

      print('Channel Name - '+str(message.channel.category_id))
      print('')

      if message.channel.id == 915493953200087102:
        if msg=='.prologue':
          await message.channel.send(open('prologue.txt', 'r').read())
          time.sleep(0.3)
          #await ctx.send(f"\n".join(text_channel_list)
          await message.channel.send(open('question1.txt', 'r').read())

      if answers[team_pos[message.channel.category_id]] == msg:
        await message.channel.send('Correct Answer!!')
        time.sleep(0.3)
        if team_pos[message.channel.category_id] == 8:
          with open('Result.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow([str(message.channel.category).strip(),message.channel.id,time.strftime("%H:%M:%S", time.localtime())])
            q=open('epilogue.txt', 'r')
            await message.channel.send(q.read())
            q.close()
            
        else:
          time.sleep(0.3)
          team_pos[message.channel.category_id]+=1
          q=open('question'+str(team_pos[message.channel.category_id])+'.txt', 'r')
          await message.channel.send(q.read())
          q.close()
          if team_pos[message.channel.category_id] == 8:
            await message.channel.send(open('question9.txt', 'r').read())
      elif msg.startswith('.'):
        await message.channel.send('Wrong Answer!!')


      
client= MyClient()
client.run(os.environ['TOKEN'])