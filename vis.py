from ultralytics import YOLO
import cv2

# 모델 로드 (학습한 best.pt 경로 넣어줘)
model = YOLO(r"runs\detect\train6\weights\best.pt")

# 이미지 불러오기
img_path = "frame00.png"   # 테스트할 이미지 경로
results = model.predict(source=img_path, save=False, conf=0.25)

# 결과 시각화
for r in results:
    im_array = r.plot()  # 바운딩박스/라벨 시각화된 이미지
    cv2.imwrite("result.jpg", im_array)  # 결과를 파일로 저장
    # GUI 환경 가능하면 아래 코드로 창에 표시 가능
    # cv2.imshow("Result", im_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
