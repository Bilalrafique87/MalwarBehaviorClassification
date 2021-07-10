import json
import pandas as pd
def parser(filename):
    Features = ['ID', 'Name', 'SHA1', 'SHA256', 'SHA512', 'MD5', 'Duration',
                'Severity Score', 'Category', 'Package', 'Size', 'Label', 'Label 2', 'category',
                'Time', 'Tid', 'Api_1']

    Dataset = pd.DataFrame(columns=Features)
    allfiles = filename
    i = 0
    for f in allfiles:
     try:
        with open(f) as datafile:
            data = json.load(datafile)

        Dataset.loc[i] = [data["info"]["id"], data["target"]["file"]["name"], len(data["target"]["file"]["sha1"]),
                          len(data["target"]["file"]["sha256"]), len(data["target"]["file"]["sha512"]),
                          len(data["target"]["file"]["md5"]),
                          data["info"]["duration"],
                          data["info"]["score"],data["info"]["category"],data["info"]["package"],
                          data["target"]["file"]["size"],
                          "Malware",
                          "1",
                          data['behavior']['processes'][1]['calls'][0]['category'],
                          data['behavior']['processes'][1]['calls'][0]['time'],
                          data['behavior']['processes'][1]['calls'][0]['tid'],
                          data['behavior']['processes'][1]['calls'][0]['api']+""+data['behavior']['processes'][1]['calls'][1]['api']
                          ]

        Dataset.to_csv('C:\\Users\\MudassirRiaz\\PycharmProjects\\Malware Behavior Classification\\Json_Reports\\malware_dataset_1.csv')
        i = i + 1

        print(data["info"]["id"])  # ID
        print(data["target"]["file"]["name"])  # Name
        print(data["target"]["file"]["sha1"]) # SHA1
        print(data["target"]["file"]["sha256"])  # SHA256
        print(data["target"]["file"]["sha512"]) # SHA512
        print(data["target"]["file"]["md5"]) # MD5
        print(data["info"]["duration"]) # Duration of Execution
        print(data["info"]["score"])  # Severity Score
        print(data["info"]["category"])  # Category
        print(data["info"]["package"])  # Package i.e. exe
        print(data["target"]["file"]["size"])  # Size Bytes
        print(data['behavior']['processes'][1]['calls'][0]['category'])
        print(data['behavior']['processes'][1]['calls'][0]['api'])
        print(data['behavior']['processes'][1]['calls'][0]['time'])
        print(data['behavior']['processes'][1]['calls'][0]['tid'])
        print(data['behavior']['processes'][1]['calls'][0]['tid'])
        print(data['behavior']['processes'][1]['calls'][1]['api']+""+data['behavior']['processes'][1]['calls'][1]['api'])

     except KeyError:
         continue

     except IndexError:
         continue