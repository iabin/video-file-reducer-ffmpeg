import os

#For more information in ffmpeg go to 
# https://trac.ffmpeg.org/wiki/Encode/H.265

def conversion(crf, speed):
    """Using H.265 codec, metadata is preserved using -map_metadata and 128kb audio bitrate"""
    if not os.path.exists("./rendered"):
        os.makedirs("./rendered")
    for file in os.listdir('.'):
        if not file.lower().endswith("mp4"):
            continue
        commandFFmpeg = f"ffmpeg -i {file} -c:v libx265 -crf {crf} -preset {speed} -map_metadata 0 -c:a aac -b:a 128k ./rendered/{file}"
        os.system(commandFFmpeg)


print("Recommended settings for x264 and x265 encoders:\n \
    RF 18-22 for 480p/576p Standard Definition1\n \
    RF 19-23 for 720p High Definition2\n \
    RF 20-24 for 1080p Full High Definition \n \
    RF 22-28 for 2160p 4K Ultra High Definition4 \n")
crf = input("CRF: ")
print("choose speed, always use veryslow:\n  ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow")
speed = input("SPEED: ")
conversion(crf, speed)
