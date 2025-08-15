from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


def get_available_agent():

    """
    This function filters the Users who are agents and fetches the best available agent. i.e. Agent
    with the least number of assigned tickets
    """

    agents = User.objects.filter(is_agent=True)

    # The snippet below adds an extra column to the User query and orders them in ascending order
    # i.e. the agent with the least number of assigned tickets will be first in the query set
    agents = agents.annotate(number_of_tickets=Count('assigned_tickets')).order_by('number_of_tickets')

    best_available_agent = agents.first()  # agent with the least number of tickets | first on the query

    if best_available_agent is None:
        raise Exception("Unable to assign agent!")

    return best_available_agent
