# Given a signed 32-bit integer x, return x with its digits reversed. If reversi
# ng x causes the value to go outside the signed 32-bit integer range [-231, 231 -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed or
#  unsigned). 
# 
#  
#  Example 1: 
#  Input: x = 123
# Output: 321
#  Example 2: 
#  Input: x = -123
# Output: -321
#  Example 3: 
#  Input: x = 120
# Output: 21
#  Example 4: 
#  Input: x = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  -231 <= x <= 231 - 1 
#  
#  Related Topics Math 
#  👍 4315 👎 6658


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        sign = ""
        if string[0:1] == "-":
            sign = '-'
            string = string[1:]
        string = string[::-1]
        if int(string) > 2147483647:
            return 0
        return int(sign + string)
        
# leetcode submit region end(Prohibit modification and deletion)
