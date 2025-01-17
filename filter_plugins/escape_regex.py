import re


def escape_regex(s):
    return re.escape(s)


class FilterModule(object):
    def filters(self):
        return {
            'escape_regex': escape_regex
        }
