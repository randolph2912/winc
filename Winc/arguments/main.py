# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

def greet(name, greeting_template='Hello, <name>!'):
    return  greeting_template.replace('<name>', name)
 
    

def force(mass, body='earth'):
    celestial_bodies = {
        'mercury': 3.7,
        'venus': 8.87,
        'earth': 9.798,
        'mars': 3.71,
        'jupiter': 24.79,
        'saturn': 10.44,
        'uranus': 8.87,
        'neptune': 11.15,
        'pluto': 0.58,
        'sun': 274.0,
        'moon': 1.62
    }
    gravity = celestial_bodies.get(body.lower(), 9.8)
    gravity = round(gravity, 1)
    force = mass * gravity
    return force


def pull(m1, m2, d):
    G = 6.674e-11
    F = G * (m1 * m2) / (d**2)
    return F





























