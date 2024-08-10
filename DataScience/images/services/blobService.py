import requests
from images.models.models import ImagesInfo


class BlobImages:
    @staticmethod
    def to_blob(url,api,sku,filename,vendor,collection,design):

        try:
            response=requests.get(url,timeout=180)
            content_type = response.headers['content-type']

            if content_type:

                if content_type=='image/jpeg' or content_type=='application/binary' or content_type=='application/octet-stream':
                    image_blob=response.content
                    return image_blob
                else:
                    blob_instance=ImagesInfo.objects.get(id=id)
                    blob_instance.errorType='Wrong URL'
                    blob_instance.save()
                    return None

        except Exception as e:

            print('***** error in download image *****',str(e))
            if api!='blobService' or 'rotateImage':
                blob_instance = ImagesInfo.objects.get(vendorName=vendor,SKU=sku,imageName=filename)
                blob_instance.errorType = 'Wrong URL'
                blob_instance.save()

