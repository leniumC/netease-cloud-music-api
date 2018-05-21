from apis import *

result = get_records(98166919, True)

with open('data.json', 'w') as f:
	f.write(json.dumps(result, indent=4))
