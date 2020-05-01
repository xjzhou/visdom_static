# coding=utf-8
import time
from visdom import Visdom
import requests
import os
import numpy as np

viz = Visdom(server='localhost', port=8097)
assert viz.check_connection()

# 图片
# 单张图片
viz.image(
    np.random.rand(3, 512, 256),
    opts={
        'title': 'Random',
        'showlegend': True
    }
)
# 多张图片
viz.images(
    np.random.rand(20, 3, 64, 64),
    opts={
        'title': 'multi-images',
    }
)

# 散点图
Y = np.random.rand(100)
Y = (Y[Y > 0] + 1.5).astype(int),  # 100个标签1和2

old_scatter = viz.scatter(
    X=np.random.rand(100, 2) * 100,
    Y=Y,
    opts={
        'title': 'Scatter',
        'legend': ['A', 'B'],
        'xtickmin': 0,
        'xtickmax': 100,
        'xtickstep': 10,
        'ytickmin': 0,
        'ytickmax': 100,
        'ytickstep': 10,
        'markersymbol': 'cross-thin-open',
        'width': 800,
        'height': 600
    },
)
# time.sleep(5)
# 更新样式
viz.update_window_opts(
    win=old_scatter,
    opts={
        'title': 'New Scatter',
        'legend': ['Apple', 'Banana'],
        'markersymbol': 'dot'
    }
)
# 3D散点图
viz.scatter(
    X=np.random.rand(100, 3),
    Y=Y,
    opts={
        'title': '3D Scatter',
        'legend': ['Men', 'Women'],
        'markersize': 5
    }
)

# 柱状图
viz.bar(X=np.random.rand(20))
viz.bar(
    X=np.abs(np.random.rand(5, 3)),  # 5个列，每列有3部分组成
    opts={
        'stacked': True,
        'legend': ['A', 'B', 'C'],
        'rownames': ['2012', '2013', '2014', '2015', '2016']
    }
)

viz.bar(
    X=np.random.rand(20, 3),
    opts={
        'stacked': False,
        'legend': ['America', 'Britsh', 'China']
    }
)
