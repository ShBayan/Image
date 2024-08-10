import colorsys

class ColorConvert:
    def convert_to_hsv(self,rgb):
        r=rgb[0]
        g=rgb[1]
        b=rgb[2]
        hsv_raw_color = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        hsv_color = (hsv_raw_color[0] * 360, hsv_raw_color[1] * 100, hsv_raw_color[2] * 100)
        return hsv_color