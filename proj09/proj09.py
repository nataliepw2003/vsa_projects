# proj09: Simulating robots
# Name:
# Date:

import math
import random

import proj09_visualize
import pylab
import random
# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tileList = []

        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.tileList.append(pos)
        print "self.titleList equals", self.tileList


    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        for pos in self.tileList:
            x = pos.getX()
            y = pos.getY()
            if x==m and y==n:
                return True
        return False
    
    def getNumTiles(self):
        area = self.width * self.height
        NumTiles = area
        print NumTiles
        """
        Return the total number of tiles in the room.

        returns: an integer
        """

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        a = 0
        for tile in self.tileList:
            if self.isTileCleaned==True:
                a = a + 1
        print "a equals",a

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        self.width = 5
        self.height = 5
        self.x = random.randint(0, self.width)
        self.y = random.randint(0, self.height)
        Position = (self.x, self.y)
        print "position equals",Position
        return Position

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        for pos in self.tileList:
            x = pos.getX()
            y = pos.getY()
            if x<=self.width and y<=self.height:
                print"isPositionInRoom equals", True
                return True
        return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """#******
        room = RectangularRoom(5, 5)
        self.room = room
        self.speed = speed
        self.position=self.room.getRandomPosition()
        self.direction=0.0
    def getRobotPosition(self):
        print self.position
        return self.position
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        #raise NotImplementedError
    
    def getRobotDirection(self):
        print self.direction
        return self.direction
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """


        #raise NotImplementedError

    def setRobotPosition(self, position):
        self.position=position
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        #raise NotImplementedError

    def setRobotDirection(self, direction):
        self.direction=direction
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        #r#aise NotImplementedError

    def updatePositionAndClean(self):
        cleanTileAtPosition
        while tileList<area:
            getNewPosition()
            if isPositionInRoom==True:
                position=setRobotPosition
            if position in tileList:
                position = setRobotPosition
            else:
                cleanTileAtPosition
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError

room = RectangularRoom(5, 5)
robot=Robot(room,3)
print "cleanTileAtPosition equals",room.cleanTileAtPosition(Position(3, 4))
print "isTileCleaned",room.isTileCleaned(3, 4)
print "getNumTiles",room.getNumTiles()
print "getNumCleaned", room.getNumCleanedTiles()
print "getRandomPosition",room.getRandomPosition()
print "isPositionInRoom", room.isPositionInRoom(room.getRandomPosition())
print "getRobotPosition", robot.getRobotPosition()
print "updatePositionAndClean", room.updatePositionAndCLean()
# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    raise NotImplementedError


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """ 
    raise NotImplementedError

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    raise NotImplementedError

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    raise NotImplementedError


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    raise NotImplementedError
