import os
from utils.pixela import Pixela

def main():
    pix = Pixela(os.environ.get('PIXELA_USER'), os.environ.get('PIXELA_TOKEN'))
    if pix.create_graph('hoursGaming'):
        print('Graph created')
    else:
        raise Exception('Unable to create graph')
    
    ## Manual stuff to add quantities
    pix.post_pixel('1.25')


if __name__ == '__main__':
    main()
