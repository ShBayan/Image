from PIL import Image
import io

class ResizeImage:

    def small_image(self,file):

        image_file = file

        try:

            if image_file is not None:
                dim=image_file.size
                width=dim[0]
                height=dim[1]

                if height>width:
                    ratio=width/height
                    height=ResizeImage.set_size(height,700,500)
                    width=height*ratio

                else:
                    ratio=height/width
                    width=ResizeImage.set_size(width,700,500)
                    height=width*ratio

                small_image=self.resize_to_small(image_file,width,height,True,70)

                return small_image


        except Exception as e:
            print( {'error_key': 'create_small', 'error': str(e), 'status': False})



    def resize_to_small(self,file,width,height,optimize=False,quality=100):
        try:

            width=int(width)
            height=int(height)
            newim = file.resize((width, height))
            bytes_io = io.BytesIO()
            newim.save(bytes_io, "JPEG", optimize=optimize, quality=quality)
            bytes_image = bytes_io.getvalue()
            return bytes_image

        except Exception as e:
            print({'error_key': 'resize_small', 'error': str(e), 'status': False})



    def thumbnail_image(self,file):

        image_file=file


        try:
            thumbnail_image=self.create_thumbnail(image_file)
            return thumbnail_image

        except Exception as e:
            print( {'error_key': 'create_thumbnail', 'error': str(e), 'status': False})




    def create_thumbnail(self,file):

        try:

            width = 128
            height = 128
            imcopy = file.copy()
            imcopy.thumbnail((width, height), Image.ANTIALIAS)
            bytes_iothumb = io.BytesIO()
            imcopy.save(bytes_iothumb, "JPEG")
            bytes_thumb = bytes_iothumb.getvalue()
            return bytes_thumb


        except Exception as e:
            print({'error_key': 'resize_thumbnail', 'error': str(e), 'status': False})



    @staticmethod
    def set_size(value, max, min):
        if value < max + min:
            h = min / value
        else:
            h = max / (value + min)

        height = value * h
        return height