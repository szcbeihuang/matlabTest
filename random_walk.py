from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    # def fill_walk(self):
    #
    #     while len(self.x_values) < self.num_points:
    #
    #         x_direction = choice([-1, 1])
    #         x_direction = choice([0, 1, 2, 3, 4])
    #         x_step = x_direction * x_direction
    #
    #         y_direction = choice([-1, 1])
    #         y_direction = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    #         y_step = y_direction * y_direction
    #
    #         if x_step == 0 and y_step == 0:
    #             continue
    #
    #         x = self.x_values[-1] + x_step
    #         y = self.y_values[-1] + y_step
    #         self.x_values.append(x)
    #         self.y_values.append(y)
    def fill_walk(self):
        """ 计算随机漫步所包含的所有点 """
        direction = [-1, 1]
        distance = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice(direction)
            x_distance = choice(distance)
            x_step = x_direction * x_distance

            y_direction = choice(direction)
            y_distance = choice(distance)
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
