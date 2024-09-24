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


# Function to plot user neutrophil count against the average range
def plot_neutrophil(user_neutrophil):
    plt.figure(figsize=(6, 5))
    plt.ylim(0, 15)

    # Normal neutrophil range (2-7 x10^9/L)
    normal_lower_bound = 2
    normal_upper_bound = 7

    # Plot normal neutrophil range as bars
    plt.bar(0, normal_upper_bound, color='lightcoral',
            label=f'Normal Neutrophil Range ({normal_lower_bound} - {normal_upper_bound}) x10^9/L')
    plt.bar(0, normal_lower_bound, color='white', edgecolor='lightcoral', hatch='//')

    # Extend bars above the normal range for visual contrast
    plt.bar(0, 15 - normal_upper_bound, bottom=normal_upper_bound, color='white', edgecolor='lightcoral', hatch='//')

    # Plot the user's neutrophil count as a point
    plt.scatter(x=0, y=user_neutrophil, color='blue', marker='o',
                label=f"User Neutrophil Count: {user_neutrophil} x10^9/L")

    # Remove x-axis labels as we only have one bar
    plt.xticks([])
    plt.ylabel('Neutrophil Count (x10^9/L)')
    plt.title('User Neutrophil Count vs. Normal Range')

    # Center the legend and make it slightly smaller
    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.2), fontsize='small')
    plt.tight_layout()
    plt.show()


# Function to assess the user's neutrophil count
def assess_neutrophil(user_neutrophil):
    normal_lower_bound = 2
    normal_upper_bound = 7

    if user_neutrophil < normal_lower_bound:
        below_average = round(normal_lower_bound - user_neutrophil, 2)
        print(f"Neutrophil count is below normal by {below_average} x10^9/L. This could indicate neutropenia.")
    elif user_neutrophil > normal_upper_bound:
        above_average = round(user_neutrophil - normal_upper_bound, 2)
        print(f"Neutrophil count is above normal by {above_average} x10^9/L. This could indicate neutrophilia.")
    else:
        print("Neutrophil count is within the normal range.")


# Main function to handle input and processing
def main():
    user_neutrophil = get_valid_input("Enter neutrophil count (x10^9/L): ")

    # Plot the neutrophil count comparison
    plot_neutrophil(user_neutrophil)

    # Assess the user's neutrophil count against the normal range
    assess_neutrophil(user_neutrophil)


if __name__ == "__main__":
    main()
