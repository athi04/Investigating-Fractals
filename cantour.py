import matplotlib.pyplot as plt

def cantor(ax, x_start, x_end, y, depth):
    if depth == 0:
        ax.plot([x_start, x_end], [y, y], linewidth=2, color='black')
        return
    
    third = (x_end - x_start) / 3
    # left segment
    cantor(ax, x_start, x_start + third, y, depth - 1)
    # right segment
    cantor(ax, x_end - third, x_end, y, depth - 1)

# Parameters
depth = 7

# Create figure
fig, ax = plt.subplots(figsize=(12, 3))

# Draw Cantor layers
for i in range(depth):
    cantor(ax, 0, 1, -i, depth=i)

# Remove axes, ticks, border
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
ax.set_ylim(-depth + 1, 1)
ax.set_frame_on(False)

# Remove padding
plt.tight_layout(pad=0)

# Save PNG
output_path = "cantor_set_black_7_iterations.png"
plt.savefig(output_path, dpi=600, transparent=True, bbox_inches='tight', pad_inches=0)
plt.close()

print("Saved to:", output_path)