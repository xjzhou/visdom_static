import visdom
import numpy as np

viz = visdom.Visdom(env='fromLocal', server='http://47.96.23.181', port=9801)

viz.text('Hello, world!')

x, y = 0, 0
for i in range(50):
    x = i
    y = i*i
    viz.line(
        X = np.array([x]),
        Y = np.array([y]),
        win = 'window',
        update = 'append')
