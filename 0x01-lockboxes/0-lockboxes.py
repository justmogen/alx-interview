def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (list): List of lists of integers representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False
    if len(boxes) == 1:
        return True

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False