import argparse as arg
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Ellipse
from mpl_toolkits.mplot3d import Axes3D
from ROOT import TTree
from ROOT import TFile


tfilename = "simulation_ni.root"

# Detector parameters.
nsipm = 8;
sipm_pitch = 10.;       # distance between SiPMs
sipm_edge_width = 5.;   # distance between SiPM and edge of board

# Variables for computing an EL point location.
xlen = 2*sipm_edge_width + 7*sipm_pitch;       # (mm) side length of rectangle
ylen = 2*sipm_edge_width + 7*sipm_pitch;       # (mm) side length of rectangle
wbin = 2.0;                                    # (mm) bin width
print "xlen = {0}, ylen = {1}".format(xlen,ylen);

# Maximum bins
xbmax = math.floor(xlen/wbin);
ybmax = math.floor(ylen/wbin);
print "Max x bins = {0}, max y bins = {1}".format(xbmax,ybmax);

# Return the x-location of a given EL point.
def xloc(elpt):
    xbin = (int) (elpt % xbmax);
    print "xbin for point {0} is = {1}".format(elpt,xbin);
    return (xbin*wbin) + 1;

# Return the y-location of a given EL point.
def yloc(elpt):
    ybin = (int) (elpt / ybmax);
    print "ybin for point {0} is = {1}".format(elpt,ybin);
    return (ybin*wbin) + 1;

# Parse the argument: the EL point ID.
parser = arg.ArgumentParser(description="Input the EL ID argument");
parser.add_argument("-p", default=0, type=int);
args = parser.parse_args();
pt = args.p;

# Set up the arrays of SiPM positions.
pos_x = np.ones(nsipm**2)*sipm_edge_width + (np.ones(nsipm*nsipm)*range(nsipm**2) % nsipm)*sipm_pitch
pos_y = np.ones(nsipm**2)*sipm_edge_width + np.floor(np.ones(nsipm*nsipm)*range(nsipm**2) / nsipm)*sipm_pitch

# Get the point from the tree.
elpt = 0; xcoord = 0.; ycoord = 0.; sipm_probs = np.zeros(64)
f = TFile(tfilename);
tr = f.Get("sim_responses")
tr.GetEntry(pt);

# Set up a plot.
fig = plt.figure();
ax1 = fig.add_subplot(111);
ax1.axis([0, 80, 0, 80]);
#ax2 = fig.add_subplot(122)
#ax2.axis([-60, 60, -50, 50])

# Find the minimum and shift.
ip = 0; probs = np.zeros(nsipm*nsipm)
for p in tr.sipm_prob:
    probs[ip] = p
    ip += 1
print probs
minprob = min(probs); probs += abs(minprob)
print probs
maxprob = max(probs); probs /= maxprob
print probs
# Get the IDs
#ids = tbl[ndet*pt+19:ndet*(pt+1),1];

# Compute the actual (x,y) location of the EL point.
xpt = xloc(tr.elpt);
ypt = yloc(tr.elpt);
print "\nActual location is (x,y) = ({0},{1})".format(xpt,ypt);

# Create circles and plot them according to the probabilities.    
for x,y,p in zip(pos_x, pos_y, probs):

    # Offset the position according to which daughter board we are on.
    print "Placing sipm at ({0},{1}) with prob {2}".format(x,y,p);
    
    # Set up the location; note we must invert y due to a pi rotation
    #  about the x-axis.
    r = Ellipse(xy=(x,y), width=2., height=2.);
    r.set_facecolor('0');
    r.set_alpha(0.02 + 0.98*p);
    ax1.add_artist(r);
    mrk = Ellipse(xy=(xpt,ypt), width=2., height=2.);
    mrk.set_facecolor('r');
    ax1.add_artist(mrk);
    #ax1.text(x,y,'%g'%(i-19));  # label with ID numbers

# Show the plot.
plt.xlabel("x (mm)");
plt.ylabel("y (mm)");
plt.savefig("png/nsipm_debug_{0}.png".format(pt));
plt.show();
plt.close();

# Loop over IDs and plot IDs at corresponding x and y values.
#fig = plt.figure();
#plt.axis([-50, 50, -50, 50]);
#xvals = []; yvals = []; IDvals = [];
#nn = 0;
#for x,y,ID in zip(idchk[:,0],idchk[:,1],idchk[:,3]):

    # Cut on IDs < 20 or >= 20
#    if(ID < 20 and nn < 1000):
#        print "Got x = {0}, y = {1}, ID = {2}.".format(x,y,ID);
#        plt.text(x,y,ID);
#        nn += 1;

#plt.show();
