from multiprocessing import Queue, Process, freeze_support
import cv2
from ultralytics import YOLO
### 加载模型，定义rtsp/video path
model = YOLO('path/to/model')
video_path = "path/to/video" 
imgsz=[960,1280] ##[480,640],[320,480]  HW
iou=0.6
conf= 0.3
delay=50 # ms
inputQNum = 1
outputQNum = 1
### 输入管道管道和队列

def inputQ(queue):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('camera', frame)
            queue.put(frame)
            print(queue.qsize())
        else:
            break
        if (cv2.waitKey(1)) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
### 推理输出管道
def outputQ(queue,queue_out):
    while True:
        frame = queue.get()
        # img_gray = cv2.cvtColor(im_rd, cv2.COLOR_RGB2GRAY)
        results = model.track(source=frame,imgsz=imgsz,iou=iou,conf=conf,persist=True,line_width=1)
        anno_frame = results[0].plot()
        queue_out.put(anno_frame)

def show(queue_out):
    cv2.namedWindow("out", 1)
    while True:
        frame = queue_out.get()
        cv2.imshow('out', frame)
        if (cv2.waitKey(delay=delay)) == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    freeze_support()
    record1 = [] #store input process
    record2 = [] #stroe output process
    queue = Queue()
    queue_out = Queue()
    # 输入进程
    for i in range(inputQNum):
        process = Process(target=inputQ, args=(queue,))
        process.start()
        record2.append(process)
    #输出进程
    for i in range(outputQNum):
        process = Process(target=outputQ, args=(queue,queue_out))
        process.start()
        record2.append(process)
    #显示进程
    for i in range(1):
        process = Process(target=show, args=(queue_out,))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()
    for p in record2:
        p.join()