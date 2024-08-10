from images.services.getColor import GetColors
class ColorController:
    def color_controller(self,request):
        vendor = request.GET['vendor']
        color_instance = GetColors()
        color_instance.get_colors(vendor)
