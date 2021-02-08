import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import matplotlib.patches as patches

#random figure
width=1600
height=900
#arr_onecolor=np.random.rand(height,width)
arr=np.zeros([height,width,3])
for i in range(3):
	arr_onecolor=np.random.rand(height,width)
	#arr=np.zeros([height,width,3])
	arr[:,:,i]=arr_onecolor[:,:]

#read a photo
img = mpimg.imread('myPicture2018.11.jpg')
#print(img.shape)

img1=img[:,:,2]

myDpi=300
figsize=[width/myDpi,height/myDpi]
fig=plt.figure(figsize=figsize)
sub=fig.add_subplot(111)

#sub.imshow(img) #彩色
sub.imshow(img1, cmap='gray',vmin=0,vmax=255) #单色-灰色
sub.set_axis_off()
fig.subplots_adjust(top=1,bottom=0,right=1,left=0)
#fig.savefig('./happy_gray.png', dpi=myDpi) #保存单色照片到桌面
plt.show()
plt.close(fig)