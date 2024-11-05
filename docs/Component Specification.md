**1. Software components.**   
   ***a. Data Manager***     
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raw FTIR datasets (in a specified format like CSV or Excel), image files for analysis, and user-defined filters
    (e.g., wavelength ranges, specific peaks).    
   ***b. Visualization Manager***   
    Manages data visualization tasks, creating FTIR plots or graphical outputs of processed images.   
   ***c. User Interaction Interface***   
    Provides an interactive, guided interface where non-programmer users (Lab Scientists) interact with the system
    through pop-up questions. It simplifies the data input and analysis process without requiring direct coding.   
  ***d. Packages***   
    Pandas, Matplotlib, PyImageJ   

**2. Interactions to accomplish use cases.**   
   ***a. Generating an FTIR Plot***    
    The User Interaction Interface prompts the user with a pop-up to:   
    Select an FTIR dataset file.   
    Ask the user to lean and reorganize the dataset.   
    Imports the raw FTIR dataset.   
    Generates and Displays an FTIR plot.   
   ***b. Processing an Image (e.g., Adding a Filter)***   
    The User Interaction Interface asks the user to:   
    Select an image file for processing.   
    Choose an image processing filter (e.g., contrast enhancement).   
    Return the processed image or the intensity read based on user's request.   
    
**3. User Interaction Interface**   
  Develop pop-up guides to help users select FTIR data for plotting or choose images and filters for processing.   
  Separate options for FTIR plotting and image processing to streamline user choices.   
  ***a. Data Manager***    
    Implement FTIR data handling, including filtering by wavelength.   
    Set up image loading and basic filter applications (e.g., contrast, change to green) with PyImageJ.   
   ***b. Visualization Manager***    
    Build FTIR plotting function.   
    Enable image display for processed results, allowing users to preview and save.   
   ***c. Component Integration and Testing***    
    Combine all components and test for seamless interaction between data preparation and visualization.   
  
