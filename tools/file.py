import click
from tqdm import tqdm
import requests


@click.command()
@click.option("-url", "--url", help="file url", required=True)
@click.option("-name", "--name", help="Picture rename")
def file(url, name):
    """File download"""
    _download(url, name)


def _download(url, name):
    if not name:
        name = get_file_name(url)
    resp = requests.get(url, stream=True)

    # 获取文件大小
    file_size = int(resp.headers['content-length'])

    with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, ascii=True, desc=name) as bar:
        with requests.get(url, stream=True) as r:
            with open(name, 'wb') as fp:
                for chunk in r.iter_content(chunk_size=512):
                    if chunk:
                        fp.write(chunk)
                        bar.update(len(chunk))


def get_file_name(url):
    if '?' in url:
        return url.split('?')[0].split('/')[-1]
    else:
        return url.split('/')[-1]
