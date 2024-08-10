from PIL import Image
import math


class CropMargin:
    def crop_margin(self,img):
        image=Image.open(img)
        pix=image.load()
        dim=image.size
        width = dim[0]
        height = dim[1]
        half_of_width=width/2
        half_of_width=int(math.ceil(half_of_width))
        half_of_height=height/2
        half_of_height=int(math.ceil(half_of_height))

        crop_dim1=crop_dim2=crop_dim3=crop_dim4=crop_dim5=crop_dim6=crop_dim7=crop_dim8=0

        for i in range(0, half_of_width):

            if pix[i, half_of_height][0] != 255 or pix[i, half_of_height][1] != 255 or pix[i, half_of_height][2] != 255:
                crop_dim1 = i
                break

        for i in range(0,half_of_height):
            if pix[half_of_width,i][0]!=255 or pix[half_of_width,i][1]!=255 or pix[half_of_width,i][2]!=255:
                crop_dim2=i
                break

        for i in range(1, half_of_width):
            if pix[width - i, half_of_height][0] != 255 or pix[width - i, half_of_height][1] != 255 or pix[width - i, half_of_height][2] != 255:
                crop_dim3 = width - i - 1
                break

        for i in range(1,half_of_height):
            if pix[half_of_width,height-i][0]!=255 or pix[half_of_width,height-i][1]!=255 or pix[half_of_width,height-i][2]!=255:
                crop_dim4=height-i-1
                break


        if crop_dim1>0 or crop_dim2>0 or crop_dim3>0 or crop_dim4>0:
            new_image = image.crop((crop_dim1, crop_dim2, crop_dim3, crop_dim4))
            return new_image

        else:
            return image



