import matplotlib.pyplot as plt
import matplotlib.patches as Polygon
import numpy as np

def sierpinski(ax, p1, p2, p3, depth):
    if depth == 0:
        triangle = Polygon.Polygon([p1, p2, p3], closed=True, edgecolor='black', facecolor='none', linewidth=2)
        ax.add_patch(triangle)
        return
    
    # midpoints
    m12 = (p1 + p2) / 2
    m23 = (p2 + p3) / 2
    m31 = (p3 + p1) / 2
    
    # recursive calls (draw the 3 corner triangles)
    sierpinski(ax, p1, m12, m31, depth - 1)
    sierpinski(ax, p2, m23, m12, depth - 1)
    sierpinski(ax, p3, m31, m23, depth - 1)

# Figure setup
fig, ax = plt.subplots(figsize=(6, 6))

# Main triangle vertices
p1 = np.array([0, 0])
p2 = np.array([1, 0])
p3 = np.array([0.5, np.sqrt(3)/2])

sierpinski(ax, p1, p2, p3, depth=7)

ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout(pad=0)
plt.savefig("sierpinski_gasket.png", dpi=600, bbox_inches='tight', pad_inches=0, transparent=True)
plt.savefig("sierpinski_gasket.svg", bbox_inches='tight', pad_inches=0, transparent=True)
plt.show()