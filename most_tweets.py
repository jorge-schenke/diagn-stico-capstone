import json

def most_retweeted(url):
    top = []
    with open(url, "r", encoding='utf-8') as file:
        data = file.readlines()
        i = 3
        for line in data:
            line_json = json.loads(line)
            if len(top) < 10:
                top.append({"user": line_json["user"]["username"].encode("utf-8"), "statusesCount": line_json["user"]["statusesCount"]})
            else:
                puesto = False
                for i in range(1, len(top)+1):
                    if line_json["user"]["statusesCount"] > top[-i]["statusesCount"]:
                        if not puesto:
                            index = 10 - i
                            top.pop(0)
                            top.insert(index, {"user": line_json["user"]["username"].encode("utf-8"), "statusesCount": line_json["user"]["statusesCount"]})
                            puesto = True
        return(top)