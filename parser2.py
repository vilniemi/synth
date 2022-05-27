import re
import sys

# if (len(sys.argv) < 2):
#     print ("give filename")
#     exit(0)

# filename = sys.argv[1]

def open_file(filename):
    f = open(filename,"r")
    #path.is_file()

    lines = f.readlines()
    # def get_token(str):
    #     for c in str:
    #         print (c)
    def get_note(str):
        exit
    tracks = []
    tracks_arr = []
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
                    if (lastelem_seconds):
                        seconds = lastelem_seconds
                    else:
                        seconds = "0"
                else:
                    seconds = elem[1]
                tune['seconds'] = seconds
                tune['tone'] = note
                #print ("note: "+note+" seconds: "+seconds)
                #print (tune)
                track.append(tune)
                lastelem_seconds = seconds
            tracks_dict_row = {}
            tracks_dict_row['tracknum'] = tracknum
            if (int(tracknum)-1 < len(tracks)):
                tracks_dict_row['wave'] = tracks[int(tracknum)-1]
            else:
                print ('error on '+tracknum+' track not exists')
            #print (tracks[0])
            tracks_dict_row['track'] = track
            tracks_arr.append(tracks_dict_row)
    return (tracks_arr)

   # if data[0] == 
    
    #print (data)
    #print(line, end="")
#print ("tempo: "+tempo)
#print (tracks)
#print (tracks_dict)

# for track in tracks_arr:
#     print (track['tracknum'])
#     for tune in track['track']:
#         print (tune['tone'] + tune['seconds'])
#print (tracks_arr[0])
#
# for track in tracks_arr:
#     print (track['wave'])
#     for note in track['track']:
#         print (note)
# for note in  tracks_arr[0]['track']:
#     print (note)

# for sdsd in  tracks_arr[1]['track']:
#     print (sdsd)