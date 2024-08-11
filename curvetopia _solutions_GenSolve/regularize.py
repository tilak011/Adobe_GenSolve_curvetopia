import numpy as np
import matplotlib.pyplot as plt

def is_circle(polyline, tolerance=1e-2):
    """
    Check if the given polyline approximates a circle.
    """
    center = np.mean(polyline, axis=0)
    radii = np.linalg.norm(polyline - center, axis=1)
    return np.std(radii) < tolerance

def is_straight_line(polyline, tolerance=1e-2):
    """
    Check if the given polyline approximates a straight line.
    """
    vector = polyline[-1] - polyline[0]
    distances = np.cross(vector, polyline - polyline[0]) / np.linalg.norm(vector)
    return np.all(np.abs(distances) < tolerance)

def regularize_curve(curve):
    """
    Regularizes the given curve based on its shape.
    """
    if is_circle(curve):
        print("Curve is a circle.")
        # Return the regularized circle here.
    elif is_straight_line(curve):
        print("Curve is a straight line.")
        # Return the regularized straight line here.
    else:
        print("Curve is irregular, applying smoothness.")
        # Apply other regularizations, like smoothing.

# Example usage
def read_csv(csv_path):
    np_path_XYs = np.genfromtxt(csv_path, delimiter=',')
    path_XYs = []
    for i in np.unique(np_path_XYs[:, 0]):
        npXYs = np_path_XYs[np_path_XYs[:, 0] == i][:, 1:]
        path_XYs.append(npXYs)
    return path_XYs

def plot_paths(paths_XYs):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    for XYs in paths_XYs:
        ax.plot(XYs[:, 0], XYs[:, 1], linewidth=2)
    ax.set_aspect('equal')
    plt.show()

if __name__ == "__main__":
    path_XYs = read_csv("examples/isolated.csv")
    for curve in path_XYs:
        regularize_curve(curve)
    plot_paths(path_XYs)
