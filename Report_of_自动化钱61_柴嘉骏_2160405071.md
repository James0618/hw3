# 直方图增强
---
   自动化钱61 柴嘉骏 2160405071
# 1. 绘制直方图
<br>  绘制附件图片的直方图得到如下所示结果：</br>
## 1.1 CityWall
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/citywall.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/citywall1.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/citywall2.jpg?raw=True" width="25%" height="25%"/>
</div>
<div align="center"> Figure1.1 Histogram of CityWall </div>

## 1.2 Elain
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/elain.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/elain1.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/elain2.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/elain3.jpg?raw=True" width="20%" height="20%"/>
</div>
<div align="center"> Figure1.2 Histogram of Elain </div>

## 1.3 Lena
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/lena.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/lena1.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/lena2.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/lena4.jpg?raw=True" width="20%" height="20%"/>
</div>
<div align="center"> Figure1.3 Histogram of Lena </div>

## 1.4 Woman
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/woman.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/woman1.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task1/woman2.jpg?raw=True" width="25%" height="25%"/>
</div>
<div align="center"> Figure1.4 Histogram of Woman </div>

<br>  从直方图中可以看到，一组相似图片在直方图上也几乎一样，不过是在原图像的基础上加入了一定的噪声或是在调色板上进行了改动。</br>

# 2. 直方图均衡
<br>  对于离散取值的图片，使用其概率与求和代替处理概率密度与积分，使用直方图均衡对图片进行处理，从结果可以看到进行直方图均衡后的图片，其直方图较为平滑，分布更加均匀。</br>
## 2.1 CityWall
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/citywall.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/citywall1.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/citywall2.jpg?raw=True" width="25%" height="25%"/>
</div>
<div align="center"> Figure2.1 Equalized CityWall </div>

## 2.2 Elain
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/elain.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/elain1.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/elain2.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/elain3.jpg?raw=True" width="20%" height="20%"/>
</div>
<div align="center"> Figure2.2 Equalized Elain </div>

## 2.3 Lena
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/lena.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/lena1.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/lena2.jpg?raw=True" width="20%" height="20%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/lena4.jpg?raw=True" width="20%" height="20%"/>
</div>
<div align="center"> Figure2.3 Equalized Lena </div>

## 2.4 Woman
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/woman.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/woman1.jpg?raw=True" width="25%" height="25%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task2/woman2.jpg?raw=True" width="25%" height="25%"/>
</div>
<div align="center"> Figure2.4 Equalized Woman </div>

   <br>  从上图中可以很明显的看到进行直方图均衡后的图片清晰度，亮度更好地在直方图上分布而不影响整体的对比度。对于特别明亮的图像降低其亮度，对于特别暗的图像提升其亮度，但是我们可以看到图片中的一些细节没有得到改善，得到改善的仅仅是图片整体的情况，这也和直方图均衡是全局性的图像增强有关，其并没有显示图像细节信息的能力。</br>
   
# 3. 直方图规定化
<br>  直方图规定化在原理上十分简单，而且在连续像素分布时能达到目标图像的直方图，但是在实际中的图像是离散像素分布，从下图中我们就可以看到其表现并不出色。本次直方图规定化选取原图的直方图作为目标直方图，下图中从上到下分别是原图、直方图均衡后的图像、进行规定化后的图像。</br>
## 3.1 CityWall
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task3/citywall2.jpg?raw=True" width="50%" height="50%"/>
</div>
<div align="center"> Figure3.1. Specified CityWall </div>

## 3.2 Elain
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task3/elain2.jpg?raw=True" width="50%" height="50%"/>
</div>
<div align="center"> Figure3.2 Specified Elain </div>

## 3.3 Lena
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task3/lena2.jpg?raw=True" width="50%" height="50%"/>
</div>
<div align="center"> Figure3.3 Specified Lena </div>

## 3.4 Woman
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task3/woman.jpg?raw=True" width="50%" height="50%"/>
</div>
<div align="center"> Figure3.4 Specified Woman </div>

<br>  根据上面的处理结果可以看到，对图像进行直方图规定化并不能很好的实现处理的目标，其与源图像的差距仍然十分明显。但是值得称赞的是，每一个图片都是与源图像存在较大差距的，但是经过直方图规定化后的图像已经相较于处理前十分接近源图像，而存在偏差的原因在于图像的离散性导致不能完全保存源图像信息。</br>

