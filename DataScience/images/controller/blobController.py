
from images.services.blobService import BlobImages
class BlobController:
    def blob_controller(self,request):
        url=None
        api='blobService'
        if request.method == 'GET':
            url = request.GET['url']

        image = BlobImages.to_blob(url,api,sku=None, filename=None, vendor=None, collection=None, design=None)
        return image







