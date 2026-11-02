import cv2
import numpy as np
from tkinter import filedialog

files = filedialog.askopenfilenames(
    initialdir="/",
    title="파일 열기",
    filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*"))
)

if not files:
    print("파일이 선택되지 않았습니다.")
    exit()

def imread_unicode(filepath, flags=cv2.IMREAD_COLOR):
    try:
        np_array = np.fromfile(filepath, dtype=np.uint8)
        return cv2.imdecode(np_array, flags)
    except Exception as e:
        print(f"이미지 로드 실패: {e}")
        return None

img_color = imread_unicode(files[0], cv2.IMREAD_COLOR)
if img_color is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

win_name = "Canny Color Edge Control"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win_name, img_color.shape[1], img_color.shape[0] + 90)

cv2.createTrackbar("Thresh1", win_name, 50, 255, lambda x: x)
cv2.createTrackbar("Thresh2", win_name, 150, 255, lambda x: x)
cv2.createTrackbar("Thickness", win_name, 1, 5, lambda x: x)

background = np.full_like(img_color, 255)

while True:
    t1 = cv2.getTrackbarPos("Thresh1", win_name)
    t2 = cv2.getTrackbarPos("Thresh2", win_name)
    thick = cv2.getTrackbarPos("Thickness", win_name)

    edge_mask = cv2.Canny(img_blur, t1, t2)

    if thick > 0:
        kernel = np.ones((thick + 1, thick + 1), np.uint8)
        edge_mask = cv2.dilate(edge_mask, kernel, iterations=1)

    img_colored_edges = np.where(edge_mask[:, :, None] == 255, img_color, background)
    cv2.imshow(win_name, img_colored_edges)

    key = cv2.waitKey(30) & 0xFF
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()