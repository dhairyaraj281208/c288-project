from controller import Robot
from controller import Keyboard

robot = Robot()
kb = Keyboard()

# create unique identifier for each device
motor = robot.getDevice('A motor')

timestep = int(robot.getBasicTimeStep())
kb.enable(timestep)
motora_pos = 0

# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    key_pressed = kb.getKey()   

    # write code to move the joints with keyboard
    if(key_pressed == 49):
        motora_pos += 0.005
    if (key_pressed == 50):
        motora_pos -= 0.005
        
    motor.setPosition(motora_pos)