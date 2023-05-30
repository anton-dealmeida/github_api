import json
import os
import time

class TimestampStore:
    """
    Class for managing the last run timestamps of users.

    The timestamps are stored in a JSON file. Each user has an associated Unix timestamp
    which represents the time of the last run for the user.
    """
    def __init__(self, filename='timestamps.json'):
        """Initialize the filename where the timestamps are stored."""
        self.filename = filename

    def get_last_run_timestamp(self, username):
        """
        Get the last run timestamp of a user.

        Parameters
        ----------
        username : str
            The GitHub username of the user.

        Returns
        -------
        int
            The Unix timestamp of the last run for the user. If the user does not have a last run timestamp, return None.
        """
        try:
            with open(self.filename, 'r') as f:
                timestamps = json.load(f)
            return timestamps.get(username)
        except FileNotFoundError:
            return None

    def set_last_run_timestamp(self, username):
        """
        Set the last run timestamp of a user to the current time.

        Parameters
        ----------
        username : str
            The GitHub username of the user.
        """
        try:
            with open(self.filename, 'r') as f:
                timestamps = json.load(f)
        except FileNotFoundError:
            timestamps = {}
        timestamps[username] = int(time.time())
        with open(self.filename, 'w') as f:
            json.dump(timestamps, f)
