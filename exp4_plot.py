from matplotlib import pyplot as plt

def plot_line_chart_v2(x, y1, y2, y3):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y1, marker='o', linestyle='-', color='r', label="Random QS(0,1)")
    plt.plot(x, y2, marker='x', linestyle='-', color='g', label="Random QS(0,2)")
    plt.plot(x, y3, marker='*', linestyle='-', color='b', label="Random QS(random)")

    plt.title(f'Algorithm Compare nums vs Size')
    plt.ylabel('Compare nums')
    plt.xlabel('Size')
    plt.grid(False)
    plt.xscale('log')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    x = [10,100,1000,10000,100000,1000000,10000000]
    y1_time = [0.0, 0.0, 15.79, 53.96, 577.59, 6545.74, 74073.75]
    y2_time = [0.0,0.0,0.0,62.53,531.51,5861.03,68490.35]
    y3_time = [0.0, 0.0, 0.0, 13.50, 204.52, 2705.89, 54957.48 ]

    y1_cmp = [5,65,645,6457,64471,645513,6494997]
    y2_cmp = [7,72,714,7156,71719,718242,7210173]
    y3_cmp = [6,62,641,6385,64172,640799,6439650]

    plot_line_chart_v2(x, y1_time, y2_time, y3_time)
    plot_line_chart_v2(x, y1_cmp, y2_cmp, y3_cmp)