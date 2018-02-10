def print_exp(tree):
    str_val = ""
    if tree:
        str_val = '(' + print_exp(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val())
        str_val = str_val + print_exp(tree.get_right_child()) + ')'
    return str_val
