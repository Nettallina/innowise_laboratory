def generate_profile(age: int) -> str:
    if age >= 20:
        return "Adult"
    elif age >= 13 and age <= 19:
        return "Teenager"
    else:
        return "Child"

if __name__ == "__main__":
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_year = 2025
    current_age = current_year - birth_year
    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby.lower() == 'stop':
            break
        else:
            hobbies.append(hobby)
    life_stage = generate_profile(current_age)
    user_profile = {
        "Name": user_name,
        "Age": current_age,
        "Life Stage": life_stage,
        "Favorite Hobbies": hobbies
    }
    print("---")
    print("Profile Summary:")
    for key, value in user_profile.items():
        if key == "Favorite Hobbies":
            if not value:
                print("You didn't mention any hobbies.")
            else:
                print(f"{key} ({len(value)}):")
                for hobby in value:
                    print(f"- {hobby}")
        else:
            print(f"{key}: {value}")
    print("---")
