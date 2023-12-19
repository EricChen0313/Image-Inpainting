# Writing a White-Balance program 撰寫白平衡之程式

## English version

- Whate is White balance?

  - It refers to the adjustment of the relative color tones of white and other colors in an image in photography, videography, or image processing. Its purpose is to eliminate color casts that may occur in images under different lighting conditions, ensuring that white appears pure and accurate.
  - In the concept of white balance, white is considered a neutral color, and when white in an image appears to be biased towards blue, yellow, or other colors, it can give an unnatural look. Therefore, adjusting white balance helps correct these color biases and ensures that colors in the image are closer to the true scene.

- In this repository, there are examples of two white balance methods in the sample scripts. One (gray-world.py) is suitable for cases where there is a white point in the image; for cases where there is no white point in the photo, it is more appropriate to use the other method (advanced-white-patch.py). Therefore, before running the program, you can observe your images to choose the appropriate white balance method.
  - Using the Max White method and Gray World method to adjust white balance typically requires a reference point in the image that is recognized as white. The principles of these two methods are as follows:
    - Max White Method: This method assumes that the brightest area in the image should be white. The algorithm looks for the brightest point in the image and sets it as the white reference point, then adjusts the overall color balance based on that point.
    - Gray World Method: This method assumes that the entire world in the image is on average gray, meaning the average value of all color channels in the image should be gray. The algorithm calculates the average values of all color channels in the image and sets it as the white reference point for white balance adjustment.
  - If there are no white points in the photo, these two methods may lead to inaccurate white balance adjustments because they rely on a point in the image being identified as a white reference, and without such a reference, the chosen point may be inaccurate.
  - In practical shooting, ensuring there is a pure white reference point or an area with average gray values in the photo is often more feasible. This can be achieved by using a white card or gray card to set a known color region in the shooting scene. By using such a reference point, white balance correction can be more accurately performed, resulting in more realistic and accurate colors in the image.

## Traditional Chinese version

- 什麼是白平衡?

  - 指在攝影、攝影或影像處理中，調整影像中白色和其他顏色的相對色調，以使場景中的顏色看起來自然而準確。 它的目的是在不同的光源下，消除影像中可能出現的色偏，確保白色在不同光照條件下都呈現為純淨的白色。
  - 在白平衡的概念中，白色被認為是中性的顏色，當一張影像中的白色看起來偏向藍色、黃色或其他顏色時，就會引起觀感上的不自然。 因此，透過調整白平衡，我們可以校正這種色偏，使影像中的顏色更貼近真實場景。

