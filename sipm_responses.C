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
  
  int N = 1; // Number of photons
  
  double max_xy = 7*sipm_pitch + 2*sipm_edge_width; // maximum x and y value (80 mm)
  
  double max_p = max_xy /grid_space; // number of points per line (40)
  
  TFile f("simulation_N_1.root"); // TFile in which to store the tree.
  
  TTree * tr = new TTree("sim_responses","Locations  of  the  grid  points  and  the responses of the SiPMs for each"); 
  
  //Variables assigned to branches: location(x,y), array of responses
  
  double x, y;
  double * sipm_prob = new double[NSIPM*NSIPM];
  
  //Branches:
  
  tr->Branch("x", &x, "x/I"); // /I??
  tr->Branch("y", &y, "y/I");
  tr->Branch("sipm_prob", sipm_prob, "sipm_prob[NSIPM*NSIPM]/D");
  
  for(x=0; x<(max_p);x++){
	  
	  for(y=0; y<(max_p);y++){
		  x = x*grid_space + grid_space/2; // half point of the grid (1,3,5..79)
		  y = y*grid_space + grid_space/2; // half point of the grid (1,3,5..79)

		  get_responses(N,x,y,sipm_prob);
		  
		  tr->Fill(); 
		  
		  // So that the loop keeps working with x, y: 0,1,2..39 we undo the changes of these variables:
		  x = (x - grid_space/2)/grid_space;
		  y = (y - grid_space/2)/grid_space;
		   
		  }
  }
  
  tr->Write(); //Write the tree to the file
  f.Close() // Close the file
}
	