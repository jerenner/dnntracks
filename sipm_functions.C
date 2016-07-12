
// Assign x and y positions to each of the SiPMs
void setup_sipms(double * sipm_pos_x, double * sipm_pos_y) {

  cout << "\n FUNCTION setup_sipms" << endl;

  for(int r = 0; r < NSIPM; r++) {
    for(int c = 0; c < NSIPM; c++) {
      sipm_pos_x[r][c] = sipm_edge_width + r*sipm_pitch;
      sipm_pos_y[r][c] = sipm_edge_width + c*sipm_pitch;
      if(DEBUG > 1) {
        cout << "[SIPM (" << r << "," << c << ")] position = (" << sipm_pos_x[r][c] << ","
             << sipm_pos_y[r][c] << ")" << endl;
      }
    }
  }

}
