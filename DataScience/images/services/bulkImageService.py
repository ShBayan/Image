from __future__ import absolute_import, unicode_literals
from images.services.saveImageService import SaveImages
from images.services.blobService import BlobImages


class BulkImages:

    def save_bulkImages(self,data):

        try:

            vendor=data['vendor']
            image_info=data['imagesInfo']
            for item in image_info:
                url=item['url']
                filename=item['fileName']
                collection=item['collection']
                design=item['design']
                api = 'bulkImage'
                id=1

                file = BlobImages.to_blob(id,url,filename,vendor,collection,design,api)

                if file is not None:
                    SaveImages().save_images(id,file, filename, vendor, collection, design)

        except Exception as e:
            print({'error_key': 'send bulk images to save in azure', 'error': str(e), 'status': False})
