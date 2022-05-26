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
        tracks = data
    #if data[0] == 
    
    #print (data)
    #print(line, end="")
print (tempo)
print (tracks)