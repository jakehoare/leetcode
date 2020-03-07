from collections import deque


# Examples:
# print(CountdownSolver().countdownBFS([6, 3, 100, 75, 50, 25], 955))
# print(CountdownSolver().countdownBFS([2, 5, 7, 8, 9, 75], 569))

class CountdownSolver:
    def countdownBFS(self, input_nums, target):
        best, best_ops = 0, []      # closest to target, the list of operations to make best

        for num in input_nums:      # update best for each input num
            if num == target:
                return target, []
            if abs(target - num) < abs(target - best):
                best = num

        frontier = deque([[input_nums, []]])
        while frontier:
            nums, ops = frontier.popleft()

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    small, large = sorted([nums[i], nums[j]])               # nums used in this operation
                    unchanged = nums[:i] + nums[i + 1:j] + nums[j + 1:]     # nums noy used
                    for op in ("+", "-", "*", "//"):
                        if op == "-" and small == large:
                            continue
                        if op == "//" and large % small != 0:
                            continue
                        new_num = eval("large" + op + "small")
                        new_ops = ops + [str(large) + op + str(small) + "=" + str(new_num)]
                        if new_num == target:
                            return target, new_ops
                        if abs(target - new_num) < abs(target - best):
                            best = new_num
                            best_ops = new_ops
                        frontier.append([unchanged + [new_num], new_ops])

        return best, best_ops

    def countdownDFS(self, input_nums, target):
        self.best = 0
        self.best_ops = []

        def helper(nums, ops):      # return bool if target is found
            if any(num == target for num in nums):
                self.best = target
                self.best_ops = ops
                return True
            if len(nums) == 1:
                if abs(nums[0] - target) < abs(self.best - target):
                    self.best = nums[0]
                    self.best_ops = ops
                return False

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    small, large = sorted([nums[i], nums[j]])
                    unchanged = nums[:i] + nums[i + 1:j] + nums[j + 1:]
                    for op in ("+", "-", "*", "//"):
                        if op == "-" and small == large:
                            continue
                        if op == "//" and large % small != 0:
                            continue
                        new_num = eval("large" + op + "small")
                        if helper(unchanged + [new_num], ops + [str(large) + op + str(small) + "=" + str(new_num)]):
                            return True
            return False

        helper(input_nums, [])
        return self.best, self.best_ops
