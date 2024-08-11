import numpy as np

def detect_symmetry(curve):
    """
    Detects symmetry in the given curve.
    """
    midpoint = np.mean(curve, axis=0)
    mirrored_curve = np.flipud(curve)
    if np.allclose(curve, mirrored_curve):
        print("Curve has reflection symmetry.")
    else:
        print("Curve does not have symmetry.")

# Example usage
if __name__ == "__main__":
    path_XYs = read_csv("examples/isolated.csv")
    for curve in path_XYs:
        detect_symmetry(curve)
