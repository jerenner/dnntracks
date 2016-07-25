import logging

# ---------------------------------------------------------------------------------------------------------
# USER INPUTS
# ---------------------------------------------------------------------------------------------------------

# Directory and run names
datdir = "/home/user/data"                          # the base data directory
dname = "sipm_maps_10000"         # the data name
rdir = "/home/user/dnn/run_reconstruct"             # the run directory
rname = "reconstruct_test_8k"

# Net configuration parameters
net_name = "MNISTadv"                    # name of the neural net described in nets/neuralnets.py
train_init = True                          # if true, train from net with standard pre-training; if false, read in a previously trained net

# Response map parameters
nsipm = 8
ngrid = 1600

# Parameters describing training intervals and number of events for training and validation
ntrain_evts = 8000    # number of training evts per dataset
nval_evts = 200       # number of validation events
num_epochs = 200       # total number of epochs to train
epoch_blk_size = 1     # number of epochs to run per block (before reading new dataset); set equal to num_epochs unless data to be read in multiple blocks
dtblk_size = 8000      # number of signal and background events per training block
batch_size = 200       # training batch size

# Training optimizer parameters
opt_lr = 1.0e-4        # optimizer learning rate
opt_eps = 1.0e-6       # optimizer epsilon (for AdamOptimizer)
opt_mom = 0.9          # optimizer momentum
opt_decaybase = 0.2    # multiplicative factor for learning rate decay
opt_ndecayepochs = 40  # decay interval: apply decay by a factor of opt_decaybase every opt_ndecayepochs epochs

# Plotting and logging parameters
log_to_file = True         # set to True to output log information to a file rather than the console
logging_lvl = logging.INFO  # logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
#plt_show = False       # show plots on-screen for dnnplot
#plt_imgtype = "png"    # image type to which to save plots

# END USER INPUTS
# ------------------------------------------------------------------------------------------

# Calculated parameters (based on user inputs)
batches_per_epoch = int(dtblk_size/batch_size)
num_epoch_blks = num_epochs / epoch_blk_size
num_dt_blks = ntrain_evts / dtblk_size
nsensors = nsipm * nsipm
