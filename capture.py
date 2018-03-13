import os
import time
import tweepy

consumer_key ="DjDYPZ2tPvmUucVG4bsIvLXdb"
consumer_secret ="bEgoyf7m3Cd9MkL2JrbTRfDHvhDEdqIRkoTSRD4ZiJU6AujiOJ"
access_token ="967252920877142016-qHSudiNuLNgFqwgLhMpPPClt0lMmLsb"
access_token_secret ="oHs1JF7DmUTTSAvAeLQwtJ8x1HfWL445VFiLuVfWl1MKn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  

b=1
a=0

while a<=2:
   
    cmd="fswebcam -F 3 --fps 20 -r 800*600 /home/cs2017a107/Desktop/img.jpg"
    os.system(cmd)
    img="/home/cs2017a107/Desktop/img.jpg"
    print("pic taken")
    api.update_with_media(img, status="nice one")
    print('wait for five seconds for selfie')
    time.sleep(5)
    a+=1
    
    print('success')
