# Function Specification

## Target Users and Their Knowledge

### 1. Who are the Users?
- The primary users are **Lab Scientists** who may not have programming experience. The tool is designed to be accessible to non-programmers, enabling them to efficiently process and analyze data.

### 2. User Information Requirements
- Users need to obtain **FTIR Plots** for their datasets.
- Users also want to perform **Image Processing** (using PyImageJ) to analyze images, apply filters, or enhance image quality.

## User Interaction Scenarios

### 1. How Users Interact with the System
- Users interact with the system through a simple and guided **interactive interface**.
- They can choose to **generate an FTIR plot** or **process an image** by following on-screen prompts and selecting relevant files or options.
- The interface is designed to help users achieve their goals without requiring any coding knowledge.

## Project Plan

### 1. Preliminary Project Plan
This section outlines the development plan, focusing on the tasks to be completed in the upcoming weeks, with an emphasis on building a user-friendly interface and core functionalities.

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