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

# Function to plot user temperature against the average range
def plot_temperature(user_temp):
    plt.figure(figsize=(6, 5))
    plt.ylim(30, 40)

    # Average temperature bounds
    avg_lower_bound = 36.1
    avg_upper_bound = 37.2

    # Plot average temperature range as bars
    plt.bar(0, avg_upper_bound, color='lightgreen', label=f'Avg Temperature Range ({avg_lower_bound}°C - {avg_upper_bound}°C)')
    plt.bar(0, avg_lower_bound, color='white', edgecolor='lightgreen', hatch='//')

    # Extend bars above the average upper bound for visual contrast
    plt.bar(0, 40 - avg_upper_bound, bottom=avg_upper_bound, color='white', edgecolor='lightgreen', hatch='//')

    # Plot the user's temperature as a point
    plt.scatter(x=0, y=user_temp, color='blue', marker='o', label=f"User Temperature: {user_temp}°C")

    # Remove x-axis labels as we only have one bar
    plt.xticks([])
    plt.ylabel('Temperature in degrees Celsius')
    plt.title('User Temperature vs. Global Average')

    # Center the legend and make it slightly smaller
    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.2), fontsize='medium')
    plt.tight_layout()
    plt.show()

# Function to assess the user's temperature
def assess_temperature(user_temp):
    if user_temp < 36.1:
        below_average = round(36.1 - user_temp, 2)
        print(f"Body temperature is below average by {below_average}°C. Decreased temperature could be a response to sepsis.")
    elif user_temp > 37.2:
        above_average = round(user_temp - 37.2, 2)
        print(f"Body temperature is above average by {above_average}°C. Increased temperature could be a response to sepsis.")
    else:
        print("Body temperature is within the normal range.")

# Main function to handle input and processing
def main():
    user_temp = get_valid_input("Enter body temperature in degrees Celsius: ")

    # Plot the temperature comparison
    plot_temperature(user_temp)

    # Assess the user's temperature against the normal range
    assess_temperature(user_temp)

if __name__ == "__main__":
    main()

