def commit_callback(commit):
    if commit.author_email == b"shashikantprasad1111@gmail.com":
        commit.author_name = b"Sashank Paudel"
        commit.author_email = b"sashankpaudel07@gmail.com"
    if commit.committer_email == b"shashikantprasad1111@gmail.com":
        commit.committer_name = b"Sashank Paudel"
        commit.committer_email = b"sashankpaudel07@gmail.com"

from git_filter_repo import FilterRepo
repo = FilterRepo()
repo.add_commit_callback(commit_callback)
repo.run()