import json

def most_retweeted(url):
    top = []
    with open(url, "r", encoding='utf-8') as file:
        data = file.readlines()
        i = 3
        for line in data:
            line_json = json.loads(line)
            if len(top) < 10:
                top.append({"content": line_json["content"].encode("utf-8"), "retweetCount": line_json["retweetCount"]})
            else:
                puesto = False
                for i in range(1, len(top)+1):
                    if line_json["retweetCount"] > top[-i]["retweetCount"]:
                        if not puesto:
                            index = 10 - i
                            top.pop(0)
                            top.insert(index, {"content": line_json["content"].encode("utf-8"), "retweetCount": line_json["retweetCount"]})
                            puesto = True
        return(top)