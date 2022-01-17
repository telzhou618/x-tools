import click
import requests


@click.command()
@click.option("-url", "--url", help="Picture URL")
@click.option("-name", "--name", help="Picture rename")
def image(url, name=None):
    """Image download"""
    assert url is not None
    if name is None:
        name = url.split('/')[-1]
    content = requests.get(url).content
    with open("./" + name, 'wb') as file:
        file.write(content)
        click.echo(name)
