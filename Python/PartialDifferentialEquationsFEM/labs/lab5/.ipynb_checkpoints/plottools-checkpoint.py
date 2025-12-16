import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def plot_mesh_2d(P, T, dirichlet_nodes = None, 
                 plot_nodes=True, 
                 label_nodes=True, 
                 label_triangles=True):
    X = P[:,0]
    Y = P[:,1]

    # Get a new figure
    plt.figure()
    plt.triplot(X, Y, T.copy())
    if plot_nodes:
        plt.plot(X, Y, "or", markersize=8)

    if dirichlet_nodes and plot_nodes:
        plt.plot(X[dirichlet_nodes], Y[dirichlet_nodes], "og", markersize=8)

    if label_nodes:
        for j, p in enumerate(P):
            plt.text(p[0], p[1], j, ha='right', color="red") # label the points
    if label_triangles:
        for j, s in enumerate(T):
            p = P[s].mean(axis=0)
            plt.text(p[0], p[1], '#%d' % j, ha='center', color="black") # label triangles

    plt.show()

def _plot2D(ax, X, Y, Z, triangles=None):
    """ Little helper function for switching between grid point based 
    and triangle mesh based plotting"""
    if triangles is not None:
        ax.plot_trisurf(X, Y, Z, triangles=triangles.copy(), cmap=cm.viridis, linewidth=0.0) #viridis
    else:
        ax.plot_surface(X, Y, Z,             
                rstride=1, cstride=1, # Sampling rates for the x and y input data
                cmap=cm.viridis, # Use the new fancy colormap viridis
                linewidth=0.0)      

def plot2D(X, Y, Z, title='', triangles=None, block=True):
    fig = plt.figure()
    # ax = fig.gca(projection='3d')
    ax = fig.add_subplot(projection = '3d')
    _plot2D(ax, X, Y, Z, triangles)
    ax.set_title(title)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    plt.show(block=block)

def plot_comparison_2D(X, Y, f1, f2, title_f1='', title_f2='', title_diff='', triangles=None, adjust_zlim=False):

    fig = plt.figure(figsize=plt.figaspect(0.33))

    # Plot f1
    ax_1 = fig.add_subplot(1, 3, 1, projection='3d')
    _plot2D(ax_1, X, Y, f1, triangles)
    ax_1.set_title(title_f1)
    ax_1.set_xlabel('$x$')
    ax_1.set_ylabel('$y$')
    ax_1.set_zlabel('$z$')

    # Plot f2
    ax_2 = fig.add_subplot(1, 3, 2, projection='3d')
    _plot2D(ax_2, X, Y, f2, triangles)
    ax_2.set_title(title_f2)
    ax_2.set_xlabel('$x$')
    ax_2.set_ylabel('$y$')
    ax_2.set_zlabel('$z$')

    # Plot f1 - f2
    ax_diff = fig.add_subplot(1, 3, 3, projection='3d')
    _plot2D(ax_diff, X, Y, f1-f2, triangles)
    ax_diff.set_title(title_diff)
    ax_diff.set_xlabel('$x$')
    ax_diff.set_ylabel('$y$')
    ax_diff.set_zlabel('$z$')

    # Find best zlim values and adjust z axes
    if adjust_zlim:
        zlim_1, zlim_2 = ax_1.get_zlim(), ax_2.get_zlim()
        zlim = (min(zlim_1[0], zlim_2[0]), max(zlim_1[1], zlim_2[1]))
        ax_1.set_zlim(zlim)
        ax_2.set_zlim(zlim)
        ax_diff.set_zlim(zlim)

    plt.show()

def _plot_frame_fdm_solution(i, ax, X, Y, U_list, zlim=None):
    ax.clear()
    print("Plotting time step %d" % i)
    ax.plot_surface(X, Y, U_list[i],             
            rstride=1, cstride=1, # Sampling rates for the x and y input data
            cmap=cm.viridis)      # Use the new fancy colormap viridis
    ax.set_zlim(-1.0, 1.0)

#def _plot_frame_fem_solution(i, ax, X, Y, U_list, triangles, title, zlim):
#   ax.clear()
## ##     print("Plotting time step %d" % i)
#   line = ax.plot_trisurf(X, Y, U_list[i], triangles=triangles, cmap=cm.viridis, linewidth=0.0)
#   if zlim is not None:
#       ax.set_zlim(zlim)
#   ax.set_title(title)
#   return line,

def _plot_frame_fem_solution(i, ax, X, Y, U_list, triangles, title):
    ax.clear()
    line = ax.plot_trisurf(X, Y, U_list[i], triangles=triangles, cmap=cm.viridis, linewidth=0.0)
    ax.set_zlim(-1.0, 1.0)
    total_frame_number = len(U_list)
    complete_title = title + (" (Frame %d of %d)" % (i,total_frame_number))
    ax.set_title(complete_title)
    return line,

# TODO: Needs still some debugging for including FDM solution plots.
# def plot_2D_animation(X, Y, U_list, triangles=None, show=True, title='', duration=10, zlim=None):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     if triangles is None:
#         fargs = (ax,X,Y,U_list)
#         frame_plotter = _plot_frame_fdm_solution
#     else:
#         fargs = (ax,X,Y,U_list,triangles, title, zlim)
#         frame_plotter = _plot_frame_fem_solution
#     
#     frames = len(U_list)
#     interval = duration/frames
#     ani = animation.FuncAnimation(fig, frame_plotter, 
#             frames=len(U_list), fargs=fargs, 
#             interval=interval, blit=False, repeat=True)
#     return ani

def plot_2D_animation_fem(X, Y, U_list, triangles=None, title='', duration=10):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    line = ax.plot_trisurf(X, Y, U_list[0], triangles=triangles, cmap=cm.viridis, linewidth=0.0)
    ax.set_zlim(-1.0, 1.0)
    fargs = (ax,X,Y,U_list,triangles,title)
    
    frames = len(U_list)
    interval = duration/frames

    ani = animation.FuncAnimation(fig, _plot_frame_fem_solution, 
            frames=len(U_list), fargs=fargs, 
            interval=20, blit=False, repeat=True)
    return ani

if __name__ == "__main__":
    
    import numpy as np
    import meshtools as mt

    N = 10
    X,Y = np.ogrid[0:1:N*1j, 0:1:N*1j]

    Z = np.sin(np.pi*X)*np.cos(np.pi*Y) 

    # Plot as grid points
    plot2D(X, Y, Z, "Grid points based plotting")
    
    P, T = mt.unitsquare_mesh(N)
    # (points, mesh.simplices)

    X = P[:,0]
    Y = P[:,1]
    Z = np.sin(np.pi*X)*np.cos(np.pi*Y) 

    plot2D(X, Y, Z, "Triangle mesh based plotting", triangles=T)
    
    
    
