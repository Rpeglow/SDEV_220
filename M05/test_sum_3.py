"""
Reed Peglow
SDEV 220
M05 Programming Assignment - Testing"""

#check sum of numbers, correct answer
#assert sum([1, 2, 3]) == 6, "Should be 6"
# incorrect AssertionError: Should be 6 called
#assert sum([1, 1, 1]) == 6, "Should be 6"

# test case, an assertion, and an entry point 
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")

