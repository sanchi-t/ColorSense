# import numpy as np
# import cv2 as cv
# from flask import Flask, jsonify, request




# app = Flask(__name__)
  
# # on the terminal type: curl http://127.0.0.1:5000/
# # returns hello world when we use GET.
# # returns the data that we send when we use POST.
# @app.route('/', methods = ['GET', 'POST'])
# def home():
#     if(request.method == 'GET'):
  
#         data = "hello world"
#         return jsonify({'data': data})


# @app.route('/image/<image>')
# def getImage(image):
#     # if(request.method == 'GET'):
  
#     data = "hello world"
#     return image




# img=cv.imread('D:\sanchit\download\passport.jpg')
# img2=img.reshape((-1,3))
# print(img.shape,img2.shape,type(img2))
# img2=np.float32(img2)

# attempts=10

# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, attempts, 1.0)
# K = 3
# ret,label,center=cv.kmeans(img2,K,None,criteria,attempts,cv.KMEANS_RANDOM_CENTERS)

# # Now convert back into uint8, and make original image
# center = np.uint8(center)
# res = center[label.flatten()]
# res2 = res.reshape((img.shape))
# print(res2.shape)

# cv.imshow('res2',res2)
# cv.waitKey(0)
# cv.destroyAllWindows()

# if __name__ == '__main__':
  
#     app.run(debug = True)


from flask import Flask, request, jsonify,render_template,send_file,session
import cv2 as cv
import os
import numpy as np
from utils import allowed_file,image_segment,change_segment_colors
import sys 

app = Flask(__name__, static_folder='static')


UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
OUTPUT_FOLDER = os.path.join(app.static_folder, 'output')

# UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = set(['txt','jpg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.path.dirname("../templates")
app.secret_key = 'xyz'






@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def uploadFile():
    if not os.path.exists(app.config['UPLOAD_FOLDER']): # Create Directory for the uploaded static
        os.mkdir(app.config['UPLOAD_FOLDER'])
    _kvalue=request.form['quantity']
    _img = request.files['file-uploaded']
    filename = _img.filename
    allowed_file(filename)
    # _img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # _img.save(os.path.join(app.root_path, 'static', 'uploads', filename))
    save_path = os.path.join(app.root_path, 'static', 'uploads', filename)
    print(save_path,flush=True)
    _img.save(save_path)
    session['uploaded_img_file_path'] = filename
    print('filename:  asna ',filename,flush=True)
    session['k_value']=_kvalue

    return render_template('index.html', success = True)


@app.route('/show_file')
def displayImage():
    img_file_path = session.get('uploaded_img_file_path', None)
    k_value=int(session.get('k_value',None))
    host_img_file_path = os.path.join('D:/sanchit/programming_shit/AIML/dockerok/src/static/uploads', img_file_path)
    print(host_img_file_path,' ghjk ',img_file_path,flush=True)
    return render_template('show_file.html', user_image = img_file_path, is_image= True, is_show_button=True,k_value=k_value)


@app.route('/detect_object',methods=["POST"])
def detectObject():
    uploaded_image_path = session.get('uploaded_img_file_path', None)
    k_value=int(session.get('k_value',None))
    img_path='/kmeanai/src/static/uploads/'+uploaded_image_path
    print('IMGAGE ',img_path,flush=True)
    colors = []
    for i in range(k_value):
        color_str=request.form[f'color{i}']
        colors.append([int(x) for x in color_str.split(',')])
    output_image_path=image_segment(img_path,k_value,colors)
    # output_image_path='output/'+uploaded_image_path
    # modified_image=change_segment_colors('static\\uploads\\passport.jpg',[(255, 0, 0), (0, 255, 0), (0, 0, 255)])
    # print('modified_image',modified_image,'output_image',output_image_path)

    return render_template('show_file.html',  user_image=output_image_path, is_image= True, is_show_button=False, k_value=k_value)
    

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg'))
    # Process the uploaded image here
    return 'Image uploaded successfully'



if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run(debug=True)
