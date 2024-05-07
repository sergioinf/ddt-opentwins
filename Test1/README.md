## Test 1

This test folter contains the scripts used to measure the latency and robustnes of the platform:
- "LineDetection_ML_4_WithData" and "util" contains the ML model from (https://github.com/axinc-ai/ailia-models/tree/master/road\_detection/lstr)
- "main" and "reciever" .py are the neccesary script to run the test.
- CSV files are the processed dataset obtained from the test.
- "graphics.ipynb" is a jupyter notebook to draw the figure.
- "images" contains a set of images to run the test.
- "automatic_control_images.py" is used to generate the images with CARLA Simulator (https://carla.org/). It must be located in CARLA/PythonAPI/examples in order to run it properly.
