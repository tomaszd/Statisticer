'''Monte Carlo simulation for the symmetric 1D
andom walk
Let us x the number of steps in an individual symmetric 
D random walk to N = 100 and consider an ensemble of n = 10
independent walks.Now, what does the distribution of end points x
Now the ensemble of walks thus considered look like?
If you want to tackle that question by means of computer simulations, you
may follow the subsequent three steps:
(i) Implement the symmetric 1D random walk model using your favorite
programming language. Using python [4], a minimal program to simulate
the above model ( 1D_randWalk.py, see supplementary material) reads:
'''
from random import seed,choice
def random_1D_walk(n=1000, N=100,printing=False ):
    '''
    Arguments:
    n - number of iterations
    N - number of iterations for pseudorandom -1 +1 
    
    '''
    for s in range(n):
        seed(s)
        endPos=0
        for i in range(N):
            endPos+=choice([-1,1])
        if printing:    
            print s,endPos
    
if __name__=='__main__':
    
    # nice to use python 1D_MonteCarlo.py > N100_n100000.dat to store data 
    kwargs={'n':1000,'N':100,'printing':True}
    
    random_1D_walk(**kwargs)    