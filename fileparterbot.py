from telethon.sync import TelegramClient 
from telethon import events
import os
from zipfile import ZipFile,ZIP_DEFLATED
from uuid import uuid4
from os import environ
globals().update(environ)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=TOKEN)

def absoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

async def zipper(filelist,name):
    with ZipFile(name, 'w') as zipMe:        
        for file in filelist:
            zipMe.write(file, compress_type=ZIP_DEFLATED)
    
   
async def unzipper(my_dir,my_zip)
    zip_file = ZipFile(my_zip, 'r')
    for files in zip_file.namelist():
        data = zip_file.read(files, my_dir)
        myfile_path = os.path.join(my_dir, files.split("/")[-1])
        myfile = open(myfile_path, "wb")
        myfile.write(data)
        myfile.close()
    zip_file.close()
   
   
async def hey(event):
    reply_message = await event.get_reply_message()
    await event.reply("Starting to part the files please wait...")
    name = await bot.download_media(reply_message,"./")
    dir = str(uuid4())
    os.mkdir(dir)
    await unzipper(dir,name)
    files = list(absoluteFilePaths(dir))
    n = 30
    k = [files[i:i + n] for i in range(0, len(files), n)]  
    ids = []
    for i in k:
        zipname = str(uuid4())+".zip"
        print(zipname)
        ids.append(zipname)
        await zipper(i,zipname)
    for id in ids:     
        await event.reply(file=id)
    os.system("rm -rf *")


        
print("---Started bot---")     
bot.add_event_handler(hey,events.NewMessage(pattern="/part"))
bot.run_until_disconnected()
