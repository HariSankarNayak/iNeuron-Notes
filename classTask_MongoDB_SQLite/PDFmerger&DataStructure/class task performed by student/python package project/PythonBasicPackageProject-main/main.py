from list_module import ListMethods
from dict_module import DictMethods

l = [1,2,3]
l_obj = ListMethods(l)
print(l_obj.l)
l_obj.append_list('s')
print(l_obj.l)
#l_obj.clear_list()
#print(l_obj.l)
y=l_obj.copy_list()
print(l_obj.l)
print(y)
y.append([4,5])
print(y)
print(l_obj.l)
print(l_obj.count_list([4,5]))
print(l_obj.l)
print(l_obj.extend_list([4,5,[66,77]]))
print(l_obj.l)
print('hi')
#print(l_obj.pop_list(2))
#print(l_obj.l)
#print(l_obj.remove_list([66, 77]))
#print(l_obj.l)
print(l_obj.reverse_list())
print(l_obj.l)
d={1: 2,
 3: 4,
 5: {7: 8, 's': 'sush'},
 7: [1, 55, 66, 88],
 12: 'lll',
 222222: 'dddddddddddd'}
d_obj = DictMethods(d)
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)
print(d_obj.popitem_dict())
print(d_obj.d)


