import requests
import datetime

class Pixela():
    """
    Class to use Pixela API
    https://pixe.la/
    """
    def __init__(self, user, token):
        self.graph = None
        self.user = user
        self.token = token
        self.url = 'https://pixe.la/v1'
        self.header = {'X-USER-TOKEN': self.token}
        self.today = self.get_today()

    def get_today(self):
        """
        Grab today as a string in yyyyMMdd format
        """
        today = datetime.datetime.today()
        return today.strftime('%Y%m%d')

    def create_graph(self, graph_name, graph_unit='hours', graph_type='float', graph_color='kuro'):
        """
        Given a user, graph name and graph data
        Create a graph in Pixela
        """
        self.graph = graph_name

        url = f'{self.url}/users/{self.user}/graphs'

        body = {
            'id': self.graph.lower(),
            'name': self.graph,
            'unit': graph_unit,
            'type': graph_type,
            'color': graph_color,
        }

        response = requests.post(url, json=body, headers=self.header)
        if response.status_code == 200:
            return True

    def delete_graph(self, graph_id=None):
        """
        Given a graph ID
        Delete that graph
        """
        if graph_id == None:
            graph_id = self.graph.lower()
        url = f'{self.url}/users/{self.user}/graphs/{graph_id}'
        response = requests.delete(url, headers=self.header)
        print(response.text)
        if response.status_code == 200:
            return True

    def post_pixel(self, quantity, date=None):
        """
        Given a quantity of units
        Post a that quantity of pixels to the graph
        """
        if date == None:
            date = self.today

        url = f'{self.url}/users/{self.user}/graphs/{self.graph.lower()}'

        body = {
            'date': date,
            'quantity': quantity,
        }

        response = requests.post(url, headers=self.header, json=body)
        if response.status_code == 200:
            return True

    def update_pixel(self, date, quantity):
        """
        Given a date in yyyyMMdd format and a quantity
        Update that date's pixel for that many quantities
        """
        url = f'{self.url}/users/{self.user}/graphs/{self.graph.lower()}/{date}'

        body = {
            'quantity': quantity,
        }
        response = requests.put(url, headers=self.header, json=body)
        if response.status_code == 200:
            return True

    def delete_pixel(self, date):
        """
        Given a date
        Delete the pixel from that date
        """
        if date == None:
            date = self.today
            
        url = f'{self.url}/users/{self.user}/graphs/{self.graph.lower()}/{date}'
        response = requests.delete(url, headers=self.header)
        if response.status_code == 200:
            return True
