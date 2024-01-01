 官方文档

Early Prediction of Lane Change Maneouvre Using Multi-task Attention-based Convolutional Neural Networks

------

用户使用文档（自写）：

**官方库：**

1. clone项目
2. 修改代码，参考我的云端库（已修改代码）
3. 准备数据集，放于EarlyLCPred文件夹同目录：
   - Dataset(文件夹)
     - HighD(文件夹)
       - Metas(放_recordingMeta.csv)
       - Pickles(放_tracks.csv,_frames.csv)
       - Statics(放_tracksMeta.csv)
       - Tracks(放_tracks.csv)
     - Processed_highD(文件夹)
       - CroppedImages(空)
       - RenderedDataset(空)
       - Scenarios(空)
       - WholeImages(放_highway.png)
   - EarlyLCPred(文件夹)
4. main.py

**用户库（已经进行过相关操作）：**配好环境直接进行3，4即可
