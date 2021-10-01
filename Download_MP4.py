# pip install youtube_dl
# pip install pafy

import pafy
url = input('Enter URL: ')
video = pafy.new(url)
audio_stream = video.audiostreams
for i in audio_stream:
    print(i)
best_video = video.getbest()
best_audio = best_video.download()
