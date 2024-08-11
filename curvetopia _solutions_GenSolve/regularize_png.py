import cv2
import numpy as np

def raster_to_polylines(image_path):
    """
    Converts a raster image to polylines.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    polylines = [contour.squeeze() for contour in contours]
    return polylines

# Example usage
if __name__ == "__main__":
    polylines = raster_to_polylines("examples/image.png")
    plot_paths(polylines)
