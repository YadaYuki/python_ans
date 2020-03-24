"""
このファイルに解答コードを書いてください
"""
def sort_num_dict(num_dict):
    sorted_num_dict = {}
    sorted_key = sorted(num_dict)
    for key in sorted_key:
        sorted_num_dict[key] = num_dict[key]
    return sorted_num_dict

def get_num_dict_and_m(filename):
    with open(filename) as f:
        # read line of file as list
        num_dict_list = [s.strip() for s in f.readlines()]

    # define m
    m = int(num_dict_list[-1])

    # generate num_dict
    num_dict = {}
    for i in range(len(num_dict_list)-1):
        # split num string by ":"
        num,name = num_dict_list[i].split(":")
        num_dict[int(num)] = name

    # sort dict
    num_dict = sort_num_dict(num_dict)
    return num_dict,m

def print_name(num_dict,m):
    i = 0 # number of divisors
    for num,name in num_dict.items():
        if m % num == 0:
            print(name,end="")
            i += 1 # count the number of divisors
    if i == 0:
        print(m)
        

if __name__ == "__main__":
    num_dict,m = get_num_dict_and_m("input.txt")
    print_name(num_dict,m)
    