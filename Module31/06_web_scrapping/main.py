import re
import requests


my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')

result = re.findall(r'<h3.+>(.+)\b</h3>', my_req.text)
print(result)
