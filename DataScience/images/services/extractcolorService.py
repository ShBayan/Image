from PIL import Image
import colorgram

class Extract_Color:
    def ext_color(self,im):
        colors=colorgram.extract(im,5)
        first_color=colors[0]
        return first_color.rgb







