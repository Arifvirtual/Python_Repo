#!/usr/bin/python
"""
Program to change the file permission

"""
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, str(j))
    return text

def digit_permission(per_string) :
    '''
    :param per_string:
    :return:
    '''
    dict1 = {'r': 4, 'w': 2, 'x': 1, '-': 0}
    replce_perm = replace_all(per_string, dict1)
    indices = [(0, 2), (3, 5), (6,8)]
    replace_data = [replce_perm[s:e + 1] for s, e in indices]
    print replace_data
    datasum = [sum([int(newdata) for newdata in data]) for data in replace_data]
    str1 = ''.join(str(e) for e in datasum)
    print str1
digit_permission('rwx--x-r-')
