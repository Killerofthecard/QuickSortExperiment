import argparse
import os

from algorithm import generate_array, vanilla_quick_sort, randomized_quick_sort
import time


def save_log(path, exp_type, alg_type, info:dict):
    cost_time = info["time"]
    seed = info["seed"]
    scope = info["scope"]
    array_size = info["size"]
    cmp_nums = info["cmp_num"]
    format = ".txt"
    file_name = f"\\{alg_type}" + "_qs_" + "data_" + exp_type + format
    save_path = path + file_name
    data_line = f"size={array_size} seed={seed} scope=[{scope[0]},{scope[1]}] time={cost_time:.2f} cmp_nums={cmp_nums}\n"
    with open(save_path, "a") as file:
        file.write(data_line)
    print(f"当前算法运行时间已保存至{save_path}")



def parse_args():
    parser = argparse.ArgumentParser("", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-size",
                        "--size",
                        type=int,
                        required=True,
                        help="size of the array")
    parser.add_argument("-low",
                        "--low",
                        type=int,
                        required=True,
                        help="lower bound of the array")
    parser.add_argument("-up",
                        "--up",
                        type=int,
                        required=True,
                        help="upper bound of the array")
    parser.add_argument("-seed",
                        "--seed",
                        type=int,
                        required=False,
                        help="random seed")
    parser.add_argument("-alg_type",
                        "--alg_type",
                        type=str,
                        required=True,
                        help="the type of algorithm")

    parser.add_argument("-exp_type",
                        "--exp_type",
                        type=str,
                        required=True,
                        help="the type of experiment, user can choose the type in"
                             "[random, ascend, descend]")
    return parser.parse_args()


if __name__ == "__main__":

    import sys

    sys.setrecursionlimit(1000000)
    # 参数初始化
    forTest = False
    if not forTest:
        args = parse_args()
        size = args.size
        low = args.low
        up = args.up
        seed = args.seed
        alg_type = args.alg_type
        exp_type = args.exp_type
    else:
        size = 200
        low = 1
        up = 1000
        seed = 42
        alg_type = "Randomized"
        exp_type = "random"
    array = generate_array(size, low, up, seed, exp_type)
    compare_nums = [0]

    # --------- 执行快排 -------------- #
    start_time = time.time()
    if alg_type == "Deterministic":
        if exp_type == "random":
            sorted_array = vanilla_quick_sort(array, compare_nums)
        elif exp_type == "ascend":
            sorted_array = vanilla_quick_sort(array, compare_nums,"descend")
        elif exp_type == "descend":
            sorted_array = vanilla_quick_sort(array, compare_nums,"ascend")
        else:
            raise "请确定一种实验类型"
    else:
        if exp_type == "random":
            sorted_array = randomized_quick_sort(array, compare_nums)
        elif exp_type == "ascend":
            sorted_array = randomized_quick_sort(array, compare_nums, "descend")
        elif exp_type == "descend":
            sorted_array = randomized_quick_sort(array, compare_nums, "ascend")
        # elif exp_type == "random_gaussian":
        #     sorted_array = randomized_quick_sort(array, compare_nums, "ascend")
        else:
            raise "请确定一种实验类型"
    end_time = time.time()
    cost_time = (end_time - start_time) * 1000
    print(f"确定性快排执行用时:{cost_time:.2f} ms")
    # 保存到txt
    current_file_path = os.path.dirname(__file__)
    info = {"seed":seed,
            "time":cost_time,
            "scope":[low, up],
            "size":size,
            "cmp_num": compare_nums[0]
            }

    save_log(path=current_file_path, exp_type=exp_type, alg_type=alg_type, info=info)


