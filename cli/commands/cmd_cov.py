import subprocess
import click


@click.command()
@click.argument('path', default='snakeeyes')
def cli(path):
    cmd = f'pytest --cov-report term-missing --cov {path}'
    return subprocess.call(cmd, shell=True)
