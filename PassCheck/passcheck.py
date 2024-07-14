import re
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def password_strength(password):
    length = len(password)
    complexity = 0
    suggestions = []
    
    if length >= 8:
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Make your password at least 8 characters long.")

    if re.search(r"[a-z]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one uppercase letter.")

    if re.search(r"\d", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        complexity += 1
    else:
        suggestions.append("🔸 " + Fore.YELLOW + "Include at least one special character (e.g., !, @, #, $, etc.).")

    if re.search(r"(.)\1{2,}", password):
        complexity -= 1
        suggestions.append("🔸 " + Fore.YELLOW + "Avoid sequences of the same character (e.g., 'aaa').")

    if complexity == 0:
        strength = "Very Weak"
        color = Fore.RED
        emoji = "🔴"
    elif complexity == 1:
        strength = "Weak"
        color = Fore.RED
        emoji = "🟠"
    elif complexity == 2:
        strength = "Moderate"
        color = Fore.YELLOW
        emoji = "🟡"
    elif complexity == 3:
        strength = "Strong"
        color = Fore.GREEN
        emoji = "🟢"
    elif complexity == 4:
        strength = "Very Strong"
        color = Fore.GREEN
        emoji = "🟢"
    else:
        strength = "Excellent"
        color = Fore.CYAN
        emoji = "🔵"
    
    return f"{color}Password Strength: {strength} {emoji}", suggestions

def main():
    tool_name = "PassCheck"
    ascii_art = pyfiglet.figlet_format(tool_name, font="drpepper")
    colored_ascii = f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}"
    print(colored_ascii)

    linkedin_saikat = "https://www.linkedin.com/in/0xsaikat/"
    linkedin_bms = "https://www.linkedin.com/company/brainwave-matrix-solutions"
    
    link_saikat = f"\033]8;;{linkedin_saikat}\033\\@0xSaikat\033]8;;\033\\"
    link_bms = f"\033]8;;{linkedin_bms}\033\\Brainwave Matrix Solutions\033]8;;\033\\"
    
    print(f"{Fore.RED}V-1.0\n")
    print(f"{Fore.GREEN}Created by {Style.BRIGHT}{link_saikat}{Style.RESET_ALL}{Fore.GREEN} during an internship at {Style.BRIGHT}{link_bms}{Style.RESET_ALL}{Fore.GREEN}.\n")
    
    while True:
        user_password = input(Fore.GREEN + "🔑 Enter your password to check its strength (or press 'q' to quit): " + Style.RESET_ALL)
        
        if user_password.lower() == 'q':
            print(Fore.CYAN + "Goodbye! 👋")
            break
        
        print()  
        
        strength, suggestions = password_strength(user_password)
        print(strength + "\n")  
        
        if suggestions:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(suggestion)
        else:
            print(Fore.GREEN + "✅ Your password is strong enough.")
        
        print()  

if __name__ == "__main__":
    main()




