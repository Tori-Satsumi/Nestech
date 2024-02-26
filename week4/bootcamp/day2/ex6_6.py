#!/usr/bin/env python3

import json
import urllib.request

"""
Read https://docs.python.org/3/howto/urllib2.html#urllib-howto
"""


def repositories(github_login):
    """
    Trả về list name của các repos của GitHub user github_login
    """
    with urllib.request.urlopen(
        "https://api.github.com/users/{}/repos".format(github_login)
    ) as f:
        repos = json.load(f)
        if len(repos) > 2:
            for info in repos[2:]:
                yield info["name"]
        else:
            raise ReferenceError("This user does not have any repository")



def solve(input_data):
    return repositories(input_data)


def main():
    for repo_name in solve("pallets"):
        print(repo_name)
        # print('hàm Main')


if __name__ == "__main__":
    main()