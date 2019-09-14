from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
#from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
#======================================================================================
botStart = time.time()
#======================================================================================
print ("\n\nคุณชายเจคนหล่อ\n❴✯ʟɪᴋᴇ•ʙʏ⁂❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶✯❵")
maxgie = LINE("")
maxgie.log("Auth Token : " + str(maxgie.authToken))
maxgie.log("Timeline Token : " + str(maxgie.tl.channelAccessToken))

waitOpen = codecs.open("Max2.json","r","utf-8")
settingsOpen = codecs.open("max.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
wait = json.load(waitOpen)
images = json.load(imagesOpen)
settings = json.load(settingsOpen)
stickers = json.load(stickersOpen)
#==============================================================================#
maxgieMID = maxgie.profile.mid
maxgieProfile = maxgie.getProfile()
maxgieSettings = maxgie.getSettings()
#==============================================================================#
maxgiePoll = OEPoll(maxgie)
maxgieMID = maxgie.getProfile().mid
admin = [maxgieMID]
loop = asyncio.get_event_loop()
listToken = ['desktopmac','desktopwin','iosipad','chromeos','win10']
mc = {"wr":{}}
unsendchat = {}
msgdikirim = {}
msg_image={}
msg_video={}
msg_sticker={}
wbanlist = []
msg_dict = {}
temp_flood = {}

#==============================================================================#
did = {"join": True,}
kcn = {"autojoin": False,"Members":5,}
sets = {
    "l":True, 
      "c":True, 
      "cm":"☑️ᴀᴜᴛᴏ‣ʟɪᴋᴇ•ʙʏ⁂❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶✳\n💟ติดต่อเช่าเซลบอทกดลิ้งด้านล่าง💟\n\n📱line://ti/p/~mj.ktc\n\n📱https://www.facebook.com/profile.php?id=100009178673186",  
    "winvite": False,
    "wblacklist": False,
    "tagsticker": False,
    "Sticker": False,
    "autoJoin": False,
    "autoCancel": False,
    "autoJoinTicket": False,
   "changePictureProfile": False, 
    "addSticker": {
        "name": "",
        "status": False,
    },
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "tag": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "lv": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "wc": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "add": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
            "join2": {
                "STKID": "",
                "STKPKGID": "",
                "STKVER": ""
            },
        }
    },
    "ilstpict": {},
}
chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}
nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}
tagadd = {
    "tagss": False,
    "tags": False,
    "tag": "แทคทำไมมีอะไรคิดถึงกูหรอนอนรอในห้องไป",
    "add": "ยินดีที่ได้รู้จักนะครับ 😃\nรับแอดละน้า. >_<",
    "wctext": "",
    "lv": "บ๊ายบาย >< ขอให้เธอโชคดีงับ >_<",
    "b": "บัญชีนี้ถูกป้องกันด้วย Self Bot By. ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶ ระบบได้บล็อคบัญชีคุณอัตโนมัติ >_<",
    "c":"☑️ᴀᴜᴛᴏ‣ʟɪᴋᴇ•ʙʏ⁂❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶✳\n💟ติดต่อเช่าเซลบอทกดลิ้งด้านล่าง💟\n\n📱line://ti/p/~mj.ktc\n\n📱https://www.facebook.com/profile.php?id=100009178673186",
    "m": "สวัสดีครับ ผมมุดลิ้งมานะครับ >_<",
}
apalo = {
    "winvite": False,
    "wblacklist": False,
    "blacklist":{},
    "Talkblacklist": {},
    "talkban": True,
    "Talkwblacklist": False,
    "Talkdblacklist": False,
}
temp = {"te": "#CC0033","t": "#000000"}
read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}
rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

ProfileMe = {
    "coverId": "",
    "statusMessage": "",
    "PictureMe": "",
    "NameMe": "",
}
peler = { 
    "receivercount": 0,
    "sendcount": 0
}
hoho = {
    "savefile": False,
    "namefile": "",
}

user1 = maxgieMID
user2 = ""

setTime = {}
setTime = rfuSet['setTime']

contact = maxgie.getProfile() 
backup = maxgie.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time()
Start = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

