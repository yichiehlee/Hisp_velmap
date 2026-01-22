# Hisp_velmap: Joint GNSS and InSAR 3D Velocity Inversion

This repository contains the Python implementation of **VELMAP**, used for the joint inversion of GNSS and InSAR velocity fields to reconstruct high-resolution 3D surface velocity. We use **Hispaniola** as a primary case study, demonstrating how sparse GNSS networks and high-resolution InSAR tracks can be fused to interpret 3D velocity field.

---

## Main Driver
The primary workflow is contained in **[`Run_python.ipynb`](https://github.com/yichiehlee/Hisp_velmap/blob/main/Run_python.ipynb)**. This notebook handles the data integration, weight optimization, and the final 3D velocity reconstruction.

---

## Required Input Files

### 1. GNSS Velocity Field
* **Example:** `UNR_B12_C10_C22.txt` (located in the `/Data` folder).
* **Content:** Horizontal and vertical geodetic velocities with associated uncertainties.

### 2. InSAR LOS Data
Stored as `.mat` files (e.g., `AT04A1all.mat` and `DT142A1all.mat`). These files must contain:

| Variable | Description |
| :--- | :--- |
| **`G_insar`** | Sparse matrix of the 1D Line-Of-Sight (LOS) geometry. |
| **`velo`** | Observed velocity field. |
| **`velostd`** | Standard deviation of the velocity. |
| **`losx, losy, losz`** | Unit vectors defining the LOS direction in East, North, and Up coordinates. |
| **`inc`, `az`** | Satellite incidence and azimuth angles (degrees). |
| **`lon`, `lat`** | Geographic coordinates for each pixel. |



### 3. InSAR Covariance Matrix
* **Generation:** Created using **[`create_cov_insar.ipynb`](https://github.com/yichiehlee/Hisp_velmap/blob/main/create_cov_insar.ipynb)**.


---

## Reference
For detailed information regarding the methodology, data processing, and tectonic implications, please refer to:

**[Dense 3D Geodetic Velocities and Strain-rate Field for Hispaniola and Implications for Seismic Hazard](https://essopenarchive.org/doi/full/10.22541/essoar.174643341.10197058)**

---
