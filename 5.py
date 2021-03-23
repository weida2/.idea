def showLine():
    f_name = input('请输入需要打开的文件:')
    while True:
        jud = int(input('进入:'))
        if jud == 1:
            n = input('请输入需要打开的行数如【13:15】:')
            with open(f_name, 'r') as f:

                f_list = list(f)
                f_len = len(f_list)
                n_split = n.split(':')
                if n == ':':
                    print('文件 %s全文的内容为:' % f_name)
                    for each in f_list:
                        print(each)

                elif len(n_split) == 2 and n[0] == ':':
                    print('从文件开头到第 %d行内容为:' % int(n_split[1]))
                    for i in range(int(n_split[1])):
                        print(f_list[i])

                elif len(n_split) == 2 and n[-1] == ':':
                    print('从文件第 %d行到末尾的内容为:' % (int(n_split[0])))
                    for i in range(int(n_split[0]) - 1, f_len):
                        print(f_list[i])

                elif len(n_split) == 2 and not '' in n_split:
                    print('从文件第 %d行到第 %d行的内容为:' % (int(n_split[0]), int(n_split[-1])))
                    for i in range(int(n_split[0]) - 1, int(n_split[-1])):
                        print(f_list[i])
        else:
            break

showLine()