class Solution(object):
    def countSeniors(self, details):
        count = 0
        for k in details:
            if int(k[11:13]) > 60:
                count += 1
        return count