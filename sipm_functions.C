// Assign x and y positions to each of the SiPMs
void setup_sipms(double * sipm_pos_x, double * sipm_pos_y) {

  cout << "\n FUNCTION setup_sipms" << endl;

  for(int r = 0; r < NSIPM; r++) {
    for(int c = 0; c < NSIPM; c++) {
      sipm_pos_x[r + c*NSIPM] = sipm_edge_width + r*sipm_pitch;
      sipm_pos_y[r + c*NSIPM] = sipm_edge_width + c*sipm_pitch;
      if(DEBUG > 1) {
        cout << "[SIPM (" << (r + NSIPM*c) << ")] position = (" << sipm_pos_x[r + c*NSIPM] << ","
             << sipm_pos_y[r + c*NSIPM] << ")" << endl;
      }
    }
  }
}

// Caculate a random set of 64 SiPM responses (normalized to mean = 0, sigma = 1).
void get_responses(int N, int x, int y, double * sipm_prob) {

  double mean;
  double sigma;

  // Calculate the probabilities.
  for(int r = 0; r < NSIPM*NSIPM; r++) {
    sipm_prob[r] = (1/((4*TMath::Pi()*d_gap)/sqrt(pow((x - sipm_pos_x[r]),2) + pow((y - sipm_pos_y[r]),2) + pow(ze,2)))) * (1 - sqrt((pow((x - sipm_pos_x[r]),2) + pow((y - sipm_pos_y[r]),2) + pow(ze,2))/(pow((x - sipm_pos_x[r]),2) + pow((y - sipm_pos_y[r]),2) + pow((ze + d_gap),2))));
	}

  // Throw "binomial"-distributed random numbers of photons about some average N*prob.
  for(int r = 0; r < NSIPM*NSIPM; r++) {
      sipm_prob[r] = rd.Gaus(N*sipm_prob[r], sqrt(N*sipm_prob[r]*(1 - sipm_prob[r])));
  }

  // Shift the mean to 0.
  mean = TMath::Mean(64, sipm_prob);
  for(int r = 0; r < NSIPM*NSIPM; r++) {
  	sipm_prob[r] = sipm_prob[r] - mean;
  }	
  
  // Shift the standard deviation to 1.
  sigma = TMath::RMS(64, sipm_prob);
  for(int r = 0; r < NSIPM*NSIPM; r++) {
  	sipm_prob[r] = sipm_prob[r]/sigma;
  }
}	
