def postorder_eval(parse_tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mil, '/':operator.truediv}

    res1 = None
    res2 = None

    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()
        
