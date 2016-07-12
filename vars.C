
// Global variables
#define DEBUG 2
#define NSIPM 8

double * sipm_pos_x = new double[NSIPM*NSIPM];
double * sipm_pos_y = new double[NSIPM*NSIPM];
double sipm_pitch = 10.0;       // SiPM pitch in mm
double sipm_edge_width = 5.0;   // width of edge of dice board in mm
double ze = 10.0;               // distance between SiPM plane and EL gap
double grid_space = 2.0;        // grid spacing in mm
