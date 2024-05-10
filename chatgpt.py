import openai
import pandas as pd
openai.api_key = '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'
def text_topics(message):
   messages = [ {"role": "system", "content":f"You have 30 year experience of blog writing on {message}. write titles 200 on {message} . best titles in only spanish. return me comma seperated titles. dont write number or any other charecter, just return topics  "},{"role": "user", "content": "write 200 best topic names for "+message}, ]
   chat = openai.ChatCompletion.create( model="gpt-4", messages=messages)
   answer = chat.choices[0].message.content
   topics=pd.DataFrame({"topics":answer.split(",")})
   topics.to_csv("topics.csv",index=False)
   return answer

def text_subtopic(message):
   messages = [ {"role": "system", "content":"You have 30 year experience of blog writing. write subtopics. must be comma seperated. should be best subtopics in spanish. i need in spanish language"},{"role": "user", "content": "write an 4 sub topics on main topic=  ["+message+"] in spanish"}, ]
   chat = openai.ChatCompletion.create( model="gpt-4", messages=messages)
   answer = chat.choices[0].message.content
   return answer

def text_gen(message):
   messages = [ {"role": "system", "content":"You have 30 year experience of content writing. write three best paragraphs. write in only spanish. dont use any sub headings just write 3 long paragraph on given topic  "},{"role": "user", "content": "write an perfect three paragraph in spanish and focuse on topic. this is= "+message}, ]
   chat = openai.ChatCompletion.create( model="gpt-4", messages=messages)
   answer = chat.choices[0].message.content
   return answer

def text_prompt(message):
   messages = [ {"role": "system", "content":" You have 30 year experience of prompt writing . write an prompt for image generation. image must describe the main purpose of topic. return best image generation prompt. make it short prompt. i want 8k images quality. hight quality image focuse on main topic. i need for feature image. write an best prompt for feature image according to user data ."},{"role": "user", "content":message }, ]
   chat = openai.ChatCompletion.create( model="gpt-4", messages=messages)
   answer = chat.choices[0].message.content
   return answer

def text_title(message):
   messages = [ {"role": "system", "content":"You have 30 year experience of title writting. anaylyze the complete text and writ best title.retun an only title. "},{"role": "user", "content":message }, ]
   chat = openai.ChatCompletion.create( model="gpt-4", messages=messages)
   answer = chat.choices[0].message.content
   return answer




# importing other libraries 
import requests 
from PIL import Image
from io import BytesIO


def save_image_from_url(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save("feature_image.png")
def generate(text): 
   res = openai.Image.create( 
      # text describing the generated image 
      prompt=text, 
      # number of images to generate 
      n=1, 
      # size of each generated image 
      size="1024x1024", 
   ) 
   # returning the URL of one image as 
# we are generating only one image 
   url=res["data"][0]["url"]
   save_image_from_url(url)
   return res["data"][0]["url"]