settings["myProfile"]["displayName"] = maxgieProfile.displayName
settings["myProfile"]["statusMessage"] = maxgieProfile.statusMessage
settings["myProfile"]["pictureStatus"] = maxgieProfile.pictureStatus
cont = maxgie.getContact(maxgieMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = maxgie.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["statusMessage"] = maxgieProfile.statusMessage
ProfileMe["pictureStatus"] = maxgieProfile.pictureStatus
coverId = maxgie.getProfileDetail()["result"]["objectId"]
ProfileMe["coverId"] = coverId
#=====================================================================
with open("max.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("Max2.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
Notify = "ucf71b8c1b067423f8ebefbfe6ae0ccc3"
maxgie.findAndAddContactsByMid(Notify)
maxgie.sendMessage(Notify,"เข้าสู่ระบบสำเร็จ")
lgncall = ""
keyword = {}
try:
    with open('keyword.json', 'r',encoding="utf_8_sig") as fpsave:
        keyword = json.load(fpsave)
    print("file keyword Go!!!")
except:
    print("Couldn't file keyword")

#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Ma '
        maxgie.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    maxgie.sendMessage(to, '', annda, 13)
def cloneProfile(mid):
    contact = maxgie.getContact(mid)
    if contact.videoProfile == None:
        maxgie.cloneContactProfile(mid)
    else:
        profile = maxgie.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = maxgie.getProfileDetail(mid)['result']['objectId']
    maxgie.updateProfileCoverById(coverId)
def backupProfile():
    profile = maxgie.getContact(maxgieMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = maxgie.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = maxgie.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        maxgie.updateProfileAttribute(8, profile.pictureStatus)
        maxgie.updateProfile(profile)
    else:
        maxgie.updateProfile(profile)
        pict = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = maxgie.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    maxgie.updateProfileCoverById(coverId)
def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        maxgie.sendMessage(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = maxgie.getGroup(msg.to).name
    sd = maxgie.waktunjir()
    maxgie.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def ClonerV2(to):
    try:
        contact = maxgie.getContact(to)
        profile = maxgie.profile
        profileName = maxgie.profile
        profileStatus = maxgie.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        maxgie.updateProfile(profileName)
        maxgie.updateProfile(profileStatus)
        profile.pictureStatus = maxgie.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if maxgie.getProfileCoverId(to) is not None:
            maxgie.updateProfileCoverById(maxgie.getProfileCoverId(to))
        maxgie.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return maxgie.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        maxgie.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
        
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(maxgie.getContact(maxgieMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus)
        ticket = "https://line.me/ti/p/~topzalove123"
        maxgie.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def ggggg(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d วัน\n───────────\n%02d ชั่วโมง\n───────────\n%02d นาที\n───────────\n' %(days ,hours, mins)
    
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@"
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    maxgie.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(maxgie.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + maxgie.getContact("ua053fcd4c52917706ae60c811e39d3ea").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = maxgie.genOBSParams({'oid': maxgieMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = maxgie.server.postContent('{}/talk/vp/upload.nhn'.format(str(maxgie.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        maxgie.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = maxgie.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def NOTIFIED_READ_MESSAGE(op):
    try:
        if read['readPoint'][op.param1]:
            if op.param2 in read['readMember'][op.param1]:
                pass
            else:
                read['readMember'][op.param1][op.param2] = True
                read['ROM'][op.param1] = op.param2
        else:
            pass
    except:
        pass
def logError(text):
    maxgie.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType,mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        maxgie.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def mentionMembers(to, mid):
    try:
        group = maxgie.getGroup(to)
        mids = [mem.mid for mem in group.members]
        jml = len(mids)
        arrData = ""
        if mid[0] == mids[0]:
            textx = ""
        else:
            textx = ""
        arr = []
        for i in mid:
            no = mids.index(i) + 1
            textx += "{}.".format(str(no))
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
        if no == jml:
            textx += ""
            textx += ""
        maxgie.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        maxgie.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def restartBot():
    print ("RESETBOT..")
    python = sys.executable
    os.execl(python, python, *sys.argv)
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
#    with open("stickerz.json","r") as fp:
#        stickerz = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': maxgie.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + maxgie.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    maxgie.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            maxgie.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
def removeCmd(cmd, text):
    key = settings["keyCommand"]
    if settings["setKey"] == False: key = ''  
    rmv = len(key + cmd) + 1
    return text[rmv:]
def duc1(to, duc1):
    data={
"type": "flex",
"altText": duc1,
"contents": {
"type": "bubble",
"styles": {
"footer": {"backgroundColor": "#FFFF00"},
},
"footer": {
"type": "box",
"layout": "vertical",
"spacing": "sm",
"contents": [
{
"type": "box",
"layout": "baseline",
"contents": [
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"size": "md"
},
{
"type": "text",
"text": duc1,
"color":"#000000",
"gravity": "center",
"align":"center",
"wrap": True,
"size": "md"
},
{
"type": "icon",
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"size": "md"
},
]
}
]
}
}
}
    sendTemplate(to, data)
#=====================================================================
#========================================================================
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('max.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('Max2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
async def maxgieBot(op):
    try:
        if settings["restartPoint"] != None:
            maxgie.sendMessage(settings["restartPoint"], 'ล็อคอินแล้วเรียบร้อย ><')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
             # if op.param2 in admin:
                 # return
              maxgie.findAndAddContactsByMid(op.param1)
              maxgie.sendMessage(op.param1,"{}".format(tagadd["add"]))
              msgSticker = sets["messageSticker"]["listSticker"]["add"]
              if msgSticker != None:
                  sid = msgSticker["STKID"]
                  spkg = msgSticker["STKPKGID"]
                  sver = msgSticker["STKVER"]
                  sendSticker(op.param1, sver, spkg, sid)
              print ("[ 5 ] AUTO ADD")
        if op.type == 5:
            if settings["autoblock"] == True:
                maxgie.blockContact(op.param1)   
                time.sleep(0.0001)
                maxgie.sendMessage(Notify,"มีคนแอดตัวนี้มา  contact ด้านล่างนี้เลย")
                time.sleep(0.0001)
                maxgie.sendMessage(Notify, None, contentMetadata={'mid': op.param1}, contentType=13)
                time.sleep(0.0001)
                maxgie.sendMessage(op.param1,tagadd["b"])
                maxgie.blockContact(op.param1)
                print ("[ 5 ] AUTO BLOCK")              
        if op.type == 13:
            if settings["spamGroup"] == True:
                group = maxgie.getGroup(op.param1)
                group.members = [] if not group.members else group.members
                if len(group.members) <= 4:
                    maxgie.acceptGroupInvitation(op.param1)
                    time.sleep(random.uniform(0.001,5))
                    maxgie.leaveGroup(op.param1)                      
        if op.type == 13:
         if kcn["autojoin"] == True:
             G = maxgie.getCompactGroup(op.param1)
             if len(G.members) <= kcn["Members"]:
                 maxgie.acceptGroupInvitation(op.param1)
                 maxgie.leaveGroup(op.param1)               	
             else:
                 maxgie.acceptGroupInvitation(op.param1)
                 
        if op.type == 13:
            if maxgieMID in op.param3:
                G = maxgie.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            maxgie.acceptGroupInvitation(op.param1)
                        else:
                            maxgie.leaveGroup(op.param1)
                    else:
                        maxgie.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        maxgie.acceptGroupInvitation(op.param1)
                        maxgie.leaveGroup(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in apalo["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    maxgie.acceptGroupInvitation(op.param1, matched_list)
                    maxgie.leaveGroup(op.param1, matched_list)
                    print ("[ 17 ] LEAVE GROUP")
        if op.type == 15:
          if settings["Leave"] == True:
            if op.param2 in admin:
                return
            g = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            cover = maxgie.getProfileCoverURL(op.param2)
            gname = g.name
            name = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            s = ""
            s += "".format(gname)
            s += "บายยน้า : {}".format(name)
            s += tagadd["wctext"]
            data = {
"type":"flex","altText":" 🐯 มีคนสวยออกกลุ่ม 🐯 ","contents":{"styles":{"header":{"backgroundColor":"#990000","separator":True,"separatorColor":"#FFFFFF"},"body":{"backgroundColor":"#000000","separator":True,"separatorColor":"#FFFFFF"},"footer":{"backgroundColor":"#990000","separator":True,"separatorColor":"#FFFFFF"}},"type":"bubble","header":{"type":"box","layout":"horizontal","contents":[{"type":"button","style":"secondary","color":"#FFFFFF","height":"sm","gravity":"center","flex":1,"action":{"type":"uri","label":"⫷BOTLNEBY:❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶⫸","uri":"line://nv/profilePopup/mid=u7ff3c8f1829ee9fbb7684294b51345e6"}}]},"hero":{"type":"image","url":"https://thumbs.gfycat.com/ColorlessPinkLangur-size_restricted.gif","size":"full","aspectRatio":"4:3","action":{"type":"uri","uri":"http://nav.cx/8OFQLI4"}},"body":{"type":"box","layout":"horizontal","spacing":"md","contents":[{"type":"separator","color":"#FFFFFF"},{"type":"box","layout":"vertical","flex":0,"contents":[{"type":"separator","color":"#FFFFFF"},{"type":"image","url":"https://profile.line-scdn.net/" + str(pp),"size":"sm","gravity":"bottom"}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","layout":"vertical","flex":2,"contents":[{"type":"text","text":"BOTLINE:❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶","color":"#FFCC00","size":"sm","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","color":"#FFFFFF"},{"type":"separator","color":"#FFFFFF"},{"type":"text","text": "{}".format(s),"color":"#FFCC00","size":"sm","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","color":"#FFFFFF"},{"type":"separator","color":"#FFFFFF"},{"type":"text","text":"ออกสะแล้วบายยนะครับ😎","color":"#FFCC00","size":"sm","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","color":"#FFFFFF"}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","style":"secondary","color":"#FFFFFF","height":"sm","gravity":"center","flex":1,"action":{"type":"uri","label":"⫷ ติดต่อผู้สร้าง ⫸","uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37"}},{"type":"spacer","size":"sm"}],"flex":0}}}
            sendTemplate(op.param1, data)
        if op.type == 15:
          if settings["lv"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["lv"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Welcome"] == True:
            if op.param2 in admin:
                return
            g = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            cover = maxgie.getProfileCoverURL(op.param2)
            gname = g.name
            name = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            s = ""
            s += "".format(gname)
            s += "สวัสดีครับคุณ : {}".format(name)
            s += tagadd["wctext"]
            data = {
"type":"flex","altText":" 🐯  มีคนเข้ากลุ่ม  🐯 ","contents":{"styles":{"header":{"backgroundColor":"#990000","separator":True,"separatorColor":"#FFFFFF"},"body":{"backgroundColor":"#000000","separator":True,"separatorColor":"#FFFFFF"},"footer":{"backgroundColor":"#990000","separator":True,"separatorColor":"#FFFFFF"}},"type":"bubble","header":{"type":"box","layout":"horizontal","contents":[{"type":"button","style":"secondary","color":"#FFFFFF","height":"sm","gravity":"center","flex":1,"action":{"type":"uri","label":"⫷❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶⫸","uri":"line://nv/profilePopup/mid=u7ff3c8f1829ee9fbb7684294b51345e6"}}]},"hero":{"type":"image","url":"https://media.giphy.com/media/MG1B6RPKn8OLC/giphy.gif","size":"full","aspectRatio":"4:3","action":{"type":"uri","uri":"http://nav.cx/8OFQLI4"}},"body":{"type":"box","layout":"horizontal","spacing":"md","contents":[{"type":"separator","color":"#FFFFFF"},{"type":"box","layout":"vertical","flex":0,"contents":[{"type":"separator","color":"#FFFFFF"},{"type":"image","url":"https://profile.line-scdn.net/" + str(pp),"size":"sm","gravity":"bottom"}]},{"type":"separator","color":"#FFFFFF"},{"type":"box","layout":"vertical","flex":2,"contents":[{"type":"text","text":"BOTLINE:❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶","color":"#FFCC00","size":"sm","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","color":"#FFFFFF"},{"type":"separator","color":"#FFFFFF"},{"type":"text","text": "{}".format(s),"color":"#FFCC00","size":"sm","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","color":"#FFFFFF"},{"type":"separator","color":"#FFFFFF"},{"type":"text","text":"ยินดีต้อนรับเข้ารวมกลุ่มนะครับ😎","color":"#FFCC00","size":"sm","weight":"bold","flex":3,"wrap":True,"gravity":"top"},{"type":"separator","color":"#FFFFFF"}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","style":"secondary","color":"#FFFFFF","height":"sm","gravity":"center","flex":1,"action":{"type":"uri","label":"⫷ ติดต่อผู้สร้าง ⫸","uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",}},{"type":"spacer","size":"sm"}],"flex":0}}}
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = maxgie.getGroup(op.param1)
            contact = maxgie.getContact(op.param2)
            cover = maxgie.getProfileCoverURL(op.param2)
            names = contact.displayName
            status = contact.statusMessage
            pp = contact.pictureStatus
            data = {
                "type": "flex",
                "altText": "มีคนเข้ากลุ่ม",
                "contents": {
                    "type": "bubble",
                    'styles': {
                        "body": {
                            "backgroundColor": '#EE1289'
                        },
                     },
                     "hero": {
                         "type":"image",
                         "url": cover,
                         "size":"full",
                         "aspectRatio":"20:13",
                         "aspectMode":"cover"
                     },
                     "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                             {
                                 "type": "image",
                                 "url": "https://profile.line-scdn.net/" + str(pp),
                                 "size": "lg"
                             },
                             {
                                 "type":"text",
                                 "text":" "
                             },
                             {
                                 "type":"text",
                                 "text":"{}".format(names),
                                 "size":"xl",
                                 "weight":"bold",
                                 "color":"#00F5FF",
                                 "align":"center"
                             },
                             {
                                 "type": "text",
                                 "text": status,
                                 "wrap": True,
                                 "align": "center",
                                 "gravity": "center",
                                 "color": "#00F5FF",
                                 "size": "md"
                            },
                        ]
                    }
                }
            }
            sendTemplate(op.param1, data)
        if op.type == 17:
          if settings["wcsti2"] == True:
              ginfo = maxgie.getGroup(op.param1)
              msg = sets["messageSticker"]["listSticker"]["wc"]
              if msg != None:
                  contact = maxgie.getContact(maxgieMID)
                  a = contact.displayName
                  stk = msg['STKID']
                  spk = msg['STKPKGID']
                  data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                  sendTemplate(op.param1, data)
#=====================================================================
       # if op.type == 26:
         #   print ("[ 26 ] RECEIVE MESSAGE")
         #   msg = op.message
         #   text = str(msg.text)
         #   msg_id = msg.id
         #   receiver = msg.to
         #   sender = msg._from
         #   cmd = command(text)
         #   setKey = settings["keyCommand"].title()
         #   if settings["setKey"] == False: setKey = ""
         #   isValid = True
         #   if isValid != False:
               # if msg.toType == 0 and sender != maxgieMID: to = sender
               # else: to = receiver
               # if msg.toType == 0 and settings["replays"] and sender != maxgieMID:
                   # contact = maxgie.getContact(sender)
                    #if contact.attributes != 32 and "[ auto reply ]" not in text.lower():
                     #   msgSticker = sets["messageSticker"]["listSticker"]["replay"]
                     #   if msgSticker != None:
                     #       sid = msgSticker["STKID"]
                     #       spkg = msgSticker["STKPKGID"]
                     #       sver = msgSticker["STKVER"]
                     #       sendSticker(to, sver, spkg, sid)
                     #   if "@!" in settings["reply"]:
                     #       msg_ = settings["reply"].split("@!")
                     #       sendMention(to, sender, "「 แทคส่วนตัว 」\n" + msg_[0], msg_[1])
                     #   maxgie.sendMessage(to, "「 แทคส่วนตัว 」\n", settings["reply"])
                     
        if op.type == 24:
            if settings["autoLeave"] == True:
                maxgie.leaveRoom(op.param1)                      
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if apalo["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = maxgie.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 maxgie.sendMessage(msg.to,"-> " + _name + " ทำการเชิญสำเร็จ")
                                 break
                             elif invite in apalo["blacklist"]:
                                 maxgie.sendMessage(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 maxgie.sendMessage(msg.to,"ใช้คำสั่ง!,ล้างดำ,ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     maxgie.findAndAddContactsByMid(target)
                                     maxgie.inviteIntoGroup(msg.to,[target])
                                     maxgie.sendMessage(msg.to,"เชิญ :" + _name + "เรียบร้อย")
                                     apalo["winvite"] = False
                                     break
                                 except:
                                     try:
                                         maxgie.findAndAddContactsByMid(invite)
                                         maxgie.inviteIntoGroup(op.param1,[invite])
                                         apalo["winvite"] = False
                                     except:
                                         maxgie.sendMessage(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         apalo["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [maxgieMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg._from not in maxgieMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        maxgie.sendMention(to, "คุณติดดำผมอยู่นะครับ @! :)","",[msg._from])
                        maxgie.kickoutFromGroup(msg.to, [msg._from])
                if msg.contentType == 13:
                  if apalo["Talkwblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          maxgie.sendMessage(msg.to,"Sudah Ada")
                          apalo["Talkwblacklist"] = False
                      else:
                          apalo["Talkblacklist"][msg.contentMetadata["mid"]] = True
                          apalo["Talkwblacklist"] = False
                          maxgie.unsendMessage(msg_id)
                          duc1(to, "🌟เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว🌟")
                  if apalo["Talkdblacklist"] == True:
                    if msg._from in admin:
                      if msg.contentMetadata["mid"] in apalo["Talkblacklist"]:
                          del apalo["Talkblacklist"][msg.contentMetadata["mid"]]
                          maxgie.unsendMessage(msg_id)
                          duc1(to, "🌟เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว🌟")
                          apalo["Talkdblacklist"] = False
                      else:
                          apalo["Talkdblacklist"] = False
                          maxgie.sendMessage(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
        if op.type in [25,26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 16:
                    if msg.toType in [2,1,0]:
                        try:
                            if sets["l"] == True:
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                duc1(to,"💠ไลค์ให้แล้วนะน้องๆ💠")
                                if purl[1] not in wait['postId']:
                                    maxgie.likePost(purl[0], purl[1], random.choice([1001]))
                                if sets["c"] == True:
                                    maxgie.createComment(purl[0], purl[1], sets["cm"])
                                    wait['postId'].append(purl[1])
                                else:
                                    pass
                        except Exception as e:
                                if sets["l"] == True:
                                    purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                    duc1(to,"💠ไลค์ให้แล้วนะน้องๆ💠")
                                    if purl[1] not in wait['postId']:
                                        maxgie.likePost(msg._from, purl[1], random.choice([1001]))
                                    if sets["c"] == True:
                                        maxgie.createComment(msg._from, purl[1], sets["cm"])
                                        wait['postId'].append(purl[1])
                                    else:pass
              
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "ประกาศ":
                    sa="วิธีใช้ ประกาศกลุ่ม >\\<"
                    sa+="\n- ประกาศ ข้อความ/ไอดีไลน์"
                    sa+="\nตัวอย่าง >\\<"
                    sa+="\n- ประกาศ มอนิ่ง/nonbysignal"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~@622zdvow"}}
                    sendTemplate(to,data)
                if text.lower() == "ตั้งapi":
                    sa = "วีธีใช้ api >\\<"
                    sa += "\n- ตั้งapi คีย์เวิร์ด;;ตอบกลับ"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ตั้งapi เทส;;เทสทำไม"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶ ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~@622zdvow"}}
                    sendTemplate(to,data)
                if text.lower() == "ทัก":
                    sa = "วิธีใช้ ทัก >\\<"
                    sa += "\n- ทัก [เลขที่ต้องการ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- ทัก 1 @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~@622zdvow"}}
                    sendTemplate(to,data)
                if text.lower() == "สะกด":
                    sa = "วิธีใช้ สะกด >\\<"
                    sa += "\n- สะกดกิต [ข้อความ] @user"
                    sa += "\nตัวอย่าง >\\<"
                    sa += "\n- สะกด รักทอป @user"
                    data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶ ", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~@622zdvow"}}
                    sendTemplate(to,data)
                if text.lower() == "เชคค่า" or text.lower() == "set":
                    sas = "☆ Settings ☆"
                    if settings["autoAdd"] == True: sa = "\n• ออโต้แอด ( เปิด )"
                    else:sa = "\n• ออโต้แอด ( ปิด )"
                    if settings["autoblock"] == True: sa += "\n• ออโต้บล็อค ( เปิด )"
                    else:sa += "\n• ออโต้บล็อค ( ปิด )"
                    if settings["autoCancel"]["on"] == True: sa +="\n• ยกเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"])
                    else:sa += "\n• ปฏิเสธกลุ่มเชิญ ( ปิด )"
                    if tagadd["tags"] == True: sa += "\n• ตอบกลับคนแทค ( เปิด )"
                    else:sa += "\n• ตอบกลับคนแทค ( ปิด )"
                    if tagadd["tagss"] == True: sa += "\n• ตอบกลับคนแทค2 ( เปิด )"
                    else:sa += "\n• ตอบกลับคนแทค2 ( ปิด )"
                    if sets["tagsticker"] == True: sa += "\n• แทคสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n• แทคสติ๊กเกอร์ ( ปิด )"
                    if settings["autolike"] == True: sa += "\n• ออโต้ไลค์ ( เปิด )"
                    else:sa += "\n• ออโต้ไลค์ ( ปิด )"
                    if settings["com"] == True: sa += "\n• คอมเม้นโพส ( เปิด )"
                    else:sa += "\n• คอมเม้นโพส ( ปิด )"
                    if settings["Welcome"] == True: sa += "\n• ต้อนรับคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n• ต้อนรับคนเข้ากลุ่ม ( ปิด )"
                    if settings["Wc"] == True: sa += "\n• ต้อนรับคนเข้ากลุ่ม2 ( เปิด )"
                    else:sa += "\n• ต้อนรับคนเข้ากลุ่ม2 ( ปิด )"
                    if settings["wcsti2"] == True: sa += "\n• ติ๊กคนเข้ากลุ่ม ( เปิด )"
                    else:sa += "\n• ติ๊กคนเข้ากลุ่ม ( ปิด )"
                    if settings["Leave"] == True: sa += "\n• คนออกกลุ่ม ( เปิด )"
                    else:sa += "\n• คนออกกลุ่ม ( ปิด )"
                    if settings["lv"] == True: sa += "\n• ติ๊กคนออกกลุ่ม ( เปิด )"
                    else:sa += "\n• ติ๊กคนออกกลุ่ม ( ปิด )"
                    if settings["unsendMessage"] == True: sa += "\n• ตรวจจับยกเลิก ( เปิด )"
                    else:sa += "\n• ตรวจจับยกเลิก ( ปิด )"
                    if settings["Sticker"] == True: sa += "\n• เชคติ๊กใหญ่ ( เปิด )"
                    else:sa += "\n• เชคติ๊กใหญ่ ( ปิด )"
                    if sets["Sticker"] == True: sa += "\n• เชคโค๊ดสติ๊กเกอร์ ( เปิด )"
                    else:sa += "\n• เชคโค๊ดสติ๊กเกอร์ ( ปิด )"
                    
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#EE1289'
                                },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": sas,
                                        "color": "#00F5FF",
                                        "align": "center",
                                        "weight": "bold",
                                        "size": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#00F5FF",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == 'cb' or text.lower() == "ล้างดำ":
                      apalo["Talkblacklist"] = []
                      duc1(to, "🌟สำเร็จ🌟")
                
                elif text.lower() == "bc":
                    if msg._from in maxgieMID:
                        if apalo["Talkblacklist"] == []:
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "🌟ไม่มีคท.คนติดดำ🌟")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                maxgie.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
                elif text.lower() == "เตะดำ":
                    if msg.toType == 2:
                        groupMemberMids = [contact.mid for contact in maxgie.getGroup(to).members]
                        matched_list = []
                        for mid in apalo["Talkblacklist"]:
                            matched_list += [x for x in groupMemberMids if x == mid]
                        if matched_list == []:
                            duc1(to, "🌟ไม่มีหมาดำ🌟")
                        else:
                            for mids in matched_list:
                                try:
                                    maxgie.kickoutFromGroup(to, [mids])
                                except:pass
                
                elif "Kick " in msg.text:
                    Ri0 = text.replace("kick ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                except:
                                    pass                              
                              
                elif "ล้อเล่น " in msg.text:
                    Ri0 = text.replace("ล้อเล่น ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = maxgie.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    maxgie.kickoutFromGroup(to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    maxgie.inviteIntoGroup(to,[target])
                                except:
                                    pass
                
                elif "เตะ " in msg.text:
                        vkick0 = msg.text.replace("เตะ ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = maxgie.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    maxgie.kickoutFromGroup(msg.to,[target])
                                    maxgie.findAndAddContactsByMid(target)
                                    maxgie.inviteIntoGroup(msg.to,[target])
                                    maxgie.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass            
                elif msg.text.lower().startswith("สีme "):
                            text_ = removeCmd("สีme", text)
                            try:
                                temp["t"] = text_
                                maxgie.sendMessage(to,"「 โค๊ดสี 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("สีอักษร "):
                            text_ = removeCmd("สีอักษร", text)
                            try:
                                temp["te"] = text_
                                maxgie.sendMessage(to,"「 โค๊ดสี 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower() == "รหัสสี":
                            c="https://i.pinimg.com/originals/d0/9c/8a/d09c8ad110eb44532825df454085a376.jpg"
                            p="https://i.pinimg.com/originals/7c/d3/aa/7cd3aa57150f8f6f18711ff22c9f6d4a.jpg"
                            m="**ตัวอย่างที่1**\nคำสั่งเปลี่ยนสี me\nพิม'ตั้งสีme #333333'\n**ตัวอย่างที่2**\nคำสั่งเปลี่ยนสี tag\nพิม'ตั้งสีแทค #333333'"
                            maxgie.sendImageWithURL(to,c)
                            maxgie.sendImageWithURL(to,p)
                            maxgie.sendMessage(to,m)
                elif msg.text.lower().startswith("ตั้งบล็อค "):
                            text_ = removeCmd("ตั้งบล็อค", text)
                            try:
                                tagadd["b"] = text_
                                maxgie.sendMessage(to,"「 ตั้งบล็อคอัตโนมัติ 」\nคือ : " + text_)
                            except:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟สำเร็จแล้ววว🌟")
                elif text.lower().startswith("ตั้งค้างเชิญ "):
                            text_ = removeCmd("ตั้งค้างเชิญ", text)
                            try:
                                settings["autoCancel"]["members"] = text_
                                maxgie.sendMessage(to,"「 ตั้งยกค้างเชิญ 」\nจำนวน : " + text_)
                            except:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟สำเร็จแล้ววว🌟")
                if text.lower() == "ดำ":
                  if msg._from in admin:
                      apalo["Talkwblacklist"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟ส่งคทลงมา...🌟")
                if text.lower() == "ขาว":
                  if msg._from in admin:
                      apalo["Talkdblacklist"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟ส่งคทลงมา...🌟")
                elif msg.text.lower().startswith("ตั้งแทค "):
                      text_ = removeCmd("ตั้งแทค", text)
                      try:
                          tagadd["tag"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งแทคแชท "):
                      text_ = removeCmd("ตั้งแทคแชท", text)
                      try:
                          settings["reply"] = text_
                          sa = "「 ตั้งคำแทค 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessage(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งต้อนรับ "):
                      text_ = removeCmd("ตั้งต้อนรับ", text)
                      try:
                          tagadd["wctext"] = text_
                          sa = "「 ตั้งต้อนรับ 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": " ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคนออก "):
                            text_ = removeCmd("ตั้งคนออก", text)
                            try:
                                tagadd["lv"] = text_
                                maxgie.sendMessage(to,"「 ตั้งคนออก 」\nคือ : " + text_)
                            except:
                                maxgie.sendMessage(to,"สำเเร็จแล้ว")
                elif msg.text.lower().startswith("ตั้งแอด "):
                      text_ = removeCmd("ตั้งแอด", text)
                      try:
                          tagadd["add"] = text_
                          sa = "「 ตั้งแอด 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower().startswith("ตั้งคอมเม้น "):
                      text_ = removeCmd("ตั้งคอมเม้น", text)
                      try:
                          settings["commet"] = text_
                          sa = "「 ตั้งคอมเม้น 」\nคือ : " + text_
                          data = {"type": "text","text": "{}".format(sa),"sentBy": {"label": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"}}
                          sendTemplate(to,data)
                      except:
                          maxgie.sendMessags(to,"Done. >_<")
                elif msg.text.lower() == "ทัก":
                  if msg.toType == 0:
                     sendMention(to, to, "──┅••••••••●✦͜͡✾͜͡✦●••••••••┅──\n", "\n──┅••••••••●✦͜͡✾͜͡✦●••••••••┅──")
                  elif msg.toType == 2:
                     group = maxgie.getGroup(to)
                     contact = [mem.mid for mem in group.members]
                     mentionMembers(to, contact)       
                if text.lower() == "เชค":
                    add = tagadd["add"]
                    tag = tagadd["tag"]
                    like = settings["commet"]
                    wc = tagadd["wctext"]
                    lv = tagadd["lv"]
                    c = settings["autoCancel"]["members"]
                    b = tagadd["b"]
                    Re = settings["reply"]
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendMessags(id, to, "ข้อความแอด :\n"+str(add)+"\n\nข้อความแทค :\n"+str(tag)+"\n\nข้อความเม้น :\n"+str(like)+"\n\nข้อความต้อนรับ :\n"+str(wc)+"\n\nข้อความคนออก :\n"+str(lv)+"\n\nจำนวนค้างเชิญ :\n"+str(c)+" จำนวน\n\nข้อความบล็อค :\n"+str(b)+"\n\nข้อความแทคแชท :\n"+str(Re))
                if text.lower() == "/คำสั่ง" or text.lower() == "/help":
                    sas = "😀 โหมดคำสั่ง😀\n"
                    sa = "• คท\n"
                    sa += "• ไอดีเรา\n"
                    sa += "• ชื่อเรา\n"
                    sa += "• ตัสเรา\n"
                    sa += "• รูปเรา\n"
                    sa += "• รูปวีดีโอเรา\n"
                    sa += "• ปกเรา\n"
                    sa += "──────────────\n"
                    sa += "• ข้อมูล\n"
                    sa += "• ออน\n"
                    sa += "• รีบอท\n"
                    sa += "• แทค\n"
                    sa += "• ยกเชิญ\n"
                    sa += "• /ลบรัน\n"
                    sa += "• ก็อป @user\n"
                    sa += "• กลับร่าง\n"
                    sa += "──────────────\n"
                    sa += "• สะกดกิต [พิม'สะกดกิต'เพื่อดูวิธี]\n"
                    sa += "• ตั้งapi [พิมเพื่อดูวิธี]\n"
                    sa += "• ล้างapi [คำที่จะลบ]\n"
                    sa += "• เชคapi\n"
                    sa += "• ทัก [พิม'stag'เพื่อดูวิธี]\n"
                    sa += "• แปรงคท [MID]\n"
                    sa += "• ยูทูป [ข้อความ]\n"
                    sa += "• image [text(ภาษาอังกฤษ)]\n"
                    sa += "• รูป [ข้อความ(ภาษาไทย)]\n"
                    sa += "• เพลสโต [ชื่อแอพ]\n"
                    sa += "• ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                    sa += "• ประกาศ [พิม'ประกาศ'เพื่อดูวิธี]\n"
                    sa += "• /ยก [ยกเลิกข้อความ]\n"
                    sa += "──────────────\n"
                    sa += "• ดำ ส่งคท.\n"
                    sa += "• ขาว ส่งคท.\n"
                    sa += "• ดำ @user\n"
                    sa += "• ล้าง @user\n"
                    sa += "• เชคดำ\n"
                    sa += "• คทดำ\n"
                    sa += "• ล้างดำ\n"
                    sa += "──────────────\n"
                    sa += "• ตั้งต้อนรับ [ข้อความ]\n"
                    sa += "• ตั้งคนออก [ข้อความ]\n"
                    sa += "• ตั้งแอด [ข้อความ]\n"
                    sa += "• ตั้งแทค [ข้อความ]\n"
                    sa += "• ตั้งคอมเม้น [ข้อความ]\n"
                    sa += "──────────────\n"
                    sa += "• เปิดแทค/ปิดแทค\n"
                    sa += "• เปิดแทค2/ปิดแทค2\n"
                    sa += "• เปิดแทค3/ปิดแทค3\n"
                    sa += "• เปิดไลค์/ปิดไลค์\n"
                    sa += "• เปิดคอมเม้น/ปิดคอมเม้น\n"
                    sa += "• เปิดบล็อค/ปิดบล็อค\n"
                    sa += "• เปิดแอด/ปิดแอด\n"
                    sa += "• เปิดกันรัน/ปิดกันรัน\n"
                    sa += "• เปิดต้อนรับ/ปิดต้อนรับ\n"
                    sa += "• เปิดต้อนรับ2/ปิดต้อนรับ2\n"
                    sa += "• เปิดคนออก/ปิดคนออก\n"
                    sa += "• เปิดยกเลิก/ปิดยกเลิก\n"
                    sa += "• เปิดโค๊ดติ๊ก/ปิดโค๊ดติ๊ก\n"
                    sa += "• เปิดติ๊กใหญ่/ปิดติ๊กใหญ่"
                    helps = "{}".format(str(sa))
                    data = {
                        "type": "flex",
                        "altText": "{}".format(sas),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#000000'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": sas,
                                        "size":"xl",
                                        "weight":"bold",
                                        "color":"#00F5FF",
                                        "align":"center"
                                    },
                                    {
                                        "type":"text",
                                        "text": " "
                                    },
                                    {
                                        "type": "text",
                                        "text": "{}".format(sa),
                                        "wrap": True,
                                        "color": "#000000",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type":"button",
                                        "style":"primary",
                                        "color":"#",
                                        "action": {
                                            "type":"uri",
                                            "label":"ผู้สร้าง",
                                            "uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                        },
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "help" or text.lower() == "คำสั่ง":
                            s = "#0033FF"
                            sa = "•🆕 me\n"
                            sa += "•🆕 /me\n"
                            sa += "•🆕 คท\n"
                            sa += "•🆕 mid\n"
                            sa += "•🆕 ชื่อเรา\n"
                            sa += "•🆕 ตัสเรา\n"
                            sa += "•🆕 รูปเรา\n"
                            sa += "•🆕 รูปวีดีโอเรา\n"
                            sa += "•🆕 ปกเรา\n"
                            sa += "•🆕 ข้อมูล\n"
                            sa += "•🆕 รีบอท\n"
                            sa += "•🆕 ออน\n"
                            sa += "•🆕 /ลบรัน\n"
                            sa += "•🆕 เชคค่า\n"
                            ss = "•🆕 แทค\n"
                            sa += "•🆕 ยกเชิญ"
                            ss += "•🆕 ก็อป @user\n"
                            ss += "•🆕 กลับร่าง\n"
                            ss += "•🆕 ตั้งapi [พิมเพื่อดูวิธี]\n"
                            ss += "•🆕 ล้างapi [คำที่จะลบ]\n"
                            ss += "•🆕 เชคapi\n"
                            ss += "•🆕 ทัก [พิม'ทัก'เพื่อดูวิธี]\n"
                            ss += "•🆕 แปรงคท [MID]\n"
                            ss += "•🆕 ยูทูป [ข้อความ]\n"
                            ss += "•🆕 บอกรัก [จำนวน @user]\n"
                            ss += "•🆕 รูป [ข้อความ]\n"
                            ss += "•🆕 เพลสโต [ชื่อแอพ]\n"
                            ss += "•🆕 ตั้งรูปโปรไฟล์ [ลิ้งยูทูป]\n"
                            ss += "•🆕 ประกาศ [พิมเพื่อดูวิธี]\n"
                            ss += "•🆕 /ยก [ยกเลิกข้อความ]"
                            sd = "•🆕 ดำ ส่งคท.\n"
                            sd += "•🆕 ขาว ส่งคท.\n"
                            sd += "•🆕 ดำ @user\n"
                            sd += "•🆕 ล้าง @user\n"
                            sd += "•🆕 เชคดำ\n"
                            sd += "•🆕 คทดำ\n"
                            sd += "•🆕 ล้างดำ\n"
                            sd += "•🆕 ตั้งต้อนรับ [ข้อความ]\n"
                            sd += "•🆕 ตั้งคนออก [ข้อความ]\n"
                            sd += "•🆕 ตั้งแอด [ข้อความ]\n"
                            sd += "•🆕 ตั้งแทค [ข้อความ]\n"
                            sd += "•🆕 ตั้งคอมเม้น [ข้อความ]\n"
                            sd += "•🆕 ตั้งค้างเชิญ [จำนวน]\n"
                            sd += "•🆕 ตั้งมุดลิ้ง [ข้อความ]\n"
                            sd += "•🆕 ตั้งคนบล็อค [ข้อความ]"
                            se = "•🆕 เปิด-ปิดแทค\n"
                            se += "•🆕 เปิด-ปิดแทค2\n"
                            se += "•🆕 เปิด-ปิดแทค3\n"
                            se += "•🆕 เปิด-ปิดไลค์\n"
                            se += "•🆕 เปิด-ปิดคอมเม้น\n"
                            se += "•🆕 เปิด-ปิดบล็อค\n"
                            se += "•🆕 เปิด-ปิดแอด\n"
                            se += "•🆕 เปิด-ปิดกันรัน\n"
                            se += "•🆕 เปิด-ปิดต้อนรับ\n"
                            se += "•🆕 เปิด-ปิดต้อนรับ2\n"
                            se += "•🆕 เปิด-ปิดคนออก\n"
                            se += "•🆕 เปิด-ปิดยกเลิก\n"
                            se += "•🆕 เปิด-ปิดติ๊กคนเข้า\n"
                            se += "•🆕 เปิด-ปิดติ๊กคนออก\n"
                            se += "•🆕 เปิด-ปิดติ๊กใหญ่"
                            sti = "•🆕 เปิด-ปิดมุดลิ้ง\n"
                            sti += "•🆕 ตั้งติ๊กคนแอด\n"
                            sti += "•🆕 ลบติ๊กคนแอด\n"
                       #     sti += "• ตั้งติ๊กแทคแชท\n"
                       #     sti += "• ลบติ๊กแทคแชท\n"
                            sti += "•🆕 ตั้งติ๊กคนแทค\n"
                            sti += "•🆕 ลบติ๊กคนแทค\n"
                            sti += "•🆕 ตั้งติ๊กคนเข้า\n"
                            sti += "•🆕 ลบติ๊กคนเข้า\n"
                            sti += "•🆕 ตั้งติ๊กคนออก\n"
                            sti += "•🆕 ลบติ๊กคนออก\n"
                            sti += "•🆕 เขียน1 [ข้อความ]\n"
                            sti += "•🆕 .โทร [จำนวน]\n"
                            sti += "•🆕 ดึง @user\n"
                            sti += "•🆕 บล็อค @user\n"
                            sti += "•🆕 เพิ่มเพื่อน @user\n"
                            sti += "•🆕 ลบเพื่อน @user\n"
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor":"#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                               "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งส่วนตัว •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sa,
                                                "color": s, 
                                                "wrap": True,
                                                "gravity": "center",
                                        #        "size": "md"
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#0000FF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อเราคลิก",
                                                     "uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งพิเศษ •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": ss, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#0000FF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อเราคลิก",
                                                     "uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งเปิด/ปิด •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sd, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#0000FF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อเราคลิก",
                                                     "uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งตั้งค่า/ติดดำ •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                           #     "text": " "
                                         #   },
                                         #   {
                                            #    "type": "text",
                                           #     "text": " "
                                          #  },
                                            {
                                                "type": "text",
                                                "text": se, 
                                                "color": s,
                                           #     "size": "lg",
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            #{
                                            #    "type": "text",
                                            #    "text": " "
                                           # },
                                          #  {
                                           #     "type": "text",
                                            #    "text": " "
                                           # },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                          #  {
                                          #      "type": "text",
                                          #      "text": "สนใจบอท ติดต่อได้ที่ปุ่มเลยค้ะ >_<",
                                          #      "color": "#B5B5B5",
                                          #      "size": "xs"
                                          #  },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#0000FF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อเราคลิก",
                                                     "uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                 },
                                            },
                                        ]
                                    },
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": "#000000"}, #"separator": True, "separatorColor": "#333333"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                                "size": "full"
                                            },
                                            {
                                                "type": "text",
                                                "text": "• คำสั่งทั่วไป •",
                                                "size": "xxl",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            { 
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                "type": "text",
                                                "text": sti, 
                                                "color": s,
                                                "wrap": True,
                                                "gravity": "center",
                                            },
                                            {
                                                "type": "text",
                                                "text": " "
                                            },
                                            {
                                                 "type":"button",
                                                 "style":"primary",
                                                 "color":"#0000FF",
                                                 "action":{
                                                     "type":"uri",
                                                     "label":"ติดต่อเราคลิก",
                                                     "uri":"line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                 },
                                            },
                                        ]
                                    },
                                },
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Help Message",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
#=====================================================================
                elif msg.text.lower().startswith("ก็อป "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = maxgie.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = maxgie.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "=͟͟͞͞➳ คุณกำลังก็อปปี้", "สำเร็จแล้ว >_<");maxgie.sendContact(to, str(BackupProfile.mid));maxgie.sendContact(to, str(contact.mid))
                elif text.lower() == "กลับร่าง":
                            try:
                                maxgiestatus = maxgie.getProfile()
                                maxgieName = maxgie.getProfile()
                                maxgieName.statusMessage = ProfileMe["statusMessage"]
                                maxgieName.pictureStatus = str(ProfileMe["pictureStatus"])
                                maxgie.updateProfile(maxgiestatus)
                                maxgieName.displayName = ProfileMe["NameMe"]
                                maxgie.updateProfile(maxgieName)
                                path = maxgie.downloadFileURL(ProfileMe["PictureMe"])
                                maxgie.updateProfilePicture(path)
                                coverId = ProfileMe["coverId"]
                                maxgie.updateProfileCoverById(coverId)
                                BackupProfile = maxgie.getContact(sender)
                                sendMention(to, BackupProfile.mid, "=͟͟͞͞➳ กลับบัญชีเดิมเรียบร้อย", ">_<");maxgie.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟คุณยังไม่ได้ก๊อปปี้🌟")
                if text.lower() == "คท":
                    maxgie.generateReplyMessage(msg.id) 
                    maxgie.sendReplyMessage(msg.id, to, None, contentMetadata={'mid': maxgieMID}, contentType=13)
#========================================================================
                if text.lower() == "mid" or text.lower() == "mid":
                    maxgie.generateReplyMessage(msg.id)
                    maxgie.sendReplyMessage(msg.id, to,maxgieMID)
                elif text.lower() == "myname" or text.lower() == "ชื่อเรา":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "「 ชื่อของคุณ 」\n"+str(h.displayName))
                elif text.lower() == "mybio" or text.lower() == "ตัสเรา":
                            h = maxgie.getContact(maxgieMID)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyMessage(msg.id, to, "「 ตัสของคุณ 」\n"+str(h.statusMessage))
                elif text.lower() == "mypicture" or text.lower() == "รูปเรา":
                            h = maxgie.getContact(maxgieMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif text.lower() == "myvideo" or text.lower() == "รูปวีดีโอเรา":
                            h = maxgie.getContact(maxgieMID)
                            if h.videoProfile == None:
                            	return maxgie.sendMessage(to, "คุณไม่ได้ใส่รูปวีดีโอ >_<")
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                elif text.lower() == "mycover" or text.lower() == "ปกเรา":
                            h = maxgie.getContact(maxgieMID)
                            cu = maxgie.getProfileCoverURL(maxgieMID)
                            image = str(cu)
                            maxgie.generateReplyMessage(msg.id)
                            maxgie.sendReplyImageWithURL(msg.id, to, image)
                elif msg.text in ["ดึง"]:
                        apalo["winvite"] = True
                        maxgie.unsendMessage(msg_id)
                        duc1(to, "🌟ส่งคทที่จะดึงลงมา..🌟")                        
                            
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif cmd.startswith('อัพชื่อกลุ่ม '):
                    if msg.toType != 2: return maxgie.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้\nคำสั่งนี้ใช้ได้ในกลุ่มเท่านั้น')
                    group = maxgie.getGroup(to)
                    gname = removeCmd(text, setKey)
                    if len(gname) > 50:
                        return maxgie.sendMessage(to, 'ไม่สามารถเปลี่ยนชื่อกลุ่มได้\nชื่อกลุ่มต้องไม่เกิน 50')
                    group.name = gname
                    maxgie.updateGroup(group)
                    maxgie.sendMessage(to, 'เปลี่ยนชื่อกลุ่มเป็น `%s`' % gname)

                elif "อัพตัส " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                elif msg.text.lower().startswith("อัพชื่อ: "):
                    string = msg.text.lower().replace("อัพชื่อ", "")
                    if len(string) <= 10000000000:
                        pname =  maxgie.getContact(sender).displayName
                        profile = maxgie.getProfile()
                        profile.displayName = string
                        line.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        maxgie.sendFooter(to, "Update Name\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)
                elif msg.text.lower().startswith("อัพตัส: "):
                    string = msg.text.lower().replace("อัพตัส", "")
                    if len(string) <= 10000000000:
                        pname = maxgie.getContact(sender).statusMessage
                        profile = maxgie.getProfile()
                        profile.statusMessage = string
                        maxgie.updateProfile(profile)
                        userid = "https://line.me/ti/p/~" + line.profile.userid
                        maxgie.sendFooter(to, "Update Status\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string), userid, "http://dl.profile.line-cdn.net/"+line.getContact(sender).pictureStatus, line.getContact(sender).displayName)                        
                elif text.lower() == "ผส":
                        maxgie.sendContact(to,"ub65037fce83ce14909759e3a932182c9") 
                elif text.lower() == "อัพดิส":
                    sets["changePictureProfile"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งรูปที่จะอัพลงมาครับ..🌟")
                elif text.lower() == 'เปิดออก':
                    did["join"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ออกแชทรวมอัตโนมัติ (เปิด) ใช้งาน🌟")
                elif text.lower() == 'ปิดออก':
                    did["join"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ออกแชทรวมอัตโนมัติ (ปิด) ใช้งาน🌟") 
                if text.lower() == "ออน2":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage     
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    eltime = time.time() - mulai
                    van = ggggg(eltime)
                    van2 = "\n\n✨วันที่ :"+ datetime.strftime(timeNow,'%d-%m-%Y')+"\n───────────\n◐เวลา:"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n\n"      
                    data={
"type":"flex",
"altText":"Weclome",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#EE1289", "separator": True, "separatorColor": "#EE1289"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "✯◉เวลาทำงานของบอท◉✯",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"text": "✨ระยะเวลาของบอท✨",
"size": "md",
"align": "center",
"color": "#00F5FF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ➡ จัดทำโดย : \n ➡ ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
"size": "xs",
"margin": "none",
"color": "#00F5FF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00F5FF",
"height": "sm",
"action": {
"type": "uri",
"label": "ซื้อติ๊ก",
"uri": "line://nv/profilePopup/mid=u9a94b3e7a81df46cf088b9f35b2b6fe6",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00F5FF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อผู้สร้าง",
"uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
}
}
]
}
},
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#EE1289", "separator": True, "separatorColor": "#EE1289"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "✨ ปฏิทิน ✨",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"text": "✨วันเดือนปีและเวลา✨",
"size": "md",
"align": "center",
"color": "#00F5FF",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#00F5FF"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": van2,
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#00F5FF",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": profile,
"type": "icon",
"size": "md"
},
{
"text": " ➡ จัดทำโดย : \n ➡ ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
"size": "xs",
"margin": "none",
"color": "#00F5FF",
"wrap": True,
"weight": "regular",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#00F5FF",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อเชล",
"uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#00F5FF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อผู้สร้าง",
"uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
}
}
]
}
}
]
}
}                    
                    sendTemplate(to, data)   
                if text.lower() == "ออน" or text.lower() == "runtime":
                    contact = maxgie.getContact(sender)
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)   
                    a = "วันที่"+ datetime.strftime(timeNow,'%d-%m-%Y')+"🇹🇭เวลา"+ datetime.strftime(timeNow,'%H:%M:%S')+"\n"
                    run = "「 เวลาออน 」\n"
                    run += runtime
                    data = {
                            "type": "flex",
                            "altText": "{}".format(run),
                            "contents": {
                            "styles": {
                              "body": {
                                "backgroundColor": "#0000FF"
                              },
                              "footer": {
                                "backgroundColor": "#FFFF00"
                              }
                            },
                            "type": "bubble",
                            "body": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                      "type": "image"
                                    },
                                    {
                                      "type": "separator",
                                      "color": "#00FF00"
                                    },
                                    {
                                      "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                      "type": "image"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "horizontal"
                                },
                                {
                                  "type": "separator",
                                  "color": "#00FF00"
                                },
                                {
                                  "contents": [
                                    {
                                      "text": "✨ระยะเวลาทำงาน✨",
                                      "size": "lg",
                                      "align": "center",
                                      "color": "#00FF00",
                                      "wrap": True,
                                      "weight": "bold",
                                      "type": "text"
                                    }
                                  ],
                                  "type": "box",
                                  "spacing": "md",
                                  "layout": "vertical"
                                },
                                {
                                  "type": "separator",
                                  "color": "#00FF00"
                                },
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "{}".format(run),
                                          "size": "lg",
                                          "align": "center",
                                          "margin": "none",
                                          "color": "#00FF00",
                                          "wrap": True,
                                          "weight": "regular",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    },
                                  ],
                                  "type": "box",
                                  "layout": "vertical"
                                }
                              ],
                              "type": "box",
                              "spacing": "md",
                              "layout": "vertical"
                            },
                            "footer": {
                              "contents": [
                                {
                                  "contents": [
                                    {
                                      "contents": [
                                        {
                                          "text": "ติดต่อผู้สร้าง",
                                          "size": "xl",
                                          "action": {
                                            "uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                            "type": "uri",
                                            "label": "Add Maker"
                                          },
                                          "margin": "xl",
                                          "align": "center",
                                          "color": "#110000",
                                          "weight": "bold",
                                          "type": "text"
                                        }
                                      ],
                                      "type": "box",
                                      "layout": "baseline"
                                    }
                                  ],
                                  "type": "box",
                                  "layout": "horizontal"
                                }
                              ],
                              "type": "box",
                              "layout": "vertical"
                            }
                        }
                    }
                    sendTemplate(to, data)      
                if text.lower() == "me":
                    cover = maxgie.getProfileCoverURL(maxgie.profile.mid)
                    pp = maxgie.getProfile().pictureStatus
                    profile = "https://profile.line-scdn.net/" + str(pp)
                    name = maxgie.getProfile().displayName
                    status = maxgie.getProfile().statusMessage
                    s = temp["te"]
                    a = temp["t"]
                    data={"type":"flex","altText":"{} sendFlex".format(name),"contents":{"type":"bubble",'styles': {"body":{"backgroundColor":a}},"hero":{"type":"image","url":cover,"size":"full","aspectRatio":"20:13","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":" "},{"type":"image","url":profile,"size":"lg"},{"type":"text","text":" "},{"type":"text","text":name,"size":"xl","weight":"bold","color":s,"align":"center"},{"type":"text","text":" "},{"type":"text","text":status,"align":"center","size":"xs","color":s,"wrap":True},{"type":"text","text":" "},{"type":"button","style":"primary","color":"#ff0000","action":{"type":"uri","label":"ME","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://is.gd/pv49jP&piu=https://media.giphy.com/media/S99gt1bbp8sN8qYOpD/giphy.gif"}}]}}}
                    sendTemplate(to, data)
                elif text.lower() == "/me":
                            s = temp["te"]
                            a = temp["t"]
                            contact = maxgie.getContact(maxgieMID)
                            cover = maxgie.getProfileCoverURL(maxgieMID)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                    },
                                    "body": {
                                       "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "weight": "bold",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1
                                            },
                                            {
                                                "type": "text",
                                                "text": "รูปโปรไฟล์ >\\<",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                       ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://media.giphy.com/media/LMhC9RLAzN4h71B9tM/giphy.gif"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "กดติดต่อคนทำบอท",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "line://ti/p/~mj.ktc"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(cover),
                                        "size": "full",
                                        "aspectRatio":"20:13",
                                        "aspectMode":"cover"
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.mid),
                                                "align": "center",
                                                "color": s,
                                                "size": "sm",
                                                "flex": 1,
                                            },
                                            {
                                                "type": "text",
                                                "text": "รูปปกพื้นหลัง >\\<",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s,
                                                "size": "lg",
                                                'flex': 1,
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "กดติดต่อคนทำบอท",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "line://ti/p/~mj.ktc"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": a},
                                        "body": {"backgroundColor": a},# "separator": True, "separatorColor": "#333333"},
                                        "footer": {"backgroundColor": a, "separator": True, "separatorColor": s}
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "ชื่อ :",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "align": "center",
                                                "color": s,
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
                                                "align": "center",
                                                "color": a,
                                                "size": "sm",
                                            },
                                            {
                                                "type": "text",
                                                "text": "Status",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": s
                                            },
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.statusMessage),
                                                "align": "center",
                                                "color": s,
                                                "wrap": True,
                                                "size": "md"
                                           },
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://os.line.naver.jp/os/p/"+maxgieMID,
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "กดติดต่อคนทำบอท",
                                                        "align": "center",
                                                        "color": s,
                                                        "size": "md",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "line://ti/p/~mj.ktc"
                                                        }
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "{}".format(contact.displayName),
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                if text.lower() == "เรา":
                    contact = maxgie.getContact(sender)
                    sendTemplate(to,{"type":"flex","altText": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶","contents":{"type":"bubble","footer":{"type":"box","layout":"horizontal","contents":[{"color":"#333333","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://app/1602687308-GXq4Vvk9?type=video&ocu=https://img.live/images/2019/02/10/1549778907829.jpg"},"type":"text","text":"❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶","align":"center","weight":"bold"},{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"xs","wrap":True,"action":{"type":"uri","uri":"line://ti/p/~@622zdvow"},"type":"text","text":"ผู้สร้าง","align":"center","weight":"bold"}]},"styles":{"footer":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#CCFFFF"}},"body":{"type":"box","contents":[{"type":"box","contents":[{"type":"separator","color":"#FF3333"},{"aspectMode":"cover","gravity":"bottom","aspectRatio":"1:1","size":"sm","type":"image","url":"https://img.live/images/2019/02/21/c5f4e567380d0f1e31acb822d0b5cfd2819c8e3b_00.jpg"},{"type":"separator","color":"#FF3333"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/21/d1566d9832bd42f14ec4d2538f74ab76.jpg"},{"type":"separator","color":"#FF3333"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#FF3333"},{"type":"image","aspectMode":"cover","aspectRatio":"1:1","size":"sm","url":"https://img.live/images/2019/02/10/1549778907829.jpg"},{"type":"separator","color":"#FF3333"}],"layout":"vertical","spacing":"none","flex":1},{"type":"separator","color":"#FF3333"},{"type":"box","contents":[{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"md","wrap":True,"type":"text","text":" ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶","weight":"bold"},{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"md","wrap":True,"type":"text","text":"{}".format(contact.displayName),"weight":"bold"},{"type":"separator","color":"#FF3333"},{"color":"#FF3333","size":"xs","wrap":True,"type":"text","text":"Status Profile:","weight":"bold"},{"type":"text","text":"{}".format(contact.statusMessage),"size":"xxs","wrap":True,"color":"#FF3333"}],"layout":"vertical","flex":2}],"layout":"horizontal","spacing":"md"},"hero":{"aspectMode":"cover","margin":"xxl","aspectRatio":"1:1","size":"full","type":"image","url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)}}})            
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "เวลาออน \n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=uca43cd15fb994f5e04c0984b7c1693ef"
                        } 
                    }
                    sendTemplate(to, data)                            
                elif text.lower() == "/runtime" or text.lower() == "/ออน":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ เวลาออน ⇦\n"
                    run += runtime
                    helps = "{}".format(str(run))
                    data = {
                        "type": "text",
                        "text": "{}".format(str(run)),
                        "sentBy": {
                             "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://nv/profilePopup/mid=ubd86e8c77559b1493f0ad64b1dba2d6c"
                        }
                    }
                    sendTemplate(to, data)
                if text.lower() == "/ออน" or text.lower() == "runtime":
                    timeNow = time.time() - Start
                    runtime = timeChange(timeNow)
                    run = "⇨ เวลาออน ⇦\n"
                    run += runtime
                    data = {
                        "type": "flex",
                        "altText": "{}".format(run),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#EE1289'
                                 },
                            },
                            "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                              #  {
                                              #  "type": "image",
                                                #"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                               # "size": "full"
                                             #  },
                                    {
                                        "type": "text",
                                        "text": "{}".format(run),
                                        "wrap": True,
                                        "color": "#000000",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif text.lower() == "รีบอท" or text.lower() == "reset":
                    gifnya = ["https://media.giphy.com/media/USP1m0qzDXWR5cvD8g/giphy.gif"]
                    data = {
                        "type": "template",
                        "altText": "รอแป๊บนึงได้ป่ะ...",
                        "template": {
                            "type": "image_carousel",
                            "columns": [
                                {
                                     "imageUrl": "https://media.giphy.com/media/USP1m0qzDXWR5cvD8g/giphy.gif".format(random.choice(gifnya)),
                                     "size": "full",
                                     "action": {
                                         "type": "uri",
                                          "uri": "line://ti/p/~mj.ktc"
                                     }
                                }
                            ]
                        }
                    }
                    sendTemplate(to, data)
                    time.sleep(1)
                    ga = "สำเร็จแล้ว (｀・ω・´)"
                    data = {
                        "type": "text",
                        "text": "{}".format(str(ga)),
                        "sentBy": {
                             "label": "รีบอทสำเร็จ...",
                             "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                             "linkUrl": "line://ti/p/~mj.ktc"
                        }
                    }
                    sendTemplate(to, data)
                    restartBot()
                if text.lower() == "/sp" or text.lower() == "speed1":
                    start = time.time()
                    maxgie.sendMessage("u7ff3c8f1829ee9fbb7684294b51345e6","test speed...")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = "🆙สปีดบอท\n🆙ความเร็วปิง\n🆙Took : %.3fms\n🆙ความเร็วสปีด: %.10f️" % (took,elapsed_time)
                    data = {
                        "type": "flex",
                        "altText": "BotSpeed",
                        "contents": {
                            "type": "bubble",
                            "hero": {
                                "type":"image",
                                "url":"https://media.giphy.com/media/LkfPCqhXiqS4dzkXXx/giphy.gif",
                                "size": "full",
                                "aspectRatio": "1:1",
                                "aspectMode": "fit"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": a,
                                        "wrap": True,
                                        "color":"#363636",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)

                elif text.lower() == "spb" or text.lower() == "sp":                       
                    contact = maxgie.getContact(sender)
                    start = time.time()
#                    maxgie.sendMessage(to, "✨ทดสอบความเร็ว✨")
                    elapsed_time = time.time() - start
                    took = time.time() - start
                    a = " 🔘สปีดบอท🔘 \n🐉 ความเร็วปิง ✔️\n🐉 Took : %.3fms ✔️\n🐉 ความเร็วสปีด: %.10f ✔️" % (took,elapsed_time)
                    LINKFOTO = "https://os.line.naver.jp/os/p/" + sender
                    LINKVIDEO = "https://os.line.naver.jp/os/p/" + sender + "/vp"                            
                    data = {
                        "type": "flex",
                                "altText": "{}".format(a),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#3300FF'
                                            },
                                            "footer": {
                                                "backgroundColor": '#FFFF00'
                                                 },
                                              },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                "size": "full",
                                                "aspectRatio": "1:1",
                                                "aspectMode": "fit",
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text":  "{}".format(a),
                                                                "color": "#00FF00",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 1    
                                                            } 
                                                        ]
                                                    }
                                                ] 
                                            }
                                        ]
                                    },                                                                                                    
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "ติดต่อเราคลิก",
                                                    "uri": "line://ti/p/~mj.ktc"
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0        
                                    }
                                }
                            }
                    sendTemplate(to, data)

                elif msg.text in ["4g","Hk"]:
                    maxgie.sendMessage(msg.to, " Tëst : Prëmium Spëed™\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                    maxgie.sendMessage(msg.to, " S.p.ë.e.d")
                    start = time.time()
                    time.sleep(0.02)
                    elapsed_time = time.time() - start
                    maxgie.sendMessage(msg.to, "%sseconds" % (elapsed_time))   
                elif msg.text.lower().startswith("ส่งความรัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:                  
                                duc1(to, "🎁•รับทางแชทสต.นะ•🎁".format(str(jml)))
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                maxgie.sendMessage(receiver, "💥เทพเจแจกของ💥\n😈ระวังเพราะข้างในมันอันตราย😈\n.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.G3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God..3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God .3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God.3.God")
                                duc1(to, "✳ไปดูแชท ส.ต ด้วย✳".format(str(jml)))
                            else:
                                pass
                elif msg.text.lower().startswith(".โทร"):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        members = [mem.mid for mem in group.members]
                        maxgie.acquireGroupCallRoute(to)
                        maxgie.inviteIntoGroupCall(to, contactIds=members)
                    else:
                        duc1(to, "มาเล่นกันเถอะ ^_^📱".format(str(jml)))

                if text.lower() == "ลบแชท":						
                    maxgie.removeAllMessages(op.param2)
                    duc1(to,"「 ลบแชทเรียบร้อยครับ 」")       

                elif msg.text.startswith("โทร"):
                    dan = text.split(" ")
                    num = int(dan[1])
                    ret_ = "╭──[ เชิญโทรสำเร็จ ]"
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            for var in range(0,num):
                                group = maxgie.getGroup(to)
                                members = [ls]
                                maxgie.acquireGroupCallRoute(to)
                                maxgie.inviteIntoGroupCall(to, contactIds=members)
                            ret_ += "\n├> @!"
                        ret_ += "\n╰──────────"
                        maxgie.sendPhu(to, ret_, lists)   
                                        
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               maxgie.sendMessage(msg.to, teks)
                        else:
                           maxgie.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            maxgie.sendMessage(msg.to, tulisan)
                elif text.lower() == 'ข้อมูล' or text.lower() == "about":
                    try:
                        arr = []
                        owner = "uddb1d5f170d68f749b985babb6d42942"
                        creator = maxgie.getContact(owner)
                        contact = maxgie.getContact(maxgieMID)
                        grouplist = maxgie.getGroupIdsJoined()
                        contactlist = maxgie.getAllContactIds()
                        blockedlist = maxgie.getBlockedContactIds()
                        IdsInvit = maxgie.getGroupIdsInvited()
                        times = time.time() - Start
                        runtime = timeChange(times)
                        ret_ = "╭───「 About Your 」"
                        ret_ += "\n├ ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n├ กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n├ เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n├ บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n├ ค้างเชิญ : {}".format(str(len(IdsInvit)))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ เวลาออนบอท :"
                        ret_ += "\n├ {}".format(str(runtime))
                        ret_ += "\n├────────────"
                        ret_ += "\n├ ผู้สร้าง : {}".format(str(creator.displayName))
                        ret_ += "\n╰───「 ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶」"
                        feds = "{}".format(str(ret_))
                        data = {
                            "type": "text",
                            "text": "{}".format(str(ret_)),
                            "sentBy": {
                                 "label": "{}".format(maxgie.getContact(maxgieMID).displayName),
                                 "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
                                 "linkUrl": "line://ti/p/~mj.ktc"
                            }
                        }
                        sendTemplate(to, data)
                        maxgie.sendContact(msg.to, creator.mid)
                    except Exception as e:
                        maxgie.sendMessage(msg.to, str(e))
                elif msg.text.lower().startswith("บอกรัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:                  
                                duc1(to, "💗กำลังบอกรัก💗\n⌛รอสักครู่......".format(str(jml)))
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")                                
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")
                                maxgie.sendMessage(receiver, "🤓❣รักนะคร๊าฟจุ๊บๆ❣🤓")                                                                
                                duc1(to, "💌บอกรักสำเร็จ☑️\n\n❴✯ᴛᴇᴀᴍ⸭ʙᴏᴛ⸭❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶✯❵".format(str(jml)))
                            else:
                                pass

                elif text.lower() == "หลุดมือ":
                            gifnya = ['https://i.pinimg.com/originals/87/a8/9b/87a89b5aeaf35ba0c8879db5a136ccbd.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~mj.ktc"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif text.lower() == "รัก" or text.lower() == "รักๆ":
                            gifnya = ['https://thumbs.gfycat.com/KlutzyUglyGelding-small.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~mj.ktc"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                elif cmd == "random":
                            gifnya = ['https://thumbs.gfycat.com/AngelicCloudyJaeger-size_restricted.gif','https://thumbs.gfycat.com/AgedZealousBlackfootedferret-size_restricted.gif','https://thumbs.gfycat.com/FondHastyChinesecrocodilelizard-size_restricted.gif','https://thumbs.gfycat.com/LividCrazyDipper-size_restricted.gif','https://thumbs.gfycat.com/LoathsomeDevotedGossamerwingedbutterfly-size_restricted.gif','https://thumbs.gfycat.com/SamePhysicalHarrierhawk-size_restricted.gif','https://thumbs.gfycat.com/ColorlessPinkLangur-size_restricted.gif','https://thumbs.gfycat.com/ThoseBitesizedBrahmanbull-size_restricted.gif','https://thumbs.gfycat.com/FakeSlowBengaltiger-size_restricted.gif','https://thumbs.gfycat.com/TanSpitefulChupacabra-size_restricted.gif']
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~mj.ktc"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                            
                elif msg.text.lower().startswith("ตั้งรูปโปรไฟล์"):
                            link = removeCmd("ตั้งรูปโปรไฟล์", text)
                            contact = maxgie.getContact(sender)
                            maxgie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = maxgie.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            changeVideoAndPictureProfile(pict, vids)
                            maxgie.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================

#=====================================================================

                elif text.lower() == 'เทส':
                    duc1(to, "กำลังโหลด:▒...0%")
                    maxgie.sendMessage(to, "█▒... 10.0%")
                    maxgie.sendMessage(to, "██▒... 20.0%")
                    maxgie.sendMessage(to, "███▒... 30.0%")
                    maxgie.sendMessage(to, "████▒... 40.0%")
                    maxgie.sendMessage(to, "█████▒... 50.0%")
                    maxgie.sendMessage(to, "██████▒... 60.0%")
                    maxgie.sendMessage(to, "███████▒... 70.0%")
                    maxgie.sendMessage(to, "████████▒... 80.0%")
                    maxgie.sendMessage(to, "█████████▒... 90.0%")
                    maxgie.sendMessage(to, "███████████..100.0%")
                    duc1(to, "🕉️〘บอทยังอยู่จะท่านผู้ชม〙🕉️\n❴✯ᴛᴇᴀᴍ⸭ʙᴏᴛ⸭❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶✯❵")

                elif msg.text in ["นับ"]:
                    duc1(to,"「 ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶ 」")
                    maxgie.sendMessage(to,"??:::⭐ 1 ⭐:::💖")
                    maxgie.sendMessage(to,"💚:::⭐ 5 ⭐:::💚")
                    maxgie.sendMessage(to,"💖:::⭐ 10 ⭐:::💖")
                    duc1(to,"กุนับเส็จละไวมั้ย" +datetime.today().strftime('%H:%M:%S')+ "™") 

#=====================================================================
                elif msg.text.lower().startswith("ประกาศแชท: "):
                    sep = text.split(" ")
                    txt = text.replace(sep[0] + " ","")
                    friends = maxgie.friends
                    for friend in friends:
                        maxgie.sendMessage(friend, "「ข้อความอัตโนมัติ ประกาศแชท」\n{}".format(str(txt)))
                    duc1(to, "ส่งข้อความถึงเพื่อน {} คน".format(str(len(friends))))
#=============================================================================           
                elif msg.text.lower().startswith("ดำ "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        maxgie.sendMessage(to, 'Add to TalkBan')
                                    except:
                                        pass
                elif msg.text.lower().startswith("ล้าง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        maxgie.sendMessage(to, 'Deleted from TalkBan')
                                    except:
                                        pass
                elif text.lower() == "เชคดำ":
                            if apalo["Talkblacklist"] == {}:
                              maxgie.unsendMessage(msg_id)
                              duc1(to, "⚫ไม่พบคนที่ยัดดำ⚫")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +maxgie.getContact(m_id).displayName + "\n"
                              duc1(to,"รายชื่อคนติดดำ :\n\n"+ma+"\nจำนวน %s คนติดดำ" %(str(len(apalo["Talkblacklist"]))))

                elif text.lower() == "คทดำ":
                    if msg._from in maxgieMID:
                        if apalo["Talkblacklist"] == []:
                            duc1(to, "⚫ไม่มีคท.คนติดดำ⚫")
                        else:
                            for bl in apalo["Talkblacklist"]:
                                maxgie.sendMessage(to, text=None, contentMetadata={'mid': bl}, contentType=13)
#=====================================================================                
                if text.lower() == "เปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = True
                      sa = "🌟เปิดแล้ว (｀・ω・´)🌟"
                  else:
                      sa = "🌟เปิดอยู่แล้ว (｀・ω・´)🌟"
                  duc1(to, sa)
                if text.lower() == "ปิดบล็อค":
                  if msg._from in admin:
                      settings["autoblock"] = False
                      duc1(to,"🌟ปิดแล้ว (｀・ω・´)🌟")
                  else:
                      duc1(to,"🌟ปิดอยู่แล้ว (｀・ω・´)🌟")
                if text.lower() == "เปิดแทค":
                    tagadd["tags"] = True
                    maxgie.unsendMessage(msg_id)
                    sa = "🌟เปิดแล้วว >_<🌟"
                    duc1(to,str(sa))
                if text.lower() == "ปิดแทค":
                    tagadd["tags"] = False
                    maxgie.unsendMessage(msg_id)
                    sa = "🌟ปิดแล้ว >_<🌟"
                    duc1(to,str(sa))
                if text.lower() == "เปิดกันรัน":
                    settings["autoCancel"]["on"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดกันรันเรียบร้อย🌟")
                if text.lower() == "ปิดกันรัน":
                    settings["autoCancel"]["on"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดกันรันเรียบร้อย🌟")
                if text.lower() == "กินห้องเปิด":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = True
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟กินห้อง (เปิด) ใช้งาน🌟")
                  else:
                      maxgie.sendMessage(msg.to,"「 Status Autoleave 」\nเปิดใช้งานกินห้องอัตโนมัติแล้ว")
                if text.lower() == "กินห้องปิด":
                  if msg._from in maxgieMID:
                      kcn["autojoin"] = False
                      maxgie.unsendMessage(msg_id)
                      duc1(to, "🌟กินห้อง (ปิด) ใช้งาน🌟")
                  else:
                      maxgie.sendMessage(msg.to,"「 Status Autoleave 」\nเปิดใช้งานกินห้องอัตโนมัติแล้ว") 
                if text.lower() == "เปิดแอด":
                    settings["autoAdd"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดแอดเรียบร้อย🌟")
                if text.lower() == "ปิดแอด":
                    settings["autoAdd"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดแอดเรียบร้อย🌟")
                if text.lower() == "ปิดไลค์":
                   sets["l"] = False
                   maxgie.unsendMessage(msg_id)
                   duc1(to, "??ปิดไลค์แล้ว🌟")
                if text.lower() == "เปิดไลค์":
                   sets["l"] = True
                   maxgie.unsendMessage(msg_id)
                   duc1(to, "🌟เปิดไลค์แล้ว🌟")
                if text.lower() == "เปิดแทค2":
                    tagadd["tagss"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดแทค2เรียบร้อย🌟")
                if text.lower() == "ปิดแทค2":
                    tagadd["tagss"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดแทค2เรียบร้อย🌟")
                if text.lower() == "เปิดคอมเม้น":
                    settings["com"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดคอมเม้นเรียบร้อย🌟")
                if text.lower() == "ปิดคอมเม้น":
                    settings["com"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดคอมเม้นเรียบร้อย🌟")
                if text.lower() == "เปิดต้อนรับ":
                    settings["Welcome"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดต้อนรับเรียบร้อย🌟")
                if text.lower() == "ปิดต้อนรับ":
                    settings["Welcome"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดต้อนรับเรียบร้อย🌟")
                if text.lower() == "เปิดต้อนรับ2":
                    settings["Wc"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดต้อนรับ2เรียบร้อย🌟")
                if text.lower() == "ปิดต้อนรับ2":
                    settings["Wc"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดต้อนรับ2เรียบร้อย🌟")
                if text.lower() == "เปิดคนออก":
                    settings["Leave"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดคนออกเรียบร้อย🌟")
                if text.lower() == "ปิดคนออก":
                    settings["Leave"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดคนออกเรียบร้อย🌟")
                if text.lower() == "เปิดยกเลิก":
                    settings["unsendMessage"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดยกเลิกเรียบร้อย🌟")
                if text.lower() == "ปิดยกเลิก":
                    settings["unsendMessage"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดยกเลิกเรียบร้อย🌟")
                if text.lower() == "เปิดติ๊กใหญ่":
                    settings["Sticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดติ๊กใหญ่เรียบร้อย🌟")
                if text.lower() == "ปิดติ๊กใหญ่":
                    settings["Sticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดติ๊กใหญ่เรียบร้อย🌟")
                if text.lower() == "เปิดโค๊ดติ๊ก":
                    sets["Sticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดโค๊ดติ๊กเรียบร้อย🌟")
                if text.lower() == "ปิดโค๊ดติ๊ก":
                    sets["Sticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดโค๊ดติ๊กเรียบร้อย🌟")
                if text.lower() == "เปิดแทค3":
                    sets["tagsticker"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดแทค3เรียบร้อย🌟")
                if text.lower() == "ปิดแทค3":
                    sets["tagsticker"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดแทค3เรียบร้อย🌟")
                if text.lower() == "เปิดติ๊กคนออก":
                    settings["lv"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดติ๊กคนออกเรียบร้อย🌟")
                if text.lower() == "ปิดติ๊กคนออก":
                    settings["lv"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดติ๊กคนออกเรียบร้อย🌟")
                if text.lower() == "เปิดติ๊กคนเข้า":
                    settings["wcsti2"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดติ๊กคนเข้าเรียบร้อย🌟")
                if text.lower() == "ปิดติ๊กคนเข้า":
                    settings["wcsti2"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดติ๊กคนเข้าเรียบร้อย🌟")
                if text.lower() == "เปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟เปิดมุดลิ้งเรียบร้อย🌟")
                if text.lower() == "ปิดมุดลิ้ง":
                    sets["autoJoinTicket"] = False
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ปิดมุดลิ้งเรียบร้อย🌟")
                if text.lower() == 'เปิดเข้า':
                    settings["autoJoin"] = True
                    duc1(to, "เข้ากลุ่ม (เปิด) ใช้งาน☑")
                if text.lower() == 'ปิดเข้า':
                    settings["autoJoin"] = False
                    duc1(to, "เข้ากลุ่ม (ปิด) ใช้งาน☑")

                elif text.lower() == 'speed':start = time.time();maxgie.sendMessage("uddb1d5f170d68f749b985babb6d42942", "🌟❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶🌟");elapsed_time = time.time() - start;duc1(to, "Speed : %s second"%str(round(elapsed_time,4)))
                
                elif msg.text.lower().startswith("ประกาศ "):
                            txt = removeCmd("ประกาศ", text)
                            groups = maxgie.getGroupIdsJoined()
                            url = 'https://nekos.life/api/v2/img/ngif'
                            text1 = requests.get(url).text
                            image = json.loads(text1)['url']
                            for group in groups:
                                sa = " 💥ประกาศ💥 \n\n{}".format(str(txt))
                                data = {
"type":"flex",
"altText":"ด่วนแจกเงิน2000บาทฟรี\n1คนเท่านั้น",
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#FFFF00", "separator": True, "separatorColor": "#FF0000"},
"body": {"backgroundColor": "#0000FF", "separator": True, "separatorColor": "#FF0000"},
"footer": {"backgroundColor": "#FFFF00", "separator": True, "separatorColor": "#FF0000"}
},
"header": {
"type": "box",
"layout": "horizontal",
"contents": [
{
"type": "text",
"text": "👉ประกาศกลุ่ม👈",
"align": "center",
"size": "lg",
"weight": "bold",
"color": "#000000",
"wrap": True
}
]
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "image"
},
{
"type": "separator",
"color": "#FF0000"
},
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#FF0000"
},
{
"contents": [
{
"text": sa,
"size": "md",
"align": "center",
"color": "#00FF00",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"type": "separator",
"color": "#FF0000"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": "╔══════════════╗\n〘❣ʙᴏᴛ.ʟɪɴᴇ❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶❣〙\n╚══════════════╝",
"align": "center",
"size": "xs",
"weight": "bold",
"color": "#FFFF00",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
},
{
"contents": [
{
"url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),
"type": "icon",
"size": "md"
},
{
"text": " ➡ จัดทำโดย : \n ➡ ❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶",
"size": "xs",
"margin": "none",
"color": "#FF0000",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"type": "button",
"flex": 2,
"style": "primary",
"color": "#9900FF",
"height": "sm",
"action": {
"type": "uri",
"label": "ซื้อติ๊ก",
"uri": "line://nv/profilePopup/mid=u9a94b3e7a81df46cf088b9f35b2b6fe6",
}
},
{
"flex": 3,
"type": "button",
"style": "primary",
"color": "#9900FF",
"margin": "sm",
"height": "sm",
"action": {
"type": "uri",
"label": "ติดต่อผู้สร้าง",
"uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
}
}
]
}
}
]
}
}
                                sendTemplate(group, data)
                                time.sleep(1)
                            duc1(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
                elif msg.text.lower().startswith("ขายของ"):
                            contact = maxgie.getContact(sender) 
                            groups = maxgie.getGroupIdsJoined()
                            for group in groups:
                                dataProfile = [ 
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#0033FF'
                                              },
                                          "body": {
                                              "backgroundColor": '#FFFFFF'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FFFF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "✯ʙᴏᴛ.ʟɪɴᴇ✯❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FF00"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://media.giphy.com/media/fAKVRDMzaBWjPYZAE5/giphy.gif",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~mj.ktc"
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://media.giphy.com/media/ehzEbyTyUpYF6pwwtl/giphy.gif",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://media.giphy.com/media/Lp95cMvWHXFd38hGFG/giphy.gif",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "self bot python3",
                                                  "color": "#0000EE",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 100 บาท/เดือน",
                                                  "color": "#0000EE",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ห้องบอท",
                                                  "color": "#0000EE",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคา 200 บาท",
                                                  "color": "#0000EE",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดการใช้งาน",
                                                  "color": "#0000EE",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                       }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#0033FF'
                                              },
                                          "body": {
                                              "backgroundColor": '#FFFFFF'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FFFF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "✯ʙᴏᴛ.ʟɪɴᴇ✯❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FF00"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://media.giphy.com/media/fAKVRDMzaBWjPYZAE5/giphy.gif",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://media.giphy.com/media/lSfwBZPZTyRc9LcfPB/giphy.gif",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://media.giphy.com/media/d95tzIEGT0ACIa1hmK/giphy.gif",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ติ๊กเกอร์ ราคาถูก",
                                                  "color": "#0000EE",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "เหรียญเหมาเหรียญแท้ๆ",
                                                  "color": "#0000EE",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ติ๊กโปรทุกวัน",
                                                  "color": "#0000EE",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคาถูกสอบถามได้",
                                                  "color": "#0000EE",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "พ่อค้าแม่ค้าใจดี",
                                                  "color": "#0000EE",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                      {
                                      "type": "bubble",
                                      "styles": {
                                          "header": {
                                              "backgroundColor": '#0033FF'
                                              },
                                          "body": {
                                              "backgroundColor": '#FFFFFF'
                                              },
                                          "footer": {
                                              "backgroundColor": '#FFFF00'
                                               },
                                           },
                                            "header": {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "✯ʙᴏᴛ.ʟɪɴᴇ✯❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
                                                        "size": "md",
                                                        "weight": "bold",
                                                        "align": "center",
                                                        "color": "#00FF00"
                                                    }
                                                ]
                                            },
                                            "hero": {
                                              "type": "image",
                                              "url": "https://media.giphy.com/media/fAKVRDMzaBWjPYZAE5/giphy.gif",
                                              "size": "full",
                                              "aspectRatio": "20:13",
                                              "aspectMode": "cover",
                                              "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                              }
                                            },
                                        "body": {
                                          "type": "box",
                                          "layout": "horizontal",
                                          "spacing": "md",
                                          "contents": [
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 1,
                                              "contents": [
                                                {
                                                  "type": "image",
                                                  "url": "https://media.giphy.com/media/VzxOhWzWsAn8Vd9EC5/giphy.gif",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "size": "sm",
                                                  "gravity": "bottom"
                                                },
                                                {
                                                  "type": "image",
                                                  "url": "https://media.giphy.com/media/f757VmuGmz60ZNvu2v/giphy.gif",
                                                  "aspectMode": "cover",
                                                  "aspectRatio": "4:3",
                                                  "margin": "md",
                                                  "size": "sm"
                                                }
                                              ]
                                            },
                                            {
                                              "type": "box",
                                              "layout": "vertical",
                                              "flex": 2,
                                              "contents": [
                                                {
                                                  "type": "text",
                                                  "text": "ขายสคิป/เฟค/คิก/ธรรมดา",
                                                  "color": "#0000EE",
                                                  "gravity": "top",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ไฟลบอทล็อคอิน",
                                                  "color": "#0000EE",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ปล่อยเช่าเชิฟเวอร์",
                                                  "color": "#0000EE",
                                                  "gravity": "center",
                                                  "size": "xs",
                                                  "flex": 2
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ราคาสบายๆกระเป๋า",
                                                  "color": "#0000EE",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                                {
                                                  "type": "separator"
                                                },
                                                {
                                                  "type": "text",
                                                  "text": "ดูแลตลอดการใช้งาน",
                                                  "color": "#0000EE",
                                                  "gravity": "bottom",
                                                  "size": "xs",
                                                  "flex": 1
                                                },
                                              ]
                                            }
                                          ]
                                        },
                                        "footer": {
                                          "contents": [
                                            {
                                              "contents": [
                                                {
                                                  "contents": [
                                                    {
                                                      "text": "สนใจติดต่อ",
                                                      "size": "xl",
                                                      "action": {
                                                        "uri": "line://nv/profilePopup/mid=u7259162fa7000cd0443c1a52721ddc37",
                                                        "type": "uri",
                                                        "label": "Add Maker"
                                                      },
                                                      "margin": "xl",
                                                      "align": "center",
                                                      "color": "#000000",
                                                      "weight": "bold",
                                                      "type": "text"
                                                    }
                                                  ],
                                                  "type": "box",
                                                  "layout": "baseline"
                                                }
                                              ],
                                              "type": "box",
                                              "layout": "horizontal"
                                            }
                                          ],
                                          "type": "box",
                                          "layout": "vertical"
                                        }
                                   },
                                ]
                                data = {
                                    "type": "flex",
                                    "altText": "แจกเซลใช้ฟรี3เดือน",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                    }
                                }
                                sendTemplate(group, data)
                                time.sleep(1)
                            duc1(to, "ส่งคำประกาศจำนวน  {} กลุ่ม".format(str(len(groups))))
#==============================================================================#
                elif text.lower() == "แทค":
                        group = maxgie.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(maxgie.getProfile().mid)
                        maxgie.datamention(to,'แทคทุกคน',nama)
                elif text.lower() == "/แทค" or text.lower() == "tagall":
                    if msg._from in maxgieMID:
                        group = maxgie.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, jml = [], [], [], [], [], [], [], [], [], len(nama)
                        if jml <= 20:
                          mentionMembers(msg.to, nama)
                        if jml > 20 and jml < 40:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, len(nama)):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                        if jml > 40 and jml < 60:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, len(nama)):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                        if jml > 60 and jml < 80:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, len(nama)):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                        if jml > 80 and jml < 100:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for m in range (80, len(nama)):
                              nm5 += [nama[m]]
                          mentionMembers(msg.to, nm5)
                        if jml > 100 and jml < 120:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, len(nama)):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                        if jml > 120 and jml < 140:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for v in range (120, len(nama)):
                              nm7 += [nama[v]]
                          mentionMembers(msg.to, nm7)
                        if jml > 140 and jml < 160:
                          for i in range (0, 19):
                               nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for r in range (140, len(nama)):
                              nm8 += [nama[r]]
                          mentionMembers(msg.to, nm8)
                        if jml > 160 and jml < 180:
                          for i in range (0, 19):
                              nm1 += [nama[i]]
                          mentionMembers(msg.to, nm1)
                          for j in range (20, 39):
                              nm2 += [nama[j]]
                          mentionMembers(msg.to, nm2)
                          for k in range (40, 59):
                              nm3 += [nama[k]]
                          mentionMembers(msg.to, nm3)
                          for l in range (60, 79):
                              nm4 += [nama[l]]
                          mentionMembers(msg.to, nm4)
                          for n in range (80, 99):
                              nm5 += [nama[n]]
                          mentionMembers(msg.to, nm5)
                          for o in range (100, 119):
                              nm6 += [nama[o]]
                          mentionMembers(msg.to, nm6)
                          for q in range (120, 139):
                              nm7 += [nama[q]]
                          mentionMembers(msg.to, nm7)
                          for z in range (140, 159):
                              nm8 += [nama[z]]
                          mentionMembers(msg.to, nm8)
                          for f in range (160, len(nama)):
                              nm9 += [nama[f]]
                          mentionMembers(msg.to, nm9)

#==============================================================================#
                elif msg.text.lower().startswith("เขียน1 "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya ="http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya +"&chts=ff3333,70&chf=bg,s,ff3333"
                    maxgie.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("เขียน "):
                    sep = text.split(" ")
                    textnya = text.replace(sep[0] + " ", "")
                    text = "{}".format(textnya)
                    contact = maxgie.getContact(maxgieMID)
                    data = {
                        "type": "flex",
                        "altText": "มาอ่าน",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#00FFFF'
                                    },
                                 },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                "size": "full",
                                "aspectRatio":"1:1",
                                "aspectMode":"cover"
                            },
                            "body": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "{}".format(text),
                                        "color":"#000000",
                                        "wrap": True,
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xl"
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                elif msg.text.lower().startswith("ดึง "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       maxgie.findAndAddContactsByMid(ls)
                                       maxgie.inviteIntoGroup(to, [ls])
                                    except:
                                       duc1(to, "Limited !")
                elif msg.text.lower().startswith("สะกด"):
                  if msg.toType == 2:
                    data = text.replace("สะกด ","")
                    yud = data.split(' ')
                    yud = yud[0].replace(' ','_')
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            maxgie.unsendMessage(msg_id)
                            maxgie.sendMessage(to, yud,contentMetadata={"MSG_SENDER_NAME": str(maxgie.getContact(ls).displayName),"MSG_SENDER_ICON":"http://dl.profile.line-cdn.net/%s" % maxgie.getContact(ls).pictureStatus})
                elif msg.text.lower().startswith("ยูทูป"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#FF99CC"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#EE1289"
                                            },
                                            "footer": {
                                                "backgroundColor": "#FF99CC",
                                                "separator": True,
                                               "separatorColor": "#EE1289"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#EE1289",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=ub90fee136a68d4602aa10f734f24ff42"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#EE1289"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#EE1289",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#EE1289",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#EE1289",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#EE1289",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#EE1289",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {                                            
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                elif msg.text.lower().startswith("image "):
                                query = removeCmd("image", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "sendImage",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("เพลสโต "):
                                query = removeCmd("เพลสโต", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                elif msg.text.lower().startswith("รูป "):
                                query = removeCmd("รูป", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.boteater.co/googleimg?search={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                                        
                 #=====================================================================

                elif msg.text.lower().startswith("ยกเชิญ"):
                                if msg._from in maxgieMID:                                
                                    if msg.toType == 2:
                                        group = maxgie.getGroup(receiver)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        k = len(gMembMids)//20
                                        duc1(msg.to,"[ ยกค้างเชิญ จำนวน {} คน] \nรอสักครู่...".format(str(len(gMembMids))))
                                        num=1
                                        for i in range(k+1):
                                            for j in gMembMids[i*20 : (i+1)*20]:
                                                time.sleep(random.uniform(0.5,0.4))
                                                maxgie.cancelGroupInvitation(msg.to,[j])
                                                print ("[Command] "+str(num)+" => "+str(len(gMembMids))+" cancel members")
                                                num = num+1
                                            duc1(receiver,"รอสักครู่🕛เดียวยกต่อ 20 คน\n ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶ ")
                                            time.sleep(random.uniform(15,10))
                                        duc1(receiver,"[ ยกค้างเชิญ จำนวน {} คน เรียบร้อยแล้ว👏]".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        maxgie.sendMessage(receiver, None, contentMetadata={"STKID": "52002735","STKPKGID": "11537","STKVER": "1" }, contentType=7)
                                        gname = line.getGroup(receiver).name
                                        duc1(Notify,"[ ยกค้างเชิญ >> "+gname+"  <<] \n จำนวน {} คน เรียบร้อยแล้ว👏\n❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶".format(str(len(gMembMids))))
                                        time.sleep(random.uniform(0.95,1))
                                        maxgie.leaveGroup(receiver)
                                								
                                    duc1(receiver,"[ไม่มีค้างเชิญ แล้วนะ😁]")
                                    maxgie.sendMessage(receiver, None, contentMetadata={"STKID": "52114123","STKPKGID": "11539","STKVER": "1" }, contentType=7)
                                    maxgie.leaveGroup(receiver)
                #=====================================================================              
                elif msg.text.lower().startswith("/ยก"):
                    args = msg.text.lower().replace("/ยก","")
                    mes = 0
                    try:
                        mes = int(args[1])
                    except:
                        mes = 100
                        M = maxgie.getRecentMessagesV2(to, 100)
                        MId = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == maxgie.profile.mid:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            maxgie.unsendMessage(id)
                        for i in MId:
                            thread1 = threading.Thread(target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                        duc1(to, ' 📂「 กำลังยกเลิก 」📂\nยกเลิกทั้งหมด {} ข้อความ'.format(len(MId))) 
                        maxgie.unsendMessage(msg_id)                        
#-----------------------------------------------------------

                
                elif msg.text.lower().startswith("เพิ่มเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.findAndAddContactsByMid(ls)
                                maxgie.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Friendlist")
                elif msg.text.lower().startswith("ลบเพื่อน "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    n = len(maxgie.getAllContactIds())
                                    try:
                                        maxgie.deleteContact(ls)
                                    except:pass
                                    t = len(maxgie.getAllContactIds())
                                    maxgie.generateReplyMessage(msg.id)
                                    duc1(id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                elif msg.text.lower().startswith("บล็อค "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = maxgie.getContact(ls)
                                    maxgie.blockContact(ls)
                                maxgie.generateReplyMessage(msg.id)
                                duc1(id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                elif msg.text.lower().startswith("ทัก "):
                    sep = text.split(" ")
                    text = text.replace(sep[0] + " ","")
                    cond = text.split(" ")
                    jml = int(cond[0])
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                    for x in range(jml):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for receiver in lists:
                                contact = maxgie.getContact(receiver)
                                RhyN_(to, contact.mid)
                elif text.lower() == "/ลบรัน":
                      ag = maxgie.getGroupIdsInvited()
                      k = len(ag)//30
                      duc1(msg.to,"กำลังดำเนินการรอสักครู่...")
                      num=1
                      for i in range(k+1):
                         for j in ag[i*30 : (i+1)*30]:
                            maxgie.acceptGroupInvitation(j)
                            time.sleep(random.uniform(0.5,0.4))
                            maxgie.leaveGroup(j)
                            print ("[Command] "+str(num)+" => "+str(len(ag))+" cancel members")
                            num = num+1
                            time.sleep(random.uniform(0.30,0.30))
                         print ("[ ยกเลิกจำนวน {} กลุ่มเรียบร้อยแล้ว ]".format(str(len(ag))))
                         time.sleep(random.uniform(0.95,1))
                      duc1(to,"ยกเลิกจำนวน {} กลุ่มเรียบร้อยแล้ว".format(str(len(ag)))) 
#=====================================================================
#==============================================================================#
                elif text.lower() == 'คนสร้างกลุ่ม' or text.lower() == "แอด":
                    group = maxgie.getGroup(to)
                    cg = group.creator
                    c = cg.mid
                    name = cg.displayName
                    pp = cg.pictureStatus
                 #   profile = "https://profile.line-scdn.net/" + str(pp)
                    data = {
                        "type": "flex",
                        "altText": "แอดกลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type":"text",
                                        "text": "❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
                                        "size":"md",
                                       # "weight":"bold",
                                        "color":"#FF3333",
                                        "align":"center"
                                    },
                                    {
                                        "type": "text",
                                        "text": " "
                                    },
                                    {
                                        "type": "image",
                                        "url": "https://profile.line-scdn.net/" + str(pp),
                                        "size": "xl"
                                    },
                                    {
                                        "type":"text",
                                        "text":" "
                                    },
                                    {
                                       "type":"text",
                                       "text": name,
                                       "color":"#FF3333",
                                       "align":"center",
                                       "size":"xl",
                                    },
                                ]
                            }
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendContact(to, c)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = maxgie.getGroup(to)
                  #  
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "{ Group ID }\n" + gid.id)
                    maxgie.sendMessage(to, maxgie.getGroup(to).name, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+maxgie.getGroup(to).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~', 'type': 'mt', 'subText': "❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶", 'a-installUrl': 'https://line.me/ti/p/~', 'a-installUrl': ' https://line.me/ti/p/~', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~', 'i-linkUri': 'https://line.me/ti/p/~', 'id': 'mt000000000a6b79f9', 'text': '❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶', 'linkUri': 'https://line.me/ti/p/~'}, contentType=19)
                elif text.lower() == 'รูปกลุ่ม':
                    group = maxgie.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = maxgie.getGroup(to)
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "ชื่อกลุ่ม -> \n" + gid.name) 
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = maxgie.reissueGroupTicket(to)
                            maxgie.sendMessage(to, "ลิ้งของกลุ่ม : "+group.name+"\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'เปิดลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == False:
                           maxgie.unsendMessage(msg_id)
                           duc1(to, "🌟เปิดลิ้งเรียบร้อย🌟")
                        else:
                            group.preventedJoinByTicket = False
                            maxgie.updateGroup(group)
                            maxgie.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ปิดลิ้ง':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        if group.preventedJoinByTicket == True:
                           maxgie.unsendMessage(msg_id)
                           duc1(to, "🌟ปิดลิ้งเรียบร้อย🌟")
                        else:
                            group.preventedJoinByTicket = True
                            maxgie.updateGroup(group)
                            maxgie.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = maxgie.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ผู้สร้างกลุ่มนี้ลบชี"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(maxgie.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══『❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶』"
                    data = {
                        "type": "flex",
                        "altText": "กลุ่ม",
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "body": {
                                    "backgroundColor": '#EE1289'
                                 },
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                            #        {
                            #            "type": "image",
                            #            "url": path, 
                            #            "size": "xl"
                            #        },
                                    {
                                        "type": "text",
                                        "text": ret_,
                                        "color": "#000000",
                                        "wrap": True,
                                        "size": "md",
                                    },
                                ]
                            },
                        }
                    }
                    sendTemplate(to, data)
                    maxgie.sendImageWithURL(to, path)
                elif text.lower() == 'สมาชิก':
                    if msg.toType == 2:
                        group = maxgie.getGroup(to)
                        ret_ = "รายชื่อสามชิกในกลุ่มนี้\n"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n\nจำนวน {} คน".format(str(len(group.members)))
                        data = {
                            "type": "flex",
                            "altText": "กลุ่ม",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                        "backgroundColor": '#EE1289'
                                    },
                                },
                                   "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(maxgie.getContact(sender).pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "1:1",
                                            "aspectMode": "fit",
                                        },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": ret_,
                                            "color": "#000000",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif text.lower() == 'กลุ่มทั้งหมด':
                        groups = maxgie.groups
                        ret_ = "รายชื่อกลุ่มทั้งหมด :\n"
                        no = 0 + 1
                        for gid in groups:
                            group = maxgie.getGroup(gid)
                            ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n\nจำนวน {} กลุ่ม".format(str(len(groups)))
                        data = {
                            "type": "flex",
                            "altText": "Group list",
                            "contents": {
                                "type": "bubble",
                                "styles": {
                                    "body": {
                                         "backgroundColor": '#EE1289'
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type":"text",
                                            "text": ret_,
                                            "color": "#000000",
                                            "wrap": True,
                                            "size": "md"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                elif "อัพชื่อ " in text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.displayName = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Update to :\n" + string)
                        print ("Update Name")

                elif "อัพตัส " in msg.text.lower():
                    if msg._from in admin:
                        proses = text.split(" ")
                        string = text.replace(proses[0] + " ","")
                        profile_A = maxgie.getProfile()
                        profile_A.statusMessage = string
                        maxgie.updateProfile(profile_A)
                        maxgie.sendMessage(msg.to,"Succes Update :\n" + string)
                        print ("Update Bio Succes")
                        
                elif text.lower() == "อัพรูปโปร":
                    sets["changePictureProfile"] = True
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งรูปภาพที่จะอัพมาเลยครับ🌟")
                elif text.lower() == "อัพรูปกลุ่ม":
                    if msg.toType == 2:
                        if to not in sets["changeGroupPicture"]:
                            sets["changeGroupPicture"].append(to)
                        maxgie.unsendMessage(msg_id)
                        duc1(to, "🌟ส่งรูปภาพที่จะอัพมาเลยครับ🌟")
            
                elif text.lower() == 'เพื่อน':
                    contactlist = maxgie.getAllContactIds()
                    kontak = maxgie.getContacts(contactlist)
                    num=1
                    msgs="☢️รายชื่อเพื่อนทั้งหมด☢️"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n☢️รายชื่อเพื่อนทั้งหมด☢️\n\nมีดังต่อไปนี้ : %i" % len(kontak)
                    maxgie.sendMessage(msg.to, msgs)
            #      if msg.toType == 2:                
#
             #              ginfo = line.getGroup(receiver)
             #              try:
             #                  gcmid = ginfo.creator.mid
             #              except:
             #                  gcmid = "Error"
             #              if settings["lang"] == "JP":
             #                  line.inviteIntoGroup(receiver,[gcmid])
             #                  line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่ม")
             #              else:
             #                  line.inviteIntoGroup(receiver,[gcmid])
             #                  line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว")
                                
#====================================================================
                elif msg.text.lower()== "ตั้งติ๊กคนแทค":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "tag"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนแทค":
                    sets["messageSticker"]["listSticker"]["tag"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนแทคแล้วครับ🌟")
                elif msg.text.lower()== "ตั้งติ๊กคนเข้า":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "wc"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนเข้า":
                    sets["messageSticker"]["listSticker"]["wc"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนเข้าแล้วครับ🌟")
                elif msg.text.lower()== "ตั้งติ๊กคนออก":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "lv"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนออก":
                    sets["messageSticker"]["listSticker"]["lv"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนออกแล้วครับ🌟")
                elif msg.text.lower()== "ตั้งติ๊กคนแอด":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "add"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมา🌟")
                elif msg.text.lower() == "ลบติ๊กคนแอด":
                    sets["messageSticker"]["listSticker"]["add"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กคนแอดแล้วครับ🌟")
                elif msg.text.lower() == "ตั้งติ๊กมุดลิ้ง":
                    sets["messageSticker"]["addStatus"] = True
                    sets["messageSticker"]["addName"] = "join2"
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ส่งติ๊กที่จะใช้ลงมาครับ🌟")
                elif msg.text.lower() == "ลบติ๊กมุดลิ้ง":
                    sets["messageSticker"]["listSticker"]["join2"] = None
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ลบติ๊กมุดลิ้งแล้ว🌟")
                    
#=====================================================================
            elif msg.contentType == 1:
                if sets["changePictureProfile"] == True:
                    path = maxgie.downloadObjectMsg(msg_id)
                    sets["changePictureProfile"] = False
                    maxgie.updateProfilePicture(path)
                    maxgie.unsendMessage(msg_id)
                    duc1(to, "🌟ทำการเปลี่ยนแล้วครับ🌟")
                    
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                elif msg.contentType == 7:
                    if sets["Sticker"] == True:
                        try:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "「 Check Sticker 」\n"
                            ret_ += "\nSTKID : {}".format(stk_id)
                            ret_ += "\nSTKPKGID : {}".format(pkg_id)
                            ret_ += "\nSTKVER : {}".format(stk_ver)
                            ret_ += "\nLINK : line://shop/detail/{}".format(pkg_id)
                            print(msg)
                            maxgie.sendImageWithURL(to, "http://dl.stickershop.line.naver.jp/products/0/0/"+msg.contentMetadata["STKVER"]+"/"+msg.contentMetadata["STKPKGID"]+"/WindowsPhone/stickers/"+msg.contentMetadata["STKID"]+".png")
                            maxgie.sendMessage(to, str(ret_))
                        except Exception as error:
                            maxgie.sendMessage(to, str(error))
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in maxgieMID:
                            try:
                                maxgie.kickoutFromGroup(msg.to,[sender])
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟บอกแล้วอย่าพิมจุกไปดิครับ🌟")
                            except Exception as e:
                                print(e)
                    if "/ti/g/" in msg.text.lower():
                        if sets["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = maxgie.findGroupByTicket(ticket_id)
                                maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                maxgie.sendMessage(group.id,str(tagadd["m"]))
                            #    msgSticker = sets["messageSticker"]["listSticker"]["join2"]
                            #    if msgSticker != None:
                            #        sid = msgSticker["STKID"]
                            #        spkg = msgSticker["STKPKGID"]
                            #        sver = msgSticker["STKVER"]
                            #        sendSticker(group.id, str(sver), str(spkg), str(sid))
                                maxgie.unsendMessage(msg_id)
                                duc1(to, "🌟มุดเข้าลิ้งกลุ่ม %s เรียบร้อย 555🌟" % str(group.name))
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Sticker " + name + " Done...")
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
            elif msg.contentType == 7:
                if sets["Sticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    maxgie.sendMessage(to, str(ret_))
#=====================================================================
        if op.type == 22:
            if did["join"] == True:
                maxgie.leaveRoom(op.param1)              
        if op.type == 24:
            if did["join"] == True:
                maxgie.leaveRoom(op.param1)
#========================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == "หลุดยัง":                    
                    duc1(to,"↪[...ระบบยังทำงานปกติ...]↩\n🆙ʟɪɴᴇ𖤓ʙʏ𖤓❴ᴿˢᐪ❵⍣ᴊᴇsᴇʀ⓶")  
#========================================================================
            elif msg.contentType == 7: # Content type is sticker
                if settings['Sticker']:
                    if 'STKOPT' in msg.contentMetadata:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
                    else:
                        contact = maxgie.getContact(sender)
                        A = contact.displayName
                        stk = msg.contentMetadata['STKID']
                        spk = msg.contentMetadata['STKPKGID']
                        data={'type':'template','altText': str(A)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                        sendTemplate(to, data)
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
             #   elif msg.contentType == 7:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
            #    elif msg.contentType == 7:
            #        if "/ti/g/" in msg.text.lower():
            #            if sets["autoJoinTicket"] == True:
            #                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
            #                links = link_re.findall(text)
            #                n_links = []
            #                for l in links:
            #                    if l not in n_links:
            #                        n_links.append(l)
            #                for ticket_id in n_links:
            #                    group = maxgie.findGroupByTicket(ticket_id)
            #                    maxgie.acceptGroupInvitationByTicket(group.id,ticket_id)
                                #
             #                   maxgie.sendMessage(to, "เข้าไปสิงในห้องชื่อ %s 👈 เรียบร้อยแล้ว" % str(group.name))
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if tagadd["tags"] == True:
                             me = maxgie.getContact(sender)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in maxgieMID:
                                          cover = maxgie.getProfileCoverURL(sender)
                                          pp = me.pictureStatus
                                          profile = "https://profile.line-scdn.net/" + str(pp)
                                          name = me.displayName
                                          status = "\nสเตตัส\n" + me.statusMessage
                                          pk = str(tagadd["tag"])
                                          tz = pytz.timezone("Asia/Jakarta")
                                          timeNow = datetime.now(tz=tz)
                                          van2 = "✨เวลา:"+ datetime.strftime(timeNow,'%H:%M:%S')                                 	
                                          data = {
"type":"flex",
"altText": pk, 
"contents":{
"type": "carousel",
"contents": [
{
"type": "bubble",
"styles": {
"header": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#EE1289"},
"body": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"},
"footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#EE1289"}
},
"type": "bubble",
"body": {
"contents": [
{
"contents": [
{
"url": profile,
"type": "image"
},
{
"type": "separator",
"color": "#33FF33"
},
{
"url": profile,
"type": "image"
}
],
"type": "box",
"spacing": "md",
"layout": "horizontal"
},
{
"type": "separator",
"color": "#33FF33"
},
{
"contents": [
{
"text": name,
"size": "sm",
"align": "center",
"color": "#33FF33",
"wrap": True,
"weight": "bold",
"type": "text"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
{
"contents": [
{
"contents": [
{
"type": "text",
"text": pk, 
"align": "center",
"size": "sm",
"weight": "bold",
"color": "#33FF33",
"wrap": True
}
],
"type": "box",
"layout": "baseline"
}
],
"type": "box",
"layout": "vertical"
}
],
"type": "box",
"spacing": "md",
"layout": "vertical"
},
"footer": {
"type": "box",
"layout": "horizontal",
"spacing": "sm",
"contents": [
{
"text": " ✨➡ เวลาแทค :"+van2 +" \n ✨➡ ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶",
"size": "xs",
"margin": "none",
"color": "#33FF33",
"wrap": True,
"weight": "regular",
"type": "text"
}
]
}
}
]
}
}                                          
                                          sendTemplate(to, data)                        
        if op.type == 26:
            print ("[Self Bot ❴ᴿˢᐪ❵⍣ᴊsᴇʀ⓶ ] ")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.contentType == 0 and sender not in maxgieMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        if sets["tagsticker"] == True:
                            name = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                 if maxgieMID in mention["M"]:
                                    #  contact = maxgie.getContact(maxgieMID)
                                   #   a = contact.displayName
                                      msg = sets["messageSticker"]["listSticker"]["tag"]
                                      if msg != None:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+' ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
                                      else:
                                          contact = maxgie.getContact(maxgieMID)
                                          a = contact.displayName
                                          stk = msg['STKID']
                                          spk = msg['STKPKGID']
                                          data={'type':'template','altText': str(a)+'ส่งสติ๊กเกอร์','template':{'type':'image_carousel','columns':[{'imageUrl':'https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png'.format(stk),'action':{'type':'uri','uri':'https://line.me/S/sticker/{}'.format(spk)}}]}}
                                          sendTemplate(to, data)
#==============================================================================#
        if op.type == 19:
            if maxgieMID in op.param3:
                apalo["Talkblacklist"][op.param2] = True
        if op.type == 26 or op.type == 25:
            msg = op.message
            sender = msg._from
            try:
               if mc["wr"][str(msg.text)]:
                   maxgie.sendMessage(msg.to,mc["wr"][str(msg.text)])
            except:
              pass
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != maxgie.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if msg.text.lower().startswith("แปรงคท "):
                    delcmd = msg.text.split(" ")
                    getx = msg.text.replace(delcmd[0] + " ","")
                    maxgie.sendContact(msg.to,str(getx))
                if msg.text.startswith("ตั้งapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        get = msg.text.replace(delcmd[0]+" ","").split(";;")
                        kw = get[0]
                        ans = get[1]
                        mc["wr"][kw] = ans
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                        maxgie.sendMessage(msg.to,"คีย์เวิร์ด: " + str(kw) + "\nตอบกลับ: "+ str(ans))
                    except Exception as Error:
                        print(Error)
                if msg.text.startswith("ล้างapi "):
                    try:
                        delcmd = msg.text.split(" ")
                        getx = msg.text.replace(delcmd[0] + " ","")
                        del mc["wr"][getx]
                        maxgie.sendMessage(msg.to, "คำ " + str(getx) + " ล้างแล้ว")
                        f=codecs.open('sb.json','w','utf-8')
                        json.dump(mc, f, sort_keys=True, indent=4, ensure_ascii=False)
                    except Exception as Error:
                        print(Error)
                if msg.text.lower() == "เชคapi":
                    lisk = "[ คำตอบโต้ทั้งหมด ]\n"
                    for i in mc["wr"]:
                        lisk+="\nคีย์เวิร์ด: "+str(i)+"\nตอบโต้: "+str(mc["wr"][i])+"\n"
                    lisk+="\nวิธีล้างapi >\\<\nล้างapi ตามด้วยคำที่จะล้าง"
                    data = {"type": "text","text": "{}".format(lisk),"sentBy": {"label": "list API", "iconUrl": "https://obs.line-scdn.net/{}".format(maxgie.getContact(maxgieMID).pictureStatus),"linkUrl": "line://ti/p/~mj.ktc"}}
                    sendTemplate(to,data)
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != maxgie.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
#========================================================================
                if msg.contentType == 7:
                    if sets["messageSticker"]["addStatus"] == True:
                        name = sets["messageSticker"]["addName"]
                        if name != None and name in sets["messageSticker"]["listSticker"]:
                            sets["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            maxgie.sendMessage(to, "Success Added " + name)
                        sets["messageSticker"]["addStatus"] = False
                        sets["messageSticker"]["addName"] = None
                    if sets["addSticker"]["status"] == True:
                        stickers[sets["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[sets["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[sets["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        line.sendMessage(to, "Success Added sticker {}".format(str(sets["addSticker"]["name"])))
                        sets["addSticker"]["status"] = False
                        sets["addSticker"]["name"] = ""
                        
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != maxgieMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = maxgie.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = maxgie.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                maxgie.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    maxgie.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        maxgie.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            maxgie.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                maxgie.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    maxgie.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        maxgie.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
        if op.type in [26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                  to = receiver
               elif msg.toType == 2:
                  to = receiver
               if msg.contentType == 0:
                  if text is None:
                     return
                  else:
                    if receiver in temp_flood:
                      if temp_flood[receiver]["expire"] == True:
                        if msg.text == "/open":
                           temp_flood[receiver]["expire"] = False
                           temp_flood[receiver]["time"] = time.time()
                           maxgie.sendMessage(to,"Bot Actived")
                        return
                      elif time.time() - temp_flood[receiver]["time"] <= 5:
                         temp_flood[receiver]["flood"] += 1
                         if temp_flood[receiver]["flood"] >= 200:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            maxgie.unsendMessage(msg_id)
                            duc1(to, "🌟มีคนส่งข้อความเกิน200ระบบขอออกอัติโนมัติ🌟")
                            maxgie.leaveGroup(to)
                      else:
                       temp_flood[receiver]["flood"] = 0
                      temp_flood[receiver]["time"] = time.time()
                    else:
                      temp_flood[receiver] = {
                       "time": time.time(),
                       "flood": 0,
                       "expire": False
}
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            NOTIFIED_READ_MESSAGE(op)
    except Exception as error:
        logError(error)

#==============================================================================#
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

def run():
    while True:
        try:
            ops = maxgiePoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(maxgieBot(op))
                   maxgiePoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
if __name__ == "__main__":
    run()
