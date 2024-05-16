from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import shutil
from upload import *

def blog_post(topic,subtopics,blog1,blog2,blog3,blog4):
    print("uploading")
    wordpress_url = 'http://www.spreadit.es//xmlrpc.php'
    wordpress_username = 'spreadit.mkt@gmail.com'
    wordpress_password = 'ArthurFiverrAccess22!'
    # Create WordPress client
    client = Client(wordpress_url, wordpress_username, wordpress_password)

    # Create a new WordPress post
    post = WordPressPost()
    blog1=blog1.split("\n")
    blog2=blog2.split("\n")
    blog3=blog3.split("\n")
    blog4=blog4.split("\n")
    print("blog1  =",blog1)


    post.title = topic
    post.content = f"""
    <h3>{subtopics[0]}</h3>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog1[0]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog1[2]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog1[4]}</p>


    
    <h3>{subtopics[1]}</h3>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog2[0]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog2[2]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog2[4]}</p>



    <h3>{subtopics[2]}</h3>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog3[0]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog3[2]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog3[4]}</p>



    <h3>{subtopics[3]}</h3>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog4[0]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog4[2]}</p>
    <p align="justify" style="color: white; font-size: 18px; font-weight: bold;">{blog4[4]}</p>


    """
    post.post_status = 'publish'  # Cshange to 'draft' if you want to save as draft
    #post.thumbnail = upload_image("feature_image.png")

    # Publish the post
    post_id = client.call(NewPost(post))
    print("Post created successfully!")
    print("New post ID:", post_id)
    try:
        shutil.rmtree("images")
        print(f"Folder images deleted successfully.")
    except OSError as e:
        print(f"Error: images : {e.strerror}")
    return post_id