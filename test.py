import requests
import cv2
import supervision as sv
import matplotlib.pyplot as plt

API_KEY = "gPcWxUnYp7WTZQgXfpNh"
MODEL_ID = "elevator_button_recognition"
VERSION = "1"
image_path = "frame00.png"

url = f"https://detect.roboflow.com/{MODEL_ID}/{VERSION}?api_key={API_KEY}"

with open(image_path, "rb") as f:
    resp = requests.post(url, files={"file": f})

result = resp.json()
print("JSON 결과:", result)

if "predictions" in result:
    image = cv2.imread(image_path)
    detections = sv.Detections.from_inference(result)

    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = box_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    # 파일 저장
    cv2.imwrite("annotated_result.png", annotated_image)
    print("annotated_result.png 저장 완료")

    # matplotlib으로 표시
    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
else:
    print("Error: predictions 키 없음 → 응답 확인 필요:", result)
