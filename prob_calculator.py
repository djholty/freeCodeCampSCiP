import random
import copy


class Hat():

    def __init__(self, **kwargs):
        self.contents = []
        self.balls = kwargs  #key word arguments stored as dictionary

        #convert the hat dictionary (self.balls) to a hat list self.contents
        for k, v in self.balls.items():
            self.contents += [k] * v

        #print("self.contents", self.contents)

        #print("shuffled self.contents",self.contents)
        #print("self.balls",self.balls)

    def draw(
        self, num_balls_drawn
    ):  #randomly remove balls and return balls as a list of strings.  Balls should not go back into the hat after drawn.
        #pass in hat as a dictionary
        if num_balls_drawn > len(self.contents):
            return self.contents
        ballsdrawn = []

        #draw balls from self.contents ball list and remove one at a time
        # creating a list of drawn balls
        for i in range(num_balls_drawn):
            random.shuffle(self.contents)
            balldrawn = self.contents.pop()
            ballsdrawn.append(balldrawn)

        #print("ballsdrawn",ballsdrawn)

        return ballsdrawn  #returned as a list


def experiment(
    hat, expected_balls, num_balls_drawn, num_experiments
):  #hat is passed in as an instance of the hat class, expected balls as a dictionary
    hat = hat
    M = 0  #number of successful experiments
    for i in range(num_experiments):
        hatcopy = copy.deepcopy(
            hat
        )  #make a copy to leave the hat unaltered for subsequent experiments
        ballsdrawn = hatcopy.draw(
            num_balls_drawn)  #ballsdrawn is returned as a list

        # converts ballsdrawn from list form into a dictionary to allow comparison to the expected ball dictionary values
        ballsdrawndic = {}
        for ball in ballsdrawn:
            ballsdrawndic[ball] = ballsdrawndic.get(ball, 0) + 1


# Code to test if the drawn balls matches the expected balls to determine whether the experiment was successful
        success = None
        for color in expected_balls:
            if color in ballsdrawndic:
                # print('True,', color, 'is present in the drawn balls')
                if ballsdrawndic[color] >= expected_balls[color]:
                    # print("There are enough", color, "balls in the drawn pile")
                    success = True
                else:
                    ## print('There are not enough', color, 'balls')
                    # print('Experiment was not successful')
                    success = False
                    break

            else:
                # print("Not all expected colors have been drawn")
                success = False
                break
        if success == True:
            #print("All colors and number accounted for!!")
            M += 1
    return M / num_experiments
