# cli.py

# Import the necessary classes from the other modules.
from .services import GistService
from .stores import TimestampStore
import argparse

# Define a class for parsing command-line arguments.
class ArgParser:
    """Class for parsing command-line arguments."""
    def __init__(self):
        """Create an ArgumentParser object and add arguments."""
        self.parser = argparse.ArgumentParser(description="Gists App")
        self.parser.add_argument("username", type=str, help="GitHub username")

    def parse_args(self):
        """Parse the command-line arguments and return the result."""
        return self.parser.parse_args()

def main():
    """
    The main function of the application.
    Parse the command-line arguments, get the new gists for the user, and print them.
    Also, update the last run timestamp for the user.
    """
    arg_parser = ArgParser()
    args = arg_parser.parse_args()
    username = args.username

    timestamp_store = TimestampStore()
    last_run_timestamp = timestamp_store.get_last_run_timestamp(username)

    gist_service = GistService()
    new_gists = gist_service.get_new_gists(username, last_run_timestamp)
    for gist in new_gists:
        print(gist)

    timestamp_store.set_last_run_timestamp(username)
