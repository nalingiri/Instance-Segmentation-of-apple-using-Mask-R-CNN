import os
import torch
from PIL import Image
#####################################
class AppleDataset(object):
    def __init__(self, root_dir, transforms):
        self.root_dir = root_dir
        self.transforms = transforms
        # Load all image
        self.imgs = list(sorted(os.listdir(os.path.join(root_dir, "images"))))

    def __getitem__(self, idx):
        # Load images
        img_path = os.path.join(self.root_dir, "images", self.imgs[idx])
        img = Image.open(img_path).convert("RGB")
        image_id = torch.tensor([idx])
        target = {}
        target["image_id"] = image_id
        if self.transforms is not None:
            img, target = self.transforms(img, target)

        return img, target

    def __len__(self):
        return len(self.imgs)

    def get_img_name(self, idx):
        return self.imgs[idx]
