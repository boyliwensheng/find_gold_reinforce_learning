### 简介
这是一个基于强化学习的机器人寻找金币的小游戏，游戏网格里有三个元素：红色圆圈代表机器人、黄色圆圈代表机器人想要寻找的金币，黑色方块代表陷阱。只需要运行程序，点击“开始学习”按钮，这是一个程序自己玩的游戏，程序会自动开始探索环境，找到金币或者掉入陷阱则重新从入口开始探索。在开始运行程序的时候，机器人会像无头苍蝇一样在网格里乱走，经过一段时间的探索（大约5分钟），机器人可以很快地绕过陷阱，直达金币所在地。
程序刚开始机器人的运动轨迹：
![image](https://github.com/boyliwensheng/find_gold_reinforce_learning/blob/master/before.gif)

一段时间后机器人的运动轨迹：
![image](https://github.com/boyliwensheng/find_gold_reinforce_learning/blob/master/after.gif)

主要有两个程序




