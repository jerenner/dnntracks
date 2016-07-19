"""
dnnplot.py

Plots results from DNN analyses.

1.  plot run summary:

    python dnnplot.py summary

    -- Example: python dnnplot.py summary
                (Plots summary for run testrun)


"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
import h5py
from mpl_toolkits.mplot3d import Axes3D
from math import *
from dnninputs import *

grdcol = 0.99

# -----------------------------------------------------------------------------
# Get the arguments
# -----------------------------------------------------------------------------
usage_str = "Usage:\n\n python dnnplot.py <type> (<start>) (<end>) (si/bg)"
args = sys.argv

# Must have at least 2 arguments.
if(len(args) < 2):
    print usage_str
    exit();

# Get the run name and type of plot.
ptype = args[1]
#if(len(args) > 2):
#  epoch = args[2]
#if(len(args) > 3):
#  evt = args[3]

evt_start = -1; evt_end = -1
epoch = -1; si_bg = "bg"
if(ptype == "prob"):
  if(len(args) > 3):
    epoch = args[2]
    evt = args[3]
  else:
    print "Necesita 3 argumentos!"
    exit()
#if(ptype != "summary"):
#   print usage_str
#    exit()

# -----------------------------------------------------------------------------
# File names and directories
# -----------------------------------------------------------------------------
fn_summary = "{0}/{1}/acc/accuracy_{2}.dat".format(rdir,rname,rname)
fn_prob = "{0}/{1}/acc/prob_{2}_test_ep{3}.dat".format(rdir,rname,rname,epoch)

if(not os.path.isdir("{0}/{1}/plt".format(rdir,rname))): os.mkdir("{0}/{1}/plt".format(rdir,rname))
if(not os.path.isdir("{0}/plt".format(datdir))): os.mkdir("{0}/plt".format(datdir))
if(not os.path.isdir("{0}/plt/{1}".format(datdir,dname))): os.mkdir("{0}/plt/{1}".format(datdir,dname))

# -----------------------------------------------------------------------------
# Plotting
# -----------------------------------------------------------------------------

# Summary plot
if(ptype == "summary"):

    print "Plotting summary..."

    # Read in the results.
    accmat = np.loadtxt(fn_summary)
    acc_tr = accmat[:,1]*100.
    acc_vl = accmat[:,3]*100.
    acc_itr = [] 
    for iit in range(len(acc_tr)): acc_itr.append(iit)

    # Plot the results.
    fig = plt.figure(1);
    fig.set_figheight(5.0);
    fig.set_figwidth(15.0);

    ax1 = fig.add_subplot(111);
    ax1.plot(acc_itr, acc_tr, '-', color='blue', lw=1, label='Training')
    ax1.plot(acc_itr, acc_vl, '-', color='green', lw=1, label='Validation')
    ax1.set_xlabel("epoch")
    ax1.set_ylabel("accuracy")
    ax1.set_title("")
    ax1.set_ylim([0, 100]);
    #ax1.set_xscale('log')

    lnd = plt.legend(loc=4,frameon=False,handletextpad=0)

    # Show and/or print the plot.
    fn_plt = "{0}/{1}/plt/{2}_summary.png".format(rdir,rname,rname)
    plt.savefig(fn_plt, bbox_inches='tight')
    #if(plt_show):
    plt.show()
    plt.close()

# Probability plot
if (ptype == "prob"):

   print "Plotting probability..."

   # Read in the results.
   probtbl = np.loadtxt(fn_prob)
   ELpts = probtbl[evt,0]
   probs = probtbl[evt,1:]*100
   x_point = []
   for i in range (0,1600): x_point.append(i)
   
   #Plot the results.
   fig = plt.figure();
   fig.set_figheight(5.0);
   fig.set_figwidth(15.0);
   plt.axvline (x=ELpts, ymin=0, ymax=100, linewidth=2, color='r', linestyle='--') 

   ax1 = fig.add_subplot(111);
   ax1.plot(x_point, probs, '-', color='blue', lw=1)
   ax1.set_xlabel("ELpoint")
   ax1.set_ylabel("Probability")
   ax1.set_title("")
   ax1.set_xlim([0,1600]);
   ax1.set_ylim([0,100]);
   
   lnd = plt.legend(loc=4,frameon=False,hadletextpad=0)

   # Show and/or print the plot.
   fn_plt = "{0}/{1}/plt/{2}_prob.png".format (rdir,rname,rname)
   plt.savefig(fn_plt, bbox_inches='tight')
   #if(plt_show):
   plt.show()
   plt.close()
