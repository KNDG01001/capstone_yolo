from ultralytics import YOLO

# 1. 모델 불러오기 (COCO 사전학습된 yolov8n)
model = YOLO("yolov8n.pt")

# 2. 학습 실행
results = model.train(
    data="data.yaml",   # 데이터셋 설정
    epochs=100,         # 학습 epoch
    imgsz=640,          # 입력 크기
    batch=16,           # 배치 사이즈
    #device=0,           # GPU 사용 (0번 GPU)
    cfg="hyp.yaml",     # 증강/하이퍼파라미터 파일
    project="runs/train", # 결과 저장 폴더
    name="elevator_buttons" # 실험 이름
)
