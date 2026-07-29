class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_v = set()
        for x in emails:
            x_spl =  x.split('@')[0].split('+')[0].split('.')
            res=''.join(x_spl)+'@'+x.split('@')[1]
            set_v.add(res)
        return len(set_v)
