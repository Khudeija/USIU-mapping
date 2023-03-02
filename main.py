import operator
import constraint
from datetime import datetime
import numpy as np


class Environment():
    myGraph = {"Gate B": set(["SHSS", "SHSS parking A"]),
               "SHSS": set(["SST", "SHSS parking A", "Gate B"]),
               "SHSS parking A": set(["SHSS", "Gate B"]),
               "SST": set(["SHSS", "SST parking"]),
               "SST parking": set(["Library", "SST"]),
               "Swimming pool": set(["Student Center", "Swimming pool parking"]),
               "Swimming pool parking": set(["Auditorium parking", "Student Center", "Swimming pool"]),
               "Student Center": set(["Student Center parking", "Swimming pool parking", "Swimming pool"]),
               "Student Center parking": set(
                   ["Auditorium", "Basketball court", "Visiting faculty housing", "Student Center"]),
               "Library": set(
                   ["Auditorium", "Auditorium parking", "Library parking", "School of business", "SST parking"]),
               "Library parking": set(["Library", "School of business"]),
               "Auditorium": set(["Auditorium parking", "Library", "Basketball court", "Cafe lata", "Hostel",
                                  "Student Center parking"]),
               "Auditorium parking": set(["Auditorium", "Swimming pool parking", "Library"]),
               "School of business": set(["Library parking", "Library", "Old school of humanties"]),
               "Old school of humanties": set(["School of business", "Wooden blocks", "Main lab"]),
               "Wooden blocks": set(["Main lab", "Old school of humanties"]),
               "Main lab": set(["Wooden blocks", "Gate A", "Lilian beam", "Old school of humanties"]),
               "Basketball court": set(
                   ["Cafe lata", "Bus parking", "Visiting faculty housing", "Student Center parking", "Auditorium"]),
               "Cafe lata": set(["Bus parking", "Basketball court", "Hostel", "Auditorium", "Admin block"]),
               "Cafe lata parking lot": set(["Visiting faculty housing", "Bus parking", "Transport office","Admin block"]),
               "Hostel": set(
                   ["Cafeteria", "Lilian beam", "Cafe lata", "Auditorium", "Bus parking", "Transport office"]),
               "Bus parking": set(
                   ["Hostel", "Cafe lata parking lot", "Cafe lata", "Basketball court", "Transport office"]),
               "Cafeteria": set(["Hostel", "Lilian beam", "Admin block"]),
               "Lilian beam": set(["Main lab", "Cafeteria", "Hostel", "Admin block", "Gate A"]),
               "Admin block": set(["Cafeteria", "Lilian beam", "Admin parking", "Transport office", "Gate A"]),
               "Admin parking": set(["Transport office", "Admin block", "Gate A"]),
               "Visiting faculty housing": set(["Student Center parking", "Basketball court", "Cafe lata parking lot"]),
               "Transport office": set(
                   ["Cafe lata parking lot", "Admin parking", "Bus parking", "Hostel", "Admin block"]),
               "Gate A": set(["Admin parking", "Admin block", "Lilian beam", "Main lab"])}

    cost = {str(["Gate B", "SHSS"]): "100", str(["Gate B", "SHSS parking A"]): "100",
            str(["SHSS", "SST"]): "4", str(["SHSS", "SHSS parking A"]): "400", str(["SHSS", "Gate B"]): "200",
            str(["SHSS parking A", "SHSS"]): "500", str(["SHSS parking A", "Gate B"]): "600",
            str(["SST", "SHSS"]): "300", str(["SST", "SST parking"]): "400",
            str(["SST parking", "Library"]): "600", str(["SST parking", "SST"]): "300",
            str(["Swimming pool", "Student Center"]): "500",
            str(["Swimming pool", "Swimming pool parking"]): "200",
            str(["Swimming pool parking", "Auditorium parking"]): "700",
            str(["Swimming pool parking", "Student Center"]): "200",
            str(["Swimming pool parking", "Swimming pool"]): "200",
            str(["Student Center", "Student Center parking"]): "300",
            str(["Student Center", "Swimming pool parking"]): "300", str(["Student Center", "Swimming pool"]): "300",
            str(["Student Center parking", "Auditorium"]): "300",
            str(["Student Center parking", "Basketball court"]): "300",
            str(["Student Center parking", "Visiting faculty housing"]): "300",
            str(["Student Center parking", "Student Center"]): "300",
            str(["Library", "Auditorium"]): "300", str(["Library", "Auditorium parking"]): "300",
            str(["Library", "Library parking"]): "300", str(["Library", "School of business"]): "300",
            str(["Library", "SST parking"]): "300",
            str(["Library parking", "Library"]): "300", str(["Library parking", "School of business"]): "300",
            str(["Auditorium", "Auditorium parking"]): "300", str(["Auditorium", "Library"]): "300",
            str(["Auditorium", "Basketball court"]): "300",
            str(["Auditorium", "Cafe lata"]): "300", str(["Auditorium", "Hostel"]): "300",
            str(["Auditorium", "Student Center parking"]): "300",
            str(["Auditorium parking", "Auditorium"]): "300",
            str(["Auditorium parking", "Swimming pool parking"]): "300", str(["Auditorium parking", "Library"]): "300",
            str(["School of business", "Library parking"]): "300", str(["School of business", "Library"]): "300",
            str(["School of business", "Old school of humanties"]): "300",
            str(["Old school of humanties", "School of business"]): "300",
            str(["Old school of humanties", "Wooden blocks"]): "300",
            str(["Old school of humanties", "Main lab"]): "300",
            str(["Wooden blocks", "Main lab"]): "300", str(["Wooden blocks", "Old school of humanties"]): "003",
            str(["Main lab", "Wooden blocks"]): "300", str(["Main lab", "Gate A"]): "300",
            str(["Main lab", "Lilian beam"]): "300", str(["Main lab", "Old school of humanties"]): "300",
            str(["Basketball court", "Cafe lata"]): "300", str(["Basketball court", "Bus parking"]): "300",
            str(["Basketball court", "Visiting faculty housing"]): "300",
            str(["Basketball court", "Student Center parking"]): "300",
            str(["Basketball court", "Auditorium"]): "300",
            str(["Cafe lata", "Bus parking"]): "300", str(["Cafe lata", "Basketball court"]): "300",
            str(["Cafe lata", "Hostel"]): "300", str(["Cafe lata", "Auditorium"]): "300", 
						str(["Cafe lata", "Admin block"]): "300",
            str(["Cafe lata parking lot", "Bus parking"]): "300",
            str(["Cafe lata parking lot", "Visiting faculty housing"]): "300",
            str(["Cafe lata parking lot", "Transport office"]): "300",
						str(["Cafe lata parking lot", "Admin block"]): "300",
            str(["Hostel", "Cafeteria"]): "300", str(["Hostel", "Lilian beam"]): "300",
            str(["Hostel", "Cafe lata"]): "300", str(["Hostel", "Auditorium"]): "300",
            str(["Hostel", "Bus parking"]): "300",
            str(["Hostel", "Transport office"]): "300",
            str(["Bus parking", "Hostel"]): "300", str(["Bus parking", "Cafe lata parking lot"]): "300",
            str(["Bus parking", "Transport office"]): "300", str(["Bus parking", "Cafe lata"]): "300",
            str(["Cafeteria", "Hostel"]): "300", str(["Cafeteria", "Lilian beam"]): "300",
            str(["Cafeteria", "Admin block"]): "300",
            str(["Lilian beam", "Hostel"]): "300", str(["Lilian beam", "Cafeteria"]): "300",
            str(["Lilian beam", "Admin block"]): "300", str(["Lilian beam", "Main lab"]): "300",
            str(["Lilian beam", "Gate A"]): "300",
            str(["Admin block", "Lilian beam"]): "300", str(["Admin block", "Cafeteria"]): "300",
            str(["Admin block", "Admin parking"]): "300", str(["Admin block", "Transport office"]): "300",
            str(["Admin block", "Gate A"]): "300",
            str(["Admin parking", "Admin block"]): "300", str(["Admin parking", "Transport office"]): "300",
            str(["Admin parking", "Gate A"]): "300",
            str(["Visiting faculty housing", "Student Center parking"]): "300",
            str(["Visiting faculty housing", "Basketball court"]): "300",
            str(["Visiting faculty housing", "Cafe lata parking lot"]): "300",
            str(["Transport office", "Cafe lata parking lot"]): "300",
            str(["Transport office", "Admin parking"]): "300", str(["Transport office", "Bus parking"]): "300",
            str(["Transport office", "Hostel"]): "300", str(["Transport office", "Admin block"]): "3",
            str(["Gate A", "Admin parking"]): "300", str(["Gate A", "Admin block"]): "300",
            str(["Gate A", "Lilian beam"]): "300", str(["Gate A", "Main lab"]): "300",

            }

    myHeauristics = {
        "Gate A": ["0"],
        "Admin block": ["83"],
        "Admin parking": ["63"],
        "School of business": ["160"],
        "Lilian beam": ["100"],
        "Transport office": ["111"],
        "Visiting faculty housing": ["115"],
        "Old school of humanties": ["140"],
        "Wooden blocks": ["130"],
        "Cafe lata": ["110"],
        "Cafeteria": ["107"],
        "Main lab": ["123"],
        "Library": ["180"],
        "Library parking": ["190"],
        "Hostel": ["631"],
        "Cafe lata parking lot": ["723"],
        "SST": ["688"],
        "Bus parking": ["811"],
        "Auditorium": ["820"],
        "Basketball court": ["649"],
        "Auditorium parking": ["1088"],
        "Student Center": ["1200"],
        "Student Center parking": ["1000"],
        "SST parking": ["1243"],
        "Gate B": ["1900"],
        "Swimming pool parking": ["1590"],
        "Swimming pool": ["1500"],
        "SHSS parking A": ["1800"],
        "SHSS": ["1700"],

    }
    fireAssemblyPoints = {
        "Gate A": "Admin parking",
        "Admin block": "Admin parking",
        "Admin parking": "none",
        "School of business": "Graduation grounds ",
        "Lilian beam": "Admin Parking",
        "Transport office": "Bus parking",
        "Visiting faculty housing": "Bus parking",
        "Old school of humanties": "Wooden blocks lounge",
        "Wooden blocks": "Wooden blocks lounge",
        "Cafe lata": "Cafe lata parking",
        "Cafeteria": "Admin parking",
        "Main lab": "Wooden blocks lounge",
        "Library": "Graduation grounds",
        "Library parking": "none",
        "Hostel": "Cafe latta parking/Auditorium",
        "Cafe lata parking lot": "none",
        "SST": "Student Center parking",
        "Bus parking": "none",
        "Auditorium": "Auditorium parking",
        "Basketball court": "Auditorium parking",
        "Auditorium parking": "none",
        "Student Center": "Student Center parking",
        "Student Center parking": "none",
        "SST parking": "Student Center parking",
        "Gate B": "SHSS parking A",
        "Swimming pool parking": "none",
        "Swimming pool": "Swimming pool parking",
        "SHSS parking A": "none",
        "SHSS": "Swimming pool parking",

    }
    start = ""
    goal = ""




