import requests
import json

USER = 'tde-nico'
FILENAME = 'README.md'
VERBOSE = True

COLUMNS = {
	'Languages': 'langs',
	'Frameworks and Libraries': 'frames_and_libs',
}

EXCLUDES = [
	USER,
	'custom_osu_skin',
]




def save(fname, data):
	with open(fname, 'w') as f:
		f.write(data)


def get_repos(username):
	names = []
	page_number = 1
	while page_number <= 100:
		responce = requests.get(f'https://api.github.com/users/{username}/repos?page={page_number}')
		page_repos = json.loads(responce.text)
		if not page_repos:
			break
		names += [repo['name'] for repo in page_repos]
		page_number += 1
	return names



def get_tags(username, repo):
	req = requests.get(f'https://raw.githubusercontent.com/{username}/{repo}/master/README.md')
	content = req.content.decode()
	comment = content.split('<!--', 1)[-1].split('-->', 1)[0]

	groups = []
	langs = []
	frames_and_libs = []

	lines = [line for line in comment.split('\n') if line]

	reader = None
	for line in lines:
		if line == '#groups':
			reader = 'groups'
			continue
		elif line in ('#langs', '#languages'):
			reader = 'langs'
			continue
		elif line in ('#frames_and_libs', '#frames and libs', '#libs', '#frames'):
			reader = 'frames'
			continue

		if reader == 'groups':
			line = line.replace("_", " ")
			groups.append(line)
		elif reader == 'langs':
			langs.append(line)
		elif reader == 'frames':
			frames_and_libs.append(line)

	return groups, langs, frames_and_libs



def get_repo_info(repo, data, columns):
	info = {
		'name': repo.replace('_', ' '),
		'link_name': repo,
	}

	for col in columns.values():
		content = data.get(col, None)
		if content:
			text = '<div align="left">\n'
			for con in sorted(content, key=lambda x: x.lower()):
				text += f'\t\t\t<img src="{col}/{con}.svg"/>\n'
			text += '\t\t</div>'
		else:
			text = '<br>'
		info[col] = text
	
	return info



def generate_section(username, name, repos, columns):
	text = f"<details>\n<summary>{name}</summary>\n<br>\n<table border=3 align=\"center\">\n"

	text += '<tr>'
	for col in ['Name'] + list(columns.keys()):
		text += f"""
	<td>
		{col}
	</td>"""
	text += '\n</tr>\n'

	for repo in repos:
		info = repo
		text += '<tr>'
		text += f"""
	<td>
		<a href="https://github.com/{username}/{info['link_name']}">{info['name']}</a>
	</td><td>
		{info['langs']}
	</td><td>
		{info['frames_and_libs']}
	</td>"""
		text += '\n</tr>\n'

	text += "</table>\n<br>\n</details>\n"
	return text




def main(username, fname, columns, verbose):
	if verbose:
		print(f'[+] Grabbing {username} repos')
	try:
		repos = get_repos(username)
	except Exception:
		if verbose:
			print(f'[-] Error while grabbing {username} repos')
		return

	data = {}
	for repo in repos:
		if repo in EXCLUDES:
			continue
		if verbose:
			print(f'[+] Grabbing {repo}')
		try:
			groups, langs, frames_and_libs = get_tags(username, repo)
			data[repo] = {'groups': groups, 'langs': langs, 'frames_and_libs': frames_and_libs}
		except Exception:
			if verbose:
				print(f'[-] Error while grabbing {repo}')
	
	sections = {}
	group = 0
	default_section = 'Projects'
	for repo, info in data.items():
		if verbose:
			print(f'[+] Formatting {repo} data')
		repo_info = get_repo_info(repo, info, columns)
		#print(sections)
		if info['groups']:
			sections[info['groups'][group]] = sections.get(info['groups'][group], []) + [repo_info]
		else:
			#print(sections.get(default_section, []), repo_info)
			sections[default_section] = sections.get(default_section, []) + [repo_info]

	tree = '# link_tree\n\n'
	tree += "\n<!--\n#groups\n\n#languages\nPython\n\n#frames and libs\n\n-->\n\n\n"
	for section in sorted(sections.keys()):
		if verbose:
			print(f'[+] Generating {section} section')
		tree += generate_section(username, section, sorted(sections[section], key=lambda x: x['name'].lower()), columns)
		tree += '\n\n'

	if verbose:
		print(f'[+] Saving to {fname}')
	save(fname, tree)





if __name__ == '__main__':
	main(USER, FILENAME, COLUMNS, VERBOSE)
