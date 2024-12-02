# Image Processor Tool

## Overview

The **Image Processor Tool** is an interactive script designed to provide users with functionalities to:

1. Generate FTIR (Fourier-transform infrared spectroscopy) plots.
2. Use ImageJ for image processing, such as color changes and intensity readings.
3. Exit the program when finished.

The tool guides users through each step and provides an easy way to interactively work with image files and FTIR data.

## Features

- **Generate FTIR Plot**: Users can input FTIR data to generate a plot for visualization purposes.
- **ImageJ Integration**: Perform image processing, including color adjustments, intensity analysis, and other modifications.

To use this tool, follow the steps below:

## Install Python

Ensure Python is installed on your system.

### For Windows:
1. Download Python from the [official Python website](https://www.python.org/).
2. Run the installer and check **Add Python to PATH** during installation.
3. Open the terminal by searching for "Command Prompt" in the Start menu.

### For macOS:
1. Open Terminal (`Cmd + Space`, type `Terminal`, and press Enter).
2. Install Homebrew if not already installed:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
3. Install Python using Homebrew:
    ```sh
    brew install python
    ```

## Setup and Installation

To use this tool, follow these simple steps to set up the environment.

1. **Clone or Download the Repository**: First, clone or download the repository containing this script.

2. **Install the Package**: After cloning, navigate to the project directory
   
    ```sh
    cd path/to/folder/contains/setup.py
    ```
    
   Run the following command to install the tool along with all required dependencies:

    ```sh
    python setup.py install
    ```

    This will automatically install all the required dependencies, including `numpy`, `pandas`, `matplotlib`, `opencv-python`, and other necessary packages.

4. **Run the Tool**: After installation, you can run the tool by typing:

    ```sh
    plotGenerator
    ```

    This command will execute the tool, and you will be presented with an interactive interface.

## How to Use

1. **Interact with the Program**:
   - When prompted, you will see the following options:
     1. Generate FTIR Plot.
     2. Use ImageJ for image processing.
     3. Exit the program.
   - Enter the corresponding number to select the desired function.

2. **Follow the Prompts**: The program will guide you through the process of providing data or selecting image files as needed.

## Example Usage

After running the tool, you may be prompted as follows:

```
Welcome to the Image Processor!

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

