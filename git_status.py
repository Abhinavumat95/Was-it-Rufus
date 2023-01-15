# Importing necessary packages and libraries
from git import Repo
import git
import time
from datetime import date, datetime

# Taking input from the user
r = int(input("Do you want to clone the repository in local machine press 0 for No or 1 for yes. "))
if (r == 0):
    path2 = input("Enter the path where the repository is stored in local machine: ")
    repo = Repo(path2)
elif (r == 1):
    path1 = input("Enter path for your repository: ")
    path2 = input("Enter the path for local machine where you want to clone the repository: ")
    git.Git(path2).clone(path1)
    a = path1.split("/")
    repo = Repo(path2 + "/" + a[-1].split(".")[0])
else:
    raise Exception("Sorry, please Enter either 0 or 1.")


# Getting the active branch of repository
active_branch = repo.active_branch

# Getting the info for the latest commit
commit = repo.head.commit

# Getting the date for the last commit
authored_date = commit.authored_date
d1 = time.strftime("%Y/%m/%d", time.gmtime(authored_date))

# Getting the date for the present day
t = date.today()
d2 = t.strftime("%Y/%m/%d")

# Getting the difference between present date and last commit date 
date1 = datetime.strptime(d1, "%Y/%m/%d")
date2 = datetime.strptime(d2, "%Y/%m/%d")
delta = date2 - date1


# Checking if last commit was authored in last week
if (delta.days > 7):
    recent_commit = False
else:
    recent_commit = True

# Checking if last commit was authored by Rufus
if (commit.author.name == "Rufus"):
    blame_rufus = True
else:
    blame_rufus = False


# Getting the list of all modified files
modified_files = [ item.a_path for item in repo.index.diff(None) ]

# Checking if any files were modified
if (modified_files):
    local_changes = True
else:
    local_changes = False


# Printing the results 
print("active branch: ",active_branch)
print("local changes: ",local_changes)
print("recent commit: ",recent_commit)
print("blame Rufus: ",blame_rufus)