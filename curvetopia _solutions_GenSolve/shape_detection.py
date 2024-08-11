import numpy as np

def detect_shapes(curve):
    """
    Detects specific shapes within the curve.
    """
    if is_circle(curve):
        print("Detected a circle.")
    elif is_straight_line(curve):
        print("Detected a straight line.")
    else:
        print("Detected an irregular shape.")

# Example usage
if __name__ == "__main__":
    path_XYs = read_csv("examples/frag0.csv")
    for curve in path_XYs:
        detect_shapes(curve)
from regularize import regularize_curve
from symmetry import detect_symmetry
from curveCompletion import complete_curve
from shape_detection import detect_shapes

# Integrate these into a complete pipeline
def process_curves(input_csv):
    curves = read_csv(input_csv)
    for curve in curves:
        regularize_curve(curve)
        detect_symmetry(curve)
        detect_shapes(curve)
        completed_curve = complete_curve(curve)
        # Save or visualize the completed curve

if __name__ == "__main__":
    process_curves("examples/frag0.csv")
