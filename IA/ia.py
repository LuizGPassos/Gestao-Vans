import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

    text = pytesseract.image_to_string(gray, config='--psm 11')
    print(text)

    cv2.putText(frame, text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Car Plate Recognition", frame)
    cv2.waitKey(0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
