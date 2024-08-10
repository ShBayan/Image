from azure.storage.blob import BlockBlobService, PublicAccess
from images.services.resizeService import ResizeImage
from images.models.models import ImagesInfo
from DataScience import settings
from io import BytesIO
from PIL import Image


class SaveImages:

    def save_images(self,sku,file,firstfilename,vendor,collection,design):

        try:
            if file is not None:
                image_file = Image.open(BytesIO(file))
                resize_instance=ResizeImage()
                small=resize_instance.small_image(image_file)
                thumbnail=resize_instance.thumbnail_image(image_file)
                block_blob_service=BlockBlobService(account_name=settings.AZURE_STORAGE, account_key=settings.AZURE_KEY)
                existence=block_blob_service.exists(vendor)

                if existence is False:
                    block_blob_service.create_container(vendor)
                    block_blob_service.set_container_acl(vendor, public_access=PublicAccess.Container)


                filename=collection+'/'+design+'/'+firstfilename
                new_filename = filename + ".jpg"
                small_filename=filename+"_S.jpg"
                thumbnail_filename=filename+"_T.jpg"


                save_original=block_blob_service.create_blob_from_stream(vendor,new_filename,BytesIO(file))
                save_small = block_blob_service.create_blob_from_stream(vendor, small_filename, BytesIO(small))
                save_thumbnail = block_blob_service.create_blob_from_stream(vendor, thumbnail_filename, BytesIO(thumbnail))


                if 'object at' in str(save_original):
                    image_instance=ImagesInfo.objects.get(vendorName=vendor,SKU=sku,imageName=firstfilename)
                    image_instance.isDone=True
                    image_instance.save()


        except Exception as e:
            print({'error_key': 'save image in azure', 'error': str(e), 'status': False})

