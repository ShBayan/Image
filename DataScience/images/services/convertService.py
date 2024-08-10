from PIL import Image
import numpy as np

class ConvertImage:

    def convert_image(self,source):

        try:

            cyan=source[0]
            magenta=source[1]
            yellow=source[2]
            black=source[3]

            red=255*(1-cyan)*(1-black)
            green=255*(1-magenta)*(1-black)
            blue=255*(1-yellow)*(1-black)

            return red,green,blue

        except Exception as e:
            print('******* error in convert image *******',str(e))

    def get_pixel(self,image):
        try:
            image1 = np.zeros([image.shape[0],image.shape[1],3])
            for i in range(0, image.shape[0]):
                for j in range(0, image.shape[1]):
                    r,g,b = self.convert_image(image[i,j,:])
                    image1[i, j, 0] =r
                    image1[i, j, 1] = g
                    image1[i, j, 2] = b

            final_image =Image.fromarray(image1,'RGB')
            return final_image

        except Exception as e:
            print('****** error in get pixel *****',str(e))