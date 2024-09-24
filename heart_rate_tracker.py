import matplotlib.pyplot as plt

# Function to check if the input is a float
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Function to get a valid numerical input (either heart rate or age)
def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if is_float(value):
            return float(value)
        else:
            print("Please enter a valid number.")

# Function to get a valid gender input
def get_valid_gender():
    while True:
        gender = input("Type 'm' for male, or 'f' for female: ").strip().upper()
        if gender in ['M', 'MALE', 'F', 'FEMALE']:
            return gender
        else:
            print("Invalid input. Please enter 'm' or 'f'.")

# Function to plot the heart rate comparison
def plot_heart_rate(user_heart_rate, age_range, lower_bound, upper_bound, gender):
    plt.figure(figsize=(6, 5))
    plt.ylim(40, 120)

    # Plot lower and upper bounds as bars
    plt.bar(0, upper_bound, color='lightgreen', label=f'Avg Heart Rate Range ({lower_bound}-{upper_bound} bpm)')
    plt.bar(0, lower_bound, color='white', edgecolor='lightgreen', hatch='//')

    # Extend bars above the average upper bound
    plt.bar(0, 120-upper_bound, bottom=upper_bound, color='white', edgecolor='lightgreen', hatch='//')

    # Plot the user's heart rate
    plt.scatter(x=0, y=user_heart_rate, color='blue', marker='o', label=f"User Heart Rate: {user_heart_rate} bpm")

    plt.xticks([])  # Remove x-axis ticks since we're plotting only one bar
    plt.ylabel('Resting Heart Rate (bpm)')
    plt.title(f'User Heart Rate vs. Global Average ({gender.capitalize()}, Ages {age_range[0]} - {age_range[1]})')

    # Center the legend and make it slightly smaller
    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.2), fontsize='small')
    plt.tight_layout()
    plt.show()

# Function to assess heart rate
def assess_heart_rate(user_heart_rate, lower_bound, upper_bound):
    if user_heart_rate < lower_bound:
        print(f"Resting heart rate is below the average by {round(lower_bound - user_heart_rate, 2)} bpm. Decreased heart rate could be a response to sepsis.")
    elif user_heart_rate > upper_bound:
        print(f"Resting heart rate is above the average by {round(user_heart_rate - upper_bound, 2)} bpm. This could be abnormal. Sepsis often results in increased heart rate.")
    else:
        print("Resting heart rate is within the average range.")

# Main function to handle the logic
def main():
    user_heart_rate = get_valid_input("Enter user resting heart rate (bpm): ")
    user_age = get_valid_input("Enter user age: ")
    user_gender = get_valid_gender()

    # Check if age is within the allowed range
    if user_age < 18 or user_age > 89:
        print("Sorry, this tool only works for ages between 18 and 89.")
        return

    # Define ranges for males and females
    gender = 'male' if user_gender in ['M', 'MALE'] else 'female'

    age_brackets = {
        (18, 39): {'male': (47, 75), 'female': (52, 81)},
        (40, 59): {'male': (46, 76), 'female': (51, 78)},
        (60, 89): {'male': (45, 75), 'female': (52, 77)}
    }

    # Determine age bracket and get corresponding heart rate bounds
    for age_range, heart_rate_data in age_brackets.items():
        if age_range[0] <= user_age <= age_range[1]:
            lower_bound, upper_bound = heart_rate_data[gender]
            plot_heart_rate(user_heart_rate, age_range, lower_bound, upper_bound, gender)
            assess_heart_rate(user_heart_rate, lower_bound, upper_bound)
            break

if __name__ == "__main__":
    main()

