class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        '''
        for i in nums1 :
            if i in nums2:
                res.append(i)
        s = set(res)
        return list(s)'''

        n1 ={}
        n2 = {}
        
        for i in nums1:
            if i in n1:
                continue
            else:
                n1[i] = 1
        for i in nums2:
            if i in n2:
                continue
            else:
                n2[i] = 1
        for key in n1:
            if key in n2:
                res.append(key)
        return res