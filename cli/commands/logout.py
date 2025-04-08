<<<<<<< HEAD
import click
import os

SESSION_TOKEN_FILE = os.path.expanduser("~/.session_token")

@click.command("logout")
def logout_user():
    """Log out of the NOTECLI app."""
    if os.path.exists(SESSION_TOKEN_FILE):
        os.remove(SESSION_TOKEN_FILE)
        click.echo("✅ Successfully logged out.")
    else:
        click.echo("❌ No user currently logged in.")
=======
import click
import os

SESSION_TOKEN_FILE = os.path.expanduser("~/.session_token")

@click.command("logout")
def logout_user():
    """Log out of the NOTECLI app."""
    if os.path.exists(SESSION_TOKEN_FILE):
        os.remove(SESSION_TOKEN_FILE)
        click.echo("✅ Successfully logged out.")
    else:
        click.echo("❌ No user currently logged in.")
>>>>>>> 41573d58ff3ea5a5986c5c51461a829b2031a4f3
