import os


def from_picker(word):
    return {'lines': os.popen(f"leo '{word}'").read()}
