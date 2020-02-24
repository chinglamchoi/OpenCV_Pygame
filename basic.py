import cv2
import os

def main():
    webcam_id = 0
    cap = cv2.VideoCapture(webcam_id)
    width, height = 1280, 720
    cap.set(3, width)
    cap.set(4, height)
    width, height = int(cap.get(3)), int(cap.get(4)) #real width height depends on ur screen size not preset
    frame_count = 0

    out_dir = input("Output vid save dir with slash: ")
    try:
        os.mkdir(out_dir)
    except:
        pass #already exists

    out_file = input("Output vid file name not extension: ")
    fourcc = cv2.VideoWriter_fourcc("M", "J", "P", "G") #set video codec
    out_vid_fps = 30

    out = cv2.VideoWriter(out_dir + out_file + ".avi", fourcc, out_vid_fps, (width, height))

    try: #there are better ways to exit but im lazy
        while True:
            ret, frame = cap.read()
            cv2.imshow("output stream", frame)
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    except (KeyboardInterrupt, SystemExit):
        cap.release() 
        out.release() #vid should be automatically saved in dir
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
