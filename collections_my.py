from collections import OrderedDict,deque,Counter,defaultdict
#import OrderDict from collections
"""
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]



def check(temps):
    ordered_temps = OrderedDict(sorted(temps, key=lambda x: x[1],reverse=True))
    print(ordered_temps)
    
 
 
# check(temps)


def brackets(line):
    dq=deque()
    for sym in line:
        if sym =='(' :
            dq.append("(")
        if sym == ')':
            if len(dq) == 0:
                return False
            dq.pop()
    if len(dq) == 0:
        return True
    return False


print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("((()()))"))
# False
"""

"""
cls=[['Milk', 'Bread'], ['Meat']]
cla=[]
def get_counter(lst):
    for i in lst:
        for j in i:
            cla.append(j)
        
    cc=Counter(cla)
    return cc

cc=get_counter(cls)        
print(cc)


"""

"""
from collections import *

ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]


rat_sort=sorted(ratings,key=lambda x : (-x[1],x[0]))

cafes=OrderedDict(rat_sort)

print(cafes)
    
print(cafes['Old Gold'])

"""


tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]
 
def task_manager(tasks=[]):
    ret_dict=defaultdict(deque)
    for el in tasks:
        if el[2]==True:
            ret_dict[el[1]].appendleft(el[0])
        else:
            ret_dict[el[1]].append(el[0])
    return ret_dict

#print(task_manager(tasks))

print(task_manager(tasks = [(36871, 'office', False), (40690, 'office', False), (35364, 'voltage', False), (41667, 'voltage', True), (33850, 'office', False)]))

# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})