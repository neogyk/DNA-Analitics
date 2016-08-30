def diff(list_1,list_2):
    d_list = []
    for i in list_1:
        if i not in list_2:
            d_list.append(i)
    return  d_list
    
def Sum(array):
    sum=0
    for i in array:
        sum+=i
    return sum 