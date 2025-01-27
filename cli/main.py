import click
from cli.commands import create, read, login, logout, whoami

@click.group()
def notecli():
    """NOTECLI: A CLI-based notes app for managing personal notes."""
    click.echo("Welcome to NOTECLI - Your personal CLI-based Notes Manager!")

# Adding commands
notecli.add_command(create.create_note)
notecli.add_command(read.read_note)
notecli.add_command(login.login_user)
notecli.add_command(logout.logout_user)
notecli.add_command(whoami.whoami_user)

if __name__ == "__main__":
    notecli()
