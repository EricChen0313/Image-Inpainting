import argparse
import torch
# from torchvision import transforms

# import opt
# from places2 import Places2
# from evaluation import evaluate
from evaluation import EvaluateSingle
from net import PConvUNet
from util.io import load_ckpt

device = torch.device('cpu')
# device = torch.device('cuda')

size = (256, 256)

# img_transform = transforms.Compose([transforms.Resize(size=size), transforms.ToTensor(),transforms.Normalize(mean=opt.MEAN, std=opt.STD)])
# mask_transform = transforms.Compose([transforms.Resize(size=size), transforms.ToTensor()])
# dataset_val = Places2(args.root, './masks', img_transform, mask_transform, 'val')

model = PConvUNet().to(device)
load_ckpt('1000000.pth', [('model', model)])
model.eval()

# evaluate(model, dataset_val, device)
EvaluateSingle(model, size, 'input.jpg', 'Mask.jpg', device)
