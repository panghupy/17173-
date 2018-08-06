import requests
import json
import re
url = '''http://top.17173.com/api/gamerankinfo?gameCode=20011.js&_=1532680359400'''

response = requests.get(url)
print(re.findall('{.*?}',response.text)[2])
result = re.findall('{.*?}',response.text)[2]
req = json.loads(result)
print(req['rank_num'])
