# Instance-Segmentation-of-apple-using-Mask-R-CNN


# Install
1) Python 3.6
2) Numpy 1.16.0 (Other Numpy may create problem.)

# Training 
1) Create a folder name "output_mrcnn" in "Instance-Segmentation-of-apple-using-Mask-R-CNN"  folder.
2) Command line to train the model:-

python train_mrcnn.py --data_path /home/nalin/Instance-Segmentation-of-apple-using-Mask-R-CNN/data_set/ --model mrcnn --epoch 50 --output_dir /home/nalin/Instance-Segmentation-of-apple-using-Mask-R-CNN/output_mrcnn

3) Resume Training:-

python train_mrcnn.py --resume /path_to_model/model_39.pth --epoch 40 --output-dir /path/output_mrcnn

# prediction
1) Create a folder name "prediction_mrcnn" in "Instance-Segmentation-of-apple-using-Mask-R-CNN"  folder. Create a file name "out_data.txt".
2) make a folder of "new_images" in data_set/test/.

