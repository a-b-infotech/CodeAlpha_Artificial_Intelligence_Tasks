import cv2
from ultralytics import YOLO

def run_tracking():
    # Load free lightweight pre-trained YOLOv8 Nano model
    model = YOLO("yolov8n.pt")

    # 0 for default webcam, or specify a path: "traffic.mp4"
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video/camera source.")
        return

    print("Starting tracker. Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run tracking (ByteTrack is configured natively via persist=True)
        results = model.track(frame, persist=True, tracker="bytetrack.yaml", verbose=False)

        # Annotate bounding boxes and IDs
        annotated_frame = results[0].plot()

        cv2.imshow("CodeAlpha AI - Object Detection & Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_tracking()