import requests
from git import Repo

URL = 'https://www.alberta.ca/data/stats/covid-19-alberta-statistics-map-data.csv'
FILE = 'covid-19-alberta-statistics-map-data.csv'

def download_file():
    file_data = requests.get(URL).content
    with open(FILE, 'wb') as out_file:
        out_file.write(file_data)

PATH_OF_GIT_REPO = r'C:\Users\niels\Desktop\covid-app\calgary-covid-map\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'updating covid-19-alberta-statistics-map-data.csv'

def git_push():
    try:
        download_file()
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(['covid-19-alberta-statistics-map-data.csv'])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occurred while pushing the code')    

git_push()
