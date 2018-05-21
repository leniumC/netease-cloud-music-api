from apis import *

s = input('\n\nEnter artist name: ')
n = input('\n\nEnter name of file to save to: ')

print('\n\nSearching for %s...\n\n' % s)

result = get_search_songs(s)

if result['code'] == 200:
	print('SUCCESS\n\n')
else:
	print('FAILED\n\n')
	exit()

with open(n, 'w') as f:
    f.write(json.dumps(result, indent=4))
    print('Saved to %s\n\n' % n)
