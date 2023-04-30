import random

def handle_response(message, author) -> str:
  p_message = message.lower()

  
  if p_message == 'hi' or p_message == 'hello':
    return "Hello {author}! What's up?"
  
...