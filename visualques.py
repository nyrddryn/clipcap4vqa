import os
import cv2
aokvqa_dir = os.getenv('AOKVQA_DIR')

from load_aokvqa import load_aokvqa, get_coco_path
val_dataset = load_aokvqa(aokvqa_dir, 'val')  # also 'val' or 'test'
train_dataset = load_aokvqa(aokvqa_dir, 'train')
test_dataset = load_aokvqa(aokvqa_dir, 'test')


dataset_example = val_dataset[0]
coco_dir = os.getenv('COCO_DIR')
image_path = get_coco_path('val', dataset_example['image_id'], coco_dir)
print(image_path)
img = cv2.imread('image_path', cv2.IMREAD_COLOR)
# cv2.imshow('img',img)
