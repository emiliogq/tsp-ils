from solution import Solution

def test_comparison():

    s1 = Solution()
    s2 = Solution()
    
    assert s1 >= s2

    s1.cost = 1.0

    assert s1 >= s2
    assert s1 > s2
    assert s2 < s1

    
