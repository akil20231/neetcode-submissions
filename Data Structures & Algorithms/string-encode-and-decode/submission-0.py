class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            for c in s:
                res += chr(ord(c) + 3)
            res += " "
        
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        output = []
        curr_str = ""
        for c in s:
            if c == " ":
                output.append(curr_str)
                curr_str = ""
            else:
                curr_str += chr(ord(c) - 3)
        return output


