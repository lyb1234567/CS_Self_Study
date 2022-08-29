def modular(key,size):
    return key%size

list=[None]*20
key=[2,4,30,42]
Value=['a','b','c','d','e''f']
for k in key:
    index=modular(k,len(list))
    if not list[index]:
        list[index]=Value.pop(0)
        print("key {0}:{1}".format(k,list[index]))
    else:
        offset=index
        while list[index]:
              index+=offset
              if index>=len(list):
                  index=0
        list[index] = Value.pop(0)
        print("key {0}:{1}".format(k, list[index]))
print(list)