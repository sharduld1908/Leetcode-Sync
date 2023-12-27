import os
from git import Repo

def scrape_git_commits():
    leetcode_commits = dict()

    for commit in Repo(os.getcwd()).iter_commits():
        c_message = commit.message
        if commit.message not in leetcode_commits or c_message.startswith("Leetcode"):
            leetcode_commits[commit.message] = commit.hexsha

    return leetcode_commits

if __name__ == "__main__":
    scrape_git_commits()