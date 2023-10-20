def xor(*args):
    """
    This function returns True if only one of the arguments is True.
    :param args: This only enter values True or False.
    :return: Will return True if only one of the arguments is True. Otherwise, it will return False.
    """
    for pos, i in enumerate(args):
        for j in range(0, len(args)):
            if pos != j and i != False:
                if i == args[j]:
                    return False
    return True


if __name__ == '__main__':
    print(xor(3 > 4, 4 < 3, 1 == 3, 1 == 1))
