import random

input("Press enter to generate username")

def generate_username():
    regularwords = ['Ninja', 'alpha', 'Master', 'shadow', 'Caption', 'storm', 'Ghost', 'skeleton', 'Blaze', 'thunder', 'Star', 'galaxy', 'Angel', 'infinity', 'Binary', 'nebula']
    coolwords = ['Wizard', 'sorcerer', 'Knight', 'observer', 'Explorer', 'gamer', 'Mystic', 'radiant', 'Vibrant', 'cosmic', 'Dynamic', 'resolute', 'Plague', 'vortex', 'Quantum', 'pulse', 'Spectre', 'strike', 'Eclipse', 'starlight', 'Velocity', 'cipher', 'Solar', 'flare', 'Rift', 'nova', 'Cyber', 'celestial', 'Catalyst', 'ember', 'Apex', 'fusion', 'Vertex']

    numbers = random.randint(1000, 9999)
    
    regularwords = random.choice(regularwords)
    coolwords = random.choice(coolwords)
    
    username = f'{regularwords}{coolwords}{numbers}'
    return username

if __name__ == "__main__":
    username = generate_username()
    print(f'Generated Username: {username}')

input("Press enter to exit")