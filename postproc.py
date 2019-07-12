import numpy as np
import time

import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(ROOT_DIR)

import crf.crf as crf

color2class = {(0,255,0):0,
                 (0,0,255):1,
                 (0,255,255):2,
                 (255,255,0):3,
                 (255,0,255):4,
                 (100,100,255):5,
                 (200,200,100):6,
                 (170,120,200):7,
                 (255,0,0):8,
                 (200,100,100):9,
                 (10,200,100):10,
                 (200,200,200):11,
                 (50,50,50):12}
class2color = {0:[0,255,0],
                 1:[0,0,255],
                 2:[0,255,255],
                 3:[255,255,0],
                 4:[255,0,255],
                 5:[100,100,255],
                 6:[200,200,100],
                 7:[170,120,200],
                 8:[255,0,0],
                 9:[200,100,100],
                 10:[10,200,100],
                 11:[200,200,200],
                 12:[50,50,50]}

def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            if 'pred.obj' in filename:
                apath = os.path.join(maindir, filename)
                result.append([apath, filename])
    return result


if __name__ == "__main__":
    prob = float(sys.argv[1])
    compat = int(sys.argv[2])

    Total_Time = 0
    all_pred_file = all_path('before/pred_obj/')
    print("Start processing...")
    for pred_file_path, pred_file_name in all_pred_file:
        pred = []
        label = []
        with open(pred_file_path, "r") as fr:
            for line in fr:
                temp = []
                for s in line.split():
                    if s != 'v':
                        temp.append(float(s))
                pred.append(temp)
        pred = np.array(pred)

        coord = pred[:, 0:3].astype(np.float32)
        color = pred[:, 3:6].astype(np.uint32)

        for rgb in color:
            label.append(color2class[tuple(rgb)])

        label = np.array(label).astype(np.uint32)
        label = label[np.newaxis, :].transpose()
        cloud = np.hstack((coord, label))
        start_time = time.time()
        Q = crf.crf_process(cloud, prob, compat)
        result = np.argmax(Q, axis=0)
        end_time = time.time()
        Total_Time += end_time - start_time

        new_color = []
        for label in result:
            new_color.append(class2color[label])
        new_color = np.array(new_color)
        new_pred = np.hstack((coord, new_color))


        with open('after/pred_obj/' + pred_file_name,"w") as fw:
            for point in new_pred:
                fw.write('%s %f %f %f %d %d %d\n' % ('v', point[0], point[1], point[2], point[3], point[4], point[5]))
        with open('after/pred_txt/' + pred_file_name.split('.')[0] + '.txt',"w") as fw:
            for label in result:
                fw.write('%d\n' % (label))
        print(pred_file_name)
    print("End...")
    print("Total time for CRF post processing in Area_6: ", Total_Time)
    print("Average time for every scene in Area_6: ", Total_Time / len(all_pred_file))
