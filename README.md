# AffordanceNet_DA

This is the implementation of our RA-L work 'Learning Affordance Segmentation for Real-world Robotic Manipulation via Synthetic Images'. The framework segments affordance maps by jointly detecting and localizing candidate regions within an image. Rather than requiring annotated real-world images, the framework learns
from synthetic data and adapts to real-world data without supervision. The original arxiv paper can be found [here](https://ieeexplore.ieee.org/abstract/document/8620534).

<p align="center">
<img src="https://github.com/ivalab/affordanceNet_DA/blob/damask/fig/overlap_fewdigit.png" alt="drawing" width="300"/>
</p>

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

### Requirements

1. Caffe:
	- Install Caffe: [Caffe installation instructions](http://caffe.berkeleyvision.org/installation.html).
	- Caffe must be built with support for Python layers.
	- You will need the modified caffe layer in this repository. Please make sure you clone from here.

2. Specifications:
	- CuDNN-5.1.10
	- CUDA-8.0

### Demo

1. Clone the AffordanceNet_DA repository into your `$AffordanceNet_DA_ROOT` folder
```
git clone https://github.com/ivalab/affordanceNet_DA.git
cd affordanceNet_DA
```

2. Export pycaffe path
```
`export PYTHONPATH=$AffordanceNet_DA_ROOT/caffe-affordance-net/python:$PYTHONPATH`
```

2. Build Cython modules
```
cd $AffordanceNet_DA_ROOT/lib
make clean
make
cd ..
```

4. Download pretrained models
- trained model for DEMO on [dropbox](https://www.dropbox.com/s/u28kllclmv8rb6f/vgg16_faster_rcnn_iter_70000.caffemodel?dl=0) 
- put under `./pretrained/`

5. Demo
```
cd $AffordanceNet_DA_ROOT/tools
python demo_img.py

```

### Training
1. We train AffordanceNet_DA on GAZEBO synthetic data and UMD real data
	- You will need synthetic data and real data in Pascal dataset format. 
	- For your convinience, we did it for you. Just download this file on [dropbox](https://www.dropbox.com/s/52yo1hibsodspmx/data.tar.gz?dl=0) and extract it into your `$AffordanceNet_DA_ROOT` folder.
	- The extracted folder should contain three sub-folders: `$AffordanceNet_DA_ROOT/data/cache`, `$AffordanceNet_DA_ROOT/data/imagenet_models`, and `$AffordanceNet_DA_ROOT/data/VOCdevkit2012` .
	- You will need the VGG-16 weights pretrained on imagenet. For your convinience, please find it [here](https://www.dropbox.com/s/i4kv0vgn078d1jb/VGG16.v2.caffemodel?dl=0)
	- You will need to continue training VGG-16 weights on the model finetuned on synthetic data. For your convinience, please find it [here](https://www.dropbox.com/s/2cckpiwzig64wuk/vgg16_faster_rcnn_iter_208000.caffemodel?dl=0)
	- Put the weight into `$AffordanceNet_DA_ROOT/imagenet_models`

2. Train AffordanceNet_DA:
```
cd $AffordanceNet_ROOT
./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 pascal_voc
```

### License
MIT License

### Acknowledgment
This repo borrows tons of code from
- [affordanceNet](https://github.com/nqanh/affordance-net) by nqanh
- [da-faster-rcnn](https://github.com/yuhuayc/da-faster-rcnn) by yuhuayc


### Contact
If you encounter any questions, please contact me at fujenchu[at]gatech[dot]edu

