import io
from PIL import Image
from io import BytesIO
from DataScience import settings
from images.services.logService import LogService
from images.services.blobService import BlobImages


class RotateImages:

    def download_image(self,sku,filename,vendor,collection,design):

        try:

            url_address=settings.AZURE_HTTP_HOST+'/'+vendor+'/'+collection+'/'+design+'/'+filename+'.jpg'
            api='rotateImage'
            file=BlobImages().to_blob(url_address,api,sku,filename,vendor,collection,design)

            if file is not None:
                image = Image.open(BytesIO(file))
                return image

            else:
                return None


        except Exception as e:
            print("********* The image can't be rotated **********",str(e))


    def rotate_image(self,sku,vendor,collection,design,filename,direction):

        try:

            image=self.download_image(sku,filename,vendor,collection,design)

            if direction == 'right':
                rotated_image=image.rotate(-90, expand=1)

            elif direction == 'left':
                rotated_image=image.rotate(90, expand=1)

            else:
                rotated_image = image

            bytes_io = io.BytesIO()
            rotated_image.save(bytes_io, "JPEG")
            bytes_image = bytes_io.getvalue()
            return bytes_image


        except Exception as e:
            LogService.set_file_error(filename, '*********', str(e), '****** Save The Image *****', vendor,collection,design)


