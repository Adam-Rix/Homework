#This works likewise LIFO.

def cheking(list):
    while '()' in list or '[]' in list or '{}' in list:  #We cheking a list from print, and if we`re looking for a () or [] or {}.
        list = list.replace('()', '')                    #If we`ll find it, then replace it onto nothing.
        list = list.replace('[]', '')
        list = list.replace('{}', '')

    return not list                                      #return NOT list - return True if we have NOTHING into list!

print(cheking('(()'))                                    #_test_1 - False
print(cheking('(()()())'))                               #_test_2 - True

print(cheking('{{{}}{{}}}'))                             #_test_3 -True
print(cheking('[]]{{[]}}}]'))                            #_test_4 - False

