from python_test.module import Robot

print("output in test.py: "+__name__)

robot1 = Robot() 
robot1.speak()
robot1.walk()
print(robot1.__class__.robot_name)
Robot.speak(robot1)