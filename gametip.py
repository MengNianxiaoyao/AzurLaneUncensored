import os
import requests

url = os.environ['URL']

def update():
    repo = requests.get(f'{url}')
    if not os.path.exists('./files/AssetBundles/sharecfgdata'):
        os.mkdir('./files/AssetBundles/sharecfgdata')
    open("./files/AssetBundles/sharecfgdata/gametip", "wb+").write(repo.content)

if __name__ == '__main__':
    update()