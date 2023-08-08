# VisdroneDet-2019_sliced_640_025_yolo
this repo gives a link of google Drive of VisdroneDet-2019-Sliced-640-025 in yolo format

该仓库给出visdroneDET-2019数据集切分后子图(train,val)转换为yolo格式的数据集
https://drive.google.com/file/d/125pMvrQaw1FDML9Jbrje-dDhLK4U8sCC/view?usp=drive_link
sliced数据集从paddle社区aistudio上下载后手动转换为yolo格式
如果发现数据集中存在任何问题，请通过该github账号联系我

this project aims to imporve the yolov8s' performance on visdroneDET-2019
The following methods will be tried:
the epoch 150 and worknum=4 is recommended.
1. change imgsz to 1280, but cost more GPU, and decrease the inference speed.
2. modified default.yaml in following parameters:
    mosaic
    mixup
    copy-paste
3. use yolov8x, I personally think it does little help to the mAP.I perfer yolov8s-p2. it merges small feature in the head of yolov8s
4. modify the conf  and iou when doing inference. the conf =0.3 and iou =0.6 is recommended
5. I personally tried adding Context Aggregataion after the head of yolov8s-p2 and trained 80e get mAP:50 0.434 and mAP:50:95:0.26
6. using sahi to crop img when training and using sahi inference when doing inference. 
7. Hope these advices can help you finetune your sod model on your dataset.
8. Embadding Inference, I don't want to try it out because I have no so much GPU to use. compute unit on colab is fucking expensive.