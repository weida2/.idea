def FileRelpace():

    f_name = input('请输入文件名:')
    str_o = input('输入替换的字符:')
    str_n = input('新的字符:')

    f_old = open(f_name, 'r')
    f_list = list(f_old)

    new_f_list =  []
    num_s_o = 0

    for each in f_list:
        num_s_o += each.count(str_o)
        new_f_list.append(each.replace(str_o, str_n))

    f_old.close()

    print('文件%s中共有%d个【%s】' % (f_name, num_s_o, str_o))

    f_new = open(f_name, 'w')
    for each in new_f_list:
        f_new.writelines(each)

    print('替换成功')
    f_new.close()

FileRelpace()
