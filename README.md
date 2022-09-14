# video-file-reducer-ffmpeg
This script uses ffmpeg to reduce video file sizes using the codec H.265. 

This is a solution for the gopro file sizes. The files are to big to be stored in a photo service with limited ammount of storage.

To use this, is necesary install ffmpeg. 
 
Execute the script in the directory where all your MP4 files that you want to process are located, the script will create a 
directory named rendered with all the processed videos.

The command has two input variables, CRF and Speed.
CRF, lower is better, smaller values will increase quality but will increase the file size. 
The recomended values are.

RF 18-22 for 480p/576p Standard Definition
RF 19-23 for 720p High Definition
RF 20-24 for 1080p Full High Definition
RF 22-28 for 2160p 4K Ultra High Definition

For speed, always use veryslow, but If you do not have enough time, you can choose another speed.
ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow

The process takes some time, several hours for a 60s video. 
