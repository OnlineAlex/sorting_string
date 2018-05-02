def get_num_indices(sort_list):
    int_index = []
    for index, item in enumerate(sort_list):
        if not item.isalpha():
            int_index.append(index)

    return int_index


def get_sorted_list(sort_list, int_indices):
    int_count = len(int_indices)
    if int_indices and int_count != len(sort_list):
        sort_list.sort()
        list_int, sort_list = sort_list[:int_count], sort_list[int_count:]
        list_int.sort(key=int)
        for index in range(int_count):
            sort_list.insert(int_indices[index], list_int[index])
    elif int_indices:
        sort_list.sort(key=int)
    else:
        sort_list.sort()

    return sort_list


if __name__ == "__main__":
    user_data = input('Please, enter string:\n').split()

    num_indices = get_num_indices(user_data)  # indexes of numbers in the list
    sorted_user_list = get_sorted_list(user_data, num_indices)

    if num_indices:
        spatial_complexity = '2n'
    else:
        spatial_complexity = 'n'

    print(' '.join(sorted_user_list))
    print('Временная: O(n)\nПространственная: {}'.format(spatial_complexity))
