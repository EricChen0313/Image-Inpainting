import opt
import torch
from PIL import Image
from torchvision.utils import save_image
from util.image import unnormalize
from torchvision import transforms

def evaluate(model, dataset, device):
    image, mask, _ = dataset[10]
    image = image.unsqueeze(0)
    mask = mask.unsqueeze(0)
    with torch.no_grad():
        output, _ = model(image.to(device), mask.to(device))

    output = output.to(torch.device('cpu'))

    save_image(unnormalize(output), "OUTPUT2.jpg")
    save_image(unnormalize(image), "INPUT2.jpg")

def EvaluateSingle(model, size, imgpath, maskpath, device):
    img_transform = transforms.Compose([transforms.Resize(size=size), transforms.ToTensor(),transforms.Normalize(mean=opt.MEAN, std=opt.STD)])
    mask_transform = transforms.Compose([transforms.Resize(size=size), transforms.ToTensor()])

    gt_img = Image.open(imgpath)
    gt_img = img_transform(gt_img.convert('RGB'))

    mask = Image.open(maskpath)
    mask = mask_transform(mask.convert('RGB'))

    image = gt_img * mask
    
    image = image.unsqueeze(0)
    mask = mask.unsqueeze(0)
    gt_img = gt_img.unsqueeze(0)

    with torch.no_grad():
        output, _ = model(image.to(device), mask.to(device))

    output = output.to(torch.device('cpu'))

    save_image(unnormalize(output), "OUTPUTTT.jpg")
    save_image(unnormalize(gt_img), "INPUTTT.jpg")
