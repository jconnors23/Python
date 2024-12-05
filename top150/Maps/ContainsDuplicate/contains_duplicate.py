def main():
    print(containsDuplicate(nums = [1,2,3,1], k = 3))
    print(containsDuplicate(nums = [1,2,3,1,2,3], k = 2))

def containsDuplicate(nums, k):
    map_nums = nums_map(nums)
    return absolute_indices(map_nums, k); 

def nums_map(nums):
    map = {}
    for index, value in enumerate(nums):
        if value in map:
            map[value].append(index)
        else:
            map[value] = [index]
    return map 

def absolute_indices(map, target):
    for key in map:
        for i in range(len(map[key])):
            for j in range(len(map[key])):
                if map[key][i] == map[key][j]:
                    continue
                if abs(map[key][i] - map[key][j]) <= target:
                    return True 
    return False 

if __name__ == "__main__":
    main()

