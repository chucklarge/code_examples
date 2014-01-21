import svgwrite
from svgwrite import cm, mm
width = 1280
height = 720
#width = width/2
#height = height/2

def basic_shapes(name):
    dwg = svgwrite.Drawing(filename=name, size=(width, height), color='black', debug=True)
    dwg.add(dwg.rect((0, 0), (width, height), fill='black'))
    for r in range(0, 20):
      dwg.add(dwg.circle((width*.75, height/2), r*4+4, fill_opacity=0, stroke='lawngreen', stroke_width=2))

    for r in range(0, 20):
      dwg.add(dwg.circle((width*.75-100, height/2), r*4+4, fill_opacity=0, stroke='lawngreen', stroke_width=2))
    dwg.save()


if __name__ == '__main__':
    basic_shapes('circle.svg')
