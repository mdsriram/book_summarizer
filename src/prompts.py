system_message ='''
You are an AI assistant designed to help users create engaging and well-structured fantasy novels. Your task is to guide the user through the process of developing their book, from brainstorming ideas to outlining chapters and refining the final draft. You will provide suggestions, answer questions, and offer feedback on the user’s work. Your responses should be clear, concise, and encouraging, helping the user stay motivated and focused on their writing goals.'''

def generate_prompt(book, title):
    prompt = f"""
    **Book:** {book}
    **Title:** {title}

    **Genre:** Fantasy

    **Prompt:**
    In a world where magic is real but hidden from the everyday eye, a young protagonist discovers a mysterious artifact that unlocks their latent magical abilities. As they embark on a journey to uncover the secrets of their newfound powers, they encounter a diverse cast of characters, each with their own unique abilities and stories. Along the way, they must navigate treacherous landscapes, solve ancient puzzles, and confront a looming threat that could change their world forever.

    **Key Elements to Include:**
    1. **Protagonist:** A relatable and dynamic main character who grows throughout the story.
    2. **Setting:** A richly detailed world with its own rules of magic and history.
    3. **Supporting Characters:** Allies and adversaries who add depth and complexity to the narrative.
    4. **Conflict:** Both internal (protagonist’s personal struggles) and external (the main threat or antagonist).
    5. **Resolution:** A satisfying conclusion that ties up major plot points while leaving room for future adventures.
    """
    return prompt

# Example usage
#book = "The Enchanted Realm"
#title = "The Journey of Discovery"
#print(generate_prompt(book, title))
