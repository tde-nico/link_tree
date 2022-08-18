import json

def dump(fname, data):
	with open(fname, 'w') as f:
		json.dump(data, f, indent=4)

def load(fname):
	with open(fname, 'r') as f:
		data = json.load(f)
	return data

def save(fname, data):
	with open(fname, 'w') as f:
		f.write(data)




USER = 'tde-nico'
FILENAME = 'README.md'

COLUMNS = {
	'Languages': 'langs',
	'Frameworks and Libraries': 'frames_and_libs',
}


REPOS = load('repos.json')
SECTIONS = load('sections.json')




def low(text):
	return text.lower()


def get_repo_info(repo):
	data = REPOS.get(repo, {})
	info = {
		'name': repo.replace('_', ' '),
	}

	for col in COLUMNS:
		name = COLUMNS[col]
		content = data.get(name, None)
		if content:
			text = '<div align="left">\n'
			for con in sorted(content, key=low):
				text += f'\t\t\t<img src="{name}/{con}.svg"/>\n'
			text += '\t\t</div>'
		else:
			text = '<br>'
		info[name] = text
	
	return info



def generate_section(name, repos):
	text = f"<details>\n<summary>{name}</summary>\n<br>\n<table border=3 align=\"center\">\n"

	text += '<tr>'
	for col in ['Name'] + list(COLUMNS.keys()):
		text += f"""
	<td>
		{col}
	</td>"""
	text += '\n</tr>\n'

	for repo in repos:
		info = get_repo_info(repo)
		text += '<tr>'
		text += f"""
	<td>
		<a href="https://github.com/{USER}/{repo}">{info['name']}</a>
	</td><td>
		{info['langs']}
	</td><td>
		{info['frames_and_libs']}
	</td>"""
		text += '\n</tr>\n'

	text += "</table>\n<br>\n</details>\n"
	return text


def main():
	tree = '# link_tree\n\n'

	for section in sorted(SECTIONS):
		tree += generate_section(section, sorted(SECTIONS[section], key=low))
		tree += '\n\n'

	save(FILENAME, tree)



if __name__ == '__main__':
	main()


