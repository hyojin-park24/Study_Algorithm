class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
            
        return left

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows + 1)]

        for r in range(2, len(res)):
            for c in range(1, len(res[r]) - 1):
                res[r][c] = res[r - 1][c - 1] + res[r - 1][c]
                
        return res



class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
            
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
            
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True

# 1121 알고리즘 스터디 1.11 빠진 숫자 찾기

#Solution 1 Sotring (정렬)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        nums.sort()     #목록을 제자리에서 정렬
        
        for i, num in enumerate(nums):      #정렬된 목록을 반복해주는데 열거함수는 목록의 항목과 함께 
                                            # 0 부터 시작하는 카운터i를 추가해준다 --> 간결해짐 
            if num != i:                    # index 현재 숫자와 각 항목 비교 시작  
                return i                    # 같지 않을 때 i 리턴
            
        return n;                           # 반복이 끝난 후 누락된 숫자 N 리턴

#Solutio 2 Math (가우스 공식)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
       
        expected_sum = n * (n+1) // 2   #가우스 공식
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum

        # 예상합계 - 주어진 목록의 합계 = 누락된 숫자가 나온다 
        # 0~N --> 합계 ? ==> 가우스 공식 
        # [a,b,c] => [a+b+c] -  [b + c ] = 'a' 
        # n(n+1)//2


# 1128 알고리즘 스터디 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None     #node = 노드, prev = 이전노드  
        
        while node:                 #node가 있을 때 까지  
            next, node.next = node.next, prev # 다음 노드를 next 변수에 담고
            prev, node = node, next # 현재 next에는 이전 값을 담기 
            
        return prev                 # 반복문 종료시 이전노드 리턴


# 1205 알고리즘 스터디 (순환검출)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast =head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast : return True
        return False

# 0116 알고리즘 스터디 (유효한 괄호 검증)

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'}':'{',')':'(',']':'['}
        for bracket in s:
            if bracket in brackets.values(): #Opening bracket 
                stack.append(bracket)
            else:# Closing bracket
                if stack and brackets[bracket]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack:
            return False
        return True

# 0116 알고리즘 스터디 (재귀함수 01.계단오르기)
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1   
        for i in range(n-1):
            temp = one 
            one = one + two
            two = temp 
        return one
        
# 0123 알고리즘 스터디 (재귀함수 02.문자열 치환)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(sub_list: List, remain_list: List):
            
            if len(nums) == len(sub_list):
                result.append(sub_list)
                return
            for i , value in enumerate(remain_list):
                dfs(sub_list+[value], remain_list[:i]+remain_list[i+1:])
                #enumerate내장함수로 리스트 원소에 각 인덱스 부여
                #remain_list[:i] = "i까지 리스트 복사";
                # sub_list에는 숫자가 채워지고
                # remain_list에는 줄어듦 
                
        result = []
        dfs([], nums)        
        return result