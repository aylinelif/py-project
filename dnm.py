import cv2
import dlib


detector = dlib.get_frontal_face_detector()


cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read() 
    if not ret:
        break

    
    faces = detector(frame)

    if len(faces) > 0:
        
        x1, y1, x2, y2 = faces[0].left(), faces[0].top(), faces[0].right(), faces[0].bottom()
        face_width_in_pixels = x2 - x1
        face_height_in_pixels = y2 - y1
        face_distance = "Kameraya olan uzaklik: {} piksel".format(face_width_in_pixels)

        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, face_distance, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    
    cv2.imshow('Yuz Tanima', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()