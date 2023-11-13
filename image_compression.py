from PIL import Image
import os
import cv2

folder = 'images'
step = 5

dir_list = os.listdir(folder)
os.mkdir('compressed')
 
for Q in range(1, 100, step):
    current_folder = f'compressed/{folder}_{Q}'
    os.mkdir(current_folder)

    for im_name in dir_list:
        im = Image.open(f'{folder}//{im_name}')
        im.save(f'{current_folder}//{im_name}', format="JPEG", quality=Q)
        with open( f'{current_folder}//{im_name}', 'rb') as im :
            # im.seek(-2,2)
            # if im.read() == b'\xff\xd9':
            #     print('Image OK :', f'{current_folder}//{im_name}') 
            # else: 
                # fix image
                img = cv2.imread(f'{current_folder}//{im_name}')
                cv2.imwrite(f'{current_folder}//{im_name}', img)
                print('FIXED corrupted image :', f'{current_folder}//{im_name}')   
