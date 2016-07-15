// Main script file for simulation of SiPM responses.

// Performs initialization procedures
void init() {

  setup_sipms(sipm_pos_x, sipm_pos_y);

}

// Main method of script: runs the simulation
void run(int ni) {

  // Load the related script files.
  gROOT->ProcessLine(".L vars.C");
  gROOT->ProcessLine(".L sipm_functions.C");

  // Initialize.
  init();

  // Generate SiPM responses for each grid point and save
  // the response array to a TTree.
  
  
  int max_xy = 7*sipm_pitch + 2*sipm_edge_width; // maximum x and y value (80 mm)
  
  int max_p = max_xy /grid_space; // number of points per line (40)
  
  TFile f("simulation_ni.root","RECREATE"); // TFile in which to store the tree.
  
  TTree * tr = new TTree("sim_responses","Locations  of  the  grid  points  and  the responses of the SiPMs for each"); 
  
  //Variables assigned to branches: location(x,y), array of responses
  
  int x, y;
  int rn;
  double * sipm_prob = new double[NSIPM*NSIPM];
  
  //Branches:
  tr->Branch("x", &x, "x/D"); 
  tr->Branch("y", &y, "y/D");
  tr->Branch("sipm_prob", sipm_prob, "sipm_prob[64]/D");
  
  for(int i=0; i < ni; i++){
	  
	  // We generate a random number [0,1599] rn
	  
          rn = floor(rd.Uniform(0,1599)); // integer from [0,1599]
	  
	  x = (rn % max_p)*grid_space + 1;
	  y = (floor(rn/max_p))*grid_space + 1;
	  
	  get_responses(N,x,y,sipm_prob);
	  
	  tr->Fill(); 
	  }  
	  
  tr->Write(); //Write the tree to the file
  f.Close(); // Close the file
}
