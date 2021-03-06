from flask.cli import with_appcontext
import click

from . import utils


@click.command()
@click.option('--days-ago', type=int, default=5)
@with_appcontext
def cleanup(days_ago):
    '''Clean expired errors from the database.'''
    utils.cleanup(days_ago)


@click.command()
@with_appcontext
def fetch_errors():
    '''Fetch errors from github gist.'''
    utils.fetch_errors()


@click.command()
@with_appcontext
def send_emails():
    '''Send some pending emails.'''
    utils.send_emails()


@click.command()
@with_appcontext
def send_tweet():
    '''Send a pending tweet.'''
    utils.send_tweet()