class Agent(Environment):

    def getCost(pathToCost):
        pathCost = 0
        i = 0
        # its the length of the path to cost
        while i < len(pathToCost) - 1:
            l = []  # the list will be overwritten with every path pair

            l.append(pathToCost[i])

            l.append(pathToCost[i + 1])

            pathCost = pathCost + int(Environment.cost[str(l)])  # l needs to be a string cause its string in cost

            i += 1

        return pathCost

    def getH(vertext, goal):
        v = []
        g = []
        for i in Environment.myHeauristics[vertext]:  # get the coordinates of the vertext
            v.append(int(i))
        for i in Environment.myHeauristics[goal]:  # get the coordinates of the goal (dest)
            g.append(int(i))

        hue = abs(v[0]) + abs(g[0])
        return hue

    def Astar(graph, start, goal):
        p = []  # holds the path

        fTotal = 0

        while True:
            p.append(start)
            neighbour = graph[start]  # varibale to find out whats next to the start
            H = {}
            for i in neighbour.difference(p):

                l = []
                l.append(str(start))
                l.append(str(i))
                H[i] = Agent.getH(i, goal) + Agent.getCost(l)


            sortedH = sorted(H.items(), key=operator.itemgetter(1))
            x = next(iter(sortedH[0]))

            fTotal = fTotal + H[x]
            if x == goal:
                p.append(x)
                return p

            else:
                start = x  # continue with while loop, make the start the current position


    def __init__(self, Envrionment):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        time_list = current_time.split(":")
        time_value = round((int(time_list[1]) / 60), 1) + int(time_list[0])

        problem = constraint.Problem()  # to create the objetc

        # Variables
        problem.addVariables("t",
                             np.arange(0.0, 24.5, 0.1))  # Variable followed by range. Both T and F have the same range
        problem.addVariables("d", range(1, 8))  # Variable followed by range. Both T and F have the same range

        # Constraints
        def busyConst(t, d):  # put your variables in
            if ((8.6 <= t <= 9.0 or 10.6 <= t <= 11.0 or 12.6 <= t <= 13.3 or 15.0 <= t <= 15.5
                 or 17.2 <= t <= 18.0 or 19.0 <= t <= 19.3 or 21.0 <= t <= 21.3) and (
                    d != 7 or d != 6 or d != 5)):  # Monday to Thur
                return True
            elif ((11.3 <= t <= 11.6 or 21.60 <= t <= 21.3) and d == 5):  # Friday
                return True
            elif ((12.3 <= t <= 12.6 or 16.8 <= t <= 18.2) and d == 6):  # Saturday
                return True

        problem.addConstraint(busyConst, "td")
        solutions = problem.getSolutions()
        dayAndTime = {"d": (datetime.today().weekday()) + 1, "t": time_value}
        for solution in solutions:
            busy_times = solution

            if (busy_times["d"] == (datetime.today().weekday()) + 1) and (round(busy_times["t"]) == time_value):
                Environment.cost[str(["Cafeteria", "Hostel"])] = 400
                Environment.cost[str(["Cafeteria", "Lilian beam"])] = 400
                Environment.cost[str(["Cafeteria", "Admin block"])] = 400
                Environment.cost[str(["Hostel", "Cafeteria"])] = 400
                Environment.cost[str(["Lilian beam", "Cafeteria", ])] = 400
                Environment.cost[str(["Admin block", "Cafeteria", ])] = 400
                break
            else:
                Environment.cost[str(["Cafeteria", "Hostel"])] = 300
                Environment.cost[str(["Cafeteria", "Lilian beam"])] = 300
                Environment.cost[str(["Cafeteria", "Admin block"])] = 300
                Environment.cost[str(["Hostel", "Cafeteria"])] = 300
                Environment.cost[str(["Lilian beam", "Cafeteria", ])] = 300
                Environment.cost[str(["Admin block", "Cafeteria", ])] = 300

        if (Environment.goal == Environment.start):
            print("Already at destination: ", Environment.goal)

        else:
            print("Recommended Route: ", Agent.Astar(Environment.myGraph, Environment.start, Environment.goal))


while True:
    menu = int(input("Welcome to the USIU navigation guide.\n"
          "==================================== \n"
          "What would you like to do?\n"
          "1. Find the route from one location to a destination of choice? \n"
          "2. Find a Fire Assembly point \n "
                     "Choice: "))
    if(menu == 1):
        print("\n This option finds the best route from one location to the other \n"
               "-----------------------------------------------------------------")
        print("Below are the building options to choose from "
              "(make sure the spelling and cases match the options given below):\n ")
        print(Environment.myGraph.keys(), "\n")
        Environment.start = input("Enter Starting point: ")
        Environment.goal = input("Enter Destination: ")
        theEnvironment = Environment()
        theAgent = Agent(theEnvironment)
        break
    elif(menu ==2):
        print("This option will find the closest Fire Assembly point to a certain building")
        SearchFirePoint = input("Which buildings Fire Assembly point are you looking for? ")
        theEnvironment = Environment()
        print("\n The assembly point for that building is:  ", Environment.fireAssemblyPoints.get(SearchFirePoint))
        break
    else:
        print("Invalid Menu choice. Pick again")



