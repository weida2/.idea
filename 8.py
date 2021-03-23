import os

result_list = list()
tg_list = ['rmvp', 'avi', 'mp4', 'mov']

def find_v(f_path):
    global result_list
    global tg_list

  # f_path = input('请输入文件夹名称:')
    f_list = os.listdir(f_path)

    for each in f_list:
        if os.path.isdir(f_path + '\\' + each):
            find_v(f_path + '\\' + each)
        else:
            f_name = each.split('.')
            if len(f_name)  >= 2 and f_name[-1] in tg_list:
                result_list.append(f_path + '\\' + each)


    with open(f_path + '.txt', 'w') as f_out:
        for each in result_list:
            f_out.writelines(each + '\n')



find_v('E:/视频')