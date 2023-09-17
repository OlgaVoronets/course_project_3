import utils

# Открываем и обрабатываем файл в сортированный список
operations_list = utils.get_operations_list('operations.json')

filtered_operations_list = utils.get_filtered_list(operations_list, 'state', 'EXECUTED')

sorted_operations_list = utils.get_sorted_list(filtered_operations_list, 'date')


# цикл для перебора 5 последних элементов списка операций и вывода на печать
for operation in sorted_operations_list[:5]:
    print(utils.get_operations_output(operation))
