from lists import UnorderedList, Node
import unittest
import random


class QueueLL:
    """ A class to simulate a Queue data structure as using linked lists """
    def __init__(self):
        """ create our unordered list object as the simulator """
        self.queue = UnorderedList()

    def __str__(self):
        """ override the string output method """
        # I didn't like the output of the overridden string method from queue class
        current = self.queue.head
        output = "Front <-"
        while current != None:
            output = "".join((output, "[" + str(current.getData()) + "]", " <- "))
            current = current.getNext()
        output = "".join((output, "Back of the queue"))
        return output

    def isEmpty(self):
        """ check if our queue is empty"""
        if self.queue.size() == 0:
            return True
        else:
            return False

    def enqueue(self, new_data):
        """ creates a new node in our queue containing given data """
        # append function errors out if there is nothing already in the queue
        if self.queue.size() == 0:
            self.queue.add(new_data)
        else:
            self.queue.append(new_data)

    def dequeue(self):
        """ return and remove item at the front of the queue """
        return self.queue.pop(0)

    def peek(self):
        """ looking at the top item in the queue """
        peek = self.queue.pop(0)
        self.queue.add(peek)
        return peek

    def size(self):
        """ returns # of items in queue """
        return self.queue.size()


class TestQueueLL(unittest.TestCase):
    """ Test class for the Queuell class and child Traffic Simulator Queue class
     Will test dequeue and peek methods, then test overridden string function and one of the setter methods """
    def testDequeue(self):
        """ looking for deque to return the first added piece of data"""
        self.q = QueueLL()
        self.q.enqueue(7)
        self.q.enqueue(8)
        self.q.enqueue(9)
        self.assertEqual(self.q.dequeue(), 7)

    def testPeek(self):
        """ test that the peek looks at the oldest data and that it does not remove said data """
        self.q = QueueLL()
        self.q.enqueue(7)
        self.q.enqueue(8)
        self.q.enqueue(9)
        self.assertEqual(self.q.peek(), 7)
        self.assertEqual(self.q.peek(), 7)

    def testToString(self):
        """ testing the equvilance of the too string method between class inheritance """
        self.t = TrafficSimulatorQueue()
        self.q = QueueLL()
        self.assertEqual(str(self.t), str(self.q))

    def testSetter(self):
        """ testing the the setter functions of the Traffic Sim class """
        self.t = TrafficSimulatorQueue()
        self.t.setProbabilityArrival(0.9)
        self.t.setMinutesGreen(2)
        self.t.setMinutesRed(1)
        self.assertEqual(self.t.prob_arrival, 0.9)
        self.assertEqual(self.t.time_steps_light_is_green, 120)
        self.assertEqual(self.t.time_steps_light_is_red, 60)



class TrafficSimulatorQueue(QueueLL):
    """
    A class to simulate traffic arriving and leaving an intersection with a stop
    light.  As with all simulations, time is discretized so that each loop
    iteration represents one (1) second of time.

    Fields:
      * queue [from inheritance] - the internal structure that holds the queue
      * traffic_light_state - current status of the traffic light, either 'red' or 'green'
      * time_steps_needed_for_1_car_to_exit - time steps (e.g. 'seconds') needed for front car to exit intersection
      * prob_arrival - probability that an automobile arrives on any given iteration/epoch
      * time_steps_light_is_red - number of time steps (e.g. 'seconds') the traffic light is red
      * time_steps_light_is_green - number of time steps (e.g. 'seconds') the traffic light is green

    Methods:
      * __init__() - constructor to initialize class fields/attributes
      * isEmpty() [from inheritance]
      * enqueue(new_item) [from inheritance]
      * dequeue() [from inheritance]
      * size() [from inheritance]
      * peek() [from inheritance]
      * setProbabilityArrival(prob_arrival) - modify the probability that a car arrives at any given time step
      * setMinutesRed(min_red) - modify the number of minutes the traffic light is red for (and convert to seconds/time_steps)
      * setMinutesGreen(min_red) - modify the number of minutes the traffic light is red for (and convert to seconds/time_steps)
      * checkForArrivingAuto() - check to see if a car arrives (intended to be called at each time step)
      * simulateTraffic(n) - simulate traffic for n cycles of red and green lights, starting with red first and
                             printing status, queue, etc. as the simulation is carried out
    """

    def __init__(self):
        """ utilizes the constructor from parent class and constants for simulation """
        super().__init__()
        self.traffic_light_state = 'red'
        self.time_steps_needed_for_1_car_to_exit = 3
        self.prob_arrival = (1/3)
        self.time_steps_light_is_red = 60
        self.time_steps_light_is_green = 60

    def setProbabilityArrival(self, new_prob):
        """ setter for probability of car arrival """
        self.prob_arrival = new_prob

    def setMinutesRed(self, new_Rtime):
        """ setter for time red light """
        self.time_steps_light_is_red = new_Rtime*60

    def setMinutesGreen(self, new_Gtime):
        """ setter for time green light """
        self.time_steps_light_is_green = new_Gtime*60

    def checkForArrivingAuto(self):
        """
        Generate a random number between 0 and 1, then see if it less than
        self.prob_arrival. If it is, then add a new auto/car to the queue.
        """
        r = random.random()
        if r < self.prob_arrival:
            car_arriving = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            super().enqueue(car_arriving)

    def simulateTraffic(self, number_redgreen_cycles):
        """ Run the simulation where each iteration of the while loop represents 1 second. """
        print("Traffic light is red, current queue size = " + str(self.size()))

        i = number_redgreen_cycles * (self.time_steps_light_is_red + self.time_steps_light_is_green)
        i_light = self.time_steps_light_is_red

        while i > 0:
            # cars can arrive regardless of whether the light is red or green
            self.checkForArrivingAuto()

            # light is red, so just decrement the light counter, i_light
            # once i_light has counted down to 0, then set everything needed to
            # change it to green
            if self.traffic_light_state == "red":
                i_light -= 1
                if i_light == 0:
                    self.traffic_light_state = 'green'
                    i_light = self.time_steps_light_is_green
                    print("Traffic light changing to green, current queue size = " + str(self.size()) + ", queue:")
                    print(" "*2, self)

            # light is green, so just decrement light counter AND check to see if
            # time_steps_needed_for_1_car_to_exit iterations have passed (if so, removed a car from the queue)
            # once i_light has counted down to 0, then set everything needed to change the light to red
            else:
                i_light -= 1
                if i % self.time_steps_needed_for_1_car_to_exit == 0:
                    car_leaving = super().dequeue()
                    print(" "*4, "car,", car_leaving, ", exiting intersection")
                if i_light == 0:
                    self.traffic_light_state = 'red'
                    i_light = self.time_steps_light_is_red
                    print("Traffic light changing to red, current queue size = " + str(self.size()) + ", queue:")
                    print(" "*2, self)
            i -= 1


if __name__ == '__main__':

    print('='*30, 'Simulation 1:', '='*30)
    ts = TrafficSimulatorQueue()

    # set probability that a car arrives on any given second (i.e. loop # iteration) to 33.3%
    ts.setProbabilityArrival(1/3)

    # set the light to be red for 1 minutes (needs to be converted to seconds inside)
    ts.setMinutesRed(1)

    # set the light to be green for 2 minute (needs to be converted to seconds inside)
    ts.setMinutesGreen(2)

    # run simulation for two red-green cycles (i.e. red -> green -> red -> green)
    ts.simulateTraffic(2)

    print("Traffic simulator queue size at end of simulation =", ts.size())
    print("Traffic simulator queue at end of simulation:")
    print(ts)
    unittest.main()
