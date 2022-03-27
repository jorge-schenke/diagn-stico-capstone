import json
with open("farmers-protest-tweets-2021-03-5.json", "r") as file:
    data = file.readlines()
    print(type(json.loads(data[0])))
    print(json.loads(data[0])["url"])

def most_retweeted(url):
    top = []
    with open(url, "r", encoding='utf-8') as file:
        data = file.readlines()
        i = 3
        for line in data:
            line_json = json.loads(line)
            if len(top) < 10:
                top.append({"content": line_json["content"], "retweetCount": line_json["retweetCount"]})
            else:
                puesto = False
                for i in range(1, len(top)+1):
                    if line_json["retweetCount"] > top[-i]["retweetCount"]:
                        if not puesto:
                            index = 10 - i
                            top.pop(0)
                            top.insert(index, {"content": line_json["content"], "retweetCount": line_json["retweetCount"]})
                            puesto = True
        return(top)