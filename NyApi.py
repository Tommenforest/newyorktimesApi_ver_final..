
import requests
import json




sivunumero = 1
while sivunumero <= 5:
    response = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&page={}&api-key=2L6CJGmGCgR9YuwGKt7BOAXGpF4sf2pC' .format(sivunumero) )
    print(response.json())
    file = open("tulos.json", "a")
    file.write(str(response.content))
    file.close()
    sivunumero += 1












