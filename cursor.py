import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np

class SnaptoCursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.ly = ax.axvline(color='k', alpha=0.2)  # the vert line
        self.marker, = ax.plot([0], [0], marker="o", color="crimson", zorder=3)
        self.x = x
        self.y = y
        self.txt = ax.text(0.7, 0.9, '')

    def mouse_move(self, event):
        if not event.inaxes:
            return
        x, y = event.xdata, event.ydata
        self.ly.set_xdata(x)
        self.marker.set_data([x], [y])
        self.txt.set_text('Jour=%1.f, temperature=%1.f' % (x, y))
        self.txt.set_position((x, y))
        self.ax.figure.canvas.draw_idle()