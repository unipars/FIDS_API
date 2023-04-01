import requests
import json
requests.packages.urllib3.disable_warnings()

#assining dates
START_DATE = 1
END_DATE = 5
for day in range(START_DATE,END_DATE+1):
    date = f'1402-01-0{day}'
    airline = 'irb'
    url = 'https://www.airport.ir/NetForm/Service/fids?'
    result = url+'date={}&airline={}&AUTH_TOKEN=9890071'.format(date,airline)
    print(result)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    response = requests.get(result,headers=headers,verify = False)
    data = json.loads(response.text)
    # making the json file for each day
    with open(f'output_02010{day}.json', 'w') as f:
        json.dump(data, f)
# making integrated data list
combined_data = []
for day in range(START_DATE,END_DATE+1):
    with open(f'output_02010{day}.json') as f:
        file_data = json.load(f)
        combined_data.append(file_data)
# making integrated json file
with open("integrated_data.json", "w") as f:
    json.dump(combined_data, f)

