# Solution to the challenge found at:
# http://www.reddit.com/r/dailyprogrammer/comments/2f6a7b/9012014_challenge_178_easy_transformers_matrices/

import math
import sys

def translate(cords, moveby):
    x, y = cords[0], cords[1]
    a, b = moveby[0], moveby[1]
    return (x + a, y + b)


def rotate(cords, around, angle):
    x, y = cords[0], cords[1]
    a, b = around[0], around[1]
    return (math.cos(angle)*(x-a) - math.sin(angle)*(y-b) + a,
            math.sin(angle)*(x-a) + math.cos(angle)*(y-b) + b)


def scale(cords, point, magnitude):
    x, y = cords[0], cords[1]
    a, b = point[0], point[1]
    return ((x - a) * magnitude + a,
            (y - b) * magnitude + b)


def reflect(cords, axis):
    x, y = cords[0], cords[1]
    if axis == 'x' or axis == 'X':
        return (x, -1 * y)
    elif axis == 'y' or axis == 'Y':
        return (-1 * x, y)
    else:
        return (x, y)


def parseArgs(command):
    args = command[command.index('(') + 1:len(command) - 1]
    point_a = float(args[:args.index(',')])
    args = args[args.index(' ') + 1:]
    point_b = float(args[:args.index(',')])
    value = float(args[args.index(' ') + 1:])
    return (point_a, point_b), value


def main():
    x = raw_input('Enter x co-ordinate: ')
    y = raw_input('Enter y co-ordinate: ')
    cords = (float(x), float(y))
    while True:
        print "Current State: (%r, %r)" % (round(cords[0], 2), round(cords[1], 2))
        command = raw_input('Enter command: ').lower()
        if 'translate' in command:
            moveby = (float(command[command.index('(')+1:command.index(',')]),
                      float(command[command.index(' ')+1:command.index(')')]))
            cords = translate(cords, moveby)

        elif 'scale' in command:
            point, magnitude = parseArgs(command)
            cords = scale(cords, point, magnitude)

        elif 'rotate' in command:
            around, angle = parseArgs(command)
            cords = rotate(cords, around, angle)

        elif 'reflect' in command:
            axis = command[command.index('(') + 1 : len(command) - 1]
            cords = reflect(cords, axis)

        else:
            print "Final point is: (%r, %r)" % (round(cords[0], 2), round(cords[1], 2))
            sys.exit(0)


if __name__ == '__main__':
    main()
