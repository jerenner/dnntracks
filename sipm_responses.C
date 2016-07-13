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
  

  
  int N = 1; // photons
  
  double max_xy = 7*sipm_pitch + 2*sipm_edge_width; // maximum x and y value (80 mm)
  
  double max_p = max_xy /grid_space; // number of points per line (40)
  
  for(double x=0; x<(max_p);x++){
	  
	  for(double y=0; y<(max_p);y++){
		  x = x*grid_space + grid_space/2;
		  y = y*grid_space + grid_space/2;
		  double * sipm_prob = new double[NSIPM*NSIPM];
		  
		  cout << "(" << x << ", " << y << ") " << endl; // llamar a la función get_responses(N,x,y,sipm_prob)
		  //get_responses(N,x,y,sipm_prob);
		  
		  x = (x - grid_space/2)/grid_space;
		  y = (y - grid_space/2)/grid_space;
		   
		  }
  }
  
 /* for(double i=0; i<pow(max_p,2); i++){
	  
	  int p = i % max_p;
	  
	  double y = p*grid_space+1; 
	  double x = floor(i/max_p)*max_p*grid_space-1;
	  
	  double * sipm_prob = new double[NSIPM*NSIPM];
	  

	  
	  cout << "(" << x << ", " << y << ") " << endl;
	 
	  
  }*/
  
  
}
	