def main():
    print(max_average(nums = [1,12,-5,-6,50,3], k = 4))
    print(max_average(nums = [5], k = 1))
    print(max_average(nums = [-4, 0, 0], k = 1))


def max_average(nums, k):
    max = 0 
    for i in range(len(nums)):
        if i + k > len(nums):
            return max
        else: 
            calculate = nums[i: i+k]
            sum = 0
            for num in calculate:
                sum +=num
            average = sum / len(calculate)
            if average > max:
                max = average
    return max

if __name__ == "__main__":
    main()