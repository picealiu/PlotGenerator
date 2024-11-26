import os
import tempfile
import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
from imageJ_tool import (color_change, batch_process_images,
                         divide_and_measure_intensity,
                         process_images_and_save_intensity, image_processing)
from utils import (get_user_input, get_directory, get_filename, get_file_path)
from plot_FTIR import (plot_FTIR, modify_inputs, is_first_column_xaxis,
                       user_input_FTIR)


class TestHelpFunctions(unittest.TestCase):

    def test_get_user_input(self):
        """
        Test get_user_input with different data types.
        """
        with patch('builtins.input', side_effect=["42", "invalid", "21"]):
            # Valid integer input
            self.assertEqual(get_user_input("Enter a number: ", int), 42)
            # Retry with valid input
            self.assertEqual(get_user_input("Enter a number: ", int), 21)

    def test_get_directory(self):
        """
        Test get_directory with valid and invalid directory inputs.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            # Valid directory
            with patch('builtins.input', side_effect=[temp_dir]):
                self.assertEqual(get_directory("Enter a valid directory: "),
                                 temp_dir)

            # Invalid directory followed by a valid directory
            with patch('builtins.input', side_effect=["/invalid/dir",
                                                      temp_dir]):
                self.assertEqual(get_directory("Enter a valid directory: "),
                                 temp_dir)

    def test_get_filename(self):
        """
        Test get_filename with valid and invalid filenames.
        """
        with patch('builtins.input', side_effect=["valid_name.txt",
                                                  "invalid:name.txt",
                                                  "correct_file.png"]):
            self.assertEqual(get_filename("Enter a valid filename: "),
                             "valid_name.txt")
            self.assertEqual(get_filename("Enter a valid filename: "),
                             "correct_file.png")

    def test_get_file_path(self):
        """
        Test get_file_path with valid and invalid file paths.
        """
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            valid_file_path = temp_file.name

        try:   # Test file path
            with patch('builtins.input', side_effect=[valid_file_path]):
                self.assertEqual(get_file_path("Enter a valid file path: "),
                                 valid_file_path)
            with patch('builtins.input', side_effect=["/invalid/path.txt",
                                                      valid_file_path]):
                self.assertEqual(get_file_path("Enter a valid file path: "),
                                 valid_file_path)
        finally:
            os.remove(valid_file_path)


class TestFTIRProcessing(unittest.TestCase):

    @patch("pandas.read_excel")
    @patch("matplotlib.pyplot.show")
    def test_plot_FTIR(self, mock_show, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({
            'xaxis': [1000, 2000, 3000],
            'Sample1': [0.1, 0.2, 0.3],
            'Sample2': [0.4, 0.5, 0.6]
        })
        title = "Test FTIR Plot"
        dataPath = "test_data.xlsx"
        smoothLevel = 1
        fig, axs = plot_FTIR(title, dataPath, smoothLevel)

        self.assertIsNotNone(fig)
        self.assertIsNotNone(axs)
        self.assertEqual(len(axs), 2)

    @patch("builtins.input", side_effect=[
        "2",              # Modify smooth level
        "4",              # New smooth level
        "4"               # Keep all inputs and continue
    ])
    @patch("plot_FTIR.get_file_path", return_value="test_data.xlsx")
    @patch("plot_FTIR.get_user_input", side_effect=[4, "New Title"])
    def test_modify_inputs(self, mock_get_user_input,
                           mock_get_file_path, mock_input):
        dataPath = "initial_path.xlsx"
        smoothLevel = 2
        title = "Initial Title"
        updated_dataPath, updated_smoothLevel, updated_title = modify_inputs(
          dataPath, smoothLevel, title)
        # File path should remain unchanged
        self.assertEqual(updated_dataPath, "initial_path.xlsx")
        # Smooth level should be updated to 4
        self.assertEqual(updated_smoothLevel, 4)
        # Title should remain unchanged
        self.assertEqual(updated_title, "Initial Title")

    @patch("pandas.read_excel")
    def test_is_first_column_xaxis(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame(columns=["xaxis",
                                                             "Sample1",
                                                             "Sample2"])
        dataPath = "test_data.xlsx"
        result = is_first_column_xaxis(dataPath)

        self.assertTrue(result)

    @patch("builtins.input", side_effect=[
        "test_data.xlsx",  # File path
        "1",               # Smooth level
        "Test Title",      # Title
        "yes",             # Save figure
        "plot.png",        # Save file name
        "/tmp",            # Save directory
        "no"               # Do not modify anything else
    ])
    @patch("plot_FTIR.get_file_path", return_value="test_data.xlsx")
    @patch("plot_FTIR.get_user_input", side_effect=[1, "Test Title"])
    @patch("plot_FTIR.get_filename", return_value="plot.png")
    @patch("plot_FTIR.get_directory", return_value="/tmp")
    @patch("pandas.read_excel")
    @patch("matplotlib.pyplot.show")
    @patch("matplotlib.figure.Figure.savefig")
    def test_user_input_FTIR(self, mock_savefig, mock_show, mock_read_excel,
                             mock_get_directory, mock_get_filename,
                             mock_get_user_input, mock_get_file_path,
                             mock_input):

        mock_read_excel.return_value = pd.DataFrame({
            'xaxis': [1000, 2000, 3000],
            'Sample1': [0.1, 0.2, 0.3],
            'Sample2': [0.4, 0.5, 0.6]
        })

        user_input_FTIR()


class TestImageProcessingFunctions(unittest.TestCase):

    @patch('cv2.imread', return_value=np.array([[100, 200], [150, 250]],
                                               dtype=np.uint8))
    @patch('cv2.imwrite')
    def test_color_change(self, mock_imwrite, mock_imread):
        color_change('input_path.tif', 'output_path.tif', 'red', 150)
        mock_imwrite.assert_called_once()

    @patch('os.listdir', return_value=['image1.tif', 'image2.tif'])
    @patch('cv2.imread', return_value=np.array([[100, 200], [150, 250]],
                                               dtype=np.uint8))
    @patch('cv2.imwrite')
    def test_batch_process_images(self, mock_imwrite, mock_imread,
                                  mock_listdir):
        batch_process_images('input_dir', 'output_dir', 'green', 150)
        self.assertEqual(mock_imwrite.call_count, 2)

    @patch('cv2.imread', return_value=np.array([[100, 200, 150],
                                                [150, 250, 100],
                                                [200, 100, 50]],
                                               dtype=np.uint8))
    def test_divide_and_measure_intensity(self, mock_imread):
        intensities = divide_and_measure_intensity('image_path.tif')
        expected_intensities = [150.0, 166.67, 116.67]
        for i in range(len(intensities)):
            self.assertAlmostEqual(intensities[i], expected_intensities[i],
                                   places=1)

    @patch('os.listdir', return_value=['image1.tif', 'image2.tif'])
    @patch('cv2.imread', return_value=np.array([[100, 200], [150, 250]],
                                               dtype=np.uint8))
    @patch('pandas.DataFrame.to_excel')
    def test_process_images_and_save_intensity(self, mock_to_excel,
                                               mock_imread, mock_listdir):
        process_images_and_save_intensity('input_dir', 'output_excel.xlsx')
        mock_to_excel.assert_called_once()

    @patch('builtins.input', side_effect=[
        "1",  # Method choice: Change color
        "input_dir",  # Input directory for color change
        "output_dir",  # Output directory
        "2",  # Color choice: Green
        "150",  # Threshold value
        "yes"  # Confirm
    ])
    @patch('os.listdir', return_value=['image1.tif', 'image2.tif'])
    @patch('cv2.imread', return_value=np.array([[100, 200], [150, 250]],
                                               dtype=np.uint8))
    @patch('cv2.imwrite')
    def test_image_processing_change_color(self, mock_imwrite, mock_imread,
                                           mock_listdir, mock_input):
        image_processing()
        self.assertEqual(mock_imwrite.call_count, 2)

    @patch('builtins.input', side_effect=[
        "2",  # Method choice: Get intensity
        "input_dir",  # Input directory for intensity calculation
        "results.xlsx",  # Output Excel filename
        "yes"  # Confirm
    ])
    @patch('os.listdir', return_value=['image1.tif', 'image2.tif'])
    @patch('cv2.imread', return_value=np.array([[100, 200], [150, 250]],
                                               dtype=np.uint8))
    @patch('pandas.DataFrame.to_excel')
    def test_image_processing_get_intensity(self, mock_to_excel, mock_imread,
                                            mock_listdir, mock_input):
        image_processing()
        mock_to_excel.assert_called_once()


if __name__ == "__main__":
    unittest.main()
