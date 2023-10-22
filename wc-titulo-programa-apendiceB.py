import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

#TITULO PROGRAMA

df = pd.read_csv("../../Documents/data-csv/titulo-programa.csv",
                 names=["id", "keywords", "searches"])

stopwords = set(STOPWORDS)
stopwords.update(['DA', 'DE', 'DO', 'DAS', 'DOS', 'E', 'EM', 'LTDA', 'PARA', 'O'])

print(df['keywords'])

wc = WordCloud(stopwords=stopwords,
                      background_color="white",
                      width=1600, height=800)
wc.generate(df['keywords'].to_string())
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()