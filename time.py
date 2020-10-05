

import time

t = time.time()
minutes = t / 60
m = int(minutes)
mins = str(m)
mns = 'mins '

hours = minutes //60
h = int(hours)
hr = str(h)
hrs = 'hrs '

remainder = minutes - hours *60
s = int(remainder)
sec = str(s)
secs = 'secs'

print(hr + hrs + mins + mns + sec + secs)





