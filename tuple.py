# colours =["red", "green", "blue"]
# print(len(colours))

# x,y=(17,2)
# print(x)

# coll=(20,20,20,11,20,25,26)
# print(coll.index(20))
# print(coll.count(20))
# print(len(coll))

from collections import namedtuple
மாணவர் = namedtuple("மாணவர்", ["பெயர்", "வகுப்பு"])
s = மாணவர்("அரவிந்த்", 10)
print(s.பெயர்)