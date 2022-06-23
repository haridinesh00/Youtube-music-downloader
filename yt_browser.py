from youtubesearchpython import VideosSearch
import yt_downloader as ytd
import moviepy.editor as mpe

def combine_audio(vidname, audname, outname, fps):
    my_clip = mpe.VideoFileClip(vidname)
    audio_background = mpe.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

def search(key):
    videosSearch = VideosSearch(key, limit = 20)
    res = videosSearch.result()
    for i in range(len(res['result'])):
        print("{} : Title: {} \tURL: {}".format(i, res['result'][i]['title'],res['result'][i]['link']))
    choice = int(input("Enter Choice : "))
    ytd.inp_choice(res['result'][choice]['link'])
key = input("Enter the search keyword : ")
search(key)