from images.services.saveImageService import SaveImages
from images.models.serializers import ImageSerializer

class SaveImageController:
    def save_image_controller(self,request):
        if request.method=='POST':

            filename=request.GET['filename']
            vendor=request.GET['vendor']
            sku=request.GET['sku']
            collection=request.GET['collection']
            design=request.GET['design']
            temp_file=request.FILES['file']
            file = temp_file.read()
            serializer = ImageSerializer(data={'imageName': filename, 'vendorName':vendor, 'collectionName': collection, 'designName': design, 'SKU': sku})
            if serializer.is_valid():
                serializer.save()
            SaveImages().save_images(sku, file, filename, vendor, collection, design)
