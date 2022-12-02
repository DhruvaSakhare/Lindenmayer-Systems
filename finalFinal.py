"""
Please enjoy the Lindenmayer System Program, which we worked on as our exam project. We chose this project because it seemed intriguing and was a good way to use some of the programming skills we have learnt in this semester.
Lindenmayer system was created to simulate natural systems like the Sierpinski triangle and the Koch curve
what this program does is that it first asks you to choose which Lindenmayer system you want to perform.
It will then ask the number of iterations.
However, there is a limit to the number of iterations that can be put in for the function to work as higher number of iterations take a lot of time to compute.
You will then have the opportunity to map the system using the program. This will display the specified Lindenmayer system's plot.
We have also made it as user-friendly as much as possible.
We have also used try-except to deal with possible errors.
Enjoy

By: Dhruva Sakhare, Lawrence Ryan and Santhosh Balaji
"""


import numpy as np
from matplotlib import pyplot as plt


def LindIter(System, N):
    '''
    Computes the Lindenmayer String after N iterations.
    :param System: The type of system the user wants to compute.
    :param N: The number of iterations.
    :return: LindenmayerString,It is the final Lindenmayer String after N iterations.
    '''

    if System == "Koch":
        LindenmayerString = "S"  # the first letter of Koch System
    elif System == "Sierpinski":
        LindenmayerString = "A"  # the first letter of Sierpinski System

    rules = {"S": "SLSRSLS", "L": "L", "R": "R", "A": "BRARB", "B": "ALBLA", "D": "DLDDRDL"}


    def LindString(string):
        '''
        Translates string according to rules dictionary, for example it converts S to SLSRSLS.
        :param string: String that needs to be translated.
        :return: Translated String
        '''

        output = ''
        for letter in string:
            LindenmayerString = rules[letter]  # Translates according to rules.
            output += LindenmayerString
        return output

    for i in range(N):  # Iterates N times.
        LindenmayerString = LindString(LindenmayerString)

    return LindenmayerString


'''
The turtleGraph(LindenmayerString,N) function determines the plot commands from the Lindenmayer String, which was computed by LindIter(System, N).
It does this by translating the string into commands based on the commands dictionary, which is unique to the system.
LindenmayerString: The Lindmayer String computed before.
N: The number of iterations.
'''

def turtleGraph(LindenmayerString,N):
    '''
    The function determines the plot commands from the Lindenmayer String, which was computed by LindIter(System, N).
    :param LindenmayerString: The lindenmayer string computed by LindIter.
    :param N: The number of iterations.
    :return: turtleCommands, An array of numbers which signify the distance and angle the to plot the graph.
    '''

    turtleCommands = []
    if LindenmayerString[0] == "S":  # As S is always the first letter of Koch system.
        kochCommands = {"S": (1/3 ** N), "L": (np.pi / 3), "R": (-2*np.pi/3)}  # commands
        for letter in LindenmayerString[:]:
            LindenmayerString = kochCommands[letter]
            turtleCommands.append(LindenmayerString)

    elif LindenmayerString[0] == "A" or "B":  # As the first letter of Sierpinski system can be A or B.
        sierpinskiCommands = {"A": (1/2**N), "B": (1/2**N), "L": (np.pi/3), "R": (-np.pi/3)}  # commands
        for letter in LindenmayerString[:]:
            LindenmayerString = sierpinskiCommands[letter]
            turtleCommands.append(LindenmayerString)
    turtleCommands = np.array(turtleCommands)
    return turtleCommands


'''
The turtlePlot(turtleCommands) uses the commands computed in turtleGraph(LindenmayerString,N) to plot the final graph.
turtleCommands: An array of numbers which signify the distance and angle the "turtle" should move to plot the graph. Computed by turtleGraph(LindenmayerString,N).
'''
def turtlePlot(turtleCommands):
    '''
    This function uses the commands computed in turtleGraph(LindenmayerString,N) to plot the final graph.
    :param turtleCommands: An array of numbers which signify the distance and angle the to plot the graph.
    :return: Outputs plot.
    '''

    coords = np.array([[0, 0]])  # Starting from the origin (0,0).
    length = np.array([turtleCommands[0], 0])  # The first length is the first command.
    angle = np.array([[1, 0], [0, 1]])  # The direction of the vector is initialised in the positive x direction.

    for i in range(len(turtleCommands)):
        if i % 2 != 0:  # as indexes start from 0, the odd indexes are the angles
            # We first compute the direction matrix.
            directionMatrix = np.array([[np.cos(turtleCommands[i]), -np.sin(turtleCommands[i])], [np.sin(turtleCommands[i]), np.cos(turtleCommands[i])]])
            # Then we use the formula from the Projects documentation, to find the next angle.
            angle = np.dot(directionMatrix, angle)

        else:
            # We now find the next coordinates where the vector lands.
            newCoords = [np.add(coords[-1], np.dot(angle, length))]  # Using the formula from the Projects documentation to find the next coordinate.
            # We append our coordinates set with the new coordinates.
            coords = np.append(coords, newCoords, axis=0)

        # plotting the first column of the coordinates for the x-axis
        xcoords = [x[0] for x in coords]
        # plotting the second column of the coordinated for the y-axis
        ycoords = [x[1] for x in coords]

    # create and show the graph
    plt.plot(xcoords, ycoords)
    plt.show()
    # in next iteration new coordinates are made from the previous coordinates


