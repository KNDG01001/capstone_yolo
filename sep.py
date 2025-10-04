import os, shutil

# 원본 경로
IMG_DIR = "dataset/images/wrist_cam_images"  # 현재 디렉토리 구조에 맞게 수정
LAB_DIR = "dataset/labels/wrist_cam_autolabels"  # 현재 디렉토리 구조에 맞게 수정

# 경로가 존재하는지 확인
if not os.path.exists(IMG_DIR):
    print(f"경로가 존재하지 않습니다: {IMG_DIR}")
    print("현재 작업 디렉토리:", os.getcwd())
    print("사용 가능한 디렉토리:", os.listdir("."))
    exit(1)

# 타겟 폴더
TRAIN_IMG = "dataset/images/train"
VAL_IMG   = "dataset/images/val"
TRAIN_LAB = "dataset/labels/train"
VAL_LAB   = "dataset/labels/val"

for d in [TRAIN_IMG, VAL_IMG, TRAIN_LAB, VAL_LAB]:
    os.makedirs(d, exist_ok=True)

# 모든 파일 정렬 (.jpg, .png, .rf로 끝나는 파일 모두 포함)
files = sorted([f for f in os.listdir(IMG_DIR) if f.endswith((".jpg", ".rf.jpg", ".png", ".rf.png"))])

print(f"총 {len(files)}개 이미지 파일을 찾았습니다.")

if len(files) == 0:
    print(f"경로 {IMG_DIR}에서 이미지를 찾을 수 없습니다!")
    exit(1)

# ------------------------------
# 시퀀스 단위 분할 (예: 20프레임씩 묶기)
# ------------------------------
SEQ_SIZE = 20
sequences = [files[i:i+SEQ_SIZE] for i in range(0, len(files), SEQ_SIZE)]

# train:val = 80:20
split_idx = int(0.8 * len(sequences))
train_seqs = sequences[:split_idx]
val_seqs   = sequences[split_idx:]

def move_files(seq_list, img_out, lab_out):
    count = 0
    for seq in seq_list:
        for f in seq:
            img_src = os.path.join(IMG_DIR, f)
            # 파일명에서 확장자와 .rf 제거하여 기본 이름 생성
            base_name = f.replace(".rf.jpg", "").replace(".jpg", "").replace(".rf.png", "").replace(".png", "")
            lab_src = os.path.join(LAB_DIR, f"{base_name}.txt")
            
            if os.path.exists(img_src):
                shutil.copy(img_src, os.path.join(img_out, f))
                count += 1
            
            if os.path.exists(lab_src):
                shutil.copy(lab_src, os.path.join(lab_out, f"{base_name}.txt"))
    return count

train_count = move_files(train_seqs, TRAIN_IMG, TRAIN_LAB)
val_count = move_files(val_seqs, VAL_IMG, VAL_LAB)

print(f"✅ Train: {train_count}장, Val: {val_count}장 분할 완료")
