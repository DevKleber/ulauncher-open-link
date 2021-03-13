query = "https://google.com"
# query = "google.com"
# query = query.replace('https://', '')
# query.replace('http', '')

if "http" in query: 
    print("tem")
    print(query)
else:
    print("nao tem")
    print('https://'+query)