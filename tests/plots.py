import numpy as np
from pyquante2 import basisset,rhf,h2
from pyquante2.graphics.vtk import vtk_orbital
from pyquante.graphics.lineplot import test_plot_orbs,test_plot_bfs
from pyquante.graphics.contourplot import test_contour

def lineplot_orbs(): return test_plot_orbs()
def lineplot_bfs(): return test_plot_bfs()
def contour_orb(): return test_contour(True)
    
def plot_h2():
    bfs = basisset(h2,'sto3g')
    solver = rhf(h2,bfs)
    ens = solver.converge()

    # Note: these orbitals are not coming out symmetric. Why not??
    print solver
    print solver.orbs
    vtk_orbital(h2,solver.orbs,bfs)

def plot_orbs():
    bfs = basisset(h2,'sto3g')
    orbs = np.array([[1.0,1.0],
                     [1.0,-1.0]],'d')
    
    vtk_orbital(h2,orbs,bfs)
    return

if __name__ == '__main__':
    plot_h2()
