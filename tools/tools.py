import click

from .file import file
from .request import request
from .password import password


@click.group()
@click.help_option('-h', '--help', help="Show this message and exit")
def cli():
    """X-tools is a collection of tools developed in Python"""


def main():
    cli.add_command(file)
    cli.add_command(password)
    cli.add_command(request)
    cli()


if __name__ == '__main__':
    main()
