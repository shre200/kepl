import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to calculate position in an inertial frame
def inertial_frame(t):
    x = np.cos(t)
    y = np.sin(t)
    return x, y

# Function to calculate position in a non-inertial (rotating) frame
def rotating_frame(t, omega):
    x = np.cos(t) * np.cos(omega * t)
    y = np.sin(t) * np.cos(omega * t)
    return x, y

# Animation update function
def update(frame, line_inertial, line_rotating):
    t = frame / 10.0

    # Update inertial frame
    inertial_x, inertial_y = inertial_frame(t)
    line_inertial.set_data(inertial_x, inertial_y)

    # Update rotating frame
    rotating_x, rotating_y = rotating_frame(t, omega=0.2)
    line_rotating.set_data(rotating_x, rotating_y)

    return line_inertial, line_rotating

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Plot inertial frame
line_inertial, = ax.plot([], [], 'b', label='Inertial Frame')

# Plot rotating frame
line_rotating, = ax.plot([], [], 'r', label='Rotating Frame')

# Set up legend
ax.legend()

# Animation settings
ani = animation.FuncAnimation(fig, update, frames=200, fargs=(line_inertial, line_rotating),
                              interval=50, blit=True)

# Show the animation
plt.show()