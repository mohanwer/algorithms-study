# https://leetcode.com/explore/interview/card/bloomberg/68/array-and-strings/402/
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        char=chars[0]
        i=1
        count=1
        while i<len(chars):
            if chars[i]==char:
                count+=1
                chars.pop(i)
            elif count==1:
                char=chars[i]
                i+=1
            else:
                c=str(count)
                for digit in c:
                    chars.insert(i,digit)
                    i+=1
                count=1
        if i==len(chars) and count!=1:
            c=str(count)
            for digit in c:
                chars.append(digit)