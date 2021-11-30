from multiprocessing import Pool

def f(x):
    return x*x

def start(x):
    with Pool(5) as p:
        print(x, p.map(f, [1, 2, 3]))

for i in range (10):
    start(i)
