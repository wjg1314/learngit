import copy


def func(data_list):
    data_list[1] = 99
    print(data_list)


lst = [1,2,3]
# 拷贝一份数据
new_lst = copy.copy(lst)
func(new_lst)
print(lst)