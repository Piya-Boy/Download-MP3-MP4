# pip install youtube_dl
# pip install pafy

import pafy
url = input('Enter URL: ')
video = pafy.new(url)
audiostreams = video.audiostreams
for x in audiostreams:
    print(x.get_filesize())
audiostreams[3].download()
print('Download Successful !')