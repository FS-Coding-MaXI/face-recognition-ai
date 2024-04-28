import os

import cv2
from insightface.app import FaceAnalysis

app_l = FaceAnalysis(name="buffalo_l", root=".", providers=["CPUExecutionProvider"])
app_l.prepare(ctx_id=0, det_size=(640, 640))

EXAMPLE_DIR = os.path.join("images/teacher-mateusz_osik")
example_files = os.listdir(EXAMPLE_DIR)

for example_file in example_files:
    image = cv2.imread(os.path.join(EXAMPLE_DIR, example_file))
    img = cv2.resize(image.copy(), None, fx=0.2, fy=0.2)
    results = app_l.get(img)
    img_copy = img.copy()
    for i in results:
        print(example_file, i["age"], sep=": ")
        x1, y1, x2, y2 = i["bbox"].astype(int)
        cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 255), 2)

        kps = i["kps"].astype(int)
        for k1, k2 in kps:
            cv2.circle(img_copy, (k1, k2), 2, (255, 255, 0), -1)
    cv2.imshow(example_file, img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
