import json

def most_used_hashtags(url):
    with open(url, "r", encoding='utf-8') as file:
        data = file.readlines()
        hashtags = {}
        for line in data:
            line_json = json.loads(line)
            content = line_json['content']
            hashtag = ""
            reading = False
            terminado = False
            for letra in content:
                if letra == "#":
                    terminado = False
                    reading = True
                if reading:
                    if letra != (" " or "\\"):
                        hashtag += letra
                    else:
                        terminado = True
                        if reading and terminado:
                            hasht = hashtag.encode('utf-8')
                            # print(hasht)
                            if hasht not in hashtags.keys():
                                hashtags[hasht] = 1
                                # print("Puse")
                            else:
                                hashtags[hasht] += 1
                                # print("No puse, sume")
                        reading = False
                        terminado = False
                        hashtag = ""
        sortedhash = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
        return(sortedhash[0:10])