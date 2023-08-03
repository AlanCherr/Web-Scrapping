with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Ejemplo: Encontrar todos los títulos <h2> en el archivo HTML
sections = soup.find_all('section')
with open('datos.txt', 'w', encoding='utf-8') as txt_file:
    for section in sections:
        pregunta_div = section.find('div', {'id': 'Pregunta'})
        respuesta_div = section.find('div', {'id': 'Respuesta'})

        if pregunta_div and respuesta_div:
            pregunta = pregunta_div.get_text()
            respuesta = respuesta_div.get_text()

            print("Pregunta:", pregunta)
            print("Respuesta:", respuesta)
            print("-" * 40)
            # Escribe la pregunta y la respuesta en el archivo de texto
            txt_file.write("Pregunta: {}\n".format(pregunta))
            txt_file.write("Respuesta: {}\n".format(respuesta))
            txt_file.write("-" * 40 + "\n")