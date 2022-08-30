from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
import json
import socket
import threading
import wikipedia
import asyncio
import urllib
import base64
import threading

from threading import Thread
from pydub import AudioSegment
import math
import datetime
from datetime import datetime
import string
from google.cloud import texttospeech
import google.cloud.texttospeech as tts
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageCms
import nltk
from nltk.corpus import stopwords
from random import randrange
from nrclex import NRCLex
import requests
import os
import re
import shutil
import cv2
import pyttsx3
import subprocess

import os
import random
import random,string

# create handler for each connection

from datetime import date

import requests
import json

from time import sleep

import collections
import urllib, json

avatar=11
Language = "en-GB"
Gender = "MALE"
screen = "youtube"  # insta or else

cliplength = 0
talklength = 0
currentlaugh = 0
Count = 0
Sentanc = ""
Laugh = 0
Title = ""
Author = ""
Date = datetime.today()
subtitleletters = 0
lettercountsub = 0
width = 1080
height = 1920
FPS = 24

vframetalk = 0
facewidth = 0
faceheight = 0
shoulderwidth = 0
shoulderheight = 0
headtobodycorrection = 800 / 150  # adjusted for body size to fit head
initialheadwidth = width / 3
# camera control
lebelposition = 250
labellinespace = 50
fontsize = 48
subtitleposition = 300
zoomlimit = 50
lettersinline = 40
thumbnail = 0
intro = 1
engine = pyttsx3.init()
Zoom = 1
emotion = NRCLex("initiating global emotion") #initiating global emotion

intro = 1 #0 no intro, 1 with intro
vframes = 0
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
move = np.zeros((vframes, 16), dtype=int)
#move = np.zeros((vframes, 8), dtype=int)
cameradirector = np.zeros((vframes, 4), dtype=int) #stage zoom, camera move (right, left), avatar size, avatar placement

### initial setup of avatar
theme = 1
filenameoutput = ""
avatarpath = ".\myapp\Images\Avatar/{}"
avatarfacemask = avatarface = Image.open(avatarpath.format(avatar) + "/face1.png") #.convert('RGB')
#avatarfacemask = Image.open(avatarpath.format(avatar) + "/face1.jpg")
avatareyesmask = avatareyes = [Image.open(avatarpath.format(avatar) + "/eyes1.png"),
                  Image.open(avatarpath.format(avatar) + "/eyes2.png"),
                      Image.open(avatarpath.format(avatar) + "/eyes3.png"),
                      Image.open(avatarpath.format(avatar) + "/eyes4.png")]
avatarmouthmask = avatarmouth = [Image.open(avatarpath.format(avatar) + "/mouth1.png"), Image.open(avatarpath.format(avatar) + "/mouth2.png"), Image.open(avatarpath.format(avatar) + "/mouth3.png"), Image.open(avatarpath.format(avatar) + "/mouth4.png")]
brows = [Image.open(avatarpath.format(avatar) + "/brow1.png"),
         Image.open(avatarpath.format(avatar) + "/brow2.png"),
         Image.open(avatarpath.format(avatar) + "/brow3.png"),
         Image.open(avatarpath.format(avatar) + "/brow4.png")]

Faces = [Image.open(avatarpath.format(avatar) + "/face1.png")]


letters = string.ascii_lowercase
shepherd = ''.join(random.choice(letters) for i in range(10))
Body = [Image.open(avatarpath.format(avatar) + "/body1.png")]
Arm = [Image.open(avatarpath.format(avatar) + "/arm1.png")]

mic = Image.new("RGB", (150, 432), 0)
stage = Image.new("RGB", (width, height), 0)
rposition = [(0, 0), (0, 0)]

setscene = [0,  # 0 for sitting, > 0  for standing
            1,  # Zoom
            0,  # xlocation
            0  # ylocation
            ]
xface = 10
yface = 10
headangel = [(int(round(-xface * Zoom)), (int(round(-yface * Zoom)))), (0, (int(round(-yface * Zoom)))),
             ((int(round(xface * Zoom))), (int(round(-yface * Zoom)))),
             ((int(round(-xface * Zoom))), 0), (0, 0), ((int(round(xface * Zoom))), 0), ((int(round(-xface * Zoom))), (int(round(yface * Zoom)))),
             (0, (int(round(yface * Zoom)))), ((int(round(xface * Zoom))), (int(round(yface * Zoom))))]


import time

'''this is imports'''

