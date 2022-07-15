import json

data  = '{"name":"ashwini", "age":17}'

use = json.loads(data)

print(use['age'])


