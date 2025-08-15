from django.contrib.auth import get_user_model

User = get_user_model()


def get_available_agent():
    """
    This function iterates through the User objects and returns the agent with the fewest number of assigned tickets.
    """

    agents = User.objects.filter(is_agent=True)

    best_available_agent = None  # To store the first agent who has the fewest assigned tickets
    max_assigned_tickets = 0

    for agent in agents:
        if agent.assigned_tickets.count() < max_assigned_tickets:
            max_assigned_tickets = agent.assigned_tickets.count()
            best_available_agent = agent

    return best_available_agent
