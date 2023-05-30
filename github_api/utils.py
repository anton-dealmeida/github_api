import datetime

def extract_gists_after_timestamp(gists, timestamp):
    """
    Filter a list of gists and return the ones that were created after a given timestamp.

    Parameters
    ----------
    gists : list
        A list of gists. Each gist is represented as a dictionary and has a "created_at" field which represents its creation time.
    timestamp : int
        A Unix timestamp.

    Returns
    -------
    list
        A list of gists that were created after the timestamp.
    """
    threshold_date = datetime.datetime.fromtimestamp(timestamp)
    return [gist for gist in gists if datetime.datetime.strptime(gist["created_at"], "%Y-%m-%dT%H:%M:%SZ") > threshold_date]
