# PointNet + CRF

利用条件马尔科夫随机场对 PointNet 的语义分割结果进行后处理



### 环境:

```shell
Cython==0.29.12  
h5py==2.9.0    
numpy==1.16.4   
open3d-python==0.7.0.0     
pydensecrf==1.0rc3   
```



### 工程文件:

```python
|-raw/	#从PointNet获得的原始语义分割数据,包含groundtruth, prediction, 格式为 x,y,z,r,g,b
|-gt/	#从raw中pick出来的grountruth文件
	|- gt_obj/
	|_ gt_txt/
|-before/	#从raw中pick出来的prediction文件
	|- pred_obj/
	|_ pred_txt/
|-after/	#before中的prediction文件后处理后的结果
	|- pred_obj/
	|_ pred_txt/
|-eval/		#eval_iou_accuracy.py运行后结果存放地
|-graph/	#对结果进行可视化后,pcd图文件存放地
	|- gt/
	|- pred/
	|- pred_proc/
	|_ scene_name.txt
|-postproc.py	#后处理程序, 参数为 CRF 的probability 和 compat
|-plot.py		#绘图程序,将gt,pred,pred + proc的结果分别作图后保存为pcd文件
|-show.py		#展示上述的pcd文件, 参数为场景索引 index(0~47) 和 type(1,2,3,other)
|-eval_iou_accuracy.py	#结果评估程序
|-pick.py		#PointNet原始结果分拣程序
|-autorun.sh	#批量运行后处理并保存评估结果的bash
|_scene_name.txt
```



### 使用方法:

1. 进入postproc文件夹并运行如下命令得到批量结果存于eval文件夹

```
bash autorun.sh
```

2. 单步运行
   - 分拣:将PointNet原始结果拷贝至raw文件夹, 运行python pick.py
   - 后处理: python postproc.py	probability(float)	compat(int)
   - 绘图: python plot.py
   - 评估: python eval_iou_accuracy.py
   - 展示: python show.py	index	type