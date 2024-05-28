import requests


"""
Api DETAISL

mode=0:
    when you select mood 0 it return of PII from text
mode=1
    here it will return you original PII and fake PII using gemini. here data is not moving to gemini but tell the gemini to
    generate fake pii. due to limitation of gemini you may get errors. if you use gemini paid of chatgpt then it will works
    perfect

mode=2
    it returns original pii, fake pii and fake pii with text. the text you give as input it will return you same text with 
    fake pii. need paid gemini or chatgpt

mode=3
    it returns original pii, fake pii, text with fake pii and response from llm model. so the llm model will 
    give response with fake text pii. need paid llm

mode=4
    it returns original pii, fake pii, text with fake pii, llm response with fake text and replaced fake pii in llm to 
    return original pii in llm response. hance no original data moves to llm model. needs an paid chatgpt.
"""
url = "http://127.0.0.1:8000/email"


text="raheemkolachi@gmail.com"

mode=4 # change the mode of you want.

payload = {"text": text,"mood":mode}
response = requests.post(url, json=payload)
if response.status_code == 200:
    result = response.json()
    print("result:", result)
else:
    print("Error:", response.text)
