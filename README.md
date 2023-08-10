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
val: Scanning /content/datasets/VisDrone/VisDrone2019-DET-val/labels... 548 images, 0 backgrounds, 0 corrupt: 100% 548/548 [00:00<00:00, 721.77it/s]
val: New cache created: /content/datasets/VisDrone/VisDrone2019-DET-val/labels.cache
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 35/35 [01:36<00:00,  2.76s/it]
                   all        548      38759      0.531      0.413      0.432      0.259
            pedestrian        548       8844      0.546      0.462      0.492      0.231
                people        548       5125      0.544      0.372      0.402      0.164
               bicycle        548       1287      0.322      0.145      0.149     0.0702
                   car        548      14064      0.727      0.814      0.834      0.593
                   van        548       1975      0.518      0.461       0.47      0.336
                 truck        548        750       0.54       0.38      0.393      0.263
              tricycle        548       1045       0.49      0.285      0.306      0.173
       awning-tricycle        548        532      0.342      0.203      0.179      0.113
                   bus        548        251      0.709      0.518      0.587      0.417
                 motor        548       4886      0.575      0.486      0.504      0.231


Ultralytics YOLOv8.0.149 🚀 Python-3.10.12 torch-2.0.1+cu118 CUDA:0 (Tesla T4, 15102MiB)
YOLOv8s-p2_CA summary (fused): 243 layers, 10633860 parameters, 0 gradients
val: Scanning /content/datasets/VisDrone/VisDrone2019-DET-val/labels.cache... 548 images, 0 backgrounds, 0 corrupt: 100% 548/548 [00:00<?, ?it/s]
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% 35/35 [01:40<00:00,  2.88s/it]
                   all        548      38759      0.544      0.416      0.435      0.263
            pedestrian        548       8844       0.58      0.466      0.502      0.237
                people        548       5125      0.567      0.366      0.403      0.163
               bicycle        548       1287      0.371      0.152      0.167     0.0766
                   car        548      14064      0.736      0.813      0.835      0.595
                   van        548       1975      0.528      0.466       0.47      0.336
                 truck        548        750      0.542      0.371      0.389      0.259
              tricycle        548       1045      0.453      0.331      0.306      0.176
       awning-tricycle        548        532      0.337      0.195       0.18      0.117
                   bus        548        251      0.748       0.51       0.59      0.438
                 motor        548       4886      0.578      0.488      0.509      0.236
Speed: 1.2ms preprocess, 9.7ms inference, 0.0ms loss, 9.6ms postprocess per image
ok.. ContextAggregation does no help...
