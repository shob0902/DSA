class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        a=set()
        for e in emails:
            local,domain=e.split('@')
            local=local.split("+")[0]
            local=local.replace(".","")
            a.add((local,domain))
        return len(a)