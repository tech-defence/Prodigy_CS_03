import re

# ANSI escape codes for colors
class Colors:
    GREEN = "\033[92m"  # Green
    YELLOW = "\033[93m"  # Yellow
    RED = "\033[91m"     # Red
    RESET = "\033[0m"    # Reset to default color

def check_password_strength(password):
    # Password strength criteria
    strength = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special_char': bool(re.search(r'[@$!%*#?&]', password))
    }

    # Calculate password strength score
    score = sum(strength.values())

    # Provide feedback based on score
    if score == 5:
        feedback = f"\n{Colors.GREEN}🎉 *** STRONG PASSWORD! *** 🎉{Colors.RESET}\n\n"
    elif 3 <= score < 5:
        feedback = f"\n{Colors.YELLOW}⚠️ *** MODERATE PASSWORD *** ⚠️{Colors.RESET}\nConsider adding more character variety."
    else:
        feedback = f"\n{Colors.RED}🚫 *** WEAK PASSWORD *** 🚫{Colors.RESET}\n\n" + \
                   "*** Suggestions to make your password stronger ***\n\n" + \
                   "1. Make sure your password is at least 8 characters long.\n" + \
                   "2. Include uppercase and lowercase letters.\n" + \
                   "3. Add digits and special characters (e.g., @, $, %, &).\n\n\n"

    return feedback

# ASCII header
def print_header():
    print(f"""{Colors.GREEN}
 _____                                                    _____ 
( ___ )                                                  ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   | ╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╔═╗┌┬┐┬─┐┌─┐┌┐┌┌─┐┌┬┐┬ ┬ |   | 
 |   | ╠═╝├─┤└─┐└─┐││││ │├┬┘ ││  ╚═╗ │ ├┬┘├┤ ││││ ┬ │ ├─┤ |   | 
 |   | ╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  ╚═╝ ┴ ┴└─└─┘┘└┘└─┘ ┴ ┴ ┴ |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                  (_____) ---BY tech-defence
{Colors.RESET}""")

# Print ASCII header
print_header()

# Test the function
password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
