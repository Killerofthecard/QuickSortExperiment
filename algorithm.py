import random
import numpy as np
from pyarrow import array
from scipy.special import expit

def median_of_three(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return b

def normal_distribution(seed, miu, sigma) -> int:
    np.random.seed(seed)
    return expit([np.random.normal(miu, sigma)])[0]

def vanilla_quick_sort(array:list,
                       compare_nums:list=None,
                       order:str="ascend") -> list:
    if len(array) <= 1:
        return array
    else:
        # pivot = median_of_three(array[0], array[int(len(array)/2)], array[-1])
        pivot = array[0]
        if compare_nums is not None:
            compare_nums[0] += 1
        if order == "ascend":
            return (vanilla_quick_sort([x for x in array[1:] if x <= pivot], compare_nums, order)
                + [pivot]
                + vanilla_quick_sort([x for x in array[1:] if x > pivot], compare_nums, order))
        else:
            return (vanilla_quick_sort([x for x in array[1:] if x > pivot], compare_nums, order)
                    + [pivot]
                    + vanilla_quick_sort([x for x in array[1:] if x <= pivot], compare_nums, order))

def randomized_quick_sort(array:list,
                          compare_nums:list=None,
                          order:str="ascend") -> list:
    if len(array) <= 1:
        return array
    else:
        # pivot = random.choice(array)
        n = normal_distribution(seed=42, miu=0, sigma=1)
        pivot = array[round(len(array) * n)]
        if compare_nums is not None:
            compare_nums[0] += 1
        if order == "ascend":
            return (randomized_quick_sort([x for x in array[0:] if x <= pivot], compare_nums, order)
                + [pivot]
                + randomized_quick_sort([x for x in array[0:] if x > pivot], compare_nums, order))
        else:
            return (randomized_quick_sort([x for x in array[0:] if x > pivot], compare_nums, order)
                    + [pivot]
                    + randomized_quick_sort([x for x in array[0:] if x <= pivot], compare_nums, order))

def generate_array(size:int,
                   lower_bound:int,
                   upper_bound:int,
                   seed:int,
                   exp_type:str
                   ) -> list:
    assert lower_bound < upper_bound
    if seed is not None:
        random.seed(seed)
    if exp_type == "random" or exp_type == "random_gaussian":
        res = [random.randint(lower_bound, upper_bound) for _ in range(size)]
        return res
    elif exp_type == "ascend":
        res = [x for x in range(size)]
        return res
    elif exp_type == "descend":
        res = [size-x for x in range(size)]
        return res
    else:
        raise NotImplementedError