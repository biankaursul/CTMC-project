# Cell Tracking with DeepSORT

This project adapts the popular DeepSORT algorithm for the CTMC cell tracking challenge.
Most of the code we wrote can be found inside Cell-DeepSORT.ipynb. Additional scripts we wrote are located inside scripts.

## Demo

Our tracking algorithm performing on the 3T3-run05 sequence: 

![3t3](https://github.com/biankaursul/CTMC-project/blob/master/3t3.gif)

Tracking result for CRE-BAG2-run03 sequence:

![cre](https://github.com/biankaursul/CTMC-project/blob/master/cre-bag2.gif)



## 
## Dependencies

This project builds on the original DeepSORT (https://github.com/nwojke/deep_sort) and YOLOv5 (https://github.com/ultralytics/yolov5).

For re-identifcation (siamese) network training, it uses this repo. (https://github.com/abhyantrika/nanonets_object_tracking)

Results are evaluated with TrackEval (https://github.com/JonathonLuiten/TrackEval).

On the published training data, we are able to achieve a MOTA score of 41.89, and IDF1 score of 54.44. 


