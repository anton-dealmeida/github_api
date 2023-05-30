# GitHub API

This is a simple Python application that fetches and displays a GitHub user's publicly available gists.

## Prerequisites

- Python 3.8 or later. You can download it from [here](https://www.python.org/downloads/).
- `requests` Python package.

## Setup

Before running the script, you need to install the necessary Python libraries. The libraries needed for this project are listed in the [`requirements.txt`](./requirements.txt) file.

You can install these using pip (using a [venv](https://docs.python.org/3/library/venv.html) is recommended):

```bash
pip install -r requirements.txt
```

## Running the Application

To run the application:

```bash
python -m github_api <username>
```

Where <username> is the GitHub username whose gists you want to fetch.

The first time you run the script for a particular user, it will display all of the user's public gists. On subsequent runs, it will display only the gists that have been published since the last run.

## Project Structure

This application follows a modular structure:

- [`cli.py`](./github_api/cli.py) contains the command-line interface for the application.
- [`services.py`](./github_api/services.py) contains the `GistService` class, which is responsible for fetching gists from the GitHub API.
- [`stores.py`](./github_api/stores.py) contains the `TimestampStore` class, which is responsible for storing the timestamp of the last run for each user.
- [`utils.py`](./github_api/utils.py) contains utility functions.
- [`__main__.py`](./github_api/__main__.py) is the entry point for the application.

## References

- [GitHub API Documentation]()
- [Python requests library](https://docs.python-requests.org/en/latest/)
- [Python argparse library](https://docs.python.org/3/library/argparse.html)
- [Python json library](https://docs.python.org/3/library/json.html)

## License

This project is licensed under the terms of the MIT license. For more information, see [LICENSE](./LICENSE).