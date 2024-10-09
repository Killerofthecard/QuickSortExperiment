import os
import re
import argparse
from matplotlib import pyplot as plt

def is_dim_equal(x, y) -> bool:
    return len(x) == len(y)

def padding(short_array:list,
            long_array:list) -> None:
    x_len = len(short_array)
    y_len = len(long_array)
    for _ in range(y_len - x_len):
        short_array.append(None)

def plot_line_chart(x, y1, y2, img_type, exp_type):
    if not is_dim_equal(x, y1):
        padding(y1,x)
    if not is_dim_equal(x, y2):
        padding(y2, x)
    plt.figure(figsize=(10, 5))  # 设置图形的大小
    plt.plot(x, y1, marker='o', linestyle='-', color='r', label="Vanilla QS")
    if y2 is not None:
        plt.plot(x, y2, marker='x', linestyle='--', color='g', label="Randomized QS")
    if img_type == "time":
        plt.title(f'Algorithm Runtime vs Size({exp_type})')
        plt.ylabel('Runtime (ms)')
    elif img_type == "compare":
        plt.title(f'Algorithm compare nums vs Size({exp_type})')
        plt.ylabel('Compare nums')

    plt.xlabel('Size')

    plt.grid(False)  # 显示网格
    plt.xscale('log')  # 如果size的尺度很大，可以使用对数尺度
    # 显示图例
    plt.legend()

    # 显示图形
    # plt.show()

    # 保存图片
    save_path = f"{img_type}_{exp_type}.png"
    plt.savefig(fname=save_path, format="png")

def extract_data(path):
    data = []
    with open(path,"r") as file:
        for line in file:
            data_dict = {}
            parts = line.split(" ")
            for part in parts:
                if "\n" in part:
                    part = part.rstrip("\n")
                part = part.split("=")
                key, value = part[0], part[1]
                if key == "size" or key == "seed":
                    value = int(value)
                elif key == "time":
                    value = float(value)
                elif key == "cmp_nums":
                    value = int(value)
                else:
                    matches = re.findall(r'\[(.*?)\]', value)
                    if matches:
                        value = [int(num.strip()) for num in matches[0].split(',')]
                data_dict[key] = value
            data.append(data_dict)
    return data

def parse_args():
    parser = argparse.ArgumentParser("", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-exp_type",
                        "--exp_type",
                        type=str,
                        required=True,
                        help="type of experiment")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    exp_type = args.exp_type
    path = os.path.dirname(__file__)
    vanilla_file_name = f"\Deterministic_qs_data_{exp_type}.txt"
    randomized_file_name = f"\Randomized_qs_data_{exp_type}.txt"
    vanilla_path = path + vanilla_file_name
    randomized_path = path + randomized_file_name

    vanilla_data = extract_data(vanilla_path)
    randomized_data = extract_data(randomized_path)
    x_size = [value for item in vanilla_data for key,value in item.items() if key == "size"]

    y_time_vanilla = [value for item in vanilla_data for key, value in item.items() if key == "time"]
    y_time_randomized = [value for item in randomized_data for key, value in item.items() if key == "time"]
    y_cmp_num_vanilla = [value for item in vanilla_data for key, value in item.items() if key == "cmp_nums"]
    y_cmp_num_randomized = [value for item in randomized_data for key, value in item.items() if key == "cmp_nums"]

    plot_line_chart(x_size, y_time_vanilla, y_time_randomized,"time", exp_type) # time chart
    plot_line_chart(x_size, y_cmp_num_vanilla, y_cmp_num_randomized,"compare", exp_type) # compare nums chart

