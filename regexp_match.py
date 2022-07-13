import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern=re.compile(p)
        matches=pattern.findall(s)
        if s in matches:
            return True
        return False