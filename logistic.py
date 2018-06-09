import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(object):
    def __init__(self, cells_shape):
        """
        cellsShape : 一个元组，表示画布的大小
        """

        # 矩阵的四周不参与运算
        self.cells = np.zeros(cells_shape)

        self.cells[50:70, 40:45] = np.random.randint(2, size=(20, 5))
        self.cells[1:5, 1:5] = np.random.randint(2, size=(4, 4))

        self.timer = 0
        self.mask = np.ones(9)
        self.mask[4] = 0



    def is_alive(self,i,j):
        neighbor = self.cells[i - 1:i + 2, j - 1:j + 2].reshape((-1,))
        neighbor_num = np.convolve(self.mask, neighbor, 'valid')[0]

        if neighbor_num == 3:
            return 1
        elif neighbor_num == 2:
            return self.cells[i, j]
        else:
            return 0


    def updateState(self):
        """更新一次状态"""

        cells = self.cells
        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[0] - 1):
                # 计算该细胞周围的存活细胞数
                self.cells[i][j] = self.is_alive(i,j)
        self.timer += 1

    def plot_state(self):
        """画出当前的状态"""
        plt.title('Iter :{}'.format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def update_and_plot(self, n_iter):
        """更新状态并画图
        Parameters
        ----------
        n_iter : 更新的轮数
        """
        plt.ion()
        while True:
            plt.title('conveys game')
            plt.axis('off')
            plt.imshow(self.cells,cmap=plt.cm.gray)
            self.updateState()
            plt.pause(0.2)
        plt.ioff()


if __name__ == '__main__':
    game = GameOfLife(cells_shape=(200, 200))
    game.update_and_plot(200)