### 简介
这是一个基于强化学习的机器人寻找金币的小游戏，游戏网格里有三个元素：红色圆圈代表机器人、黄色圆圈代表机器人想要寻找的金币，黑色方块代表陷阱。这是一个程序自己玩的游戏，只需要运行程序，点击“开始学习”按钮，程序会自动开始探索环境，找到金币或者掉入陷阱则重新从入口开始探索。在开始运行程序的时候，机器人会像无头苍蝇一样在网格里乱走，经过一段时间的探索（大约5分钟），机器人可以很快地绕过陷阱，直达金币所在地。

程序刚开始机器人的运动轨迹：

![image](https://github.com/boyliwensheng/find_gold_reinforce_learning/blob/master/before.gif)

一段时间后机器人的运动轨迹：

![image](https://github.com/boyliwensheng/find_gold_reinforce_learning/blob/master/after.gif)

### 模块

这个程序非常简单，主要有两个模块。

- Main_grid.py：利用PyQt5前端构建网格以及场景里边的元素。
- RL_brain.py：构建一个强化学习模型，所用到的思想是基本的Q-learning算法。这是一种无模型的强化学习算法，主要利用了贝尔曼方程迭代地优化策略。

### 以后有时间的改进

自定义设置“陷阱”，增加使用者的参与性。






