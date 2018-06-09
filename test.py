import  unittest

from logistic import *
class TestLogistic(unittest.TestCase):
    def testUpdateState(self):
        game = GameOfLife(cellsShape=(4, 4))
        game.cells = np.array([[0,0,1,1],[0,1,0,0],[0,0,1,0],[0,0,1,1]])
        game.updateState()
        # 测试邻域有2个活细胞
        self.assertEqual(1, game.cells[1, 1])
        # 测试邻域有4个活细胞
        self.assertEqual(0, game.cells[1, 2])
        # 测试邻域有3个活细胞
        self.assertEqual(1, game.cells[2, 1])
        # 测试邻域有3个活细胞
        self.assertEqual(1, game.cells[2, 2])


if __name__ =='__main__':
    unittest.main()