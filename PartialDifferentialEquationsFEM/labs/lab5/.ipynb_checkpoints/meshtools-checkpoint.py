#%%
import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull

import matplotlib.tri as tri
import math


import plottools as pt

def rectangle_mesh(p, q, N, M):
    """Generates a Delaunay triangulation for the rectangle
    defined by corner points p and q and (N+1)*(M+1) mesh points
    defined by N and M uniform subintervals in x and y
    direction. Returns (p,t) consisting of the 
    points and connectivity matrix"""

    #TODO: Add kwargs to pass stuff like marker size etc on
    # to plot function
    # TODO: Remove automatic scaling and add fix coordinate system

    x_coord = np.linspace(p[0], q[0], N+1)
    y_coord = np.linspace(p[1], q[1], M+1)

    x, y = np.meshgrid(x_coord, y_coord)              # x,y are matrices
    points = np.array([x.flatten(), y.flatten()]).T   # 

    mesh = Delaunay(points)
    return  (points, mesh.simplices)
 
def rectangle_tria (p, q, N, M):

    x_coord = np.linspace(p[0], q[0], N+1)
    y_coord = np.linspace(p[1], q[1], M+1)

    x, y = np.meshgrid(x_coord, y_coord)              # x,y are matrices
    points = np.array([x.flatten(), y.flatten()]).T   # 

    T = Delaunay(points)
    
    # Find edges at the boundary
    # https://stackoverflow.com/questions/59419537/how-do-i-get-the-boundary-of-a-delaunay-triangulation
    boundary = []
    for i in range(len(T.neighbors)):
        for k in range(3):
            if (T.neighbors[i][k] == -1):
                nk1,nk2 = (k+1)%3, (k+2)%3 
                boundary.append([T.simplices[i][nk1],T.simplices[i][nk2]])
    
    # edges = list(boundary)
    
    return  (points, T.simplices, boundary )

def unitsquare_mesh(N):
    return rectangle_mesh((0, 0), (1,1), N, N)

if __name__ == "__main__":
   
    # Create unitsquare mesh
    N = 3
    P, T = unitsquare_mesh(N)

    # Plot mesh
    pt.plot_mesh_2d(P, T)

    # Define rectangle mesh with corner points (0,0) and (1,2)
    p = (0,0)
    q = (1,2)
    N, M = 5, 10
    P, T = rectangle_mesh(p, q, N, M)

    # Plot mesh
    pt.plot_mesh_2d(P, T)

def circle_mesh(N):

    angle = np.linspace(0, 2.0*np.pi, N+1)

    M = np.ceil(0.3*(N+1))
    h = 1.0/M

    x = np.cos(angle) # points[:,0]
    y = np.sin(angle) # points[:,1]

    X=np.array([0])
    Y=np.array([0])

    for i in range(5+1):
        r = i*h
        X=np.append(X,r*x,axis=0)
        Y=np.append(Y,r*y,axis=0)

    points = np.array([X,Y]).T
    mesh = Delaunay(points)

    T = mesh.simplices

        # Get a new figure
    #plt.figure()
    #plt.triplot(X, Y, T.copy())
    #plt.show()

