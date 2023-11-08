import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Directory containing your CSV files
csv_directory = "r:/Cambuhy/BS0/00"

for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        # Load the CSV data into a DataFrame
        csv_file_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(csv_file_path)

        # Select the first and second columns of the DataFrame
        x = df.iloc[:, 0]  # First column
        y = df.iloc[:, 1]  # Second column
        print(df.iloc[0, 0])
        print(df.iloc[0, 1])

        # Create a scatterplot using Seaborn
        sns.set(style='whitegrid')  # Customize the plot style if needed
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
        # # https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
        # sns.scatterplot(x=x, y=y, marker='.')
        # Use plt.plot() to create a continuous line plot
        plt.plot(x, y)  # You can add a label if needed
        # plt.plot(x, y/65535.0)  # You can add a label if needed
        plt.title(os.path.splitext(filename)[0])
        plt.xlabel('Wavelength [nm]')
        plt.ylabel('Intensity [16bits_65535.0]')

        # Customize the plot appearance using Seaborn functions
        # Adjust the plot's limits to ensure the first data point is visible
        # plt.xlim(x.min(), x.max())
        plt.ylim(0, 65535.0)
        # plt.ylim(0, 1)

        # Save the plot as a PNG file with the same name as the CSV file
        plot_filename = os.path.splitext(filename)[0] + '.png'
        plot_filepath = os.path.join(csv_directory, plot_filename)
        plt.savefig(plot_filepath, dpi=300)  # You can adjust the DPI as needed
        plt.close()  # Close the plot to avoid overlapping plots

print("Plots generated and saved as PNG files.")

###############################################################################################################

# for filename in os.listdir(csv_directory):
#     if filename.endswith('.csv'):
#         # Load the CSV data into a DataFrame
#         csv_file_path = os.path.join(csv_directory, filename)
#         df = pd.read_csv(csv_file_path)

#         # Select the first and second columns of the DataFrame
#         x = df.iloc[:, 0]  # First column
#         y = df.iloc[:, 1]  # Second column

#         # Create a line plot using Seaborn
#         sns.set(style='whitegrid')  # Customize the plot style if needed
#         plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
#         # Use plt.plot() to create a continuous line plot
#         plt.plot(x, y, label=filename)  # You can add a label if needed

#         # Customize the plot appearance using Seaborn functions or other plt functions

#         # Save the plot as a PNG file with the same name as the CSV file
#         plot_filename = os.path.splitext(filename)[0] + '.png'
#         plot_filepath = os.path.join(csv_directory, plot_filename)
#         plt.savefig(plot_filepath, dpi=300)  # You can adjust the DPI as needed
#         plt.close()  # Close the plot to avoid overlapping plots

# print("Plots generated and saved as PNG files.")



# ###############################################################################################################
# for filename in os.listdir(csv_directory):
#     if filename.endswith('.csv'):
#         # Load the CSV data into a DataFrame
#         csv_file_path = os.path.join(csv_directory, filename)
#         df = pd.read_csv(csv_file_path)

#         # Select the first and second columns of the DataFrame
#         x = df.iloc[:, 0]  # First column
#         y = df.iloc[:, 1]  # Second column

#         # Create a scatterplot using Seaborn
#         sns.set(style='whitegrid')  # Customize the plot style if needed
#         plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

#         # Create a scatterplot manually, add x and y labels
#         plt.scatter(x, y, marker='.')
#         plt.xlabel('X Label')  # Replace 'X Label' with your desired X-axis label
#         plt.ylabel('Y Label')  # Replace 'Y Label' with your desired Y-axis label

#         # Add the first x, y row to the plot
#         # plt.text(x.iloc[0], y.iloc[0], f'({x.iloc[0]:.2f}, {y.iloc[0]:.2f})', fontsize=12, ha='right')

#         # Adjust the plot's limits to ensure the first data point is visible
#         # plt.xlim(x.min(), x.max())
#         # plt.ylim(y.min(), y.max())

#         # Save the plot as a PNG file with the same name as the CSV file
#         plot_filename = os.path.splitext(filename)[0] + '.png'
#         plot_filepath = os.path.join(csv_directory, plot_filename)
#         plt.savefig(plot_filepath, dpi=300)  # You can adjust the DPI as needed
#         plt.close()  # Close the plot to avoid overlapping plots

# print("Plots generated and saved as PNG files.")