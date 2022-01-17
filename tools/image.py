import click
import requests


@click.command()
@click.option("-url", "--url", help="Picture url", required=True)
@click.option("-name", "--name", help="Picture rename")
def image(url: str, name=None):
    """Image download"""

    if name is None:
        if '?' in url:
            name = url.split('?')[0].split('/')[-1]
        else:
            name = url.split('/')[-1]
    content = requests.get(url).content
    with open("./" + name, 'wb') as file:
        file.write(content)
        click.echo(name)
