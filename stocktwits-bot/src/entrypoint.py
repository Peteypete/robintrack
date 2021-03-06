""" Robintrack Stocktwits Bot """

import os

from top_popularity_changes import run_top_popularity_changes

MODE_FUNCTIONS = {"top_popularity_changes": run_top_popularity_changes}


def get_mode_function() -> str:
    mode = os.environ.get("STOCKTWITS_BOT_MODE")
    if mode is None:
        print("Error: the `STOCKTWITS_BOT_MODE` env. variable must be set with a valid run mode.")
        exit(1)

    mode_function = MODE_FUNCTIONS.get(mode)

    if mode_function is None:
        print(f"Error: {mode} is not a valid mode.")
        exit(1)

    return mode_function


def main():
    mode_function = get_mode_function()
    mode_function()


if __name__ == "__main__":
    main()
