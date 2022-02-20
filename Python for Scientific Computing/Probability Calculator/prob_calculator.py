import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self,n:int) -> list:
        if n >= len(self.contents):
            return self.contents

        # Get random values and remove them from the list
        drawn = random.sample(self.contents, k=n)
        for ball in drawn:
            self.contents.remove(ball)

        return drawn
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        M = 0
        for _ in range(num_experiments):  
            tmp_hat = copy.deepcopy(hat)
            drawn_balls = tmp_hat.draw(num_balls_drawn)
            b = True
            for key, value in expected_balls.items():
              if  drawn_balls.count(key) < value:
                  b = False
            if b :
                M += 1
        return M/num_experiments
