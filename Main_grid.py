import sys
import time
from PyQt5.QtWidgets import QWidget, QApplication,QRadioButton,QPushButton,QGraphicsScene
from PyQt5.QtGui import QPainter, QColor, QPen,QFont,QMouseEvent,QIcon
from PyQt5.QtCore import Qt,QTimer
import numpy as np
from RL_brain import QLearningTable

pixe = 50   # pixels
column = 5  # 列数
raw = 5  # 行数

class Maze(QWidget):
    def __init__(self):
        super().__init__()
        self.action_space = ['u', 'd', 'l', 'r']#动作空间
        self.n_actions = len(self.action_space)
        # self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self.origin = np.array([25, 25])  ##生成一个（20，20）的矩阵
        self.people = np.array([25, 25])
        self.gold_center = self.origin + pixe * 2
        self.hell1_center = self.origin + np.array([pixe * 2, pixe])
        self.hell2_center = self.origin + np.array([pixe, pixe * 2])
        self.episode = 0
        self.acho = 10
        self.RL = QLearningTable(actions=list(range(self.n_actions)))
        self.done = True
        self.hell_num = 0

        # self.button1 = QRadioButton('设置陷阱', self)
        # self.button1.move(280, 150)
        # self.button1.resize(100, 60)
        self.button_start = QPushButton('开始学习', self)
        self.button_start.move(280, 10)
        self.button_start.resize(85, 45)
        self.button_start.setIcon(QIcon("start.png"))
        self.button_stop = QPushButton('停止学习', self)
        self.button_stop.move(280, 70)
        self.button_stop.resize(85, 45)
        self.button_stop.setIcon(QIcon("stop.png"))

        self.button_start.clicked.connect(self.startgame)
        self.button_stop.clicked.connect(self.stopgame)
        self.initUI()



    def startgame(self):
        self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_image)
        self.timer.timeout.connect(self.learning)
        self.timer.start(50)  # 其实感觉這个定时器时长作用不大，只是保证了程序能一直执行
    def stopgame(self):
        self.timer.stop()
        self.people = np.array([25, 25])#把小人初始化到入口
        self.update()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('机器人找金币')
        self.update()
        self.show()
        # self.learning()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(qp)
        qp.end()
    # def drawHell(self,qp,zuobiao):#todo:有机会添加手动布置陷阱功能
    #     pen = QPen(Qt.white, 2, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.setBrush(QColor(800, 0, 0))
    #     self.hell_center = self.origin + zuobiao*pixe
    #     qp.drawRect(self.hell_center[0] - 20, self.hell_center[1] - 20, 40, 40)  ##(起点坐标，终点坐标，长，宽)



    def drawGrid(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)

        # 创建网格
        for c in range(0, column * (pixe+1), pixe):  # 创建列
            x0, y0, x1, y1 = c, 0, c, column * pixe
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)
        for r in range(0, raw * (pixe+1), pixe):  # 创建行
            x0, y0, x1, y1 = 0, r, raw * pixe, r
            qp.setPen(pen)
            qp.drawLine(x0, y0, x1, y1)

        #绘制文字
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont("Decorative", 10))
        qp.drawText(0,0,30,30, Qt.AlignCenter, '入口')


        pen = QPen(Qt.white, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(800, 0, 0))

        # 陷阱1
        self.hell1_center = self.origin + np.array([pixe * 2, pixe])
        qp.drawRect(self.hell1_center[0] - 20, self.hell1_center[1] - 20,40,40)##(起点坐标，终点坐标，长，宽)

        #陷阱2
        self.hell2_center = self.origin + np.array([pixe, pixe * 2])
        qp.drawRect(self.hell2_center[0] - 20, self.hell2_center[1] - 20, 40, 40)  ##(起点坐标，终点坐标，长，宽)

        self.hell3_center = self.origin + np.array([pixe*3, pixe * 2])
        qp.drawRect(self.hell3_center[0] - 20, self.hell3_center[1] - 20, 40, 40)  ##(起点坐标，终点坐标，长，宽)



        # 金币
        pen = QPen(Qt.yellow, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(255, 215, 0))
        # self.gold_center = self.origin + UNIT * 2
        # qp.drawRoundedRect(self.gold_center[0] - 20, self.gold_center[1] - 20, 40, 40,30,15)  #后边两个参数是圆角的半径
        qp.drawEllipse(self.gold_center[0] - 20, self.gold_center[1] - 20,40,40)
        #机器人
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(self.people[0] - 15, self.people[1] - 20, 30, 40)
        # qp.drawRoundedRect(self.people[0] - 20, self.people[1] - 20,40, 40, 30, 15)  # 后边两个参数是圆角的半径

    # def mouseDoubleClickEvent(self, event):
    #     print('heaiwbdnasd')



####基础框架已经搭建好了，只要调用self.update即可更新。
#初始化
    def reset(self):
        time.sleep(0.5)
        self.people = np.array([25, 25])
        self.update()
        return self.people   ##可能缺一个长和宽

    def step(self, action):#机器人动作，其中，防止机器人走出范围
        s = self.people
        base_action = np.array([0, 0])
        if action == 0:  # up
            if s[1] > pixe:
                base_action[1] -= pixe
        elif action == 1:  # down
            if s[1] < (raw - 1) * pixe:
                base_action[1] += pixe
        elif action == 2:  # right
            if s[0] < (column - 1) * pixe:
                base_action[0] += pixe
        elif action == 3:  # left
            if s[0] > pixe:
                base_action[0] -= pixe

        self.people = s + base_action  # move agent
        # self.update()##todo:是否需要更新

        s_ = self.people

        # 回报函数
        if np.all(s_ == self.gold_center):
            reward = 1
            done = True
            s_ = 'terminal'
        elif np.all(s_ == self.hell1_center) or np.all(s_ == self.hell2_center) or np.all(s_ == self.hell3_center):#在這个列表的数字里
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done

    #更新画面
    def _render(self):
        time.sleep(0.5)
        self.update()

    def learning(self):##todo:放在循环里更新函数就失效了？？？？？？
        if self.done == True:
            self.observation = self.reset()
            self.done = False
        else:
            action = self.RL.choose_action(str(self.observation))


            observation_, reward, self.done = self.step(action) #新的观察值，回报值，是否完成
            # print('done:',self.people)
            print('done:', self.done)

            self.RL.learn(str(self.observation), action, reward, str(observation_))

            # swap observation
            self.observation = observation_
            # self.gengxin()
            self._render()

##测试环境是否可用。
    def update_image(self):
        # self.step(1)

        # for t in range(10):
        s = self.reset()
        print(s)
        # while True:
        # self._render()
        a = 1
        s, r, done = self.step(a)
        print(s)
        print(r)
        print(done)

        if done:
                self.timer.stop()
                print('stop')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Maze()
    # update_image()
    sys.exit(app.exec_())