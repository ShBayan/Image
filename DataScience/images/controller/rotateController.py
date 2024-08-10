from images.services.rotateService import RotateImages
from images.services.saveImageService import SaveImages
class RotateController:
    def rotate_controller(self,request):
        vendor = request.GET['vendor']
        collection = request.GET['collection']
        design = request.GET['design']
        filename = request.GET['filename']
        sku=request.GET['sku']
        direction = request.GET['direction']
        api = 'rotateImage'
        rotated_image = RotateImages().rotate_image(sku,vendor, collection, design, filename, direction)
        SaveImages().save_images(sku, rotated_image, filename, vendor, collection, design)
        return rotated_image







