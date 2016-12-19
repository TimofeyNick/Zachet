def find(s,subs):
    for k in range(0, len(s)-len(subs)+1):
        for i in range(len(subs)):
            if s [k+i]!=subs[i]:
                break
        else:
            return k

S = 'abcdabecdtgabd'
subs = 'abd'
print(find(S, subs))


#str1 = "this is string example....wow!!!"
#str2 = "exam"

#print(str1.find(str2))
#print(str1.find(str2, 14))
#print(str1.find(str2, 40))