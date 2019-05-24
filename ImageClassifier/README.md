This project is based on the Tensorflow Image Retrain.py script.

The first stage of image analysis begins by assembling the necessary dependencies and paths.
*This requires root/administrator permissions and may cause issues with file permissions for a given user.
*To remedy this you must assign the proper file permissions based on your given task (ex:"chmod a+rw ~path/fileName".)
This is easily performed using the "image_setup.sh" script (for RedHat/CentOS).

Once setup is complete you may begin training your image datasets by running the "image_analyzer.sh" script.
This will analyze "image.jpeg" found in your Downloads/test directory.

**There is currently an issue based on data sets not purging old/outdated data
**For instance if a model is trained on 'cars' and 'people', then is switched to another data set based on 'cats' and 'dogs'
**then the second data set will be based on 'cars' and 'people' rather than 'cats' and 'dogs'
