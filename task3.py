import os
import operator

path_dir = os.path.join(os.getcwd(), 'txt_files\\')
files_list_dir = [x for x in os.listdir(path_dir) if x.endswith(".txt")]

files_list = []

for file_name_item in files_list_dir:
    name_file = file_name_item

    text_item_file = ''
    with open(path_dir+name_file, "r", encoding="utf-8") as item_file:
        file_dict = {}
        line_count = 0
        for line in item_file:
            line_count += 1
            text_item_file += line

        file_dict['line_count'] = line_count
        file_dict['name'] = name_file
        file_dict['text'] = text_item_file

        files_list.append(file_dict)


# Сортируем по кол. строчек в файле
files_list.sort(key=operator.itemgetter('line_count'))


# Записываем в файл данные
with open('file_result.txt', "w", encoding="utf-8") as result_file:
    for files_list_item in files_list:
        result_file.write(files_list_item['name']+'\n')
        result_file.write(str(files_list_item['line_count'])+'\n')
        result_file.write(files_list_item['text']+'\n')
        result_file.write('\n')