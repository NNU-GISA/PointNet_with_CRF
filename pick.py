# Author:   Yunyao Mao
# Date:     2019.7.10
# Usage:    Pick *gt.obj files from before to after/gt_obj
#           Pick *gt.txt files from before to after/gt_txt
import os
import sys
import shutil
if __name__ == "__main__":
    for maindir, subdir, file_name_list in os.walk('raw'):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if 'gt.obj' in filename:
                shutil.copy(apath, 'gt/gt_obj/'+filename)
            elif 'gt.txt' in filename:
                shutil.copy(apath, 'gt/gt_txt/'+filename)
            elif 'pred.obj' in filename:
                shutil.copy(apath, 'before/pred_obj/'+filename)
            elif 'pred.txt' in filename:
                shutil.copy(apath, 'before/pred_txt/'+filename)