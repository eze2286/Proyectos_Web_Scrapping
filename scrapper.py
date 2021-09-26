import requests
import lxml.html as html
import os
import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
encabezados  = {
    "user-agent" : "Mozilla / 5.0 (X11; Linux x86_64) AppleWebKit / 537.36 (KHTML, como Gecko) Ubuntu Chromium / 71.0.3578.80 Chrome / 71.0.3578.80 Safari / 537.36" ,
}
home_url = 'https://www.ambito.com/'
Links = '//div[@class="info-wrapper"]/h2/a/@href'
Titulos = '//h1[@class="title"]//text()'
Resumen = '//h2[@class="excerpt"]//text()'
Cuerpo = '//section[@class="body-content note-body content-protected-false"]//text()'

def parse_notice(link, today):
    try:
        response = requests.get(link, encabezados)
        if response.status_code == 200:
            #notice = response.text
            notice=response.content
            parsed = html.fromstring(notice)
            try:
               title = parsed.xpath(Titulos)[0].strip()
               title = title.replace('\"', '').replace("?", "").replace("¿", "").replace(":", " ").replace("/", "-")
               summary = parsed.xpath(Resumen)[0].strip()
               body_base = parsed.xpath(Cuerpo)[0:]
               body_final = ""
               for linea in body_base:
                    body_final += " " + linea.replace("\n", "").strip()
                        
    

            except IndexError:
                return
            with open(f'{today}/{title}.txt', "w", encoding = "utf-8") as f:
                f.write(title)
                f.write("\n\n")
                f.write(summary)
                f.write("\n\n")
                f.write(body_final)
                f.write("\n")
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)




def parse_home():
    try:
        response = requests.get(home_url, encabezados)
        
        if response.status_code == 200:
             
            home=response.content
            parse = html.fromstring(home)  # Usando lxml me transforma el codigo html de requests a codigo xpath
            links_xpath = parse.xpath(Links)
            

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in links_xpath:
                parse_notice(link, today)

        else:
            raise ValueError(f"Error {response.status_code}")
    except ValueError as ve:
        print(ve)
        
def word_cloud():
    today = datetime.date.today().strftime('%d-%m-%Y')
    #archivos_txt = os.listdir(r'C:\Users\ezequiel\{}'.format(today))
    archivos_txt = os.listdir(r'D:\Desktop\Todas mis cosas\Cursos\EXCEL\Platzi\Git y GitHub\Web_Scrapping\{}'.format(today))
    lista_cruda_noticias = []
    for i in archivos_txt:
        #archivo = open(r'C:\Users\ezequiel\{}\{}'.format(today,i), 'r', encoding = "utf-8", errors='strict')
        archivo = open(r'D:\Desktop\Todas mis cosas\Cursos\EXCEL\Platzi\Git y GitHub\Web_Scrapping\{}\{}'.format(today,i), 'r', encoding = "utf-8", errors='strict')
        contenido = archivo.read()
        contenido = contenido.replace('\n',"")
        contenido = contenido.replace('\t',"")
        contenido = contenido.replace('  '," ")
    #lista_cruda_noticias = lista_cruda_noticias + " " + contenido
        lista_cruda_noticias.append(contenido)
        archivo.close()
    lista_cruda_noticias_one_string = ' '.join(lista_cruda_noticias)
    return lista_cruda_noticias_one_string

def message_cleaning():
    message = word_cloud()
    Test_punc_removed = [char for char in message if char not in string.punctuation]
    Test_punc_removed_join = ''.join(Test_punc_removed)
    Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if word.lower() not in stopwords.words('spanish')]
    news_cleaning_final = ' '.join(Test_punc_removed_join_clean)
    plt.figure(figsize=(30,30))
    plt.imshow(WordCloud().generate(news_cleaning_final))
    plt.show()
    
    
def run():
    parse_home()
def run2():
    message_cleaning()
    

if __name__ == "__main__":
    run()
    run2()
    