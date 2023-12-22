# Image Inpainting for Irregular Holes Using Partial Convolutions

## English version

- What is Image Inpainting?

  - Image inpainting is a computer vision and graphics technique used to fill in missing or damaged parts of an image. The goal is to reconstruct the missing information seamlessly, making the inpainted regions visually consistent with the surrounding areas. This process involves predicting and generating plausible content for the damaged or masked regions based on the available information in the image.
  - Various inpainting methods utilize different approaches, such as patch-based algorithms, deep learning techniques, or a combination of both. These methods aim to address issues like removing unwanted objects, restoring damaged portions, or completing incomplete scenes in images. Image inpainting finds applications in image editing, restoration, and the enhancement of visual content.

- In this repository, we reference the method presented in "Image Inpainting for Irregular Holes Using Partial Convolutions" from 2018 and apply this technique to inpaint faces and accessories.

## Traditional Chinese version

- 什麼是圖像修補?

  - 圖像修補是一種計算機視覺和圖形技術，用於填補圖像中缺失或損壞的部分。其目標是無縫地重建缺失的信息，使修補區域在視覺上與周圍區域一致。這個過程涉及根據圖像中的可用信息，預測並生成損壞或被遮擋區域的合理內容。
  - 各種修補方法使用不同的方法，包括基於補丁的算法、深度學習技術，或兩者的結合。這些方法旨在解決一些問題，如移除不需要的對象、恢復損壞的部分，或完成圖像中的不完整場景。圖像修補在圖像編輯、修復和增強視覺內容等領域中得到應用。

- 在這個 Repo 中，我們參考出自於 2018 年的"Image Inpainting for Irregular Holes Using Partial Convolutions"，並使用此方法來針對人臉以及配飾做填補。

## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [Give it a try with yourself](#give-it-a-try-with-yourself)
- [Result](#result)
- [What's included](#whats-included)
- [References](#references)

## Environment

Windows 10 64-bit, Visual Studio Code, Python @3.11.5, Anaconda3.

## Installation

1. Download [VSCode](https://code.visualstudio.com/Download), [Anaconda](https://www.anaconda.com/download).
2. After VScode install completely, you can use the Extension in VSCode. Searching for the Python package to plug in.
3. Open Anaconda prompt, and enter the command 'pip install opencv-python', then you can use opencv in VSCode.
4. Model weight can be downloaded [here](https://drive.google.com/file/d/1PgcE4hNlf7ML5H68wd5nXwQXa9YBKGzO/view). If there is any problem, feel free to ask us.
   m11202107@gapps.ntust.edu.tw , m11202125@gapps.ntust.edu.tw .

## Give it a try with yourself

```bash
###REMINDER###
# Before run your own pics, please RENAME it as 'input.jpg'.
# Then put it in this folder.
# Also download the weight, this can be available

# clone the repo
$ git clone https://github.com/EricChen0313/Image-Inpainting.git

# open the folder in Visual Studio Code

# push the 'Terminal' button above#
$ pip install -r requirements.txt   # Install python requirements.
$ python ImageInpainting.py         # Run the code.

# then it will give out the result.
# go to check the 'OUTPUTTT.jpg' you generated.
```

## Result

![Remove mole & nose ring](https://github.com/EricChen0313/Image-Inpainting/blob/main/Image%20Inpainting/reference%20pics/mole%20and%20nose%20ring.png)
![Remove earring & logo](https://github.com/EricChen0313/Image-Inpainting/blob/main/Image%20Inpainting/reference%20pics/earring%20and%20logo.png)
![Remove scar & tattoo](https://github.com/EricChen0313/Image-Inpainting/blob/main/Image%20Inpainting/reference%20pics/scar%20and%20tattoo.png)

## What's included

```
Image Inpainting
├── _pycache_/
├── imgs/
├── models/
├── reference pics/
│   └── earring and logo.png
│   └── mole and nose ring.png
│   └── scar and tattoo.png
|
├── util/
|
├── INPUTTT.jpg        # the image you want to inpaint
├── Mask.jpg           # the mask you MaskCreator to generate
├── ImageInpainting.py
├── OUTPUTTT.jpg       # the result
├── evaluation.py
├── input.jpg
├── train.py
├── generate_data.py
├── places2.py
├── loss.py
├── net.py
├── opt.py
├── requirements.txt
├── test.py
│
└── README.md
```

## References

- [the dataset of human face](https://www.kaggle.com/datasets/ashwingupta3012/human-faces)
- [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/pdf/1804.07723.pdf)
- [詳解 Partial Convolution](https://zhuanlan.zhihu.com/p/519446359)
- [Official Partial Convolution Layer for Padding and Image Inpainting](https://github.com/NVIDIA/partialconv)
