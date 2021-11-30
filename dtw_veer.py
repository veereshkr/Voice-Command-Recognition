from fastdtw import fastdtw
from scipy.io.wavfile import read
from scipy import stats
import numpy as np
import threading
import datetime
from multiprocessing import Pool

q = read("/Users/veeresh/Documents/testing/test1.wav")
q2 = read("/Users/veeresh/Documents/testing/test2.wav")
qz={}
q2z={}
qz['score'] = stats.zscore(q[1])
q2z['score']  = stats.zscore(q2[1])
qz['name'] = 'test1'
q2z['name'] = 'test2'

d = read("/Users/veeresh/Documents/testing/greek_salad.wav")
d2 = read("/Users/veeresh/Documents/testing/greek_salad_2.wav")
dz={}
d2z={}
dz['score'] = stats.zscore(d[1])
d2z['score']  = stats.zscore(d2[1])
dz['name'] = 'greek_salad1'
d2z['name'] = 'greek_salad_2'

t = read("/Users/veeresh/Documents/testing/cream_soup_tomato.wav")
t2 = read("/Users/veeresh/Documents/testing/cream_soup_tomato_2.wav")
tz=t2z={}
tz['score'] = stats.zscore(t[1])
t2z['score']  = stats.zscore(t2[1])
tz['name'] = 'cream_soup_tomato'
t2z['name'] = 'cream_soup_tomato_2'

u = read("/Users/veeresh/Documents/testing/cream_soup_chicken.wav")
u2 = read("/Users/veeresh/Documents/testing/cream_soup_chicken_2.wav")
uz={}
u2z={}
uz['score'] = stats.zscore(u[1])
u2z['score']  = stats.zscore(u2[1])
uz['name'] = 'cream_soup_chicken'
u2z['name'] = 'cream_soup_chicken_2'

b = read("/Users/veeresh/Documents/testing/tod_man_kung_small.wav")
b2 = read("/Users/veeresh/Documents/testing/tod_man_kung_small_4.wav")
bz={}
b2z={}
bz['score'] = stats.zscore(b[1])
b2z['score'] = stats.zscore(b2[1])
bz['name'] = 'tod_man_kung_small'
b2z['name'] = 'tod_man_kung_small_2'

c = read("/Users/veeresh/Documents/testing/cdb.wav")
c2 = read("/Users/veeresh/Documents/testing/cdb2.wav")
c3 = read("/Users/veeresh/Documents/testing/cdb3.wav")
c4 = read("/Users/veeresh/Documents/testing/cdb4.wav")
cz={}

c2z={}
c3z={}
c4z={}
cz['score'] = stats.zscore(c[1])
c2z['score'] = stats.zscore(c2[1])
c3z['score'] = stats.zscore(c3[1])
c4z['score'] = stats.zscore(c4[1])
c3z['name'] = 'cbd3'
cz['name'] = 'cbd1'
c2z['name'] = 'cbd22'
c4z['name'] = 'cbd4'

b4 = read("/Users/veeresh/Documents/testing/mdb3.wav")
b4z={}
b4z['score'] = stats.zscore(b4[1])
b4z['name'] = 'mutton donne biriyani3'

b5 = read("/Users/veeresh/Documents/testing/mdb2.wav")
b5z={}
b5z['score'] = stats.zscore(b5[1])
b5z['name'] = 'mutton donne biriyani2'


b6 = read("/Users/veeresh/Documents/testing/mdb1.wav")
b6z={}
b6z['score'] = stats.zscore(b6[1])
b6z['name'] = 'mutton donner biriyani'

arr = [bz, dz, qz, tz, uz, c4z, cz, c2z, c3z, b4z, b5z, b6z]
#distance, path = fastdtw(q, q2, radius=30)


def fd(x):
    v = x['value']
    a = x['a']
    radius = x['radius']
    distance, path = fastdtw(v['score'], a['score'], radius=radius)
    return (v['name'], a['name'], distance)
    #print ('=====', v['name'], a['name'])
    
def dtwv(value, rad, arr):
    try:
        #print('*****', value)
        y =[]
        for a in arr:
            x={}
            x['value'] = value
            x['a'] = a
            x['radius'] = rad
            y.append(x)
        with Pool(4) as p:

            print(p.map(fd, y))
        """k=0
        for a in arr:
            distance, path = fastdtw(value['score'], a['score'], radius=rad)
            print (value['name'], a['name'], distance)
            k+=1"""
    except:
        print('check', value)

threads = []
time1 = datetime.datetime.now()
print (time1)
for i in range(0,len(arr),3):
    threads = []
    t1 = threading.Thread(target = dtwv, args=(arr[i+0], 10, arr))
    t2 = threading.Thread(target = dtwv, args=(arr[i+1], 10, arr))
    t3 = threading.Thread(target = dtwv, args=(arr[i+2], 10, arr))

    threads.extend([t1, t2,t3])
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()

time2 = datetime.datetime.now()
elapsedTime = time2 - time1
print (elapsedTime)
