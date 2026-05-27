import numpy as np
import matplotlib.pyplot as plt


def julia_set(c,
              x_min, x_max,
              y_min, y_max,
              width=1200, height=1200,
              max_iter=300, escape_radius=2.0):

    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z0 = X + 1j * Y
    z = Z0.copy()

    iter_counts = np.zeros(z.shape, dtype=int)
    active = np.ones(z.shape, dtype=bool)
    escape2 = escape_radius ** 2

    for i in range(1, max_iter + 1):
        z_active = z[active]
        z_active = z_active * z_active + c
        z[active] = z_active

        escaped_now = np.abs(z[active])**2 > escape2
        iter_counts[active] = np.where(escaped_now & (iter_counts[active] == 0),
                                       i, iter_counts[active])

        new_active = np.zeros_like(active)
        new_active[active] = ~escaped_now
        active = new_active

        if not active.any():
            break

    iter_counts[iter_counts == 0] = max_iter
    return iter_counts


# ---------------------------
# Interactive Viewer
# ---------------------------

class JuliaViewer:
    def __init__(self, c):
        self.c = c

        # Initial view
        self.x_min, self.x_max = -1.5, 1.5
        self.y_min, self.y_max = -1.5, 1.5

        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.fig.canvas.mpl_connect("scroll_event", self.on_scroll)
        self.fig.canvas.mpl_connect("button_press_event", self.on_press)
        self.fig.canvas.mpl_connect("motion_notify_event", self.on_drag)
        self.fig.canvas.mpl_connect("key_press_event", self.on_key)

        self.drag_start = None

        self.update_plot()

    def update_plot(self):
        self.ax.clear()
        data = julia_set(self.c,
                         self.x_min, self.x_max,
                         self.y_min, self.y_max)

        self.ax.imshow(
            data,
            extent=[self.x_min, self.x_max, self.y_min, self.y_max],
            origin="lower",
            cmap="inferno"
        )
        self.ax.set_title(f"Julia Set for c = {self.c}")
        self.fig.canvas.draw_idle()

    # Zoom with mouse wheel
    def on_scroll(self, event):
        # event.step is +1 for scroll up, -1 for scroll down (also on many trackpads)
        if event.xdata is None or event.ydata is None:
            return

        # Choose zoom factor based on scroll direction
        if event.step > 0:       # scroll up -> zoom in
            zoom_factor = 0.8
        else:                    # scroll down -> zoom out
            zoom_factor = 1.25

        mouse_x = event.xdata
        mouse_y = event.ydata

        self.x_min = mouse_x - (mouse_x - self.x_min) * zoom_factor
        self.x_max = mouse_x + (self.x_max - mouse_x) * zoom_factor
        self.y_min = mouse_y - (mouse_y - self.y_min) * zoom_factor
        self.y_max = mouse_y + (self.y_max - mouse_y) * zoom_factor

        self.update_plot()

    # Start dragging
    def on_press(self, event):
        if event.button == 1:  # left mouse button
            self.drag_start = (event.xdata, event.ydata)

    # Drag/pan
    def on_drag(self, event):
        if self.drag_start is None:
            return

        if event.xdata is None or event.ydata is None:
            return

        dx = self.drag_start[0] - event.xdata
        dy = self.drag_start[1] - event.ydata

        self.x_min += dx
        self.x_max += dx
        self.y_min += dy
        self.y_max += dy

        self.drag_start = (event.xdata, event.ydata)
        self.update_plot()

    # Reset with 'r'
    def on_key(self, event):
        if event.key == "r":
            self.x_min, self.x_max = -1.5, 1.5
            self.y_min, self.y_max = -1.5, 1.5
            self.update_plot()


def main():
    # Change c here or make this user input if you prefer
    c = complex(input("Enter c (example: -0.8+0.156j): "))
    JuliaViewer(c)
    plt.show()


if __name__ == "__main__":
    main()