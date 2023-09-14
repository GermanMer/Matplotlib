import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Descargar recursos de NLTK si es necesario
#nltk.download('punkt')
#nltk.download('stopwords')

# Texto de ejemplo
with open(r'D:\Germán\Desktop\Python Files\Carta de Presentacion.txt', 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

# Tokenización y eliminación de palabras vacías
words = word_tokenize(texto, language='spanish')  # Cambia 'spanish' por tu idioma
stop_words = set(stopwords.words('spanish'))  # Cambia 'spanish' por tu idioma
words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

# Calcular la frecuencia de las palabras
word_freq = Counter(words)

# Configuración de la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
