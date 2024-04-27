
plt.scatter(origin[0], origin[1], color='green',
            marker='x', label='Origin (0, 0)')
plt.scatter(ellipse_points[selected_indices, 0],
            ellipse_points[selected_indices, 1], color='red', label='Selected Points')