import os
import time
from multiprocessing import Process
import numpy as np 
import sys
# from extract_scenarios import ExtractScenarios
from data_prep.extract_scenarios import ExtractScenarios
# from render_scenarios import RenderScenarios
from data_prep.render_scenarios import RenderScenarios
import param as p
'''
多线程数据处理
当前脚本目录查看方法，debug→os.path.dirname(os.path.abspath(__file__))
    （'E:\\Github\\EarlyLCPred\\data_prep'）
'''
np.set_printoptions(threshold=sys.maxsize)

def extract(core_num, file_numbers):
    start = time.time()
    for file_number in file_numbers:
        print('Core number: ', core_num, ' started on file number: ', file_number)
        
        extractor = ExtractScenarios(
            file_number,
            p.track_paths[file_number], 
            p.track_pickle_paths[file_number],
            p.frame_pickle_paths[file_number], 
            p.static_paths[file_number],
            p.meta_paths[file_number],
            p.DATASET)
        extractor.extract_and_save() 
    
    end = time.time()
    print('Core Number: ', core_num, ' Ended in: ', end-start, ' s.')

def render(core_num, file_numbers):
    # p=params
    for file_number in file_numbers:
        print('Core number: ', core_num, ' started on file number: ', file_number)
        start = time.time()
        
        renderer = RenderScenarios(
            file_number,
            p.track_paths[file_number], 
            p.frame_pickle_paths[file_number], 
            p.static_paths[file_number],
            p.meta_paths[file_number],
            p.DATASET
        )
        renderer.update_dirs() 
        renderer.load_scenarios()
        renderer.render_scenarios()
        renderer.save_dataset()  

        end = time.time()
    print('Core Number: ', core_num, ' Ended in: ', end-start, ' s.')




if __name__ =="__main__":
    
    np.random.seed(0)   
    '''
    # Single Core (For Debugging purposes)
    
    i = np.array([26])
    #extract(1, i)    
    render(1, i)
    exit()
    '''

    # Extract LC scenarios (multi-threads)
    '''
    根据给定的文件数量和核心数，在多个进程中并行执行某个函数（extract）来处理文件
    '''
    # total_cores = 3
    total_cores,file_numbers = 4, np.arange(1,61)#1,2,3...,60
    total_files = len(file_numbers)
    file_per_core = int(total_files/total_cores)
    procs = []
    for core_num in range(total_cores):
        file_row = file_per_core*core_num
        core_fle_numbers = file_numbers[file_per_core*core_num:(file_per_core*(core_num+1))]
        # 创建一个新的进程对象，将 extract 函数作为目标，并传递核心编号和文件编号作为参数
        proc = Process(target= extract, args = (core_num+1, core_fle_numbers))
        procs.append(proc)
        # ：启动进程，使其开始执行 extract 函数。
        proc.start()
    # 等待所有子进程执行完毕，然后再继续执行主线程中的后续代码。
    '''
    proc.join() 的作用是等待每个进程执行完毕。虽然进程已经启动，但主线程会继续执行下面的代码。
    如果没有使用 proc.join() 来等待进程的结束，主线程可能会在子进程尚未完成的情况下继续执行后面的代码，导致不确定的结果。
    使用 proc.join() 会阻塞主线程，直到所有子进程都执行完毕，才会继续执行后面的代码。这样可以确保在整个程序完成之前，所有的子进程都已经完成任务。
    '''
    for proc in procs:
        proc.join()
    print("------------------所有进程执行完毕，数据提取完成 in extract------------------")

    # Render extracted LC scenarios (multi-threads)
    for core_num in range(total_cores):
        file_row = file_per_core*core_num
        core_fle_numbers = file_numbers[file_per_core*core_num:(file_per_core*(core_num+1))]
        proc = Process(target= render, args = (core_num+1, core_fle_numbers))
        procs.append(proc)
        proc.start()
    
    for proc in procs:
        proc.join()
    print("------------------所有进程执行完毕，数据提取完成 in render------------------")