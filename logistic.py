import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(object):
    def __init__(self, cellsShape):
        """
        Parameters
        ----------
        cells_shape : 一个元组，表示画布的大小。
        Examples
        --------
        建立一个高20，宽30的画布
        game = GameOfLife((20, 30))
        """

        # 矩阵的四周不参与运算
        self.cells = np.zeros(cellsShape)

        realWidth = cellsShape[0] - 2
        realHeight = cellsShape[1] - 2
        self.cells[50:70, 40:45] = np.random.randint(2, size=(20, 5))
        self.cells[1:5, 1:5] = np.random.randint(2, size=(4, 4))
        #self.cells[1:-1, 1:-1] = np.random.randint(2, size=(realWidth, realHeight))
        self.timer = 0
        self.mask = np.ones(9)
        self.mask[4] = 0

    def updateState(self):
        """更新一次状态"""
        buf = np.zeros(self.cells.shape)
        cells = self.cells
        for i in range(1, cells.shape[0] - 1):
            for j in range(1, cells.shape[0] - 1):
                # 计算该细胞周围的存活细胞数
                neighbor = cells[i - 1:i + 2, j - 1:j + 2].reshape((-1,))
                neighborNum = np.convolve(self.mask, neighbor, 'valid')[0]

                if neighborNum == 3:
                    buf[i, j] = 1
                elif neighborNum == 2:
                    buf[i, j] = cells[i, j]
                else:
                    buf[i, j] = 0
        self.cells = buf
        self.timer += 1

    def plot_state(self):
        """画出当前的状态"""
        plt.title('Iter :{}'.format(self.timer))
        plt.imshow(self.cells)
        plt.show()

    def updateAndPlot(self, n_iter):
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
    game = GameOfLife(cellsShape=(200, 200))
    game.updateAndPlot(200)