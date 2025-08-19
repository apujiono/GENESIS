def get_prompt(data):
    user_id = data.get('userId', 'user1')
    return f"Track finances for {user_id}. Provide budget insights and VIRAI transaction history."
