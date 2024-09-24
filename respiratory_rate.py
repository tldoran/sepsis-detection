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

# Function to plot user respiratory rate against the average range
def plot_respiratory_rate(user_resp_rate):
    plt.figure(figsize=(6, 5))
    plt.ylim(10, 30)

    # Average range for respiratory rate (12-20 breaths/min)
    avg_lower_bound = 12
    avg_upper_bound = 20

    # Plot lower and upper bounds as bars
    plt.bar(0, avg_upper_bound, color='lightgreen', label=f'Avg Respiratory Rate Range ({avg_lower_bound}-{avg_upper_bound} breaths/min)')
    plt.bar(0, avg_lower_bound, color='white', edgecolor='lightgreen', hatch='//')

    # Extend bars above the average upper bound (for visual contrast)
    plt.bar(0, 30-avg_upper_bound, bottom=avg_upper_bound, color='white', edgecolor='lightgreen', hatch='//')

    # Plot the user's respiratory rate as a point
    plt.scatter(x=0, y=user_resp_rate, color='blue', marker='o', label=f"User Respiratory Rate: {user_resp_rate} breaths/min")

    # No x-axis labels since we only have one bar
    plt.xticks([])
    plt.ylabel('Respiratory Rate (breaths per minute)')
    plt.title('User Respiratory Rate vs. Global Average')

    # Center the legend and make it slightly smaller
    plt.legend(loc='center', bbox_to_anchor=(0.5, -0.2), fontsize='small')
    plt.tight_layout()
    plt.show()

# Function to assess the user's respiratory rate
def assess_respiratory_rate(user_resp_rate):
    if user_resp_rate < 12:
        below_average = round(12 - user_resp_rate, 2)
        print(f"Respiratory rate is below the average by {below_average} breaths/min. This could be abnormal. Sepsis tends to increase respiratory rate.")
    elif user_resp_rate > 20:
        above_average = round(user_resp_rate - 20, 2)
        print(f"Respiratory rate is above the average by {above_average} breaths/min. Increased breathing rate could be a response to sepsis.")
    else:
        print("Respiratory rate is within the normal range (12-20 breaths/min).")

# Main function to handle input and processing
def main():
    user_resp_rate = get_valid_input("Enter respiratory rate in breaths per minute: ")

    # Plot the respiratory rate comparison
    plot_respiratory_rate(user_resp_rate)

    # Assess the user's respiratory rate against the normal range
    assess_respiratory_rate(user_resp_rate)

if __name__ == "__main__":
    main()
