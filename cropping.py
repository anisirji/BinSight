import cv2
import glob
import os
from ultralytics import YOLO

model = YOLO("./runs/detect/train5/weights/last.pt")
folder_path = './bins'
image_pattern = '*.jpg' 
output_folder = './output'
os.makedirs(output_folder, exist_ok=True)

def saveOutput(output_folder,cropped_image,filename):
    output_path = os.path.join(output_folder, f'cropped_{filename}')
    cv2.imwrite(output_path, cropped_image)

def crop_image(image, x1, y1, x2, y2, filename, output_folder):
    # Convert x1, y1, x2, y2 to integers
    x1, y1, x2, y2 = map(int, [x1, y1-100, x2, y2])

    cropped_image = image[y1:y2, x1:x2]
    saveOutput(output_folder, cropped_image, filename)
    return cropped_image


def predictDustbins(image_file, image,filename,output_folder):
    print("predicting images")
    results = model.predict(image_file)

    for detection in results:
        boxes = detection.boxes.numpy()
        xyxy=boxes.xyxy

        for box in xyxy:
            x1 = box[0]
            y1 = box[1]
            x2 = box[2]
            y2 = box[3]
            print(x1,y1,x2,y2)
            crop_image(image,x1,y1,x2,y2,filename,output_folder)
   
    

def main():
    image_files = glob.glob(f'{folder_path}/{image_pattern}')

    x1, y1, x2, y2 = 100, 50, 300, 200 



    for image_file in image_files:
        image = cv2.imread(image_file)
        filename = os.path.basename(image_file)

        predictImages = predictDustbins(image_file,image,filename,output_folder)
        # saveOutput(output_folder,cropped_image,filename)

        cv2.destroyAllWindows()


main()