def handle_client():
    global avatar

    import requests
    import json
    import urllib.request



    global cliplength, talklength, vframes, vframetalk

    path = ".\\user"

    newpath = threading.current_thread().name
    fullpath = path + newpath
    print(fullpath)
    os.makedirs(fullpath, 1)

    filemake = (fullpath + "\TempAudio.mp3")
    filemake2 = (fullpath + "\Joke.mp3")
    noise_video = (fullpath + "\my_noise.mp4")
    final_path = (fullpath+'.\my_Result.mp4')
    full_video = (fullpath+'\Fullvideo.mp4')
    FinalVideo = (fullpath+'\Finalvideo.mp4')
    thumbnail_path = (fullpath+'\my_thumbnail.PNG')
    print('done')
    url = "http://127.0.0.1:7000/api/"
    print('not done')
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    print(data[-1])
    responses_list = []

    for i in data:
        if i['unique'] == "null":
            get_null_id = i['id']
            responses_list.append(get_null_id)

    print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
    print(data[-1])
    print(responses_list)
    currrent = (responses_list[0])

    withformat = str(currrent) + "/"

    url2 = 'http://127.0.0.1:7000/details/' + withformat

    response = urllib.request.urlopen(url2)
    data = json.loads(response.read())

    mypara = data.get("JokeParagraph")
    print(mypara)

    title = data.get("VideoTitile")
    avatar_get = data.get("avatarid")
    username = data.get("username")
    json_id = data.get("id")
    myobj = {'unique': newpath}

    x = requests.put(url2, json=myobj)
    print(title)
    print(avatar_get)
    print(username)
    TitleName = title
    Creator = username
    avatar = avatar_get


    # ------------------setting start-----------------------------

    credential_path = "myapp\JSON/exalted-strata-114009-274905b5d1f0.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    # ----------------setting end--------------------

    def selectavatar(avatarselect):
        print("----------------Funtion4----------------------")
        global avatar, avatarface, Zoom, facewidth, setscene, faceheight, shoulderwidth, shoulderheight, headangel, Faces, Body, Arm, avatareyes, avatarmouth, rposition, move, avatareyesmask, avatarmouthmask, mic, brows, head, jar, headmask, jarmask, stage
        avatar = avatarselect

        setscene = [0,  # 0 for sitting, > 0  for standing
                    1,  # Zoom
                    0,  # xlocation
                    0  # ylocation
                    ]
        setscene[0] = randrange(1, 3)  # sitting down is 33% probability
        if setscene[0] != 0:
            setscene[1] = randrange(zoomlimit, 2 * zoomlimit, 10) / 100  # zoom from zoomlimit to 2 * zoomlimit
            Zoom = setscene[1]
            print(Zoom)
        else:
            Zoom = 1

        headangel = [(int(round(-xface * Zoom)), (int(round(-yface * Zoom)))), (0, (int(round(-yface * Zoom)))),
                     ((int(round(xface * Zoom))), (int(round(-yface * Zoom)))),
                     ((int(round(-xface * Zoom))), 0), (0, 0), ((int(round(xface * Zoom))), 0),
                     ((int(round(-xface * Zoom))), (int(round(yface * Zoom)))),
                     (0, (int(round(yface * Zoom)))), ((int(round(xface * Zoom))), (int(round(yface * Zoom))))]

        if avatar > 0:

            avatarpath = "./myapp/Images/Avatar/{}"
            avatarface = Image.open(avatarpath.format(avatar) + "/face1.png")  # .convert('RGB')

            avatarfacemask = avatarface

            avatareyes = [Image.open(avatarpath.format(avatar) + "/eyes1.png"),
                          Image.open(avatarpath.format(avatar) + "/eyes2.png"),
                          Image.open(avatarpath.format(avatar) + "/eyes3.png"),
                          Image.open(avatarpath.format(avatar) + "/eyes4.png")]

            avatareyesmask = avatareyes

            avatarmouth = [Image.open(avatarpath.format(avatar) + "/mouth1.png"),
                           Image.open(avatarpath.format(avatar) + "/mouth2.png"),
                           Image.open(avatarpath.format(avatar) + "/mouth3.png"),
                           Image.open(avatarpath.format(avatar) + "/mouth4.png")]

            avatarmouthmask = avatarmouth

            brows = [Image.open(avatarpath.format(avatar) + "/brow1.png"),
                     Image.open(avatarpath.format(avatar) + "/brow2.png"),
                     Image.open(avatarpath.format(avatar) + "/brow3.png"),
                     Image.open(avatarpath.format(avatar) + "/brow4.png")]

            Faces = [Image.open(avatarpath.format(avatar) + "/face1.png")]

            Body = [Image.open(avatarpath.format(avatar) + "/body1.png"),
                    Image.open(avatarpath.format(avatar) + "/body2.png"),
                    Image.open(avatarpath.format(avatar) + "/body3.png"),
                    Image.open(avatarpath.format(avatar) + "/body4.png")]

            Arm = [Image.open(avatarpath.format(avatar) + "/arm1.png"),
                   Image.open(avatarpath.format(avatar) + "/arm2.png"),
                   Image.open(avatarpath.format(avatar) + "/arm3.png"),
                   Image.open(avatarpath.format(avatar) + "/arm4.png"),
                   Image.open(avatarpath.format(avatar) + "/arm5.png"),
                   Image.open(avatarpath.format(avatar) + "/arm6.png"),
                   Image.open(avatarpath.format(avatar) + "/arm7.png"),
                   Image.open(avatarpath.format(avatar) + "/arm8.png"),
                   ]

            Chairpath = "./myapp/Images/Theme/Chair/Chair{}.png"
            Chair = [Image.open(Chairpath.format(1))
                     ]

            # resizing
            xwidth, yheight = avatarface.size
            x1 = round(width / 2)
            y1 = round(x1 * (yheight / xwidth))
            avatarface = avatarface.resize((x1, y1), Image.NEAREST)
            avatarfacemask = avatarfacemask.resize((x1, y1), Image.NEAREST)
            x = x1 / xwidth
            y = y1 / yheight

            i = 0
            for image in avatareyes:
                xwidth, yheight = image.size
                avatareyes[i] = image.resize(
                    (int(Zoom * initialheadwidth), int(Zoom * initialheadwidth * yheight / xwidth)), Image.NEAREST)
                # avatareyesmask[i] = avatareyesmask[i].resize((int(xwidth * x), int(yheight * y)), Image.NEAREST)
                i = i + 1

            i = 0
            for image in avatarmouth:
                xwidth, yheight = image.size
                avatarmouth[i] = image.resize(
                    (int(Zoom * initialheadwidth), int(Zoom * initialheadwidth * yheight / xwidth)), Image.NEAREST)
                # avatarmouthmask[i] = avatarmouthmask[i].resize((int(xwidth * x), int(yheight * y)), Image.NEAREST)
                i = i + 1

            i = 0
            for image in brows:
                xwidth, yheight = image.size
                brows[i] = image.resize((int(Zoom * initialheadwidth), int(Zoom * initialheadwidth * yheight / xwidth)),
                                        Image.NEAREST)
                # brows[i] = brows[i].resize((int(xwidth * x), int(yheight * y)), Image.NEAREST)
                i = i + 1

            i = 0
            for image in Faces:
                xwidth, yheight = image.size
                Faces[i] = image.resize((int(Zoom * initialheadwidth), int(Zoom * initialheadwidth * yheight / xwidth)),
                                        Image.NEAREST)
                facewidth, faceheight = Faces[i].size
                # Faces[i] = Faces[i].resize((int(xwidth * x), int(yheight * y)), Image.NEAREST)
                i = i + 1

            i = 0

            for image in Body:
                xwidth, yheight = image.size
                Body[i] = image.resize((int(Zoom * (xwidth * headtobodycorrection) * (facewidth / initialheadwidth)),
                                        int((int(Zoom * (xwidth * headtobodycorrection) * (
                                                    facewidth / initialheadwidth)) / xwidth) * yheight)), Image.NEAREST)
                shoulderwidth, shoulderheight = Body[i].size
                i = i + 1

            i = 0

            for image in Arm:
                xwidth, yheight = image.size
                Arm[i] = image.resize((shoulderwidth, shoulderheight), Image.NEAREST)
                i = i + 1

            rposition = [(0, 0), (
            0, 0)]  # position of eyes and mouth relevant to left top corner of face (xeyes, yeyes),(xmouth,ymouth)

            if setscene[0] != 0:
                setscene[2] = randrange(round(-(width - facewidth) / 2), round((width - facewidth) / 2) + 1)
                if Zoom > 1:
                    setscene[3] = randrange(-int(round(height / 6)), int(round(height / 6)))
                else:
                    setscene[3] = randrange(0, int(round(height / 6)))
            else:
                setscene[3] = 0
        else:
            photo = Image.open(r"./myapp/Images/Avatar/0/photo.jpg")
            photo1 = photo2 = photo.resize((400, 600), Image.NEAREST)

            head = photo1.crop((0, 0, 400, 470))  # .crop((left, top, right, bottom))
            jar = photo2.crop((0, 470, 400, 600))
            # open(r"./Images/Avatar/0/head.jpg")
            # jar = Image.open(r"./Images/Avatar/0/jar.jpg")
            headmask = Image.open(r"./myapp/Images/Avatar/0/headmask.jpg").convert("L")
            jarmask = Image.open(r"./myapp/Images/Avatar/0/jarmask.jpg").convert("L")
            facewidth, faceheight = head.size
            jarwidth, jarheight = jar.size
            x = round(width / 2)
            y = round(x * (faceheight / facewidth))
            head = head.resize((x, y), Image.NEAREST)
            jar = jar.resize((x, round(x * (jarheight / jarwidth))), Image.NEAREST)
            xwidth, yheight = head.size
            xxwidth, yyheight = jar.size
            headmask = headmask.resize((xwidth, yheight), Image.NEAREST)
            jarmask = jarmask.re((xxwidth, yyheight), Image.NEAREST)

            x1 = xwidth
            y1 = yheight

        if avatar == 6 or avatar == 8:
            bodyposition = int(round((height / 3) + (faceheight * (130 / 250) * 0.85))) + setscene[
                3]
        else:
            bodyposition = int(round((height / 3) + (faceheight * 0.85))) + setscene[3]

        move = np.full((vframes, 16),
                       [int(round((width / 2 - facewidth / 2))) + setscene[2],  # Head left-top cornner X coordinate
                        int(round((height / 3))) + setscene[3],  # Head left-top cornner Y coordinate
                        0,
                        int(round((width / 2 - shoulderwidth / 2))) + setscene[2],  # body location point
                        bodyposition,  # int(round((height / 3 + faceheight))),
                        0,
                        0,  # eyes select
                        0,  # mouth select
                        0,  # brows select
                        0,  # head direction select
                        0,  # Body select
                        0,  # Arm select
                        0,
                        0,
                        0,
                        0], dtype=int)  # fill move matrix with initial position

    def selecttheme():
        print("----------------Funtion5----------------------")
        global Chair, stage, theme

        theme = randrange(1, 5)
        if avatar == 3 or avatar == 2 or avatar == 1 or avatar == 5 or avatar == 6 or avatar == 7 or avatar == 8 or avatar == 9 or avatar == 10 or avatar == 11:
            stagefile = "./myapp/Images/Theme/stage/{}/white1.png"
            stage = Image.open(stagefile.format(screen)).convert('RGB')

        else:

            themepath = "./myapp/Images/Theme/stage/{}/{}.jpg"
            stage = Image.open(themepath.format(screen, theme)).convert('RGB')

        stage = stage.resize((width, height), Image.NEAREST)
        # stage = stage.crop((left, top, right, bottom))

    def searchimage(word):
        print("----------------Funtion6----------------------")
        url = 'https://www.googleapis.com/customsearch/v1?key={}&cx={}&searchType=image&q={}&num=10'
        key = "AIzaSyCa5bAvXrJEkHb0hdCx2v6rrKI2j0Kgnjg"
        cx = "4028ae6fc2c9dd6b7"
        q = word
        extension = ["jpg", "jpeg"]
        i = 1
        j = 1
        data = requests.get(url.format(key, cx, q)).json()
        ilist = []
        search_items = data.get("items")

        for i, search_item in enumerate(search_items, start=1):
            try:
                link = search_item.get("link")
                image = requests.get(link, stream=True)
                if image.status_code == 200:
                    m = re.search(r'[^\.]+$', link)
                    if m.group() in extension:
                        # filename = './{}-{}.{}'.format("Item", j, m.group())
                        ilist.append(link)

                        j = j + 1
            except:
                pass
            i += 1
            if len(ilist) > 0:
                x = randrange(0, len(ilist))
                # print(len(ilist))
                #  print(x)
                link = ilist[x]
                image = requests.get(link, stream=True)
                with open("./Images/TVimage.jpg", 'wb') as f:
                    image.raw.decode_content = True
                    shutil.copyfileobj(image.raw, f)

    def twodigit(item):
        print("----------------------function15---------------------------")
        if len(str(item)) == 1:
            return "0" + str(item)
        else:
            return str(item)

    def setscreenlabel():
        print("-----------------------function16----------------------------")
        global Title, Author, Date, filenameoutput
        Title = TitleName
        Author = Creator
        Date = datetime.today().strftime('%d-%m-%y')
        now = datetime.now()

        filenameoutput = str(now.year) + twodigit(str(
            now.month)) + twodigit(str(now.day)) + "_" + twodigit(str(now.hour)) + twodigit(
            str(now.minute)) + "_" + Title.translate({ord(c): None for c in string.whitespace})

    def addvideo():

        #   finalclip = VideoFileClip("./Videos/FinalJoke.mp4")
        #   vi = VideoFileClip("./Videos/vidout.mp4")
        #   final = concatenate_videoclips([finalclip, vi], "chain")
        #   final.write_videofile("./Videos/FinalJoke.mp4", fps=24)
        #   time.sleep(3)
        #   finalclip.close()
        #   vi.close()

        # A list of the paths of your videos
        videos = [final_path, noise_video]  # appending finaljoke to include vidout

        # Create a new video
        video = cv2.VideoWriter(full_video, fourcc, float(FPS), (
        width, height))  # finaljoke will be added to new_video then vidout will be added to new_video

        # Write all the frames sequentially to the new video
        for v in videos:
            curr_v = cv2.VideoCapture(v)
            while curr_v.isOpened():
                r, frame = curr_v.read()  # Get return value and curr frame of curr video
                if not r:
                    break
                video.write(frame)  # Write the frame
        video.release()  # Save the video

    def Actor():
        print('-------------------------function18--------------------------------------------------')
        global vframes, subtitleletters, lettercountsub, thumbnail
        c = 0
        cxx = 0
        postremains = 0


        video = VideoWriter(noise_video, fourcc, FPS, (width, height))

        #    directing = cameraset()

        # setmovement(x, y) # update movement table
        # print(vframes, len(dbfs))
        framenumber = 0
        backgroundimagelist = ProperNounExtractor(Sentanc)
        # print(backgroundimagelist)
        selectthumbnail = randrange(1, vframes)
        for _ in range(vframes):  # add Actor frame by frame based on Move coordinates

            if theme == 0:
                frame = np.random.randint(0, 70,
                                          (height, width, 3),
                                          dtype=np.uint8)  # build black background
                PIL_image1 = Image.fromarray(frame.astype('uint8'), 'RGB')

            else:
                PIL_image1 = Image.new("RGB", (width, height), 0)
                PIL_image1.paste(stage, (0, 0))

            if len(backgroundimagelist) > 20:
                if framenumber == backgroundimagelist[c][1]:  # fitch TVimage from custom search
                    # print(framenumber, c)
                    searchimage(backgroundimagelist[c][0])
                    cxx = c
                    if c < (len(backgroundimagelist) - 1):
                        c = c + 1
                try:
                    if ((framenumber >= (backgroundimagelist[cxx][1])) and (framenumber <= (
                            backgroundimagelist[cxx][1] + (FPS * 2)))):  # load image and keep image for 2 seconds
                        TVimage = Image.open(r"./Images/TVimage.jpg")
                        TVimagewidth, TVimagehight = TVimage.size
                        TVimage = TVimage.resize(
                            (int(width / (10 / 4)), int(TVimagehight / TVimagewidth * width / (10 / 4))), Image.NEAREST)
                        PIL_image1.paste(TVimage, (int((55 / 100) * width), int(width / 10)))
                except:
                    pass

            if avatar == 0:
                face = head
                face1 = face.rotate(move[framenumber][2])
                jar1 = jar.rotate(move[framenumber][5])
                headmask1 = headmask.rotate(move[framenumber][2])
                jarmask1 = jarmask.rotate(move[framenumber][5])
                PIL_image1.paste(face1, (move[framenumber][0], move[framenumber][1]), headmask1)
                PIL_image1.paste(jar1, (move[framenumber][3], move[framenumber][4]), jarmask1)

            else:  # avatar > 0:
                if framenumber < vframetalk:
                    ontalk = 1
                else:
                    ontalk = 0

                draw = ImageDraw.Draw(PIL_image1)
                font = ImageFont.truetype("arial.ttf", fontsize)
                if Language == "ar-XA":
                    # draw.text((50, lebelposition), Title, font=font, fill="#000", direction='rtl')
                    draw.text((50, lebelposition), Title, font=font, fill="#000")
                else:
                    draw.text((50, lebelposition), Title, font=font, fill="#000")
                draw.text((50, lebelposition + font.getsize(Title)[1]), Author, font=font, fill="#000")
                today = date.today()


                # cartoon = cv2.bitwise_and(asset, asset, mask=edge_mask(asset))

                cartooned = Body[move[framenumber][10]]
                # PIL_image1.paste(Body[move[framenumber][10]], (move[framenumber][3], move[framenumber][4]), Body[move[framenumber][10]])
                PIL_image1.paste(cartooned, (move[framenumber][3], move[framenumber][4]), cartooned)

                cartooned = Arm[move[framenumber][11]]
                # PIL_image1.paste(Arm[move[framenumber][11]], (move[framenumber][3], move[framenumber][4]), Arm[move[framenumber][11]])
                PIL_image1.paste(cartooned, (move[framenumber][3], move[framenumber][4]), cartooned)

                cartooned = Faces[0]
                # PIL_image1.paste(Faces[0], (move[framenumber][0], move[framenumber][1]), Faces[0])  # avatarfacemask.convert("L")
                PIL_image1.paste(cartooned, (move[framenumber][0], move[framenumber][1]),
                                 cartooned)  # avatarfacemask.convert("L")

                cartooned = avatareyes[move[framenumber][6]]
                PIL_image1.paste(cartooned, (
                (move[framenumber][0] + rposition[0][0] + round(1.2 * headangel[(move[framenumber][9])][0])),
                (move[framenumber][1] + rposition[0][1] + headangel[(move[framenumber][9])][1])),
                                 cartooned)  # .convert('L')

                cartooned = avatarmouth[move[framenumber][7]]

                PIL_image1.paste(cartooned,
                                 ((move[framenumber][0] + rposition[1][0] + headangel[(move[framenumber][9])][0]),
                                  (move[framenumber][1] + rposition[1][1] + headangel[(move[framenumber][9])][1])),
                                 cartooned)  # .convert("L"))

                cartooned = brows[move[framenumber][8]]
                PIL_image1.paste(cartooned,
                                 ((move[framenumber][0] + rposition[1][0] + headangel[(move[framenumber][9])][0]),
                                  (move[framenumber][1] + rposition[1][1] + + headangel[(move[framenumber][9])][1])),
                                 cartooned)
            # PIL_image1.show()
            ####PIL_image1.paste(mic, (move[0][0]-mic.width-20, move[0][1]+250), mic)
            # Image._show(avatarmouth[move[framenumber][7]])
            # Image._show(PIL_image1)
            # video.write(np.asarray(PIL_image1))
            print("------------------Vframes-----------------------")
            print(vframetalk)
            print(lettercountsub)
            print(subtitleletters)
            subtitleprogress = round(subtitleletters * (lettercountsub / vframetalk))
            print(subtitleprogress)
            subtitlepointer = round(1.2 * subtitleprogress)
            n = lettersinline
            writesubtitle = Sentanc[:subtitlepointer]
            print(n)
            print(subtitlepointer)
            if len(Sentanc) < lettersinline:  # maximium subtitle length
                print("666666666666666666666666666666666666")
                print("i am inside very first")
                n = len(Sentanc)
            else:
                print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
                print("first else part")
                n = lettersinline
            if subtitleletters <= subtitleprogress:
                print("uuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
                print(" i am on second if part")
                writesubtitle = Sentanc[(subtitlepointer - n): subtitleletters]
            else:
                if subtitlepointer < n:  # maximum letter in subtitle raw
                    print("9999999999999999999999999999999999999")
                    print("i am now if else if part")
                    writesubtitle = Sentanc[:subtitlepointer]
                else:
                    print("0000000000000000000000000000000000")
                    print("now i am inside lastly")
                    writesubtitle = Sentanc[(subtitlepointer - n): subtitlepointer]

                # cv2.putText(PIL_image1, writesubtitle, ((int(width * 0.33 - 20 * 10)), height - 300), cv2.FONT_HERSHEY_SIMPLEX,
                #                2, (250, 250, 250), 3, cv2.LINE_AA, False)  # subtitle

            draw = ImageDraw.Draw(PIL_image1)
            wsubtitle, hsubtitle = font.getsize(writesubtitle)
            xsubtitle = (int(width * 0.33 - 250))
            ysubtitle = height - subtitleposition
            draw.rectangle((xsubtitle, ysubtitle, xsubtitle + wsubtitle, ysubtitle + hsubtitle),
                           fill=(0, 0, 0, 127))  # add subtitle black background
            if Language == "ar-XA":
                # draw.text((xsubtitle, ysubtitle), writesubtitle, font=font, fill=(255, 255, 255, 20), direction='rtl') #not supported without libraqm'
                draw.text((xsubtitle, ysubtitle), writesubtitle, font=font, fill=(255, 255, 255, 127))
            else:
                draw.text((xsubtitle, ysubtitle), writesubtitle, font=font, fill=(255, 255, 255, 127))

            lettercountsub = lettercountsub + 1

            video.write(cv2.cvtColor(np.asarray(PIL_image1), cv2.COLOR_RGB2BGR))

            if framenumber == selectthumbnail:
                if thumbnail == 0:
                    PIL_image1.save(thumbnail_path)


            #  print(framenumber, vframes)
            framenumber = framenumber + 1


        video.release()
        lettercountsub = 0
        thumbnail == 0
    def setscreensize():
        print("------------------function14-------------------------")
        global width, height, FPS, lebelposition, labellinespace, fontsize, subtitleposition, zoomlimit, lettersinline
        if screen == "insta":
            width = 1080
            height = 1920
            FPS = 24
            lebelposition = 250
            labellinespace = 50
            fontsize = 80
            subtitleposition = 300
            zoomlimit = 40
            lettersinline = 30

        else:
            width = 1280
            height = 720
            FPS = 24
            lebelposition = 50
            labellinespace = 25
            fontsize = 80
            subtitleposition = 100
            zoomlimit = 30
            lettersinline = 45

    def createmovement(beats):
        print("----------------------Function22-------------------------------")
        global move
        # print(len(beats), len(move), vframes)
        j = 0
        hold = holdarms = holdbody = 0

        for i in beats:
            # print(j)
            # move[j][4] = move[j][4] + i * 2

            if i > 5:
                r = randrange(1, 48)  # probability of blink once two second if voice loud
            else:
                r = randrange(1, 24)  # probability of blink once a second if voice is low

            if r == 1:
                move[j][6] = 3  # blink
            else:
                if hold == 0:
                    if r % 6 == 1:
                        move[j][6] = 1  # eyes right open

                    elif r % 6 == 2:
                        move[j][6] = 2  # eyes left open

                    else:
                        move[j][6] = 0  # eyes open
                    hold = 24
                    pose = move[j][6]
                else:
                    move[j][6] = pose
                    hold = hold - 1

            move[j][9] = 4
            if i < 15:
                r = randrange(1, 72)
                if r == 17:
                    move[j][9] = move[j - 1][9] - 1
                elif r == 23:
                    move[j][9] = move[j - 1][9] + 1
                else:
                    move[j][9] = move[j - 1][9]
            else:
                move[j][9] = 4
            if move[j][9] < 0 or move[j][9] > 8:
                move[j][9] = 0
            # print([move[j][9]])

            if i > 10:  # select mouth wide depending on volume
                move[j][7] = 3
            elif i > 5:
                move[j][7] = 2
            elif i > 0:
                move[j][7] = 1
            else:
                move[j][7] = 0

            if i > 0:
                print(emotion.affect_frequencies)
                if emotion.affect_frequencies["anger"] > 0 or emotion.affect_frequencies["disgust"] > 0:
                    move[j][8] = 2
                elif emotion.affect_frequencies["sadness"] > 0 or emotion.affect_frequencies[
                    "fear"] > 0:  # eyebrows select based on emotion
                    move[j][8] = 3
                elif emotion.affect_frequencies["surprise"] > 0:
                    move[j][8] = 1
                else:
                    move[j][8] = 0
            else:
                move[j][8] = 0

            if holdbody == 0:
                if setscene[0] != 0:

                    move[j][10] = randrange(0, 4)

                else:

                    move[j][10] = randrange(2, 4)

                holdbody = 24
                posebody = move[j][10]

            else:

                holdbody = holdbody - 1
                move[j][10] = posebody

            if holdarms == 0:
                if i > 0:
                    # print(emotion.affect_frequencies)
                    if emotion.affect_frequencies["anger"] > 0 or emotion.affect_frequencies["disgust"] > 0:
                        move[j][11] = randrange(6, 8)

                    elif emotion.affect_frequencies["sadness"] > 0 or emotion.affect_frequencies[
                        "fear"] > 0:  # eyebrows select based on emotion
                        move[j][11] = randrange(3, 6)
                    elif emotion.affect_frequencies["surprise"] > 0:
                        move[j][11] = randrange(6, 8)
                    else:
                        move[j][11] = randrange(0, 8)
                else:
                    move[j][11] = randrange(0, 8)

                holdarms = 24
                posearms = move[j][11]

            else:
                holdarms = holdarms - 1

                move[j][11] = posearms

            j = j + 1

    def createvideo(dbfs):
        print("------------------------function23-------------------------------")
        global vframes, vframetalk, subtitleletters
        vframes = round(int(FPS * cliplength))
        vframetalk = round(int(FPS * talklength))
        createmovement(dbfs)
        subtitleletters = len(Sentanc)
        Actor()
        addvideo()



    def ProperNounExtractor(text):
        print("----------------Funtion7----------------------")
        # print('PROPER NOUNS EXTRACTED :')
        wordlist = [] * 2
        exclusionlist = ["today", "yesterday", "tomorrow", "now", "lord", "god"]
        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            words = [word for word in words if word not in set(stopwords.words('english'))]
            # print(words)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            for (word, tag) in tagged:
                if (tag == 'NN' or tag == 'NNP' or tag == 'NNS' or tag == 'NNPS' or tag == 'VBP') and len(
                        word) > 2 and (word.lower() not in exclusionlist) and (
                        word not in str(wordlist)):  # If the word is a proper noun
                    # print(word)
                    # print(len(text))
                    # print(text.find(word))
                    wordlist.append((word, int(vframetalk * (text.find(word) / len(text)))))
                    # break
        # print(wordlist)
        return wordlist

    def excludelaugh(
            i):  # not finding one of the stars would return -1 that disables the min() sentance to locate next *'s
        print("----------------Funtion8----------------------")
        if i > -1:
            return i
        else:
            return 100000
        pass

    def AudiodBFS(audioclipframes):
        print("--------------------funtion10--------------------------")
        Actual_dBFS = []
        modified_dBFS = []
        skip = int(int((len(audioclipframes) / audioclipframes.duration_seconds)) / FPS)
        j = 0

        for i in range(0, len(audioclipframes), int(round(len(audioclipframes) / vframetalk))):

            if math.isinf(audioclipframes[i].dBFS):  # canceling infinity values
                # Actual_dBFS.append(0)
                modified_dBFS.append(0)
            else:
                modified_dBFS.append(abs(int(audioclipframes[i].dBFS)) / 4)

            j = j + 1

        # print(len(audioclipframes), int((len(audioclipframes)/audioclipframes.duration_seconds)), FPS, round(int(FPS * cliplength)), 24*audioclipframes.duration_seconds, 24*talklength, 24*cliplength)
        for i in range(len(modified_dBFS), vframes):
            modified_dBFS.append(0)

        # print(len(modified_dBFS), vframes)
        # for i in range(0, len(audioclipframes), FPS):

        return modified_dBFS

    def voicedata():
        print("----------------------------Funtion11---------------------------------------")

        sound1 = AudioSegment.from_file(filemake, format="mp3")

        # print(len(AudiodBFS(sound1)))
        return AudiodBFS(sound1)

    def addvoice(laugh):
        print("----------------Funtion13----------------------")
        global cliplength, talklength, vframes, vframetalk

        sound1 = AudioSegment.from_file(filemake, format="mp3")
        talklength = sound1.duration_seconds
        sound1 = sound1 + 6

        laughfile = "./myapp/Sounds/laugh/{}.mp3"
        sound2 = AudioSegment.from_file(laughfile.format(int(laugh)), format="mp3")
        # cliplength = sound1.duration_seconds + sound2.duration_seconds
        combined = sound1.append(sound2, crossfade=500)
        cliplength = combined.duration_seconds
        print("------------------------Vframes----------------------------------")
        print(vframes)
        c = threading.current_thread().name
        print(c)
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")



        introsoundpath = "./myapp/Sounds/intromusic/intro{}.mp3"
        introsound = AudioSegment.from_file(introsoundpath.format(randrange(1, 7)), format="mp3")
        introsound = introsound + 8
        introclap = AudioSegment.from_file(introsoundpath.format(0), format="mp3")
        introclap = introclap + 8

        introsound = introsound.append(introclap, crossfade=2400)
        combined1 = introsound.append(combined, crossfade=1000)
        combined1.export(filemake2, format="mp3")

        if vframes != 0:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            introsound = introsound.append(introclap, crossfade=2400)
            combined_new = introsound.append(combined, crossfade=1000)

            combined_new.export(filemake2, format="mp3")

        vframes = round(int(FPS * cliplength))
        vframetalk = round(int(FPS * talklength))

        # combined = sound3 + louder + sound2
        # combined.export("./Sounds/Joke.mp3", format="mp3")

    def texttovoice(sentanc):
        print("----------------Funtion9----------------------")
        global emotion
        """   engine.setProperty('rate', 150)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.save_to_file(sentanc, './myapp/Sounds/TempAudio.mp3')
        engine.runAndWait()
        """
        # v = gTTS(sentanc, lang="en", slow =True)
        # v.save("./Sounds/TempAudio.mp3") #initiat temp file
        if sentanc.strip() == "":
            sentanc = "eh"
        client = texttospeech.TextToSpeechClient()

        synthesis_input = texttospeech.SynthesisInput(text=sentanc)
        voice = texttospeech.VoiceSelectionParams(language_code=Chlist[Ch][0], name=Chlist[Ch][1],
                                                  ssml_gender=Chlist[Ch][2])

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=0.9,  # [0.25, 4.0]
            pitch=0  # [-20.0, 20.0]
        )

        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        with open(filemake, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)

        for i in range(len(sentanc)):
            emotion = NRCLex(sentanc)

    def soundvideo():

        subprocess.run(['ffmpeg' , '-i' ,full_video, '-i' ,filemake2 ,'-f', 'mp4' ,'-b', '100k' ,FinalVideo])






    def excludelaugh(
            i):  # not finding one of the stars would return -1 that disables the min() sentance to locate next *'s
        print("----------------Funtion8----------------------")
        if i > -1:
            return i
        else:
            return 100000
        pass

    def list_of_voices(language_code=None, genders=None):
        print("----------------Funtion3----------------------")
        client = tts.TextToSpeechClient()
        response1 = client.list_voices(language_code=language_code)
        voices = sorted(response1.voices, key=lambda voice: voice.name)
        print(f" Voices: {len(voices)} ".center(60, "-"))
        Voicepersonality = []
        for voice in voices:
            languages = ", ".join(voice.language_codes)
            name = voice.name
            gender = tts.SsmlVoiceGender(voice.ssml_gender).name
            rate = voice.natural_sample_rate_hertz
            if name.find("Standard") > 0:
                if genders == None or gender == genders:
                    if gender == "FEMALE":
                        gen = 2
                    else:
                        gen = 1
                    Voicepersonality.append((languages, name, gen, rate))  # (language, name, gender, rate)
        return Voicepersonality

    setscreensize()
    # print(width, height)
    setscreenlabel()

    new = cv2.VideoWriter(final_path, fourcc, float(FPS), (width, height))

    if intro == 1:  # creating intro frames
        print("---------------creating into frames-------------------")
        introframes = (
                                  FPS * 5) - FPS / 2  # length of intro music is 5 seconds and accounting to 500 miliseconds cross over
        introimagepath = "./myapp/Images/Theme/intro/{}/{}.png"
        introimage = Image.open(introimagepath.format(screen, "black2")).convert('RGB')
        introimage = introimage.resize((width, height), Image.NEAREST)
        PIL_image1 = Image.new("RGB", (width, height), 0)
        fullimagepath = "./myapp/Images/Avatar/{}/full1.png"
        fullimage = Image.open(fullimagepath.format(avatar)).convert('RGB')
        fullx, fully = fullimage.size
        if screen == "insta":
            fullimage = fullimage.resize((int(round(700 * (fullx / fully))), 700), Image.NEAREST)
        else:
            fullimage = fullimage.resize((int(round(500 * (fullx / fully))), 500), Image.NEAREST)

        for i in range(round(int(introframes))):
            PIL_image1.paste(introimage, (0, 0))
            PIL_image1.paste(fullimage, (int(round(2 * width / 3)) - 100, lebelposition))
            draw = ImageDraw.Draw(PIL_image1)
            font = ImageFont.truetype("arial.ttf", fontsize)
            if Language == "ar-XA":
                # draw.text((50, lebelposition), Title, font=font, fill="#000", direction='rtl')
                draw.text((50, lebelposition), Title, font=font)
            else:
                draw.text((50, lebelposition), Title, font=font)
            draw.text((50, lebelposition + font.getsize(Title)[1]), Author, font=font)

            new.write(cv2.cvtColor(np.asarray(PIL_image1), cv2.COLOR_RGB2BGR))

    else:

        for _ in range(1):
            frame = np.random.randint(0, 10,
                                      (height, width, 3),
                                      dtype=np.uint8)  # build black background

            PIL_image1 = Image.fromarray(frame.astype('uint8'), 'RGB')
            new.write(np.asarray(PIL_image1))

    new.release()
    selecttheme()

    Chlist = list_of_voices(Language, Gender)
    Ch = randrange(0, len(Chlist))
    Sentanc = ""

    para = mypara
    para = para.strip()
    while len(para) > 0:
        laugh = 0
        Sentanc = ""
        subtitleletters = 0
        l = para.find("*")
        ll = para.find("**")
        lll = para.find("***")
        llll = para.find("****")
        Nextlocation = min(excludelaugh(l), excludelaugh(ll), excludelaugh(lll), excludelaugh(llll))

        if (Nextlocation == llll):
            laugh = 4
            Sentanc = str(para[:llll].strip())
            lettercountsub = 0
            para = para[llll + 4:]

        elif (Nextlocation == lll):
            laugh = 3
            Sentanc = str(para[:lll].strip())
            lettercountsub = 0
            para = para[lll + 3:]

        elif (Nextlocation == ll):
            laugh = 2
            Sentanc = str(para[:ll].strip())
            lettercountsub = 0
            para = para[ll + 2:]

        elif (Nextlocation == l):
            laugh = 1
            Sentanc = str(para[:l].strip())
            lettercountsub = 0
            para = para[l + 1:]

        else:
            Sentanc = str(para[:].strip())
            lettercountsub = 0
            para = ""
            laugh = 4

        texttovoice(Sentanc)

        addvoice(laugh)

        # print(cliplength)
        dbfs = voicedata()
        selectavatar(avatar)
        createvideo(dbfs)
        lettercountsub = 0
    soundvideo()

    a = threading.current_thread().name
    print(a)

    string_location = str(json_id)

    withformat = string_location + "/"

    url2 = 'http://127.0.0.1:7000/details/' + withformat
    c = threading.current_thread().name
    print(type(c))
    payload = {}
    files = [
        ('img_path', (thumbnail_path,
                      open(thumbnail_path, 'rb'),
                      'image/jpeg'))
    ]

    files2 = [
        ('video_path', (FinalVideo,
                        open(FinalVideo, 'rb'),
                        'image/jpeg'))]



    headers = {
        'Accept-Language': 'en-US',
        'Authorization': 'Bearer yourToken'
    }


    response = requests.request("PUT", url2, headers=headers, data=payload, files=files)
    response = requests.request("PUT", url2, headers=headers, data=payload, files=files2)
    response = urllib.request.urlopen(url2)
    data = json.loads(response.read())
    video = data.get("video_path")
    print(video)

    image = data.get("img_path")
    print(image)

    url3 = "http://127.0.0.1:7000/new_api/"
    myobj2 = {'my_id': json_id,'video_path':video,'img_path':image}

    x = requests.post(url3, json=myobj2)


'''this is code for video micbust'''
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Connected",event)
        self.send({


            'type':'websocket.accept'
        })


    def websocket_receive(self, event):
        print("message received",event)
        print(type(event))
        param= event['text']

        dictionary_param = json.loads(param)
        print(dictionary_param['JokeParagraph'])
        print(dictionary_param['VideoTitile'])
        print(dictionary_param['avatarid'])
        thread = threading.Thread(target=handle_client, args=())
        thread.start()

        
        self.send({

            'type':'websocket.send',
            'text':'{"video":"this is path of video", "image":"this is path of image"}'
        })
        


    def websocket_disconnect(self,event):
        print("disconnected",event)
        raise StopConsumer()

