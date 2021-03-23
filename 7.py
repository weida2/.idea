import os

def count_file_format_num():
    file_path = input('请输入文件路径:')
    result_dict = dict()

    result_dict['无后缀文件名'] = 0
    result_dict['文件夹'] = 0

    filelist = os.listdir(file_path)
    for each in filelist:
        each_full_name = file_path + '\\' + each
        if os.path.isfile(each_full_name):
            if '.' in each:
                file_name = each.split('.')
                if file_name[-1] in result_dict.keys():
                    result_dict[file_name[-1]] += 1
                else:
                    result_dict[file_name[-1]] = 1

            else:
                result_dict['无后缀文件名'] += 1
        else:
            result_dict['文件夹'] += 1

    print('[%s]中共有[%d]类文件' % (file_path, len(result_dict.keys())))

    for key in result_dict.keys():
        print('该文件夹下共有类型为【%s】的文件【%d】个' % ('.' + key, result_dict[key]))


count_file_format_num()
