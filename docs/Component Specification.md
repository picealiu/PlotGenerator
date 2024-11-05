**1. Software components.**   
   ***a. Data Manager***     
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raw FTIR datasets (in a specified format like CSV or Excel), image files for analysis, and user-defined filters
    (e.g., wavelength ranges, specific peaks).    
   ***b. Visualization Manager***   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Manages data visualization tasks, creating FTIR plots or graphical outputs of processed images.   
   ***c. User Interaction Interface***   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Provides an interactive, guided interface where non-programmer users (Lab Scientists) interact with the system
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;through pop-up questions. It simplifies the data input and analysis process without requiring direct coding.   
  ***d. Packages***   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pandas, Matplotlib, PyImageJ   

**2. Interactions to accomplish use cases.**   
   ***a. Generating an FTIR Plot***    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The User Interaction Interface prompts the user with a pop-up to:   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select an FTIR dataset file.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ask the user to lean and reorganize the dataset.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Imports the raw FTIR dataset.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generates and Displays an FTIR plot.   
   ***b. Processing an Image (e.g., Adding a Filter)***   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The User Interaction Interface asks the user to:   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Select an image file for processing.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Choose an image processing filter (e.g., contrast enhancement).   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the processed image or the intensity read based on user's request.   
    
**3. User Interaction Interface**   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Develop pop-up guides to help users select FTIR data for plotting or choose images and filters for processing.   
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Separate options for FTIR plotting and image processing to streamline user choices.   
  ***a. Data Manager***    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Implement FTIR data handling, including filtering by wavelength.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set up image loading and basic filter applications (e.g., contrast, change to green) with PyImageJ.   
   ***b. Visualization Manager***    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Build FTIR plotting function.   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enable image display for processed results, allowing users to preview and save.   
   ***c. Component Integration and Testing***    
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Combine all components and test for seamless interaction between data preparation and visualization.   
  
