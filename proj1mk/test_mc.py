# function Test_MC

# min mu*||X||_* + sum_{ij in idx}

import numpy as np
from numpy import round, floor, sqrt, randn


# generate data
m = 40; n = 40; sr = 0.3; p = int(round(m*n*sr)); r = 3  # noqa: E702
# m = 100; n = m; sr = 0.3; p = int(round(m*n*sr)); r = 2  # noqa: E702
# m = 100; n = m ; p = 5666; sr = p/m/n; r = 10  # noqa: E702
# m = 200; n = m; p = 15665; sr = p/m/n; r = 10  # noqa: E702
# m = 500; n = m; p = 49471; sr = p/m/n; r = 10  # noqa: E702
# m = 150; n = 300; sr = 0.49; p = int(round(m*n*sr)); r = 10  # noqa: E702


# fr is the freedom of set of rank-r matrix, maxr is the maximum rank one
# can recover with p samples, which is the max rank to keep fr < 1
fr = r*(m+n-r)/p
maxr = floor(((m+n)-sqrt((m+n)**2-4*p))/2)

rs = 2021
np.random.seed(rs)
# get problem
omega_r = np.random.permutation(m*n)[:p] # omega_r gives the index of samplings within matrix
omega = np.zeros([2,self.p],dtype=int)
Omega[0,:] = Omega_r // self.m           # turn index to coordinate
Omega[1,:] = Omega_r % self.m
Omega = tuple(Omega)                     # Matrix could be indexed by A[Omega]
xl = randn(m, r)
xr = randn(n, r)
a = xl @ xr.T  # A is the matrix to be completed
m_mat = a[Omega] # M is the samples from A
