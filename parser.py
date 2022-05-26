import re
import sys

if (len(sys.argv) < 2):
    print ("give filename")
    exit(0)

filename = sys.argv[1]

f = open(filename,"r")
#path.is_file()

lines = f.readlines()
# def get_token(str):
#     for c in str:
#         print (c)
def get_note(str):
    exit
tracks = []
tracks_dict = {}
tempo = 0
for line in lines:
    if (line[0] == '#'):
        continue
    if (line[0] == '\n'):
        continue
    data = line.split()
    if data[0] == 'tempo':
         tempo = data[1]
    if data[0] == 'tracks':
        data.pop(0)
        tracks = data[0].split(',')
    if (re.search("(\d*):", data[0])):
        tracknum = data[0].split(':')
        tracknum = tracknum[0]
        data.pop(0)
        #print (data)
        track = []
        for elem in data:
            elem = elem.split('/')
            note = elem[0]
            tune = {}
            if (len(elem) == 1):
                seconds = "0"
            else:
                seconds = elem[1]
            tune['seconds'] = seconds
            tune['tone'] = note
            #print ("note: "+note+" seconds: "+seconds)
            #print (tune)
            track.append(tune)
        
        tracks_dict['tracknum'] = tracknum
        if (int(tracknum)-1 < len(tracks)):
            tracks_dict['wave'] = tracks[int(tracknum)-1]
        else:
            print ('error on '+tracknum+' track not exists')
        #print (tracks[0])
        tracks_dict['track'] = track
    

   # if data[0] == 
    
    #print (data)
    #print(line, end="")
#print ("tempo: "+tempo)
#print (tracks)
print (tracks_dict)