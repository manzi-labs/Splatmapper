import sys
import os
import imageio
import numpy as np

if __name__ == '__main__':
    # Get the filenames for the input images and output splatmap from the command line arguments
    r_channel_filename = os.path.join(os.getcwd(), sys.argv[1])
    g_channel_filename = os.path.join(os.getcwd(), sys.argv[2])
    b_channel_filename = os.path.join(os.getcwd(), sys.argv[3])
    splat_map_filename = os.path.join(os.getcwd(), sys.argv[4])

    # Open the three input PNG files with imageio
    r_channel = imageio.imread(r_channel_filename)
    g_channel = imageio.imread(g_channel_filename)
    b_channel = imageio.imread(b_channel_filename)

    # Merge the three channels into a single RGB image
    splat_map = np.dstack((r_channel, g_channel, b_channel))

    # Convert the output image to uint16 to preserve full precision
    splat_map = splat_map.astype(np.uint16)

    # Save the output image as a PNG file with imageio
    imageio.imwrite(splat_map_filename, splat_map)