from turtle import color
from utils.tools import generate_rgb, make_dots

def main():
    colors = generate_rgb('image.jpg', 20)
    make_dots(10, 10, colors)

if __name__ == '__main__':
    main()