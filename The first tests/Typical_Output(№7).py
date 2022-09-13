x = int(input())                          #enter any num
a = list(range(0, x+1))                   #creating of a list from 0 to x

y = str(a)                                #retyping your list from int to string
u = y.replace('[', ' ').replace(']', ' ') #replace a [] to nothing (just for beauty)

print('Your magnificent nums =', u)       #print your "Monster von Frankenstein"

