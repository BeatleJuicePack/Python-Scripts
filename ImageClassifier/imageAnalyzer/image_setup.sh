# Build necessary dependencies
yum -y upgrade
yum -y install python36 python36-pip
pip3 install upgrade
pip install tensorflow
pip install tensorflow-hub

# Create necessary paths
mkdir ~localdesktop/Documents/bottlenecks2
mkdir ~localdesktop/Documents/inception2
touch ~localdesktop/Documents/retrained_graph2.pb
touch ~localdesktop/Documents/retrained_labels2.txt