- 在這個 Repo 中，有兩種白平衡方式的範例程式，一('gray-world.py')為如照中有白點，可適用之方法;若照片中沒有白點，則使用另一方法('advanced-white-patch.py')較合適。因此，若要執行程式前，可以先觀察你的圖片，以選擇合適的白平縫方式。
  - 使用最大值法和灰色世界法來調整白平衡通常需要影像中存在被認定為白色的參考點，以便演算法可以根據該參考點調整整個影像的色彩平衡。 這兩種方法的原理如下：
    - 最大值法（Max White）： 此方法假定影像中最亮的區域應為白色。 演算法會尋找影像中的最亮點，並將其設定為白色參考點，然後根據該點進行白平衡調整。
    - 灰色世界法（Gray World）： 這種方法假定整個世界在灰階上是平均的，即影像中所有顏色的平均值應該是灰色。 演算法計算影像中所有色彩通道的平均值，將其設定為白色參考點，然後進行白平衡調整。
  - 如果照片中沒有白色點，那麼這兩種方法可能會產生不準確的白平衡調整。 因為它們都依賴影像中的某個點被確定為白色參考點，而在沒有白色參考的情況下，選擇的點可能不準確。
  - 在實際拍攝中，確保照片中有一個純白色的參考點或灰階平均的區域通常更容易實現準確的白平衡調整。 這可以透過使用白色卡或灰卡在拍攝場景中設定一個已知顏色的區域來實現。 透過使用這樣的參考點，可以更精確地進行白平衡校正，使影像的顏色更真實和準確。

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
   ![python extension](https://github.com/EricChen0313/A-watermarking-technique-based-on-the-least-significant-bit/blob/main/HW1_A%20watermarking%20technique%20based%20on%20the%20least%20significant%20bit/ImageExampleFolder/python%20extension%20in%20VSCode.jpg)
3. Open Anaconda prompt, and enter the command 'pip install opencv-python', then you can use opencv in VSCode.

## Give it a try with yourself

```bash
# clone the repo
$ git clone https://github.com/EricChen0313/A-watermarking-technique-based-on-the-least-significant-bit.git

# open the folder in Visual Studio Code

# push the 'Terminal' button above
$ cd code                   # Now, you are under the code folder. 
$ python your_file_name.py  # Replace the file name you want to run. 

# then it will give out the white-balance picture
```

## Result

![comparison 2](https://github.com/EricChen0313/white-balance/blob/main/white%20balance/result/comparison2%20emphasized%20version.jpg)
![comparison 1](https://github.com/EricChen0313/white-balance/blob/main/white%20balance/result/comparison1.jpg)

<table>
    <tr> 
        <td>position</td>
        <td>explanation</td>
    </tr>
    <tr> 
        <td>Left top corner</td>
        <td>Picture before WB.</td>
    </tr>
    <tr> 
        <td>Right top corner</td>
        <td>Picture after WB w/ gray-world method.</td>
    </tr>
     <tr> 
        <td>Left bottom corner</td>
        <td>Picture before WB.</td>
    </tr>
    <tr> 
        <td>Right bottom corner</td>
        <td>Picture after WB w/ advanced-white-patch method.</td>
    </tr>
</table>

## What's included

```
hw1_white balance
├── ImageExampleFolder/
│   └── python extension in VSCode.jpg   #Indicative sample image
|
├── dataset/
│   └── cafe.jpg                    # Original image before WB
│   └── cat inside.jpg              # Original image before WB
│   └── evening view.jpg            # Original image before WB
│   └── night view.jpg              # Original image before WB
│   └── resized cafe.jpg            # Reized image before WB
│   └── resized evening view.jpg    # Reized image before WB
│   └── resized night view.jpg      # Reized image before WB
|
├── code/
│   └── advanced-white-patch.py     #Turning the RGB image to gray onn
│   └── gray-world.py               #The code using a watermarking technique based on the least
│   └── resize.py                   #The code using a watermarking technique based on the least significant bit
│   └── resize_code.py            #Resizing the image to the desired viewing size
|
├── result/
│   └── cafe result with advanced-white-patch.jpg
│   └── cafe result with gray-world.jpg
│   └── cat inside result with advanced-white-patch.jpg
│   └── cat inside result with gray-world.jpg
│   └── evening view result with advanced-white-patch.jpg
│   └── evening view result with gray-world.jpg
│   └── night view result with advanced-white-patch.jpg
│   └── night view result with gray-world.jpg
│   └── comparison1.jpg
│   └── comparison2.jpg
│
└── README.md
```

## References

- [白平衡 - 瞭解數位攝影的白平衡](http://notepad.yehyeh.net/Content/Photograph/ExposureGuide/white-balance.php)
- [Image.fromarray 的用法（實作 array 到 image 的轉換）](https://blog.csdn.net/weixin_39450145/article/details/103874310)
- [Python 中的 X[:,0]和 X[:,1]](https://blog.csdn.net/a394268045/article/details/79104219)
- [白平衡演算法之 Gray World、White Patch、SoG-CSDN 博客](https://blog.csdn.net/weixin_43194305/article/details/101758864?ops_request_misc=&request_id=&biz_id=102&utm_term=WHITE%20PATCH&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-101758864.nonecase&spm=1018.2226.3001.4187)
- [基礎知識之————直方圖](https://blog.csdn.net/ty197846/article/details/120472710?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169647463216800225573884%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=169647463216800225573884&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-120472710-null-null.142%5Ev94%5EchatsearchT3_1&utm_term=%E7%9B%B4%E6%96%B9%E5%9B%BE&spm=1018.2226.3001.4187)