# Main function
while True:
    # The options are printed
    print("\n1.Choose the type of Lindenmayer system and the number of iterations\n2.Generate plot\n3.Quit\n")

    # The input is first put into a temp file to troubleshoot whatever the user inputted. It will check if its an int or random inputs.
    temp = input("Enter your option: ")


    # This attempts to check if it is an integer
    try:
        option = int(temp)
    except:
        # We do not want anything that isnt an integer in the main menu
        print("\nInput is not an integer")
        option = 4  #redo
    # The choice made must be an integer, and we give it some conditions thorugh if-statements.
    # Also, there is an if-statement in order to prevent error.
        option = 4  # Because it is not an integer, we still have to initialize option, we chose 4 as a random integer that isnt one of the options


    # Hard cases for each option
    valid = 0

    # Option 1 is the system choices and iterations
    if option == 1:

        # Attempt to get a valid number, valid is the condition that there is a valid input
        # We initialize the "failsafe"  where if valid is not 0, a problem has occurred.
        valid = 0

        # Runs a loop if the question is not fulfilled using the valid varible, in this case, type of Lindermayer system
        while (valid == 0):


            # Unlike valid, this is a specific case of error that is solved with the variable "problem" to solve if there was no previous load data.
            problem = 0
            # Attempt to remember previous choice, if a problem occurs, ignore
            # Attempt to remember previous choice, if a problem occurs, ignore oldSystem.
            try:
                oldSystem = System
            except:
                problem = 1


            # A temp file to hold whatever the user inputted again.
            temp = input(
                "\nChoose the type of Lindenmayer system:\n 1.Koch System\n 2.Sierpinski System\nTo cancel, type 'cancel'\n\nEnter your option: ")

            # Added a cancel feature if the user ever chooses to
            # Added a cancel feature if the user ever chooses to.
            if temp == 'cancel':
                valid = 1
                break

            # Filters through different possible cases of answers. If the answer is satisfactory, make valid != 0
            # Filters through different possible cases of answers. If the answer is satisfactory, make valid = 1.
            try:
                systemChoice = int(temp)
            except ValueError:
                print("\nPlease enter an integer option.")
                # Similarly to the "option" variable, we want to make sure it is none of the options because we still need to initialize the variable.
                systemChoice = 0


            # Selects the different choices available, 1 for Koch, 2 for Sierpinski
            if systemChoice == 1:
                System = "Koch"
                break
            elif systemChoice == 2:
                System = "Sierpinski"
                break
            else:
                # Either they wrote random gibberish or they did not input 1 or 2
                print("Please select between option 1 or 2.")

        # Similar system as the previous question, asking iterations
        # Similar system as the previous question, but asking iterations
        while (valid == 0):


            # Temp file things, still handles errors and makes it idiot proof
            temp = input("\nHow many iterations would you like? (To cancel, type 'cancel'): ")

            # Cancel function will reinput the previous choice, therefore keeping it as a "saved" load
            if temp == 'cancel':
                if problem != 1:

                    # Will input the old input if there was any, defined by problem variable. If problem occurs, skip process
                    System = oldSystem
                # Valid will return to main menu
                valid = 1
                break


            # This is similar to problem, but for iterations
            iterprob = 0

            try:
                N = int(temp)
            except ValueError:
                print("\nPlease enter an integer option.")
                iterprob = 1

            # We limited it to this specific range to keep it runnable on a potato if desired
            # iterprob will determine if there is an invalid input and will ignore these if statements
            if iterprob == 0:
                if N <= 0:
                    print("The number of iterations must be positive.")

                # We cannot handle these many iterations, even 9 is occassionally too much for some systems. Therefore we limited it to 9.
                elif N > 9:
                    print('\nThe number of iterations is limited to 9 to prevent excessive runtime. Please try again.')

            # Prints out the final "load" of the loading data process, prints out what was chosen, the menu screen will reappear
                else:
                    print(
                        f'\nYou have chosen {System} as your Lindenmayer system and chosen {N} iterations.')
                    #Unlike the other valid, this just brings it back to the main menu safely.
                    valid = 1

        # The program will bring up the main menu again, asking the 3 possible options


    # Option 2 is plotting the graph using turtle
    if option == 2:
        valid = 1

        # We check if it is possible to make a graph, if not, there were no previous "load" of data.
        try:
            # At this point, it is shown how every function in the whole program should run, and what inputs should be used for each of them
            turtlePlot(turtleGraph(LindIter(System, N), N))
        except:
            print("\nLindenmayer System not chosen.")

    # Option 3 to end the program
    if option == 3:
        print("\nGoodbye!")
        break

    # This makes sure that the input is acceptable (1, 2 or 3) and ignores everything else. Valid is to make sure that if option 1 was chosen, it will still print correct statements.
    if valid == 0:
        print("\nPlease select between option 1, 2 or 3.")
