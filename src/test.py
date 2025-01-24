import random
import matplotlib.pyplot as plt


def estimate_pi(num_points):
    inside_circle = 0

    # Randomly generate points and count the number inside the circle
    for _ in range(num_points):
        x = random.uniform(-1, 1)  # Randomly generate x coordinate
        y = random.uniform(-1, 1)  # Randomly generate y coordinate

        # Check if the point is inside the circle
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1

    # Estimate Pi
    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate


# Set the number of points for the simulation
num_points = 50000
estimated_pi = estimate_pi(num_points)
print(f"Estimated Pi: {estimated_pi}")

# Visualization
x_inside = []
y_inside = []
x_outside = []
y_outside = []

for _ in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Plot the circle and points
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the circle boundary
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2)
ax.add_artist(circle)

# Plot points inside the circle
ax.scatter(x_inside, y_inside, color='green', s=1, alpha=0.5, label="Inside Circle")

# Plot points outside the circle
ax.scatter(x_outside, y_outside, color='red', s=1, alpha=0.5, label="Outside Circle")

# Set equal aspect ratio
ax.set_aspect('equal', adjustable='box')

# Set axis limits
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

# Add title and labels
plt.title(f"Monte Carlo Simulation for Pi Estimation\nEstimated Pi: {estimated_pi:.4f}\nSamples: {num_points}", fontsize=14)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add legend
plt.legend()

# Display grid
plt.grid(True)

# Display sampling count
ax.text(1.05, 1, f"Samples: {num_points}", fontsize=12, ha='left', va='bottom', color='black')

# Show plot
plt.show()