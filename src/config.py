import numpy as np

# HSV color bounds for the cloak
# Tune these using color_sampler.py — hold the cloak up and click on it
# H (hue): 0-179, S (saturation): 0-255, V (value/brightness): 0-255
LOWER_BOUND = np.array([113, 35, 30])
UPPER_BOUND = np.array([141, 180, 200])

# Morphological cleanup kernel size
KERNEL = np.ones((5, 5), np.uint8)
