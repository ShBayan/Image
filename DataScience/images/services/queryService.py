from images.services.bulkImageService import BulkImages
from images.models.serializers import ImageSerializer
from images.services.downloadService import DownloadImage
from images.models.models import ImagesInfo


class QueryService:
    def send_to_save(self,vendor_name):
        image_instance=ImagesInfo.objects.filter(isDone=False)
        image_instance=image_instance.exclude(errorType='Wrong URL').values()
        image_instance=image_instance.filter(vendorName=vendor_name).values()
        images_info = list(image_instance)
        num=len(images_info)
        if num>=1:

            for i in range(0,num,10):
                chunked_list=images_info[i:i+10]
                download_instance=DownloadImage()
                download_instance.get_info(chunked_list)







