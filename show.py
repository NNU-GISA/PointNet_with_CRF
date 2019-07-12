import numpy as np
import open3d as o3d
import sys
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python show.py index(0~47) type(1,2,3)")
        exit(0)

    scenes = []
    index = int(sys.argv[1])
    type = int(sys.argv[2])
    with open('scene_name.txt','r') as name:
        for line in name:
            scenes.append(line[:-1]) # Remove the '\n' in the end then append to scene.

        scene_name = scenes[index]
        scene_gt_path = 'graph/gt/' + scene_name + '_gt.pcd'
        scene_pred_path = 'graph/pred/' + scene_name + '_pred.pcd'
        scene_pred_proc_path = 'graph/pred_proc/' + scene_name + '_pred.pcd'
        
        pcd_gt = o3d.io.read_point_cloud(scene_gt_path)
        pcd_pred = o3d.io.read_point_cloud(scene_pred_path)
        pcd_pred_proc = o3d.io.read_point_cloud(scene_pred_proc_path)
        if type == 1:
            o3d.visualization.draw_geometries([pcd_gt])
        elif type == 2:
            o3d.visualization.draw_geometries([pcd_pred])
        elif type == 3:
            o3d.visualization.draw_geometries([pcd_pred_proc])
        else:
            o3d.visualization.draw_geometries([pcd_gt, pcd_pred, pcd_pred_proc])