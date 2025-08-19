def get_prompt(data):
    user_id = data.get('userId', 'user1')
    return f"Motivate {user_id} with a witty, crypto-themed pep talk! Example: 'Yo, bro, keep mining that VIRAI, cuan awaits!'"
