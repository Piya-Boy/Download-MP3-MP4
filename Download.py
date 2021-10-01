# pip install youtube_dl
# pip install pafy

import pafy

def Download_MP3():
    video = pafy.new(url)
    audiostreams = video.audiostreams
    for x in audiostreams:print(x.get_filesize())
    audiostreams[3].download(filepath='C:/Users\Acer\Downloads\Music')
    print('Download Successful !')

def Download_MP4():
    video = pafy.new(url)
    audiostreams = video.audiostreams
    for i in audiostreams:print(i)
    best_video = video.getbest()
    best_audio = best_video.download(filepath='C:/Users\Acer\Downloads')
    print('Download Successful !')

while True:
    download = input('You want to download MP3 or MP4: ')
    url = input('Enter URL: ') 

    if download == 'mp3':
        Download_MP3()
    elif download == 'mp4':
        Download_MP4()    
    else:    
        print('You chose incorrectly!')
        
   