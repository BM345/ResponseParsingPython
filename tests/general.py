
def merge(*args):
    a = args[0].copy()

    for b in args[1:]:
        a.update(b)
        
    return a