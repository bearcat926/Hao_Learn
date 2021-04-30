# Written by *** for COMP9021

# Prompts the user for 4 positive integers, the last three of which
# represent a number of points (nothing will need to be done if it is 0),
# an integer max_coordinate such that all coordinates to be generated
# will be between -max_coordinate and max_coordinate included, and a
# square window size (width and height).
#
# Generates a list of x coordinates and a list of y coordinates of common
# length the number of points requested. Shows these lists, possibly truncated.
#
# x-coordinates increase from left to right,
# y-coordinates increase from bottom to top.
#
# 1. Displays the points, without duplicates, from highest to lowest,
#    and from left to right for a given height.
#
# 2. Displays the size of the smallest rectangle, as well as its top left
#    and bottom right corners, in which all points fit.
#
# 3. Displays the maximum number of points that can fit in a square window
#    with the provided size. The window has to be fully included in the
#    enclosing rectangle. In case such a window exists, then displays the
#    top left and bottom right corners of the leftmost, topmost such window.

from random import seed, randrange
import sys

try:
    for_seed, nb_of_points, max_coordinate, window_size = \
        (int(e) for e in input('Enter four positive integers: ').split())
    if for_seed < 0 or nb_of_points < 0 or max_coordinate < 0 \
            or window_size < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
if not nb_of_points:
    print('No point to play with, see you later!')
    sys.exit()
seed(for_seed)
x_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                 for _ in range(nb_of_points)
                 ]
y_coordinates = [randrange(-max_coordinate, max_coordinate + 1)
                 for _ in range(nb_of_points)
                 ]
field_width = max(max(len(str(e)) for e in x_coordinates),
                  max(len(str(e)) for e in y_coordinates)
                  )
print('Here is how the x-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in x_coordinates)
[: 80 // (field_width + 1) * (field_width + 1)]
      )
print('Here is how the y-coordinates of your points start:')
print('  ', ' '.join(f'{e:{field_width}}' for e in y_coordinates)
[: 80 // (field_width + 1) * (field_width + 1)]
      )

# INSERT CODE HERE
c_y = sorted(y_coordinates)
c_x = sorted(x_coordinates)
c_y.reverse()

# 生成坐标
print('\n' + "Here are the points, without duplicates, from highest to lowest,")
print(" and from left to right for a given height:")
generate_set = set((c_x[x], c_y[y]) for x in range(0, len(c_x))
                   for y in range(0, len(c_y)))
generate_list = list(generate_set)


# 排序
def point_sort(generate_list):
    emp_L = []
    for i in range(len(generate_list)):
        j = i
        for j in range(len(generate_list)):
            if (generate_list[i][0] < generate_list[j][0]):
                generate_list[i], generate_list[j] = generate_list[j], generate_list[i]
            if (generate_list[i][1] > generate_list[j][1]):
                generate_list[i], generate_list[j] = generate_list[j], generate_list[i]

    for kk in range(len(generate_list)):
        emp_L.append(generate_list[kk])
    return emp_L


new_list = point_sort(generate_list)

for i in range(len(new_list)):
    print(' ', new_list[i])
    i += 1

# 构建rectangle
# if window_size == 0:      #如果windowsize为0或者连个坐标同X或者同Y，size均为0
# import math
# print(c_y[0],c_y[len(c_y)-1])
# print(c_x[0],c_x[len(c_x)-1])
if window_size == 0 or c_x[0] == c_x[len(c_x) - 1] or c_y[0] == c_y[len(c_y) - 1]:
    s_size = 0
elif (c_y[0] * c_y[len(c_y) - 1] > 0) and (c_x[0] * c_x[len(c_x) - 1] < 0):
    s_size = (abs(c_x[0]) + abs(c_x[len(c_x) - 1])) * abs((abs(c_y[0]) - abs(c_y[len(c_y) - 1])))
elif (c_y[0] * c_y[len(c_y) - 1] < 0) and (c_x[0] * c_x[len(c_x) - 1] > 0):
    s_size = abs((abs(c_x[0]) - abs(c_x[len(c_x) - 1]))) * (abs(c_y[0]) + abs(c_y[len(c_y) - 1]))
else:
    s_size = (abs(c_x[0]) + abs(c_x[len(c_x) - 1])) * (abs(c_y[0]) + abs(c_y[len(c_y) - 1]))
# point1 = f'({c_x[0]},{c_y[0]})'
# point2 = f'({c_x[len(c_x)-1]},{c_y[len(c_y)-1]})'
print('\n' + f"All points fit in a rectangle of size {s_size},")
print(f" with ({c_x[0]}, {c_y[0]}) as top left corner, and")
print(f" with ({c_x[len(c_x) - 1]}, {c_y[len(c_y) - 1]}) as bottom right corner.")

# 窗口比较
print('\n' + f"The maximum number of points that fit in a square window of size {window_size}")
x_t = c_x[0]  # min(x) a
y_t = c_y[0]  # max(y) b
l_1 = []  # n
l_1_1 = []  # nlx
contain = []
x_max = []  # nl
biggest = []
if s_size >= window_size:
    while y_t - window_size >= c_y[len(c_y) - 1]:
        while x_t + window_size <= c_x[len(c_x) - 1]:
            for (x, y) in new_list:
                if x_t <= x <= x_t + window_size and y_t - window_size <= y <= y_t:
                    l_1.append((x, y))
            l_1_1.append((len(l_1), x_t))
            # l_1 = []
            x_t = x_t + 1
        x_t = c_x[0]
        # l_1_1 = sorted(l_1_1, key=lambda x: (-x[0]))
        # print(l_1_1)
        l_1_1 = sorted(l_1_1, key=lambda x: (x[0]))
        x_max.append((l_1_1[0], y_t))
        y_t = y_t - 1
    biggest = list(max(x_max))
    count_rec = biggest[0][0]
    x_1 = biggest[0][1]
    y_1 = biggest[1]
    x_2 = biggest[0][1] + window_size
    y_2 = biggest[1] + window_size
    st_point = (x_1, y_1)
    if x_1 * x_2 >= 0 and (x_1 > 0 and x_2 > 0):
        x_3 = biggest[0][1] - window_size
    else:
        x_3 = x_2
    if y_1 * y_2 >= 0 and (y_1 > 0 and y_2 > 0):
        y_3 = biggest[1] - window_size
    else:
        y_3 = y_2
    end_point = (x_3, y_3)
    print(f' enclosed within the rectangle is {count_rec}.')
    print(f'The leftmost, topmost such window has {st_point} as top left corner,')
    print(f' and {end_point} as bottom right corner.')

    print(' enclosed within the rectangle is 0.')
