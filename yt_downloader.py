from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress


def playlist_audio(url):
    p = Playlist(url, on_progress_callback=on_progress)
    for video in p.videos:
        video.streams.get_by_itag(251).download()
def single_audio(url):
    v = YouTube(url, on_progress_callback=on_progress)
    v.streams.get_by_itag(251).download()
    print()
def highqvideo(url,prg):
    hq = YouTube(url, on_progress_callback=on_progress)
    ch_streams = hq.streams.filter(progressive=prg,type="video")
    for i in ch_streams:
        #print(dir(i))
        print("Resolution:{} hdr:{} type:{} fps:{} filesize:{:.2f}MB tag:{}".format(getattr(i, 'resolution'),getattr(i, 'is_hdr'),getattr(i, 'type'),getattr(i, 'fps'),float(getattr(i, 'filesize'))/(1024*1024),getattr(i, 'itag')))
    ch = int(input("Enter tag of your selection : "))
    hq.streams.get_by_itag(ch).download()
    print("\n")

def get_output(inp,url):
    if inp == 1:
        single_audio(url)
    elif inp == 2:
        playlist_audio(url)
    elif inp == 3:
        highqvideo(url,True)
    elif inp==4:
        highqvideo(url,False)

def inp_choice(url):
    inp = int(input("Enter your Choice,  1 : Audio only \t 2 : Playlist audio\t3 : High Quality Progressive Video\t4 : HighRes video only : "))
    get_output(inp,url)