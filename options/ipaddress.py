from base.matchedoption import MatchedOption
import re

class IPAddress(MatchedOption):
    pattern = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}' +
                         r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')