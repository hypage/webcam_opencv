
#this function display the image gray converted from cam 
import cv2

def main():
    cam = cv2.VideoCapture(0)
    while True:
        #read image form camera
        val, img = cam.read()
        #convert to gray image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #display the image
        cv2.imshow("my_cam", gray)
        if c = cv2.waitKey(10) == 27: #check the keyboard each 10 ms
            break # escape to quit
        

    cam.release()# release the cam
    cv2.destroyAllWindows() #destroy the windows
if __name__ == '__main__':
    main()
