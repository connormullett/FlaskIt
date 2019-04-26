
import os
import click


@click.group()
def main():
    pass

@main.command()
def start():

    project_name = click.prompt('Enter project name')

    if click.confirm('User Authentication?'):
        pass

