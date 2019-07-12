import numpy as np
scenes = []
with open('scene_name.txt','r') as name:
        for line in name:
            scenes.append(line[:-1]) # Remove the '\n' in the end then append to scene.

pred_label_filepath = ['before/pred_txt/' + name + '_pred.txt' for name in scenes]
pred_proc_label_filepath = ['after/pred_txt/' + name + '_pred.txt' for name in scenes]
gt_label_filepath = ['gt/gt_txt/' + name + '_gt.txt' for name in scenes]
num_room = len(gt_label_filepath)

gt_classes = [0 for _ in range(13)]
positive_classes = [0 for _ in range(13)]
true_positive_classes = [0 for _ in range(13)]
for i in range(num_room):
	pred_label = np.loadtxt(pred_label_filepath[i])
	pred_label = pred_label[:,-1]
	gt_label = np.loadtxt(gt_label_filepath[i])
	for j in range(gt_label.shape[0]):
		gt_l = int(gt_label[j])
		pred_l = int(pred_label[j])
		gt_classes[gt_l] += 1
		positive_classes[pred_l] += 1
		true_positive_classes[gt_l] += int(gt_l==pred_l)


#print(gt_classes)
#print(positive_classes)
#print(true_positive_classes)

print('############Before############')
print('Overall accuracy: {0}'.format(sum(true_positive_classes)/float(sum(positive_classes))))

print ('IoU per class:')
iou_list = []
for i in range(13):
	if(gt_classes[i] == 0):
		iou = 0
	else:
		iou = true_positive_classes[i]/float(gt_classes[i]+positive_classes[i]-true_positive_classes[i])
	print(iou)
	iou_list.append(iou)

print ('IoU average:')
print(sum(iou_list)/13.0)



gt_classes = [0 for _ in range(13)]
positive_classes = [0 for _ in range(13)]
true_positive_classes = [0 for _ in range(13)]
for i in range(num_room):
	pred_label = np.loadtxt(pred_proc_label_filepath[i])
	gt_label = np.loadtxt(gt_label_filepath[i])
	for j in range(gt_label.shape[0]):
		gt_l = int(gt_label[j])
		pred_l = int(pred_label[j])
		gt_classes[gt_l] += 1
		positive_classes[pred_l] += 1
		true_positive_classes[gt_l] += int(gt_l==pred_l)


#print(gt_classes)
#print(positive_classes)
#print(true_positive_classes)

print('############After############')
print('Overall accuracy: {0}'.format(sum(true_positive_classes)/float(sum(positive_classes))))

print ('IoU per class:')
iou_list = []
for i in range(13):
	if(gt_classes[i] == 0):
		iou = 0
	else:
		iou = true_positive_classes[i]/float(gt_classes[i]+positive_classes[i]-true_positive_classes[i])
	print(iou)
	iou_list.append(iou)

print ('IoU average:')
print(sum(iou_list)/13.0)



