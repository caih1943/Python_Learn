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
#img = mpimg.imread('tramp.jpg')
img = mpimg.imread('myPicture2018.11.jpg')


# img1=img[:,:,2]


img1=img[:,:,2]

img_transp = np.zeros([img.shape[0],
 	img.shape[1], 4])
img_transp[:,:,0:3] =img[:,:,:]/255
img_transp[:,:,3] =0.75
# note that the 1st dimension is height
height=img.shape[0]
width = img.shape[1]

myDpi=300
figsize=[width/myDpi,height/myDpi]
fig=plt.figure(figsize=figsize)
sub=fig.add_subplot(111)

im=sub.imshow(img)

patch =patches.Circle((1400,1200), radius=1200,
 	transform = sub.transData)
# patch =patches.Circle((300,100), radius=100,
 	 #transform = sub.transData) #trump.jpg
#sub.add_patch(patch)#隐藏头像

im.set_clip_path(patch)
#sub.imshow(img_transp)
#sub.imshow(img1, cmap='gray',vmin=0,vmax=255) #单色-灰色
sub.set_axis_off()
fig.subplots_adjust(top=1,bottom=0,right=1,left=0)
#fig.savefig('./me_circle.png', dpi=myDpi) #保存照片到桌面
plt.show()
plt.close(fig)