def some_other_function():
    # import web_pdb; web_pdb.set_trace()
    import pudb; pudb.set_trace()
    for i in range(3):
        print(i)
    return i


def some_function():
    return some_other_function()
