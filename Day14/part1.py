# I wanted to try making some classes as practice.

RUNNING = True
RESTING = False


class Reindeer:

    def __init__(self, line):
        """
        :param line: Parses line into the class.
        """
        line = line.split()
        self.speed = int(line[3])
        self.running_time = int(line[6])
        self.resting_time = int(line[13])

    def calculate_distance_at(self, time):
        """
        :param time: Amount of time this race should continue for
        :return: The distance this reindeer has run at the end of the race.
        """
        state = RUNNING
        distance = 0
        state_timer = self.running_time
        timer = time
        for i in range(time):
            if state == RUNNING:
                distance += self.speed

            state_timer -= 1
            if state_timer <= 0:
                if state == RUNNING:
                    state = RESTING
                    state_timer = self.resting_time
                else:
                    state = RUNNING
                    state_timer = self.running_time

            timer -= 1
            if timer <= 0:
                return distance

reindeer_distances = []

with open("inputData.txt", "r") as infile:
    for line in infile:
        testing = Reindeer(line)
        reindeer_distances.append(testing.calculate_distance_at(2503))

print(str(max(reindeer_distances)))
