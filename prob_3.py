list1 = [12,13,25,26,38,39]
new_list = list(filter(lambda x:x%13==0,list1))
print(new_list)