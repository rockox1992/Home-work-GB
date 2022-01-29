import os


def status(struct):
    gb_list = []
    for root, dirs, files in os.walk(struct):
        for file in files:
            total_size = os.stat(os.path.join(root, file)).st_size
            gb_list.append(total_size)
    gb_dict = {i: gb_list.count(i) for i in gb_list}
    return gb_dict


if __name__ == "__main__":
    root_dir = "C:/Users/rocko/PycharmProjects/GB"
    print(status(root_dir))
