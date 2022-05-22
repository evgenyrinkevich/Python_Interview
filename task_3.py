# Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
# во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
# Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
# Если есть  значения, которым не хватило ключей, их необходимо отбросить.

def custom_zip(keys_list, values_list):
    len_diff = len(keys_list) - len(values_list)
    new_vals = values_list + [None] * len_diff
    result = {k: v for k, v in zip(keys_list, new_vals)}

    return result


if __name__ == '__main__':
    k_list = [let for let in 'abcdefg']
    v_list = [num for num in range(4)]
    print(custom_zip(k_list, v_list))
