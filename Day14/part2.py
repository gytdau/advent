# I wanted to try making some classes as practice.

RUNNING = True
RESTING = False


class Reindeer:

    def __init__(self, line):
        """
        :param line: Parses line into the class.
        :return: nothing
        """
        line = line.split()
        self.speed = int(line[3])
        self.running_time = int(line[6])
        self.resting_time = int(line[13])
        self.state = RUNNING
        self.state_timer = int(line[6])
        self.distance = 0
        self.points = 0

    def next_step(self):
        """
        Uses a second of a race.
        :return: nothing
        """
        if self.state == RUNNING:
            self.distance += self.speed

        self.state_timer -= 1
        if self.state_timer <= 0:
            if self.state == RUNNING:
                self.state = RESTING
                self.state_timer = self.resting_time
            else:
                self.state = RUNNING
                self.state_timer = self.running_time

    def add_point(self):
        """
        Adds one point.
        :return: nothing
        """
        self.points += 1


all_reindeer = []

with open("inputData.txt", "r") as infile:
    for line in infile:
        # Make the reindeer objects.
        all_reindeer.append(Reindeer(line))

for i in range(2503):
    for reindeer in all_reindeer:
        reindeer.next_step()

    # Calculate the largest distance of all the reindeer
    distances = [x.distance for x in all_reindeer]
    max_score = max(distances)

    # Search through the reindeer, and add a point to any reindeer that have travelled the 'largest distance'.
    for reindeer in all_reindeer:
        if reindeer.distance == max_score:
            reindeer.add_point()


# Print out the points of the largest reindeer with the most points.
final_scores = [x.points for x in all_reindeer]
print(max(final_scores))
