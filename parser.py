import re
f = open("toccata.synth","r")
lines = f.readlines()
# def get_token(str):
#     for c in str:
#         print (c)
def get_note(str):
    exit
tracks = []
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
        print (tracknum[0])
        data.pop(0)
        #print (data)
        for elem in data:
            elem = elem.split('/')
            note = elem[0]
            if (len(elem) == 1):
                seconds = "0"
            else:
                seconds = elem[1]
            print ("note: "+note+" seconds: "+seconds)
   # if data[0] == 
    
    #print (data)
    #print(line, end="")
print (tempo)
print (tracks)