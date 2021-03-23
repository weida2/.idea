def showNLinesPlus():
    file_name = input('请输入要打开的文件(C:\\test):')
    while True:
        jud = input('进入：')
        if jud == '1':
                lines_show = input('请输入需要显示的行数【格式如 13:21 或 :21 或 21:】:   ').strip();
                file_obj = open(file_name, 'r')
                file_lines = file_obj.readlines();
                file_lines_num = len(file_lines);
                file_obj.close()

                lines_split = lines_show.split(':');
                len_str = len(lines_split);

                print(len_str)
                print(lines_split)
                print(lines_show[0])

                if lines_show == ':' or len_str == 0:
                    print('%s 的全文是:' % file_name)
                    for each in file_lines:
                        print(each)
                elif len_str == 2 and lines_show[0] == ':':
                    print('%s 从开始到 %d行的内容是:' % (file_name, int(lines_split[1])))
                    for i in range(file_lines_num):  # 这里要求输入的行数必须大于0小于等于文件的行数
                        if i < int(lines_split[1]):
                            print(file_lines[i])
                elif len_str == 2 and lines_show[-1] == ':':
                    print('%s 从%d行到末尾的内容是:' % (file_name, int(lines_split[0])))
                    for i in range(file_lines_num):
                        if i >= int(lines_split[0]):
                            print(file_lines[i])
                elif len_str == 2 and '' not in lines_split:
                    print('%s 从%d行到%d行的内容是:' % (file_name, int(lines_split[0]), int(lines_split[1])))
                    for i in range(file_lines_num):
                        if i >= int(lines_split[0]) and i < int(lines_split[1]):
                            print(file_lines[i])
        else:
            break

showNLinesPlus()