import os

dotfilesDir = os.path.dirname(os.path.realpath(__file__))
homeDir = os.path.expanduser('~')

symlinks = [
    (f'{dotfilesDir}/.zshrc', f'{homeDir}/.zshrc'),
    (f'{dotfilesDir}/.gitconfig', f'{homeDir}/.gitconfig'),
]

for symlink in symlinks:
    if os.path.exists(symlink[0]) and not os.path.exists(symlink[1]):
        os.symlink(symlink[0], symlink[1])
