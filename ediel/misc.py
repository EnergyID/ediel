class open_filename(object):
    """
    Context manager that opens a filename and closes it on exit, but does
    nothing for file-like objects.
    """
    def __init__(self, filename, *args, **kwargs):
        self.closing = kwargs.pop('closing', False)
        if isinstance(filename, str):
            self.fh = open(filename, *args, **kwargs)
            self.closing = True
        else:
            self.fh = filename

    def __enter__(self):
        self.fh.seek(0)
        return self.fh

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.closing:
            self.fh.close()
        else:
            self.fh.seek(0)

        return False

def sort_mixed_list(iterable):
    """
    Sort a list of strings and other objects:
    put the strings first and the others last

    Parameters
    ----------
    iterable : list

    Returns
    -------
    list
    """
    strings = []
    others = []
    for elem in iterable:
        if isinstance(elem, str):
            strings.append(elem)
        else:
            others.append(elem)
    res = strings + others
    return res