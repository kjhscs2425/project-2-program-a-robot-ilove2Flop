from simulator import robot
import time
import random

# Constants
BOX_WIDTH = 440
BOX_HEIGHT = 660
MOTOR_SPEED = 1  # Speed of movement

# Function to move the robot
def move_robot(x, y, motor_left, motor_right):
    """Moves the robot based on motor inputs."""
    new_x = x + motor_left * MOTOR_SPEED
    new_y = y + motor_right * MOTOR_SPEED
    return new_x, new_y

# Function to check if the robot hits the wall
def check_bounds(x, y):
    """Checks if the robot is within bounds of the box."""
    if 0 <= x <= BOX_WIDTH and 0 <= y <= BOX_HEIGHT:
        return True
    return False

# Function to get inputs for motor values
def get_motor_input():
    """Asks for motor inputs."""
    motor_left = int(input("Enter left motor value (-1, 0, 1): "))
    motor_right = int(input("Enter right motor value (-1, 0, 1): "))
    return motor_left, motor_right

# Function for autonomous movement
def autonomous_movement():
    """Autonomous movement for 20 seconds, using sonar sensors to guide the robot."""
    print("Autonomous mode activated for 20 seconds.")
    start_time = time.time()
    x, y = 5, 5  # Starting near the corner of the box

    while time.time() - start_time < 20:
        # Read sonar values (simulated here with random values for testing)
        left_sonar, right_sonar = robot.sonars()

        # Determine motor values based on sonar readings
        if left_sonar < 3:  # Obstacle on the left
            motor_left, motor_right = 0, 1  # Turn right
        elif right_sonar < 3:  # Obstacle on the right
            motor_left, motor_right = 1, 0  # Turn left
        else:  # No obstacles
            motor_left, motor_right = random.choice([-1, 0, 1]), random.choice([-1, 0, 1])

        # Move the robot
        new_x, new_y = move_robot(x, y, motor_left, motor_right)
        if check_bounds(new_x, new_y):
            x, y = new_x, new_y
        else:
            print("Wall detected! Movement adjusted.")

        print(f"Robot position: ({x:.1f}, {y:.1f}), Sonars: Left={left_sonar}, Right={right_sonar}")
        time.sleep(1)

# Function for manual control
def manual_control():
    """Manual control based on user inputs."""
    x, y = 5, 5  # Starting near the corner of the box
    for _ in range(5):
        motor_left, motor_right = get_motor_input()
        new_x, new_y = move_robot(x, y, motor_left, motor_right)
        if check_bounds(new_x, new_y):
            x, y = new_x, new_y
        else:
            print("Wall hit! Movement cancelled.")
        print(f"Robot position: ({x:.1f}, {y:.1f})")

# Main function
def main():
    print("Welcome to the Robot Simulator YOPPY!!!")
    while True:
        print("\nMenu:")
        print("1. Manual Control")
        print("2. Autonomous Movement")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manual_control()
        elif choice == "2":
            autonomous_movement()
        elif choice == "3":
            print("Exiting simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
