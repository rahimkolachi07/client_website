from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods import media
import os

# WordPress site URL and credentials
wordpress_url = 'http://www.spreadit.es/xmlrpc.php'
wordpress_username = 'spreadit.mkt@gmail.com'
wordpress_password = 'ArthurFiverrAccess22!'

def upload_image(image_path):
    # Create WordPress client
    client = Client(wordpress_url, wordpress_username, wordpress_password)

    # Open the image file
    with open(image_path, 'rb') as img:
        # Prepare the data for WordPress
        data = {
            'name': os.path.basename(image_path),
            'type': 'image/png',  # Adjust accordingly
            'bits': img.read(),
            'overwrite': False
        }

        # Upload the image to WordPress media
        response = client.call(media.UploadFile(data))
        # Get the URL of the uploaded image
        return response['id']
