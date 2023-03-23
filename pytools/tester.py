import numpy as np


@profile
def fun(x):
    return x * x

@profile
def main():
    x = np.ones((256, 256))
    z = []
    for i in range(2):
        # z.append(fun(x))
        fun(x)
    del z
    
if __name__ == "__main__":
    main()
