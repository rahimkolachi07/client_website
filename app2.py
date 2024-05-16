
from chatgpt import *
from blog_upload import *
import time
from social import *

text="""

Buenas chat, a partir de ahora vamos a realizar una tarea muy pero que muy importante. Soy el dueño de Spreadit Marketing, una agencia de marketing digital que ofrecemos los siguientes servicios: Branding, Páginas web, SEO y SEM, Redes sociales, Estrategia digital, Diseño, Hostess y Eventos, Brading y Rebrading, Anuncios y publicidad, Shootings, Merchandising y soluciones IA.
Tenemos ya más de 25 clientes y hemos decidido pasar la agencia al siguiente nivel, y es por eso que estamos haciendo un rebranding completo.
A partir de ahora quiero que actúes como consultor experto en persuasión, marketing, ventas, comunicación y experto en cualquier área relacionada para que me ayudes a definir bien la marca Spreadit.
Ahora, con todo lo que sabes hasta aquí, haremos la generación de blogs en español para complementar el contenido de la página web. Debes actuar como un experto en copywritting y marketing. Debes usar palabras clave de una agencia de marketing, utiliza sobre todo, siempre que puedas, lo siguiente:

- precio página web
- diseño de paginas web precios
- gestión redes sociales
- creación páginas web profesionales
- agencias de eventos barcelona

Crea blogs con contenido muy interactivo y interesante, que cualquier persona pueda leerlo y le sea interesante, que no se haga aburrido.


"""
fields=["Branding", "Sitios Web", "SEO y SEM","Redes Sociales", "Estrategia Digital", "Diseño", "Azafatas y Eventos", "Branding y Rebranding", "Ads y Publicidad", "Shootings", "Merchandising y soluciones de IA"]

if os.path.exists("fields.csv"):
    fields=pd.read_csv("fields.csv")
else:
    field={"fields":fields}
    field=pd.DataFrame(field)
    field.to_csv("fields.csv",index=False)
    fields=pd.read_csv("fields.csv")
for i, field in enumerate(fields["fields"]):
    try:
        if field=="done":
            print("already done this field")
        else:
            print(field)
            if os.path.exists("topics.csv"):
                topics=pd.read_csv("topics.csv")
            else:
                text_topics(field)
                topics=pd.read_csv("topics.csv")
            
            for i, topic in enumerate(topics["topics"]):
                try:
                        
                    if topic=="done":
                        print("already done with this topic")
                    else:
                        subtopics1=text_subtopic(topic)

                        subtopics=subtopics1.split(",")
                        print(subtopics)
                        blog1=text_gen(subtopics[0])
                        blog2=text_gen(subtopics[1])
                        blog3=text_gen(subtopics[2])
                        blog4=text_gen(subtopics[3])

                        image_prompt=text_prompt(topic)
                        generate(image_prompt+"image quality 8k ")
                        id=blog_post(topic,subtopics,blog1,blog2,blog3,blog4)
                        time.sleep(10)
                        main_tweet=text_social(subtopics1)
                        text=text_short(main_tweet)
                        while len(text)>210:
                            print("text length is "+str(len(text)))
                            text=text_short(main_tweet)
                            main_tweet=text
                            time.sleep(5)


                        twitter_posting(text,id)


                        topics["topics"][i]="done"
                        topics.to_csv("topics.csv",index=False)
                        for i in range(12*60*60):
                            tim=12*60*60
                            i=i+1
                            b=4*60*60
                            if i%b==0:
                                main_tweet=text_social(subtopics1)
                                text=text_social(main_tweet)
                                twitter_posting(text,id)
                            time.sleep(1)
                            print("new post will be uploaded after ",tim-i," Seconds")
                except Exception as e:
                    print("error ", e)

                fields["fields"][i]="done"
                os.remove("topics.csv")
                fields.to_csv("fields.csv",index=False)

    except Exception as e:
        print("field loop error",e)