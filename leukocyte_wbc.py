import matplotlib.pyplot as plt


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


# Function to plot user leukocyte count against the average range
def plot_leukocyte(user_leukocyte):
    plt.figure(figsize=(6, 5))
    plt.ylim(0, 20)

    # Normal leukocyte range (4-11 x10^9/L)
    normal_lower_bound = 4
    normal_upper_bound = 11

    # Plot normal leukocyte range as bars
    plt.bar(0, normal_upper_bound, color='lightblue',
            label=f'Normal Leukocyte Range ({normal_lower_bound} - {normal_upper_bound}) x10^9/L')
    plt.bar(0, normal_lower_bound, color='white', edgecolor='lightblue', hatch='//')

    # Extend bars above the normal range for visual contrast
    plt.bar(0, 20 - normal_upper_bound, bottom=normal_upper_bound, color='white', edgecolor='lightblue', hatch='//')

    # Plot the user's leukocyte count as a point
    plt.scatter(x=0, y=user_leukocyte, color='blue', marker='o',
                label=f"User Leukocyte Count: {user_leukocyte} x10^9/L")

    # Remove x-axis labels as we only have one bar
    plt.xticks([])
    plt.ylabel('Leukocyte Count (x10^9/L)')
    plt.title('User Leukocyte Count vs. Normal Range')

    # Center the legend and make it slightly smaller
    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.2), fontsize='small')
    plt.tight_layout()
    plt.show()


# Function to assess the user's leukocyte count
def assess_leukocyte(user_leukocyte):
    normal_lower_bound = 4
    normal_upper_bound = 11

    if user_leukocyte < normal_lower_bound:
        below_average = round(normal_lower_bound - user_leukocyte, 2)
        print(f"Leukocyte count is below normal by {below_average} x10^9/L. This could indicate leukopenia.")
    elif user_leukocyte > normal_upper_bound:
        above_average = round(user_leukocyte - normal_upper_bound, 2)
        print(f"Leukocyte count is above normal by {above_average} x10^9/L. This could indicate leukocytosis. Could be a result of sepsis infection.")
    else:
        print("Leukocyte count is within the normal range.")


# Main function to handle input and processing
def main():
    user_leukocyte = get_valid_input("Enter leukocyte count (x10^9/L): ")

    # Plot the leukocyte count comparison
    plot_leukocyte(user_leukocyte)

    # Assess the user's leukocyte count against the normal range
    assess_leukocyte(user_leukocyte)


if __name__ == "__main__":
    main()
