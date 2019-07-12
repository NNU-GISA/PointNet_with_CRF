import numpy as np
import open3d as o3d
import os


def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            if '.obj' in filename:
                apath = os.path.join(maindir, filename)
                result.append([apath, filename])
    return result


if __name__ == "__main__":
    classes = ["gt/gt_obj", "before/pred_obj", "after/pred_obj"]
    save_folder = ["graph/gt/", "graph/pred/", "graph/pred_proc/"]
    shiftX = 3

    with open('graph/scene_name.txt', 'w') as name:
        for index, item in enumerate(classes):
            all_file = all_path(item)
            for file_path, file_name in all_file:
                cloud = []
                with open(file_path, "r") as fr:
                    for line in fr:
                        temp = []
                        for s in line.split():
                            if s != 'v':
                                temp.append(float(s))
                        cloud.append(temp)
                cloud = np.array(cloud)

                coord = cloud[:, 0:3].astype(np.float32)
                color = cloud[:, 3:6].astype(np.uint32)
                pcd = o3d.PointCloud()
                pcd.points = o3d.Vector3dVector(coord + shiftX * index)
                pcd.colors = o3d.Vector3dVector(color)
                #o3d.visualization.draw_geometries([pcd])
                o3d.io.write_point_cloud(save_folder[index] + file_name.split('.')[0] + '.pcd', pcd)

                print("Write file: ", file_name.split('.')[0] + '.pcd')
                if index == 0:
                    name.write(file_name[:-7]+'\n')
