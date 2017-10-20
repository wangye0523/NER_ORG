# -*- encoding: utf8 -*-
# -*- coding=utf8 -*-
import re, json

f = open('data/renmin.txt','r')
# d = {}
#
# for i in f:
#     for w in re.findall(r'[\u4e00-\u9fff]+',i):
#         if w not in d:
#             d[w]=1
#         else:
#             d[w]+=1



e = {}

def get_bracket(s):
    tmp = s
    r = []
    while ']' in tmp:
        rb = tmp.index(']')
        lb = rb-tmp[:rb][::-1].index('[')-1
        p = tmp[lb:rb]
        l = tmp[:lb]
        b = tmp[rb+1:]
        a = re.findall(r'[\u4e00-\u9fff]+',p)
        r += [[''.join(a), b[:b.index(' ')]]]
        tmp = l+p[1:]+b
    return r


for i in f:
    b = []
    if ']' in i:
        b = get_bracket(i)
        #print(b)
        for k in b:
            if k[0] not in e:
                e[k[0]] = {}
            if k[1] not in e[k[0]]:
                e[k[0]][k[1]] = 1
            else:
                e[k[0]][k[1]]+=1

    for w in i.split(' ')[1:]:
        tmp = w.split('/')
        if len(tmp)==2:
            try:
                tmp[0] = re.findall(r'[\u4e00-\u9fff]+',tmp[0])[0]
            except IndexError:
                continue
            if tmp[0] not in e:
                e[tmp[0]] = {}
                #e[tmp[0]][tmp[1]] = 1
            if ']' in tmp[1]:
                tmp[1] = tmp[1].split(']')[0]

            if tmp[1] not in e[tmp[0]]:
                e[tmp[0]][tmp[1]] = 1
            else:
                e[tmp[0]][tmp[1]]+=1



with open('freq.json', 'w') as f:
    a = json.dumps([e],ensure_ascii=False)
    f.write(a)
    f.close()