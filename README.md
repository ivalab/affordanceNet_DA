# AffordanceNet_DA

This is the implementation of our RA-L work 'Learning Affordance Segmentation for Real-world Robotic Manipulation via Synthetic Images'. The framework segments affordance maps by jointly detecting and localizing candidate regions within an image. Rather than requiring annotated real-world images, the framework learns
from synthetic data and adapts to real-world data without supervision. The original arxiv paper can be found [here](https://ieeexplore.ieee.org/abstract/document/8620534).

![affordance-net](https://raw.githubusercontent.com/nqanh/affordance-net/master/tools/temp_output/iit_aff_dataset.jpg "affordance-net")

If you find it helpful for your research, please consider citing:

    @inproceedings{chu2019learning,
      title = {Learning Affordance Segmentation for Real-world Robotic Manipulation via Synthetic Images},
      author = {F. Chu and R. Xu and P. A. Vela},
      journal = {IEEE Robotics and Automation Letters},
      year = {2019},
      volume = {4},
      number = {2},
      pages = {1140-1147},
      DOI = {10.1109/LRA.2019.2894439},
      ISSN = {2377-3766},
      month = {April}
    }

------------------------------------

### Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Demo](#demo)
4. [Training](#training)
5. [Notes](#notes)


### Requirements

1. Caffe
	- Install Caffe: [Caffe installation instructions](http://caffe.berkeleyvision.org/installation.html).
	- Caffe must be built with support for Python layers.

2. Hardware
	- To train a full AffordanceNet, you'll need a GPU with ~11GB (e.g. Titan, K20, K40, Tesla, ...).
	- To test a full AffordanceNet, you'll need ~6GB GPU.

3. [Optional] For robotic demo
	- [ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu)
	- [rospy](http://wiki.ros.org/rospy)
	- [OpenNI](https://github.com/OpenNI/OpenNI)
	- [PrimeSensor](https://github.com/PrimeSense/Sensor)


### Installation

1. Clone the AffordanceNet repository into your `$AffordanceNet_ROOT` folder.
	
	
2. Build `Caffe` and `pycaffe`:
	- `cd $AffordanceNet_ROOT/caffe-affordance-net`
    - `# Now follow the Caffe installation instructions: http://caffe.berkeleyvision.org/installation.html`
    - `# If you're experienced with Caffe and have all of the requirements installed and your Makefile.config in place, then simply do:`
    - `make -j8 && make pycaffe`
     

3. Build the Cython modules:
    - `cd $AffordanceNet_ROOT/lib`
    - `make`


4. Download pretrained weights ([Google Drive](https://drive.google.com/file/d/0Bx3H_TbKFPCjNlMtSGJlQ0dxVzQ/view?usp=sharing), [One Drive](https://studenthcmusedu-my.sharepoint.com/:u:/g/personal/nqanh_mso_hcmus_edu_vn/ETD6q64-L1lCgtNEryA42NwBNM9vNoyE8QyxAYzgt8NqnA?e=uRCxPg)). This weight is trained on the training set of the [IIT-AFF dataset](https://sites.google.com/site/iitaffdataset/):
    - Extract the file you downloaded to `$AffordanceNet_ROOT`
    - Make sure you have the caffemodel file like this: `'$AffordanceNet_ROOT/pretrained/AffordanceNet_200K.caffemodel`

	
### Demo

After successfully completing installation, you'll be ready to run the demo. 

0. Export pycaffe path:
	- `export PYTHONPATH=$AffordanceNet_ROOT/caffe-affordance-net/python:$PYTHONPATH`

1. Demo on static images:
	- `cd $AffordanceNet_ROOT/tools`
	- `python demo_img.py`
	- You should see the detected objects and their affordances.
	
2. (Optional) Demo on depth camera (such as Asus Xtion):
	- With AffordanceNet and the depth camera, you can easily select the interested object and its affordances for robotic applications such as grasping, pouring, etc.
	- First, launch your depth camera with ROS, OpenNI, etc.
	- `cd $AffordanceNet_ROOT/tools`
	- `python demo_asus.py`
	- You may want to change the object id and/or affordance id (line `380`, `381` in `demo_asus.py`). Currently, we select the `bottle` and its `grasp` affordance.
	- The 3D grasp pose can be visualized with [rviz](http://wiki.ros.org/rviz). You should see something like this: 
	![affordance-net-asus](https://raw.githubusercontent.com/nqanh/affordance-net/master/tools/temp_output/asus_affordance_net_demo.jpg "affordance-net-asus")
	
### Training

1. We train AffordanceNet on [IIT-AFF dataset](https://sites.google.com/site/iitaffdataset/)
	- We need to format IIT-AFF dataset as in Pascal-VOC dataset for training.
	- For your convinience, we did it for you. Just download this file ([Google Drive](https://drive.google.com/file/d/0Bx3H_TbKFPCjV09MbkxGX0k1ZEU/view?usp=sharing), [One Drive](https://studenthcmusedu-my.sharepoint.com/:u:/g/personal/nqanh_mso_hcmus_edu_vn/EXQok71Y2kFAmhaabY2TQO8BFIO1AqqH5GcMOfPqgn_q2g?e=7rH3Kd)) and extract it into your `$AffordanceNet_ROOT` folder.
	- The extracted folder should contain three sub-folders: `$AffordanceNet_ROOT/data/cache`, `$AffordanceNet_ROOT/data/imagenet_models`, and `$AffordanceNet_ROOT/data/VOCdevkit2012` .

2. Train AffordanceNet:
	- `cd $AffordanceNet_ROOT`
	- `./experiments/scripts/faster_rcnn_end2end.sh [GPU_ID] [NET] [--set ...]`
	- e.g.: `./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 pascal_voc`
	- We use `pascal_voc` alias although we're training using the IIT-AFF dataset.



### Notes
1. AffordanceNet vs. Mask-RCNN: AffordanceNet can be considered as a general version of Mask-RCNN when we have multiple classes inside each instance.
2. The current network achitecture is slightly diffrent from the paper, but it achieves the same accuracy.
3. Train AffordanceNet on your data:
	- Format your images as in Pascal-VOC dataset (as in `$AffordanceNet_ROOT/data/VOCdevkit2012` folder).
	- Prepare the affordance masks (as in `$AffordanceNet_ROOT/data/cache` folder): For each object in the image, we need to create a mask and save as a .sm file. See `$AffordanceNet_ROOT/utils` for details.



### License
MIT License

### Acknowledgment
This repo borrows tons of code from
- [affordanceNet](https://github.com/nqanh/affordance-net) by nqanh
- [da-faster-rcnn](https://github.com/yuhuayc/da-faster-rcnn) by yuhuayc


### Contact
If you encounter any questions, please contact me at fujenchu[at]gatech[dot]edu

