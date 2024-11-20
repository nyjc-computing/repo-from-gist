# repo-from-gist
Template for creating a repository from a (public) gist

# Instructions

1. From the GitHub link (https://github.com/nyjc-computing/repo-from-gist), click **Use this template > Create a new repository**. Name this repository according to what the gist will contain.
2. Open the repository in a codespace.
3. Follow the instructions below.

# Usage

```sh
$ python import-gist.py
```

or click **Run** in Codespaces.

When prompted, paste the URL of the gist.

Upon successful execution, this script will remove its contents, leaving the contents of the gist only.

# Example

```
$ python import_gist.py
Enter gist url: https://gist.github.com/nycomp/3a52fb7f85492ad4fc1787501538c6bd
Cloning https://gist.github.com/nycomp/3a52fb7f85492ad4fc1787501538c6bd ...
Cloning into 'repo'...
remote: Enumerating objects: 8, done.
remote: Total 8 (delta 0), reused 0 (delta 0), pack-reused 8 (from 1)
Receiving objects: 100% (8/8), 5.87 KiB | 5.87 MiB/s, done.
Resolving deltas: 100% (1/1), done.
https://gist.github.com/nycomp/3a52fb7f85492ad4fc1787501538c6bd successfully cloned. The contents of this repository will be removed.
Press any key to continue ...
```
