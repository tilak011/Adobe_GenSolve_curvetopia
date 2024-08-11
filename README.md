# Curvetopia Challenge

This project addresses the Curvetopia challenge, which involves processing and regularizing curves from input polyline data, identifying symmetries, and handling curve completions. The final output consists of SVG files containing Bézier curves.

## Project Structure

The solution is divided into several key components, each implemented as a separate Python script:

1. **regularize.py**: This script identifies and regularizes the given curves by detecting regular shapes such as straight lines and circles. It ensures that curves are standardized based on their geometric properties.

2. **symmetry.py**: This component detects symmetries in the curves, specifically focusing on reflection symmetries. It determines if a curve is symmetric with respect to its midpoint.

3. **curveCompletion.py**: This script completes incomplete curves by identifying gaps and smoothly connecting them, ensuring that the curves are continuous and whole.

4. **regularize_png.py**: An optional script that converts raster images (PNG format) of line art into polylines. This process involves detecting contours in images and translating them into vector-based representations.

5. **shape_detection.py**: This module detects specific shapes, such as circles and rectangles, within the curves. It differentiates between regular and irregular shapes to classify the components of the curve accurately.

## Workflow and Integration

Each script performs a specific task in the overall workflow. Here's how they integrate to solve the Curvetopia challenge:

- **Regularization**: Start by regularizing the curves to identify any standard geometric shapes, making them easier to analyze and manipulate.
  
- **Symmetry Detection**: Analyze each curve for symmetries, which can provide insights into the curve's structure and potential transformations.

- **Curve Completion**: Address any incomplete curves by detecting gaps and connecting them to form a complete, continuous curve.

- **Shape Detection**: Further analyze the curves to identify specific shapes, which can aid in understanding the overall geometry of the input data.

- **Optional Image Conversion**: If working with raster images, convert them to polylines to incorporate them into the regularization and analysis processes.

## How to Use

1. **Installation**: Clone the repository and install any required dependencies specified in the `requirements.txt` file.

    ```bash
    git clone <repository-url>
    cd curvetopia-challenge
    pip install -r requirements.txt
    ```

2. **Execution**: Run each script individually to perform specific tasks or integrate them into a single workflow using a master script to process the curves from start to finish.

3. **Input and Output**: Provide the input data as CSV files or images as needed, and the scripts will output the processed curves, which can be saved as SVG files.

## License

This project is licensed under the MIT License.
