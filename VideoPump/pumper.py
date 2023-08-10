import cv2
import os

video_info={
    "width":0,
    "height":0,
    "fps":0,
    "frame_count":0
}
# cap.get(0)	CV_CAP_PROP_POS_MSEC      视频文件的当前位置（播放）以毫秒为单位
# cap.get(1)	CV_CAP_PROP_POS_FRAMES    基于以0开始的被捕获或解码的帧索引
# cap.get(2)	CV_CAP_PROP_POS_AVI_RATIO 视频文件的相对位置（播放）：0 = 电影开始，1 = 影片的结尾。
# cap.get(3)	CV_CAP_PROP_FRAME_WIDTH   在视频流的帧的宽度
# cap.get(4)	CV_CAP_PROP_FRAME_HEIGHT  在视频流的帧的高度
# cap.get(5)	CV_CAP_PROP_FPS           帧速率
# cap.get(6)	CV_CAP_PROP_FOURCC        编解码的4字-字符代码
# cap.get(7)	CV_CAP_PROP_FRAME_COUNT   视频文件中的帧数
def CutVideo2Image(video_path, img_path):
    #将视频输出为图像
    #video_path为输入视频文件路径
    #img_path为输出图像文件夹路径
    cap = cv2.VideoCapture(video_path)
    video_info["width"] = cap.get(3)
    video_info["height"] = cap.get(4)
    video_info["fps"] = cap.get(5)
    video_info["frame_count"] = cap.get(7)
    index = 0
    while(True):
        ret,frame = cap.read() 
        if ret:
            cv2.imwrite(img_path+'/%d.jpg'%index, frame)
            index += 1
        else:
            break
    cap.release()
    

           
def CombVideo(in_path, out_path, size):
    #将图片合成视频
    #in_path为输入图像文件夹路径
    #out_path为输出视频文件路径
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(out_path,fourcc, 30.0, size)
    files = os.listdir(in_path)
    step = 10
    for i in range(0,len(files),step):
        img = cv2.imread(in_path + '/%d.jpg' % i)
        # img = cv2.resize(img, size)
        out.write(img)
        i+=10
    out.release()

video_initial = 'wrj_Trim.mp4'  #视频路径
video_finish = 'wrj_Trim_pumped.mp4'   #合成视频路径
images_initial = 'video2img/input'   #视频抽取得到的图像输出路径
# images_final = 'video2img/output'    #存放画完预测框的图像路径
if __name__ == '__main__':
    CutVideo2Image(video_initial, images_initial)
    # GetObj(images_initial, images_final)
    CombVideo(images_initial, video_finish, (video_info["width"],video_info["height"]))
