import requests

def generate_bool_questions(questions):
    """
    Given a number of questions
    Generate a list of True/False Quiz Questions from the Open Trivia Database
    Return a list of quiz information
    """
    url = 'https://opentdb.com/api.php'
    params = {'amount': questions, 'type': 'boolean'}

    r = requests.get(url, params)
    if r.status_code == 200:
        quiz_data = r.json()['results']
    else:
        r.raise_for_status()
    return quiz_data
