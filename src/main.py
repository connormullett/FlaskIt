
import os
import click


TEMPLATE_URL = 'https://github.com/connormullett/FlaskBoilerPlate.git'


@click.group()
def main():
    pass

@main.command()
def start():

    project_name = click.prompt('Enter project name')

    if click.confirm('User Authentication?'):
        path = os.getcwd()
        os.system('git clone %s %s/%s' % (TEMPLATE_URL, path, project_name))

    else:
        pass

