def file_cmp():

    f1_name = input('请输入第一个头文件名:')
    while True:
        f2_name = input('请输入第二个头文件名:')
        if not f2_name == f1_name:
            break
        else:
            print('不能输入两个相同的文件名:')
            continue

    f1 = open(f1_name, 'r')
    f2 = open(f2_name, 'r')

    f1_list = list(f1)
    f2_list = list(f2)

    f1.close()
    f2.close()

    f1_lines = len(f1_list)
    f2_lines = len(f2_list)

    dif_lines = list()

    valid_lines = min(f1_lines, f2_lines)

    for idx in range(valid_lines):
        if f1_list[idx] == f2_list[idx]:
            continue
        else:
            dif_lines.append(idx + 1)

    invalid_lines =  list(range(valid_lines + 1, max(f1_lines, f2_lines)) + 1)
    dif_lines.extend(invalid_lines)

    if dif_lines == 0:
        print('两个文件完全一致')
    else:
        print('两个文件共有【%d】处不同:' % len(dif_lines))
        for each in dif_lines:
            print('第 %d行不一样' % each)












file_cmp()