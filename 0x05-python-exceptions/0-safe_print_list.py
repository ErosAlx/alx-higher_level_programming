def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(my_list[i], end='')
            i = i + 1
    except IndexError:
        None
    return i
