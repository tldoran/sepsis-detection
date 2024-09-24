import matplotlib.pyplot as plt

# Global average blood pressure data with upper and lower bounds
global_bp_averages = {
    'male': {
        '18-39': {'systolic': (115, 123), 'diastolic': (76, 82)},  # (lower, upper) bounds
        '40-59': {'systolic': (120, 128), 'diastolic': (79, 83)},
        '60+': {'systolic': (130, 140), 'diastolic': (82, 88)}
    },
    'female': {
        '18-39': {'systolic': (108, 112), 'diastolic': (75, 79)},
        '40-59': {'systolic': (118, 126), 'diastolic': (78, 82)},
        '60+': {'systolic': (130, 138), 'diastolic': (82, 86)}
    }
}


# Function to check if the input is a valid float
def is_float(value):
    try:
        return float(value)
    except ValueError:
        return None


# Function to get a valid input from the user
def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        value = is_float(user_input)
        if value is not None:
            return value
        else:
            print("Invalid input. Please enter a valid number.")


# Function to get a valid gender input
def get_gender():
    while True:
        gender = input("Enter your gender (male/female or m/f): ").lower()
        if gender in ['male', 'm']:
            return 'male'
        elif gender in ['female', 'f']:
            return 'female'
        else:
            print("Invalid input. Please enter 'male', 'female', 'm', or 'f'.")


# Function to get a valid age group
def get_age_group():
    while True:
        age = get_valid_input("Enter your age: ")
        if age < 18:
            print("This tool is for users aged 18 or above.")
        elif 18 <= age <= 39:
            return '18-39'
        elif 40 <= age <= 59:
            return '40-59'
        else:
            return '60+'


# Function to plot user blood pressure against the demographic average with bounds
def plot_blood_pressure(user_systolic, user_diastolic, avg_systolic_bounds, avg_diastolic_bounds, gender, age_group):
    plt.ylim(40, 200)

    systolic_lower, systolic_upper = avg_systolic_bounds
    diastolic_lower, diastolic_upper = avg_diastolic_bounds

    # Plot systolic and diastolic lower bound bars
    plt.bar(0, systolic_upper, color='lightgreen', label=f'Avg Systolic Range ({systolic_lower}-{systolic_upper} mmHg)')
    plt.bar(0, systolic_lower, color='white', edgecolor='lightgreen', hatch='//')

    plt.bar(1, diastolic_upper, color='lightblue',
            label=f'Avg Diastolic Range ({diastolic_lower}-{diastolic_upper} mmHg)')
    plt.bar(1, diastolic_lower, color='white', edgecolor='lightblue', hatch='//')

    # Add bars extending above the average range
    plt.bar(0, 200 - systolic_upper, bottom=systolic_upper, color='white', edgecolor='lightgreen', hatch='//')
    plt.bar(1, 200 - diastolic_upper, bottom=diastolic_upper, color='white', edgecolor='lightblue', hatch='//')

    # Add user blood pressure values
    plt.scatter(x=0, y=user_systolic, color='red', marker='o', label=f"User Systolic: {user_systolic} mmHg")
    plt.scatter(x=1, y=user_diastolic, color='blue', marker='o', label=f"User Diastolic: {user_diastolic} mmHg")

    plt.xticks([0, 1], ["Systolic", "Diastolic"])
    plt.ylabel('Blood Pressure (mmHg)')
    plt.title(f'User Blood Pressure vs. Global Average ({gender.capitalize()}, {age_group})')

    # Center the legend and make it slightly smaller
    plt.legend(loc="best", fontsize='medium')

    plt.show()


# Function to assess the user's blood pressure
def assess_blood_pressure(user_systolic, user_diastolic, systolic_bounds, diastolic_bounds):
    systolic_lower, systolic_upper = systolic_bounds
    diastolic_lower, diastolic_upper = diastolic_bounds

    if user_systolic < systolic_lower and user_diastolic < diastolic_lower:
        print(f"Your blood pressure is below the average range for your demographic group.\nDecreased blood pressure could be a response to sepsis")
    elif user_systolic > systolic_upper or user_diastolic > diastolic_upper:
        print(f"Your blood pressure is above the average range for your demographic group.\nThis could be abnormal sepsis often results in decreased blood pressure.")
    else:
        print(f"Your blood pressure is within the average range for your demographic group.")


# Main function to handle input and processing
def main():
    print("Enter your details to compare your blood pressure with global averages:")

    # Get user's gender, age group, and blood pressure readings
    gender = get_gender()
    age_group = get_age_group()

    user_systolic = get_valid_input("Systolic pressure (mmHg): ")
    user_diastolic = get_valid_input("Diastolic pressure (mmHg): ")

    # Retrieve average systolic and diastolic bounds for the user's demographic
    avg_systolic_bounds = global_bp_averages[gender][age_group]['systolic']
    avg_diastolic_bounds = global_bp_averages[gender][age_group]['diastolic']

    # Plot the blood pressure comparison with upper and lower bounds
    plot_blood_pressure(user_systolic, user_diastolic, avg_systolic_bounds, avg_diastolic_bounds, gender, age_group)

    # Assess the user's blood pressure against the demographic-specific average bounds
    assess_blood_pressure(user_systolic, user_diastolic, avg_systolic_bounds, avg_diastolic_bounds)


if __name__ == "__main__":
    main()

