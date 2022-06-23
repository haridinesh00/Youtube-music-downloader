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
def highqvideo(url):
    hq = YouTube(url, on_progress_callback=on_progress)
    print(hq.streams.filter(progressive=True))
    hq.streams.get_by_itag(22).download()
    
def get_output(inp,url):
    if inp == 1:
        single_audio(url)
    elif inp == 2:
        playlist_audio(url)
    elif inp == 3:
        highqvideo(url)

def inp_choice(url):
    inp = int(input("Enter your Choice, 1:Single audio 2:Playlist audio 3: High Quality Video : "))
    get_output(inp,url)