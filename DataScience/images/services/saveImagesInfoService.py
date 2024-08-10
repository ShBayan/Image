from azure.storage.blob import BlockBlobService, PublicAccess
from images.services.convertService import ConvertImage
from images.services.resizeService import ResizeImage
from images.models.models import ImagesInfo
from DataScience import settings
from io import BytesIO
from PIL import Image
import datetime


class SaveImagesInfo:
    def save_images_info(self,images_info):

        try:
            open_time = datetime.datetime.now().time()
            first_filename=images_info['fileName']
            sku=images_info['sku']
            collection=images_info['collection']
            design=images_info['design']
            vendor=images_info['vendor']
            body=images_info['body']


            if body is not None:
                image_file = Image.open(BytesIO(body))


                resize_instance = ResizeImage()
                small = resize_instance.small_image(image_file)
                thumbnail = resize_instance.thumbnail_image(image_file)
                block_blob_service = BlockBlobService(account_name=settings.AZURE_STORAGE, account_key=settings.AZURE_KEY)
                existence = block_blob_service.exists(vendor)

                if existence is False:
                    block_blob_service.create_container(vendor)
                    block_blob_service.set_container_acl(vendor, public_access=PublicAccess.Container)

                filename=collection+'/'+design+'/'+first_filename
                new_filename = filename + ".jpg"
                small_filename = filename + "_S.jpg"
                thumbnail_filename = filename + "_T.jpg"
                save_original = block_blob_service.create_blob_from_stream(vendor, new_filename, BytesIO(body))
                save_small = block_blob_service.create_blob_from_stream(vendor, small_filename, BytesIO(small))
                save_thumbnail = block_blob_service.create_blob_from_stream(vendor, thumbnail_filename, BytesIO(thumbnail))

                if 'object at' in str(save_original):
                    db_instance=ImagesInfo.objects.get(vendorName=vendor,SKU=sku,imageName=first_filename)
                    db_instance.isDone=True
                    db_instance.save()
                return sku


        except Exception as e:
            print({'error_key': 'save images info in azure', 'error': str(e), 'status': False})


