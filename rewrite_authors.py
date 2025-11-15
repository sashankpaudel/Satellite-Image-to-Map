from git_filter_repo import FilterRepo

def rewrite(repo):
    for commit in repo.commits:
        if commit.author_email == b"shashikantprasad1111@gmail.com":
            commit.author_name = b"Sashank Paudel"
            commit.author_email = b"sashankpaudel07@gmail.com"
        if commit.committer_email == b"shashikantprasad1111@gmail.com":
            commit.committer_name = b"Sashank Paudel"
            commit.committer_email = b"sashankpaudel07@gmail.com"

repo = FilterRepo()
rewrite(repo)
repo.apply()