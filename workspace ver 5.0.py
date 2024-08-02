import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from shapely.geometry import Polygon

# Function to calculate the workspace of the robot end-effector
def calculate_workspace(num_joints, limit):
    # Constants
    lengths = [1] * num_joints  # Lengths of links

    # Initialize arrays to store workspace points and joint positions
    workspace_x = []
    workspace_y = []
    joint_positions = []

    # Calculate the increment value for each joint angle
    angle_increment = limit / (num_joints - 1)

    # Generate initial angles of joints
    initial_angles = np.arange(0, limit + angle_increment, angle_increment)

    # Calculate workspace points and joint positions
    for base_angle in initial_angles:
        # Convert angles to radians
        radians = [np.deg2rad(base_angle + i * angle_increment) for i in range(num_joints)]

        # Initialize coordinates of previous joint
        prev_x = 0
        prev_y = 0

        # Calculate positions of each joint
        joint_pos = [(prev_x, prev_y)]
        for i in range(num_joints):
            x = prev_x + lengths[i] * np.cos(radians[i])
            y = prev_y + lengths[i] * np.sin(radians[i])
            joint_pos.append((x, y))
            prev_x = x
            prev_y = y

        # Store joint positions for plotting
        joint_positions.append(joint_pos)

        # Calculate position of end-effector
        workspace_x.append(prev_x)
        workspace_y.append(prev_y)

    # Create a Polygon object from the workspace points
    polygon = Polygon(list(zip(workspace_x, workspace_y)))

    # Calculate the area of the Polygon
    workspace_area = polygon.area

    return workspace_area, workspace_x, workspace_y, joint_positions

# Function to calculate the area of the circular segment formed by the end-effector
def calculate_segment_area(radius, angle):
    return (np.pi * radius ** 2 * angle) / 360

# Update function for animation
def update(frame, joint_positions, ax, workspace_x, workspace_y, workspace_area):
    ax.clear()
    joints = joint_positions[frame]
    joints = np.array(joints)
    ax.plot(joints[:, 0], joints[:, 1], 'b-')
    ax.plot(joints[:, 0], joints[:, 1], 'ro')
    
    # Plot workspace points
    ax.plot(workspace_x[:frame+1], workspace_y[:frame+1], 'g--')  # Plotting the points traversed by end-effector
    
    # Calculate the radius of the circular segment formed by the end-effector
    radius = np.max(np.sqrt(np.array(workspace_x[:frame+1])**2 + np.array(workspace_y[:frame+1])**2))
    angle = (frame + 1) * (360 / len(workspace_x))
    
    # Calculate the area of the circular segment
    segment_area = calculate_segment_area(radius, angle)
    
    # Calculate the percentage of workspace area compared to circular segment area
    percentage = (workspace_area / segment_area) * 100
    
    ax.set_title(f'Frame {frame}, Workspace Area: {workspace_area:.2f} mm^2, Workspace Coverage: {percentage:.2f}%')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.axis('equal')
    ax.set_xlim([-10, 10])  # Assuming maximum range for x-axis is -6 to 6
    ax.set_ylim([-10, 10])  # Assuming maximum range for y-axis is -6 to 6

# Main function
def main():
    limit = 90  # Limit value

    num_joints_list = [3, 4, 5, 6]  # List of number of joints to analyze
    num_plots = len(num_joints_list)
    rows = int(np.sqrt(num_plots))
    cols = int(np.ceil(num_plots / rows))

    fig, axs = plt.subplots(rows, cols, figsize=(12, 10))
    animations = []  # List to store animations

    for idx, num_joints in enumerate(num_joints_list):
        workspace_area, workspace_x, workspace_y, joint_positions = calculate_workspace(num_joints, limit)
        ax = axs[idx // cols, idx % cols] if num_plots > 1 else axs
        anim = FuncAnimation(fig, update, frames=len(joint_positions), fargs=(joint_positions, ax, workspace_x, workspace_y, workspace_area), interval=500, repeat=False)
        animations.append(anim)  # Add animation to the list

    plt.show()

    # Wait for all animations to finish
    for anim in animations:
        anim.event_source.stop()

if __name__ == "__main__":
    main()
