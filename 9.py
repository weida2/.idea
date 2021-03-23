import os

result_list = list()
valid_suffix = ['rar', 'h'];


def get_spec_file_num_res(folder_path):
    global result_list
    global valid_suffix

    filelist = os.listdir(folder_path)
    for each in filelist:
        if os.path.isdir(folder_path + '\\' + each):
            get_spec_file_num_res(folder_path + '\\' + each);
        else:
            filename = each.split('.');
            if len(filename) >= 2 and filename[-1] in valid_suffix:
                result_list.append(folder_path + '\\' + each);

    f_out = open('file_list.txt', 'w');

    for each in result_list:
        f_out.writelines(each + '\n');
    f_out.close();


get_spec_file_num_res('E:/视频')