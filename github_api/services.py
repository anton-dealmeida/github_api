import requests
from .utils import extract_gists_after_timestamp

class GistService:
    """Class for interacting with the GitHub Gists API."""
    def __init__(self):
        """Initialize the base URL for the API."""
        self.base_url = "https://api.github.com"

    def get_new_gists(self, username, last_run_timestamp=None):
        """
        Fetch the new gists of a given GitHub user.

        This method fetches all gists of the user and then filters out the ones that were created before the last run timestamp.

        Parameters
        ----------
        username : str
            The GitHub username of the user.
        last_run_timestamp : int, optional
            The Unix timestamp of the last run. If it's None, all gists of the user will be returned.

        Returns
        -------
        list
            A list of new gists. Each gist is represented as a dictionary.
        """
        response = requests.get(f"{self.base_url}/users/{username}/gists")
        response.raise_for_status()
        gists = response.json()
        if last_run_timestamp is not None:
            gists = extract_gists_after_timestamp(gists, last_run_timestamp)
        return gists
