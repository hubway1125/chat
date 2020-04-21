def read_file(filename):
	content = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			content.append(line.strip())
	return content

def convert(content):
	t_content = []	
	person = None
	for c in content:
		if c == 'Allen':
			person = c + ': '
			continue
		elif c == 'Tom':	
			person = "T o m" + ': '
			continue
		if person != None:
			t_content.append(person + c)		
	return t_content

def write_file(filename, t_content):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in t_content:
			f.write(line + '\n')

def main():
	lines = read_file('input_example.txt')
	print(lines)
	t_content = convert(lines)
	print(t_content)	
	write_file('output_example.txt', t_content)

main()
