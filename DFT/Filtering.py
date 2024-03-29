# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv
import numpy as np
import cv2

class Filtering:
    image = None
    filter = None
    cutoff = None
    order = None

    def __init__(self, image, filter_name, cutoff, order=0):
        """initializes the variables frequency filtering on an input image
        takes as input:
        image: the input image
        filter_name: the name of the mask to use
        cutoff: the cutoff frequency of the filter
        order: the order of the filter (only for butterworth
        returns"""
        self.image = image
        if filter_name == 'ideal_l':
            self.filter = self.get_ideal_low_pass_filter
        elif filter_name == 'ideal_h':
            self.filter = self.get_ideal_high_pass_filter
        elif filter_name == 'butterworth_l':
            self.filter = self.get_butterworth_low_pass_filter
        elif filter_name == 'butterworth_h':
            self.filter = self.get_butterworth_high_pass_filter
        elif filter_name == 'gaussian_l':
            self.filter = self.get_gaussian_low_pass_filter
        elif filter_name == 'gaussian_h':
            self.filter = self.get_gaussian_high_pass_filter

        self.filter_name = filter_name

        self.cutoff = cutoff
        self.order = order


    def get_ideal_low_pass_filter(self, shape, cutoff):
        """Computes a Ideal low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal low pass mask"""

        height, width = shape.shape
        idealLowPass = np.zeros((height, width), dtype=np.uint8)
        centerPoint1 = height/2
        centerPoint2 = width/2

        for h in range(height):
            for w in range(width):
                distance = np.sqrt((h-centerPoint1)**2 + (w-centerPoint2)**2)
                if distance <= cutoff:
                    idealLowPass[h, w] = 1
                else:
                    idealLowPass[h, w] = 0

        return idealLowPass


    def get_ideal_high_pass_filter(self, shape, cutoff):
        """Computes a Ideal high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        height, width = shape.shape

        idealHighPass = np.zeros((shape.shape), dtype=np.uint8)
        centerPoint1 = height / 2
        centerPoint2 = width / 2

        for h in range(height):
            for w in range(width):
                distance = np.sqrt((h - centerPoint1) ** 2 + (w - centerPoint2) ** 2)
                if distance <= cutoff:
                    idealHighPass[h, w] = 0
                else:
                    idealHighPass[h, w] = 1

        return idealHighPass

    def get_butterworth_low_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth low pass mask"""

        height, width = shape.shape
        butterworthLowPass = np.zeros(shape.shape)
        centerPoint1 = height / 2
        centerPoint2 = width / 2
        for h in range(butterworthLowPass.shape[0]):
            for w in range(butterworthLowPass.shape[1]):
                distance = np.sqrt((h - centerPoint1) ** 2 + (w - centerPoint2) ** 2)
                butterworthLowPass[h, w] = 1 / (1 + (distance / cutoff) ** (2*order))
        return butterworthLowPass

    def get_butterworth_high_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        height, width = shape.shape
        butterworthHighPass = np.zeros(shape.shape)
        centerPoint1 = height / 2
        centerPoint2 = width / 2
        for h in range(butterworthHighPass.shape[0]):
            for w in range(butterworthHighPass.shape[1]):
                distance = np.sqrt((h - centerPoint1) ** 2 + (w - centerPoint2) ** 2)
                butterworthHighPass[h, w] = 1 / (1 + (cutoff / distance) ** (2*order))
        return butterworthHighPass

    def get_gaussian_low_pass_filter(self, shape, cutoff):
        """Computes a gaussian low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian low pass mask"""

        height, width = shape.shape
        gaussianLowPass = np.zeros(shape.shape)
        centerPoint1 = height / 2
        centerPoint2 = width / 2
        for h in range(gaussianLowPass.shape[0]):
            for w in range(gaussianLowPass.shape[1]):
                distance = np.sqrt((h - centerPoint1) ** 2 + (w - centerPoint2) ** 2)
                # if distance > cutoff:
                gaussianLowPass[h, w] = np.exp(-(distance ** 2) / (2 * (cutoff ** 2)))

        return gaussianLowPass


    def get_gaussian_high_pass_filter(self, shape, cutoff):
        """Computes a gaussian high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        height, width = shape.shape
        gaussianHighPass = np.zeros(shape.shape)
        centerPoint1 = height / 2
        centerPoint2 = width / 2
        for h in range(gaussianHighPass.shape[0]):
            for w in range(gaussianHighPass.shape[1]):
                distance = np.sqrt((h - centerPoint1) ** 2 + (w - centerPoint2) ** 2)
                gaussianHighPass[h, w] = 1 - np.exp(-(distance ** 2) / (2 * (cutoff ** 2)))

        return gaussianHighPass

    def post_process_image(self, image):
        """Post process the image to create a full contrast stretch of the image
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        1. Full contrast stretch (fsimage)
        2. take negative (255 - fsimage)
        """
        # J(i, j) = P·I(i, j) + L

        return 0


    def filtering(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of DFT, magnitude of filtered DFT        
        ----------------------------------------------------------
        You are allowed to used inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape, cutoff, order)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do a full contrast stretch on the magnitude and depending on the algorithm you may also need to
        take negative of the image to be able to view it (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of DFT, magnitude of filtered DFT: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8 
        """

        fft = np.fft.fft2(self.image)
        shift = np.fft.fftshift(fft)
        #  magnitude of DFT
        mag = 10*np.log(np.abs(shift))
        magnitudeOfDFT = np.uint8(mag)
        filterName = self.filter_name

        #  filtered image
        if filterName == 'butterworth_l':
            Mask = self.filter(self.image, self.cutoff, self.order)
            new_img = np.abs(np.fft.ifft2(np.fft.ifftshift(shift * Mask)))

        elif filterName == 'butterworth_h':
            Mask = self.filter(self.image, self.cutoff, self.order)
            new_img = 10 * np.abs(np.fft.ifft2(np.fft.ifftshift(shift * Mask)))

        elif filterName == 'ideal_l' or filterName == 'gaussian_l':
            Mask = self.filter(self.image, self.cutoff)
            new_img = np.abs(np.fft.ifft2(np.fft.ifftshift(shift * Mask)))

        elif filterName == 'ideal_h' or filterName == 'gaussian_h':
            Mask = self.filter(self.image, self.cutoff)
            new_img = 10 * (np.abs(np.fft.ifft2(np.fft.ifftshift(shift * Mask))))

        #  magnitude of filtered DFT
        magnitudeOfFilteredDFT = 10 * np.log(np.abs(shift*Mask)+1)

        return [new_img, magnitudeOfDFT, magnitudeOfFilteredDFT]
