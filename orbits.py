from turtle import Turtle, Screen


planets = { "earth" : {"color" : "blue", "diameter":1.0,"orbit":300,"speed":7},
            "mercury":{"color":"gray","diameter":0.9,"orbit":250,"speed":9},
            "venus":{"color":"yellow","diameter":0.5,"orbit":200,"speed":12},
            "sun":{"color":"orange","diameter":5,"orbit":0,"speed":0}}

def solar_System(planets):
    for i in planets:
        dict = planets[i]
        turtle = Turtle(shape="circle") # we set the shape of objects as circles
        # attributes of the planet will be obtained through the dict(planets).
        turtle.speed("fastest")
        turtle.shapesize(dict["diameter"])
        turtle.color(dict["color"])
        turtle.pu()  # .pu() = pen up when drawing the orbit.
        turtle.sety(-dict["orbit"])
        turtle.pd()  # .pd() = pen down when the orbit it's done.

        dict["turtle"] = turtle

    sc.ontimer(rotation,1) # calls function rotation , that contains : orbit + speed , with speed of 1 = fast
    sc.bgcolor("black")
    # sc = scrreen
def rotation():
    for i in planets:
        dict=planets[i]
        dict["turtle"].circle(dict["orbit"],dict["speed"]) # .circle orbits should move in a circle

    sc.ontimer(rotation,1)

sc = Screen()
solar_System(planets)
sc.exitonclick()
