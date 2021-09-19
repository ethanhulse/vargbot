import discord
import random

class MyClient(discord.Client):


    #INIT
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_connect(self):
        print('[LOG] CONNECTING CLIENT...')

    async def on_ready(self):
        print('[LOG] CONNECTION READY...INITIALIZED')

    async def on_message(self,message):
        #USER ID CONSTANTS
        user_dok = "<@!577555388598190106>"
        user_jam = "<@!528000000978845716>"
        user_red = "<@!365335478175531009>"

        #WORDLISTS

        liBalls = ['balls']
        liGay = ['gay', 'Gay', 'GAY']
        liFloppa = ['floppa', 'FLOPPA', 'Floppa']
        liFat = ['Fat', 'FAT', 'fat']
        liWeed = ['weed', 'Weed', 'WEED', 'marijuana', 'Marijuana']
        liWeld = ['weld', 'welder', 'welding', 'arc', 'ark', 'noah']

        #URLLISTS
        uliFloppa = ['https://cali.rule34.xxx/thumbnails/4055/thumbnail_5a2c0d1fc3ce41cddd1482d77e39c2a3.jpg?4603099','https://imgur.com/WRcPHNH','https://cali.rule34.xxx/thumbnails/4055/thumbnail_5a2c0d1fc3ce41cddd1482d77e39c2a3.jpg?4603099','https://imgur.com/6AAPOsp','https://imgur.com/OLGP443','https://imgur.com/LlXHFsV','https://imgur.com/PbyWyAr','https://imgur.com/27RywPv','https://imgur.com/6I4zsOV','https://imgur.com/2PC4ydl','https://imgur.com/v5jgJ1z','https://imgur.com/Ibzahsa','https://imgur.com/MQLDXyU','https://imgur.com/s2rARGG','https://imgur.com/Jj1KLLy','https://imgur.com/iwYWX0S','https://imgur.com/lqYiune','https://imgur.com/5DFkPMH','https://imgur.com/7Ep9oN6','https://imgur.com/4cVncuK','https://imgur.com/h2Oq2d9','https://imgur.com/M1eCPQV','https://imgur.com/ra1J9OM','https://imgur.com/VWms8OO','https://imgur.com/9J9hNXp','https://imgur.com/sioyE1w','https://imgur.com/Psjlyag','https://imgur.com/XSQSBCo','https://imgur.com/XQRPy5Q','https://imgur.com/ZePobcq','https://imgur.com/qUCIjbd','https://imgur.com/flg72cP','https://imgur.com/0Dm058a','https://imgur.com/DUyf6Tk','https://imgur.com/uCcTYir','https://imgur.com/eBdNd6a','https://imgur.com/mkG7eCg','https://imgur.com/B3dDhsq','https://imgur.com/eCHzc20','https://imgur.com/KMo3uLx','https://imgur.com/yaTbhc9','https://imgur.com/TbL6Jgu','https://imgur.com/KMGedhz','https://imgur.com/6dvSYhm','https://imgur.com/xWDHOQr','https://imgur.com/GiSG7On','https://imgur.com/P99USsL','https://imgur.com/FUBTYTl','https://imgur.com/3MNLOvQ','https://imgur.com/Bfks4kL','https://imgur.com/pEG2HCq','https://imgur.com/kglROTR','https://imgur.com/7HbG6w4','https://imgur.com/nWUu5bG','https://imgur.com/kusSeFO','https://imgur.com/wOadUZV','https://imgur.com/18Eys1S','https://imgur.com/KOVwdTy','https://imgur.com/0EdQH8G','https://imgur.com/lf7rIh9','https://imgur.com/In4XzUI','https://imgur.com/yKfO08H','https://imgur.com/KDSlZ0K','https://imgur.com/tWzMeqd','https://imgur.com/tvNGpbZ','https://imgur.com/2Zf6ERl','https://imgur.com/p9ZQckq','https://imgur.com/0oudUD6','https://imgur.com/3tHCp7s','https://imgur.com/cEdzh3f','https://imgur.com/okmf6Vi','https://imgur.com/fjpZUUc','https://imgur.com/xrvdlAf','https://imgur.com/7T4aSCz','https://imgur.com/Wv7B8OG','https://imgur.com/AffViAH','https://imgur.com/sKWdmnG','https://imgur.com/iGu0yip','https://imgur.com/WAOqGd5','https://imgur.com/ajyqF5Z','https://imgur.com/X3LD4KL','https://imgur.com/M6F1Vnd','https://imgur.com/819eXRc','https://imgur.com/GQFQaCB','https://imgur.com/THLfdBi','https://imgur.com/Cpy34YK','https://imgur.com/meC5gMo','https://imgur.com/W6LMpPq','https://imgur.com/xyIWe6X','https://imgur.com/0wfJpvY','https://imgur.com/b3bL9di','https://imgur.com/ms65oWr','https://imgur.com/4X8zY3E','https://imgur.com/ZP39u9h','https://imgur.com/fncsF9x','https://imgur.com/USNYpNf','https://imgur.com/qxzCjLg','https://imgur.com/EXUjolr','https://imgur.com/abvErtf','https://imgur.com/XLxVtG2','https://imgur.com/VfbmLrE','https://imgur.com/SJGb2PR','https://imgur.com/Hj5WkPv','https://imgur.com/GBlmwFI','https://imgur.com/xhiIe0r','https://imgur.com/xhiIe0r','https://imgur.com/qLBuSQN','https://imgur.com/Sad5tQ7','https://imgur.com/MRwgpQS','https://imgur.com/YrSM1QA','https://imgur.com/1kbLJ70','https://imgur.com/wtm5HUB','https://imgur.com/l24TnsW','https://imgur.com/BypVBMq','https://imgur.com/obZvfz0','https://imgur.com/kPsRETx','https://imgur.com/m0FV63c','https://imgur.com/w48z0Tk','https://imgur.com/pRw6wKl','https://imgur.com/8ob0Vq4','https://imgur.com/zUwSwgX','https://imgur.com/XMmSli9','https://imgur.com/Od1zSh0','https://imgur.com/dOSK8Gg','https://imgur.com/3eJSNih','https://imgur.com/OvFNPtQ','https://imgur.com/QDHpzLd','https://imgur.com/UWbHqcG','https://imgur.com/wT8oyrg','https://imgur.com/6zHyyKU','https://imgur.com/P5OaaQ7','https://imgur.com/NoxUVwt','https://imgur.com/NwIO3lP','https://imgur.com/BHRXn2X','https://imgur.com/rkQUrW1','https://imgur.com/yl9a90q','https://imgur.com/u65fVlz','https://imgur.com/aoswZ6d','https://imgur.com/qPgCFZT','https://imgur.com/i5ZnFes','https://imgur.com/3ajeO0p','https://imgur.com/7UCJNpI','https://imgur.com/diV4PII','https://imgur.com/KXRNGuZ','https://imgur.com/8kizAsw','https://imgur.com/zXNUWDa','https://imgur.com/pCdVlt1','https://imgur.com/y2WZeqQ','https://imgur.com/AjOUOYC','https://imgur.com/oscfata','https://imgur.com/kJQ1mwz','https://imgur.com/VHdfRER','https://imgur.com/WgPtsOZ','https://imgur.com/fwusRnM','https://imgur.com/m2mjH1O','https://imgur.com/R5WcqFR','https://imgur.com/R5WcqFR','https://imgur.com/ftCpeC1','https://imgur.com/lViOp8A','https://imgur.com/P0PAlGX','https://imgur.com/AwP8x2Y','https://imgur.com/xRYkkhe','https://imgur.com/OJUMdNu','https://imgur.com/eImECNF','https://imgur.com/DZJUWjR','https://imgur.com/MV6tOCr','https://imgur.com/M4xNdRB','https://imgur.com/VxfvIQe','https://imgur.com/cR6iaiA','https://imgur.com/SPW3jje','https://imgur.com/SaVWexP','https://imgur.com/GPvZfzB','https://c.tenor.com/BFiftOdI5pMAAAAM/floppa-cat-floppacat.gif','https://c.tenor.com/RFmgfvXWOsAAAAAM/floppa-big-floppa.gif','https://c.tenor.com/1y6DManILSYAAAAM/diagnosis-issue-flop.gif','https://c.tenor.com/C6bksBcqSU8AAAAM/facebook-floppa-floppa.gif','https://c.tenor.com/bs_pdRDx888AAAAM/floppa-hahaahah-big-floppa.gif','https://c.tenor.com/fuaF6-5BYtQAAAAM/floppa-pet.gif','https://c.tenor.com/H7k7hRVjrAwAAAAM/sogga-pizzer-sogga.gif','https://c.tenor.com/KT_snB2eZA8AAAAM/floppa.gif','https://c.tenor.com/nkoK4ln-jeAAAAAM/brian-floppa.gif']
        #SINGLEURL
        urlArk = 'https://media.discordapp.net/attachments/850467633891508265/888331714361954346/image0.png'
        urlGay = 'https://www.quiztest.me/Uploads/imgQ//20210826/a53ab0d60d4a284f173e1dababe35959.jpg'
        urlForklift = 'http://twentywheels.com/imgs/a/b/s/j/r/yale_gdp040_forklift_lift_truck_hilo_fork__4__000lb__cat__full_cab_enclosure_3_lgw.jpg'
    
        #MESSAGE TAG AND RESPONSE FUNCTION

    

        #CHANNEL CONSTANTS
        channel_general = self.get_channel(850467633891508265)
        channel_floppa = self.get_channel(888931669518725140)
        
        #self msg check
        if message.author == self.user:
            return
        #self init
        messageContent = message.content
       
       #length check
        if len(messageContent) > 0:
            #main

            #FLOPPA

            for word in liFloppa:
                if word in messageContent:
                    await channel_floppa.send('Floppa Alert!' + user_dok)
                    await channel_floppa.send((random.choice(uliFloppa)))
                    print(messageContent)



            #END MAIN

client = MyClient()

client.run("OLD TOKEN")


    

    





























