mylist=[1,2,3]
def add_to_list(lst,item):
    nl = lst.copy()
    nl.append(item)
    
    return nl

newlist=add_to_list(mylist,4)
print(mylist)
print(newlist)
