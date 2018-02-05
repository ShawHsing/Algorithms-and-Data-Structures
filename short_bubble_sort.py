def short_bubble_sort(a_list):
    n = 0
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i],a_list[i + 1] = a_list[i + 1],a_list[i]
                n = n + 1
                print("The %d th exchange"%(n))
        pass_num = pass_num - 1

a_list = [1, 2, 11, 4, 5, 6, 7, 10, 9]
short_bubble_sort(a_list)
print(a_list)
