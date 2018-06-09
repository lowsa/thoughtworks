import  unittest
import numpy as np
from logistic import *
class TestLogistic(unittest.TestCase):
    # 测试邻域有2个活细胞
    def testStateNum2(self):
        game = GameOfLife(cellsShape=(4, 4))
        game.cells = np.array([[0,0,1,1],[0,1,0,0],[0,0,1,0],[0,0,1,1]])
        game.updateState()
        self.assertEqual(1, game.cells[1, 1])

    # 测试邻域有4个活细胞
    def testStateNum4(self):
        game = GameOfLife(cellsShape=(4, 4))
        game.cells = np.array([[0,0,1,1],[0,1,0,0],[0,0,1,0],[0,0,1,1]])
        game.updateState()
        self.assertEqual(0, game.cells[1, 2])

    # 测试邻域有3个活细胞
    def testStateNum3(self):
        game = GameOfLife(cellsShape=(4, 4))
        game.cells = np.array([[0,0,1,1],[0,1,0,0],[0,0,1,0],[0,0,1,1]])
        game.updateState()
        self.assertEqual(1, game.cells[2, 1])

if __name__ =='__main__':
    unittest.main()