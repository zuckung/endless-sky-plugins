import requests
import os


def get_version():
	request = requests.get('https://github.com/endless-sky/endless-sky/raw/refs/heads/master/changelog')
	with open('changelog.txt', 'wb') as changelog:
		changelog.write(request.content) # downloading the changelog
	with open('changelog.txt', 'r') as sourcefile:
		onlineversion = 'v' + sourcefile.readline().replace('Version ', '').replace('\n', '') # result example: v0.10.10
	releasev = 'EndlessSky-win64-' + onlineversion + '.zip '
	env_file = os.getenv('GITHUB_ENV')
	with open(env_file, "a") as envfile:
		envfile.write("ES_VERSION=" + onlineversion + '\n')
		envfile.write("RELEASE=" + releasev + '\n')


def run():
	get_version()


if __name__ == "__main__":
	run()
