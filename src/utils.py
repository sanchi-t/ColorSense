import datetime
import os
import numpy as np
import cv2 as cv
from flask import current_app as app


OUTPUT_FOLDER = os.path.join('static', 'output')


segmented_images = {}  # Global dictionary to store segmented images and labels


def change_segment_colors(image_path: str, colors: list):
    img = cv.imread(image_path)
    with open('text.txt','w') as convert_file:
        convert_file.write(str(segmented_images))
    if image_path in segmented_images:
        labels, _ = segmented_images[image_path]
    else:
        return None  # Image not found in the segmented images dictionary

    # Assign colors to the segments based on the labels
    # colored_image = np.zeros_like(img)
    # for segment_label, color in zip(np.unique(labels), colors):
    #     segment_mask = np.where(labels == segment_label, 255, 0).astype(np.uint8)
    #     colored_segment = cv.merge([segment_mask * color[0], segment_mask * color[1], segment_mask * color[2]])
    #     colored_image = cv.bitwise_or(colored_image, colored_segment)

    # # Combine the colored segments with the original image
    # modified_image = cv.bitwise_and(img, cv.bitwise_not(colored_image))
    # modified_image = cv.bitwise_or(modified_image, colored_image)
    img[1] = [0, 0, 255]
    # Save the modified image
    cv.imwrite('static\output\dome.jpg', img)

    return img



def allowed_file(filename):
    file_extension = filename.split(".")[-1] in ("jpg", "jpeg", "png", "webp", "mp4", "mov", "avi")

    if not file_extension:
        raise HTTPException(status_code=415, detail="Unsupported file provided.")

def image_segment(img_filepath: str, K, colors, attempts=10):
    if img_filepath.split(".")[-1] in ("mp4", "mov", "avi"):
        print("\nFile is not an image")
        return 
    else:
        print("\nFile is an image",flush=True)
        img = cv.imread(img_filepath)
        img2 = img.reshape((-1, 3))
        img2 = np.float32(img2)

        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, attempts, 1.0)
        
        if img_filepath in segmented_images:
            label, center = segmented_images[img_filepath]
        else:
            ret, label, center = cv.kmeans(img2, K, None, criteria, attempts, cv.KMEANS_RANDOM_CENTERS)
            segmented_images[img_filepath] = (label, center)
        
        # ret, label, center = cv.kmeans(img2, K, None, criteria, attempts, cv.KMEANS_RANDOM_CENTERS)
        # segmented_images[img_filepath] = (label, center)
        # black_color = np.argmax(np.bincount(label.flatten()))
        # center = np.uint8(center)
        # center = np.ones((K,1), dtype = 'uint8') * 255
        # center[black_color] = [0]
        for i in range(len(colors)):
            center[i]=colors[i]
        # center[0]=colors[0]
        # center[1]=colors[1]
        # center[2]=colors[2]
        # center[3]=colors[3]
        print('Tf is this shit ',center,flush=True)
        # res = center[label.flatten()]
        # res2 = res.reshape((img.shape))
        res = center[label.flatten()]
        res2 = res.reshape((img.shape[0], img.shape[1], 3)) 


        filename = img_filepath.split("/")[-1].split(".")[0]
        output_image_path = os.path.join('/kmeanai/src/static/output/','output_image_{name}.jpg'.format(name=filename))
        print(f"========================\nImage processed: {output_image_path}\n",flush=True)
        cv.imwrite(output_image_path, res2)
        print('segmented_imgae',segmented_images)
        return f'output_image_{filename}.jpg'