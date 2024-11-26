# Plot Generator

## Overview

The **Plot Generator** is an interactive script designed to provide users with functionalities to:

1. Generate FTIR (Fourier-transform infrared spectroscopy) plots.
2. Use ImageJ for image processing, such as color changes and intensity readings.
3. Exit the program when finished.

The tool guides users through each step and provides an easy way to interactively work with image files and FTIR data.

## Features

- **Generate FTIR Plot**: Users can input FTIR data to generate a plot for visualization purposes.
- **ImageJ Integration**: Perform image processing, including color adjustments, intensity analysis, and other modifications.

## Requirements

To use this tool, you need the following packages installed in your Python environment:

```sh
pip install numpy pandas matplotlib opencv-python
```

The following Python packages are imported in the script:

- `pandas`: Data handling and manipulation.
- `numpy`: Numerical operations.
- `matplotlib`: Plotting FTIR data.
- `os`: File and directory operations.
- `sys`: System-specific parameters and functions.
- `cv2`: OpenCV library for image processing.

In addition, utility functions such as `get_user_input`, `get_directory`, and `get_filename` are used, which are defined in the `utils.py` file. Ensure that this file is available in the same directory as the script.

## How to Use

1. **Clone or Download the Repository**: First, clone or download the repository containing this script.
2. **Install Python**: If you do not have Python installed, download and install it from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to add Python to your system PATH during installation.
3. **Install Dependencies**: Install the required packages using the following command:

    ```sh
    pip install numpy pandas matplotlib opencv-python
    ```

4. **Run the Script**: To run the script, you first need to open a terminal and navigate to the directory where the `main.py` file is located.

    - **Mac**:
      1. Open the **Terminal** application.
      2. Use the `cd` command to navigate to the folder containing `main.py`. For example:

         ```sh
         cd /path/to/your/folder
         ```
      3. Run the script using:

         ```sh
         python main.py
         ```

    - **Windows**:
      1. Press **Win + R**, type `cmd`, and press Enter to open the Command Prompt.
      2. Use the `cd` command to navigate to the folder containing `main.py`. For example:

         ```sh
         cd \path\to\your\folder
         ```
      3. Run the script using:

         ```sh
         python main.py
         ```

5. **Interact with the Program**:
   - When prompted, you will see the following options:
     1. Generate FTIR Plot.
     2. Use ImageJ for image processing.
     3. Exit the program.
   - Enter the corresponding number to select the desired function.

6. **Follow the Prompts**: The program will guide you through the process of providing data or selecting image files as needed.

## Example Usage

After running the script, you may be prompted as follows:

```
Welcome to the Image Processer!

Options:
1. Generate FTIR Plot
2. Use ImageJ
3. Exit
Enter the number of the function you want to use:
```

Enter the number corresponding to the desired action, and the script will guide you through the rest of the steps.

## License

This project is licensed under the MIT License.

## Contribution

If you would like to contribute to this project, feel free to create a pull request or submit an issue.

## Contact

For any questions or issues, please contact picealiu@uw.edu.

