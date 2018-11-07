do_it = lambda f, *args: f(*args)
hello = lambda *p: print("Hello ", *p)
bye = lambda *p: print("Bye ", *p)

fns = [hello, bye]
args =  (['David','Jane'], ['Mertz', 'Doe'])
_ = list(map(do_it, fns, ['David','Jane'], ['Mertz', 'Doe']))
_ = [list(map(fn, *args )) for fn in fns]
