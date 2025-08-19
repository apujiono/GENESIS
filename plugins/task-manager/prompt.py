def get_prompt(data):
    user_id = data.get('userId', 'user1')
    return f"Manage tasks for {user_id}. Prioritize based on deadlines and importance."
