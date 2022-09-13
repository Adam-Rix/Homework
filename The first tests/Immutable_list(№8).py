x = str(input('Enter an element = '))                          #Enter a word for list.
u = int(input('Enter a position for placing = '))              #Enter the index you would like the word to have.

y = int(input('Enter a position for deleting an element = '))  #Enter the index an element in list for cutting it out.

o = int(input('Enter a position for getting an element = '))   #Enter the inex for getting an element there.

class Immut_list():
    __steals = ['C++', 'Python', 'Vue']
    def print__steals(self):
        print(self.__steals)                                   #Our list

    def __add__(self):
        return self.__steals.insert(u, x)                      #Add into the list u and 'x'.

    def __del__(self):
        return self.__steals.pop(y)                            #Deleting the element, which has an index 'y'.

    def __getitem__(self):
        print(self.__steals.__getitem__(o))                    #Looking for an element with inex 'o'.




J = Immut_list()
J.__add__()
J.__del__()
J.__getitem__()
J.print__steals()


