  import sys

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)

f = open('out2.html', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)

i = []
for x in range(0,28):
    i.append([])
i[0]='h'
i[1] = chr(13)
i[2] = chr(13),chr(13)
i[3] = chr(13),chr(13),chr(13)
i[4] = chr(13),chr(13),chr(13),chr(13)
i[5] = chr(13),chr(13),chr(13),chr(13),chr(13)
i[6] = chr(13),chr(13),chr(13),chr(13),chr(13),chr(13)
i[7] = chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13)
i[8] = chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13)
i[9] = chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13)
i[10]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13))
i[11]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13))
i[12]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13))
i[13]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13))
i[14]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13))
i[15]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))
i[16]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))
i[17]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))
i[18]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))
i[19]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13))
i[20]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13))
i[21]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13))
i[22]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13))
i[23]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13))
i[24]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))
i[25]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))
i[26]= (chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),
      chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13),chr(13))

message="KILL OBAMA TODAY IN USA AT TEN PM HE WILL BE COMING FOR THE WHITEHOUSE MEETING AT TEN JUST SHOOT HIM"
x=0
l=len(message)
listmsg=list(message)
with open("motivation2.txt") as f1:
    for line in f1:
        for word in line.split():
            if x<len(message):
                if listmsg[x]!=' ':
                    y=ord(listmsg[x])-64
                if listmsg[x]==' ':
                    print word,
                else:
                    print ''.join(i[y]),word,
                x=x+1
            else:
                print word,
                #break
            
        else:
            continue
        break

f1.close()


#print "Hello,",''.join(i1),"How",''.join(i26),"are"

#use the original
sys.stdout = original
print "This won't appear on file"  # Only on stdout
f.close()