# 4. 局部直方图均衡
<br>之前进行的直方图均衡是基于全图信息的，这样的增强很难使图像的局部特征被增强，也就是说这项像素可能会在全局变换中被忽略，因此需要将全局图像划分为局部图像后，再对子图像块进行直方图均衡。在本次作业中使用了7\*7的局部直方图增强方法，对Elain和Lena图像进行处理得到的结果如下所示：</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task4/elain.bmp?raw=True" width="75%" height="75%"/>
</div>
<div align="center"> Figure4.1 Locally Equalized Elain </div>

<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task4/lena.bmp?raw=True" width="75%" height="75%"/>
</div>
<div align="center"> Figure4.2 Locally Equalized Lena </div>

<br>  从以上局部直方图均衡的结果可以看到，图像的细节部分被突出出来了，但是与此同时也产生了很不舒服的“棋盘”效应，局部与全局之间的权衡是进行直方图均衡的一个难点。</br>

# 5. 直方图分割
<br>所谓的分割即为图像的二值化操作，基于图像空域信息的图像分割有很多种，包括灰度平均值法百分比阈值法、基于谷底最小值的阈值法、基于双峰平均值的阈值法、迭代最佳阈值法和OSTU大津法。在本次作业中分别使用了基于双峰平均值的阈值法、迭代最佳阈值法和OSTU大津法进行对比实验。得到的结果如下所示。</br>

## 5.1 基于双峰平均值的阈值法
<br>在基于双峰平均值的阈值法中，实现了一个迭代的过程。每次处理前对直方图数据进行判断，看其是否已经是一个双峰的直方图，如果不是，则对直方图数据进行半径为1（窗口大小为3）的平滑，如果迭代了一定的数量比如1000次后仍未获得一个双峰的直方图，则函数执行失败，如成功获得，则最终阈值取两个双峰的平均值作为阈值。得到如下图所示结果：</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task5/elain/elain_doublePeak.bmp?raw=True" width="40%" height="40%"/>
</div>
<div align="center"> Figure5.1 Average of Elain & Woman </div>
<br>由于Woman图像在多次迭代后仍不是双峰图像，因此并没有对Woman图像的该算法处理结果。</br>

## 5.2 迭代最佳阈值法
<br>该算法先假定一个阈值，然后计算在该阈值下的前景和背景的中心值，当前景和背景中心值得平均值和假定的阈值相同时，则迭代中止，并以此值为阈值进行二值化。</br>
<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task5/elain/elain_iteration.bmp?raw=True" width="40%" height="40%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task5/woman/woman_iteration.bmp?raw=True" width="40%" height="40%"/>
</div>
<div align="center"> Figure5.2 Iteration of Elain & Woman </div>

<br>从结果中可以看到，与双峰法不同，双峰法的阈值更大，将更多的像素点判断为背景并显示为黑色，但是保留了更多的细节，总体的表现要由于表现效果不稳定的双峰法。</br>

## 5.3 OSTU大津法
<br>OTSU算法又称为最大类间方差法,对于一幅图像，设当前景与背景的分割阈值为t时，前景点占图像比例为w0，均值为u0，背景点占图像比例为w1，均值为u1。则整个图像的均值为u=w0\*u0+w1\*u1。建立目标函数g(t)=w0\*(u0-u)^2+w1\*(u1-u)^2，g(t)就是当分割阈值为t时的类间方差表达式。OTSU算法使得g(t)取得全局最大值，当g(t)为最大时所对应的t称为最佳阈值。以下为使用OSTU法计算得到的阈值进行分割的结果：</br>

<div align="center">
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task5/elain/elain_OSTU.bmp?raw=True" width="40%" height="40%"/>
  <img src="https://github.com/James0618/Images/blob/master/Content_2/task5/woman/woman_OSTU.bmp?raw=True" width="40%" height="40%"/>
</div>
<div align="center"> Figure5.3 OSTU of Elain & Woman </div>
<br>可以清晰地看到，OSTU法分割的效果要远远优于前两个算法，该算法更能从大体上反应图像的真实情况，在细节和图像全局信息上都处理的很出色。</br>

# 6. 总结
<br>以上是本次实验的全部结果，基于直方图的各种图像增强操作都没有很好的实现增强这一目的，仅仅是从某一层面上对图像的全局信息进行均衡或分割等操作，没有考虑到图像的细节信息，因此效果较差。</br>
