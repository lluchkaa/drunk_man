from turtle import Turtle, done
from random import uniform
from math import degrees, pi, radians
from argparse import ArgumentParser

from typings import Args
from drunk_man import DrunkMan

turtle = Turtle()


def get_args() -> Args:
    parser = ArgumentParser()

    parser.add_argument("-r", "--radius", help="Field radius", default=400)
    parser.add_argument("-s", "--step", help="Drunk man step", default=30)
    parser.add_argument(
        "-a",
        "--angle",
        help="Initial drunk man direction",
        default=uniform(0, pi * 2),
    )
    parser.add_argument("-p", "--promile", help="Man drunkness", default=0.33)

    return parser.parse_args()


def draw_circle(radius: float):
    turtle.up()
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.home()
    turtle.goto(0, -radius)
    turtle.down()
    turtle.circle(radius)
    turtle.up()
    turtle.color(0, 0, 0)
    turtle.home()


def main():
    args = get_args()

    angle = float(args.angle)

    radius = float(args.radius)
    turtle.lt(angle)
    man = DrunkMan(
        step=float(args.step),
        direction=radians(angle),
        promile=float(args.promile),
    )

    draw_circle(radius)

    turtle.down()
    turtle.speed(1)

    while man.position.r < radius:
        man.go()
        new_angle = degrees(man.direction)
        turtle.lt(angle - new_angle)
        turtle.fd(man.step)
        angle = new_angle

    print(repr(man.position))


if __name__ == "__main__":
    main()
    done()
