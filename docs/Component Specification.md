# Component Specification

## Software Components

### 1. Data Manager
- Handles raw FTIR(Fourier-transform infrared spectroscopy) datasets in specified formats (e.g., CSV or Excel).
- Manages image files for analysis and user-defined filters (e.g., wavelength ranges, specific peaks).
- Implements FTIR data handling, including filtering by wavelength.
- Sets up image loading and basic filter applications (e.g., contrast, change to green) with PyImageJ.

### 2. Visualization Manager
- Manages data visualization tasks, creating FTIR plots or graphical outputs of processed images.
- Builds FTIR plotting function.
- Enables image display for processed results, allowing users to preview and save.

### 3. User Interaction Interface
- Provides an interactive, guided interface where non-programmer users (Lab Scientists) interact with the system through prompts or pop-up guides.
- Simplifies the data input and analysis process without requiring direct coding.
- Develops pop-up guides to help users select FTIR data for plotting or choose images and filters for processing.
- Separates options for FTIR plotting and image processing to streamline user choices.

### 4. Required Packages
- `pandas`: Data handling and manipulation.
- `matplotlib`: Data visualization for FTIR plotting.
- `numpy`, `os`, `sys`, `cv2`: Various tasks for numerical operations, file handling, and image processing.

## Interactions to Accomplish Use Cases

### 1. Generating an FTIR Plot
- The User Interaction Interface prompts the user with a pop-up to:
  - Select an FTIR dataset file.
  - Ask the user to clean and reorganize the dataset.
  - Import the raw FTIR dataset.
  - Generate and display an FTIR plot.

### 2. Processing an Image (e.g., Adding a Filter)
- The User Interaction Interface asks the user to:
  - Select an image file for processing.
  - Choose an image processing filter (e.g., contrast enhancement).
  - Return the processed image or the intensity read based on the user's request.

## Component Integration and Testing
- All components are integrated to ensure seamless interaction between data preparation and visualization.
- Testing is performed to verify smooth transitions between the data manager, visualization manager, and user interaction interface.

## Project Plan

#### **a. User Interface Development**
- **Objective**: Create an interactive user interface that guides users through the system.
- **Tasks**:
  - Develop a UI framework that will display **pop-up questions** to guide users step-by-step through tasks.
  - **Dynamic Responses**: Make the interface respond dynamically to user inputs, enabling actions like FTIR plot generation and image processing.
  - **Key Steps**:
    - Design the **user flow** to outline the interaction process, specifying the types of prompts, such as selecting files or choosing analysis options.
    - Create a **prototype** of the UI to establish the basic structure and ensure it interacts smoothly with backend functionalities for FTIR plotting and image processing.

#### **b. Core Function Development**
- **Objective**: Build the core functionality for FTIR plotting and image processing.
- **Tasks**:
  - **FTIR Plotting**:
    - Develop code to **import FTIR data**, format it appropriately, and generate customizable plots for visualization.
  - **Image Processing (PyImageJ)**:
    - Implement basic image processing workflows such as **cropping**, **filtering**, and **enhancing images** using PyImageJ.

#### **c. Testing and Feedback Collection**
- **Objective**: Ensure that the system functions as expected and is user-friendly.
- **Tasks**:
  - Conduct tests using **sample datasets and images** to verify functionality and identify any issues.
  - Gather **user feedback** to improve the UI, adjust the flow of questions, and make necessary refinements for better ease of use.
