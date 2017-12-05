import re

path = 'wiki_'


for ii in range(48,49):
    t = []

    n = str(ii) if ii > 9 else '0'+str(ii)
    print('File: ' + n)
    with open(path+n, 'r') as f:
        a = f.readlines()
        for i in a:
            if not bool(re.search(r'<.+>', i)):
                tmp = ' '.join(re.findall(r'[A-Za-z]+', i.strip())).lower()
                if len(tmp)>0:
                    t += [tmp]
            else:
                t+=['\n']
    file_name= str('output_'+(str(ii)))
    with open(file_name, 'w') as o:
        o.write(' '.join(t))

