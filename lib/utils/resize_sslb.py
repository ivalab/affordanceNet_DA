# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:51:03 2017

@author: yuhchen
"""

import caffe
import yaml
import numpy as np
import cv2
from fast_rcnn.config import cfg

class LabelResizeLayer(caffe.Layer):
    """
    Resize label to be the same size with the samples
    """
    def setup(self, bottom, top):

        feats = bottom[0].data
        #top[0].reshape(1,1,feats.shape[2],feats.shape[3])
        top[0].reshape(feats.shape[0],1,feats.shape[2],feats.shape[3])

    def forward(self, bottom, top):
        feats = bottom[0].data
        lbs = bottom[1].data

        lbs_resize = cv2.resize(lbs, (feats.shape[3],feats.shape[2]),  interpolation=cv2.INTER_NEAREST)

        gt_blob = np.zeros((feats.shape[0], lbs_resize.shape[0], lbs_resize.shape[1], 1), dtype=np.float32)
        #gt_blob[0, 0:lbs_resize.shape[0], 0:lbs_resize.shape[1], 0] = lbs_resize
        lbs_resize_duplicated = np.repeat(lbs_resize[:, :, np.newaxis], feats.shape[0], axis=2)

        gt_blob[0:feats.shape[0], 0:lbs_resize.shape[0], 0:lbs_resize.shape[1], 0] = lbs_resize_duplicated.transpose((2,0,1))

        channel_swap = (0, 3, 1, 2)
        gt_blob = gt_blob.transpose(channel_swap)

        top[0].reshape(*gt_blob.shape)
        top[0].data[...] = gt_blob       

    def backward(self, top, propagate_down, bottom):
        pass

    def reshape(self, bottom, top):
        pass
