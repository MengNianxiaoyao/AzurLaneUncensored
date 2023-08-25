import os
import requests, requests_cache
import shutil

url = os.environ['URL']

def update():
    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    res = []
    name = []
    session = requests_cache.CachedSession(cache_control=True, backend='memory')
    data = session.get('https://api.github.com/repos/taofan233/azurlane_uncensored/releases').json()
    for item in data:
        if item['author']['login'] == 'taofan233':
            res.append(item['tag_name'])
            name.append(item['assets'][0]['name'])
    res = res[0]
    name = name[0]
    if name == f'uncensored.plus.{res}.zip':
        assets =  requests.get(f'https://github.com/taofan233/azurlane_uncensored/releases/download/{res}/uncensored.plus.{res}.zip')
        open(f"./tmp/uncensored.plus.{res}.zip", "wb+").write(assets.content)
        if os.path.exists(f'./tmp/uncensored.plus.{res}.zip'):
            import zipfile
            with zipfile.ZipFile(f'./tmp/uncensored.plus.{res}.zip', 'r') as zf:
                zf.extractall('./tmp/')
    elif name == f'uncensored.plus.{res}.rar':
        return 1
        # assets =  requests.get(f'https://github.com/taofan233/azurlane_uncensored/releases/download/{res}/uncensored.plus.{res}.rar')
        # open(f"./tmp/uncensored.plus.{res}.rar", "wb+").write(assets.content)
        # if os.path.exists(f'./tmp/uncensored.plus.{res}.rar'):
        #     import rarfile
        #     with rarfile.RarFile(f'./tmp/uncensored.plus.{res}.rar', 'r') as zf:
        #         zf.extractall('./tmp/')
    if os.path.exists('./tmp/files') and os.path.exists('./files'):
        shutil.rmtree('./files')
        shutil.copytree('./tmp/files', './files')
        shutil.copytree('./loadingbg', './files/AssetBundles/loadingbg')
    if os.path.exists('./files/AssetBundles/char'):
        shutil.rmtree('./files/AssetBundles/char')

    repo = requests.get(f'{url}')
    if not os.path.exists('./files/AssetBundles/sharecfgdata'):
        os.mkdir('./files/AssetBundles/sharecfgdata')
    open("./files/AssetBundles/sharecfgdata/gametip", "wb+").write(repo.content)

    shutil.rmtree('./tmp')

if __name__ == '__main__':
    update()