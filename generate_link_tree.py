import json
import requests

USER = 'tde-nico'
NAME = 'test.md'

COLUMNS = [
	'Name',
	'Language',
	'Frameworks and Libraries',
]


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



REPOS = load('test.json')
SECTIONS = load('sections.json')



def get_repo_info(repo):
	data = REPOS.get(repo, {})

	langs_data = data.get('langs', None)
	if langs_data:
		langs = '<div align="left">\n'
		for lang in langs_data:
			langs += f'\t\t\t<img src="languages/{lang}.svg"/>\n'
		langs += '\t\t</div>'
	else:
		langs = '<br>'

	frames_and_libs_data = data.get('frames_and_libs', None)
	if frames_and_libs_data:
		frames_and_libs = '<div align="left">\n'
		for frame_or_lib in frames_and_libs_data:
			frames_and_libs += f'\t\t\t<img src="frameworks_and_libraries/{frame_or_lib}.svg"/>\n'
		frames_and_libs += '\t\t</div>'
	else:
		frames_and_libs = '<br>'

	info = {
		'name': repo.replace('_', ' '),
		'langs': langs,
		'frames_and_libs': frames_and_libs,
	}
	return info



def generate_section(name, repos):
	text = f"<details>\n<summary>{name}</summary>\n<br>\n<table border=3 align=\"center\">\n"

	text += '<tr>'
	for col in COLUMNS:
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
		tree += generate_section(section, sorted(SECTIONS[section]))
		tree += '\n\n'

	save(NAME, tree)



if __name__ == '__main__':
	main()




'''
import os
import requests
import json
import git


USERNAME = 'tde-nico'
FOLDER = '.' # '.' -> local folder


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


def maintain(username, name):
	if os.path.exists(name):
		print(f'[+] pulling {name}')
		repo = git.cmd.Git(name)
		repo.pull()
	else:
		print(f'[+] cloning {name}')
		git.Repo.clone_from(f'https://github.com/{username}/{name}', name)


def main():
	if not os.path.exists(FOLDER):
		os.mkdir(FOLDER)
	os.chdir(FOLDER)
	names = get_repos(USERNAME)
	for name in names:
		maintain(USERNAME, name)


if __name__ == '__main__':
	main()
'''