import numpy as np


@profile
def fun(x):
    return x * x

def main():
    x = np.random.randn(1024)
    for i in range(10):
        fun(x)
    
if __name__ == "__main__":
    main()
