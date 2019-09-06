
1. DFT:
Write code for computing forward fourier transform, inverse fourier transform, discrete cosine transfrom and magnitude of the fourier transform. 
The input is a 2D matrix of size 15X15.

2. Frequency Filtering:
Write Code to perfrom image filtering in the frequency domain by modifying the DFT of images using different masks. 

Filter images using six different filters: 
ideal low pass (ideal_l), ideal high pass (ideal_h), 
butterworth low pass (butterworth_l), butterworth high pass (butterworth_h), 
gaussian low pass (gaussian_l) and gaussian high pass filter (gaussian_h). 

The input to your program is an image, name of the mask, cuttoff frequency and order(only for butterworth filter).

--------------------------

How to Run your code?

  - Usage: ./dip_hw2_region_analysis.py -i image-name
       - image-name: name of the image
  - example: ./dip_hw2_region_analysis.py -i cells.png
  - Please make sure your code runs when you run the above command from prompt
  - Describe your method and findings in the report.md file
  - Any output images or files must be saved to "output/" folder

---------------------------

1. the first part has to run using command

  python dip_hw3_dft.py
 
  and the second part using
  
  python dip_hw3_filtering.py -i image-name -m ideal_l -c 50
  
2. Any output file or image should be written to output/ folder