DATASET,UNBALANCED,dir_ext = "Processed_highD",False,''
if UNBALANCED:
    dir_ext += 'U'

# Problem definition parameters:
# SEQ_LEN = 35
# OBS_LEN = 10
# PRED_LEN = 25
# FPS = 5
# Rendering params
# save_whole_imgs = False
# save_cropped_imgs = False
'''
FPS为1，则fr_div=25/1=25，筛选出了 DataFrame df 中 frame 列为 25 的整数倍的数据行，新数据更新间隔为1s
FPS为5，则fr_div=25/5=5，筛选出了 DataFrame df 中 frame 列为 5 的整数倍的数据行，新数据更新间隔为0.2s
FPS为25，则fr_div=25/25=1，筛选出了 DataFrame df 中 frame 列为 1 的整数倍的数据行，新数据更新间隔为0.04s

'''
SEQ_LEN,OBS_LEN,PRED_LEN,FPS = 80,30,50,25
save_whole_imgs,save_cropped_imgs,image_scaleH,image_scaleW = True,True,4,1

# parameters of CS-LSTM model
grid_max_x = 100

def generate_paths(first_leg, start_ind, end_ind, second_leg):
    path_list = []
    for i in range(start_ind, end_ind):
        path_list.append(first_leg + str(i).zfill(2) + second_leg)
    return path_list

if DATASET == "Processed_highD":
    track_paths = generate_paths('../../Dataset/HighD/Tracks/', 0, 61, '_tracks.csv')
    frame_pickle_paths = generate_paths('../../Dataset/HighD/Pickles/', 0,  61, '_frames.csv')
    track_pickle_paths = generate_paths('../../Dataset/HighD/Pickles/', 0,  61, '_tracks.csv')
    meta_paths = generate_paths('../../Dataset/HighD/Metas/', 0,  61, '_recordingMeta.csv')
    static_paths = generate_paths('../../Dataset/HighD/Statics/', 0,  61, '_tracksMeta.csv')
    cropped_height = int(20 * image_scaleH)
    cropped_width = int(200 * image_scaleW)
else:
    raise('undefined dataset')



