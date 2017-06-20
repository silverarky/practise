import collections as cl
k=['a','b','c',]
kk=cl.deque(k)
kk.appendleft("-a")
print(kk)

point=cl.namedtuple('point',['x','y'])
p=point(1,2)
p.x
p.y

raw="askdjalkdjwwpqdjpqwdqdklasdlajsdpqdq"
c=cl.Counter()
for x in raw:
    c[x]+=1
print(c)

ll=cl.OrderedDict([('a',1),('b',2)])
print(ll)
ll.move_to_end('a',last=True)
ll['c']=3
ll.popitem(last=False)
print(ll)
ll.popitem(last=False)
print(ll)

