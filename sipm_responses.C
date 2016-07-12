// Main script file for simulation of SiPM responses.

// Performs initialization procedures
void init() {

  setup_sipms(sipm_pos_x, sipm_pos_y);

}

// Main method of script: runs the simulation
void run() {

  // Load the related script files.
  gROOT->ProcessLine(".L vars.C");
  gROOT->ProcessLine(".L sipm_functions.C");

  // Initialize.
  init();

  // Generate SiPM responses for each grid point and save
  // the response array to a TTree.
}
