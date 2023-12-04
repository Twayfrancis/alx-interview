#!/usr/bin/python3
"""method that determines if all boxex can be opened"""


def canUnlockAll(boxes):
    """
    function determines if all boxes can be unlocked
    Returns:
            bool: True if all boxes can be opened else false
    """
    # number of boxes
    num_boxes = len(boxes)
    # initialize all boxes as locked
    unlocked = [False] * num_boxes
    unlocked[0] = True
    # list keys, starting with keys in first box
    keys = [key for key in boxes[0]]

    while keys:
        # get a key
        key = keys.pop()
        if key < num_boxes and not unlocked[key]:
            unlocked[key] = True
            keys += boxes[key]

    return all(unlocked)
