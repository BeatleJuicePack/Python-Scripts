# Trains the image classifier
python36 ~localdesktop/Documents/image_classifier/retrain2.py --bottleneck_dir ~localdesktop/Documents/bottlenecks2 --how_many_training_steps 500 --model_dir ~localdesktop/Documents/inception2 --output_graph ~localdesktop/Documents/retrained_graph2.pb --output_labels ~localdesktop/Documents/retrained_labels2.txt --image_dir ~localdesktop/Pictures/

# Analyzes the test image "image2.jpeg"
python36 ~localdesktop/Documents/image_classifier/guess.py ~localdesktop/Downloads/test/image.jpg 
