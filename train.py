from pathlib import Path
import shutil

from ultralytics import YOLO


FOCUS_CLASSES = {"5", "6", "7"}  # 버튼 6, O, C
FOCUS_COPIES = 3


def prepare_focus_dataset():
    base_img_dir = Path("dataset/images/train")
    base_lbl_dir = Path("dataset/labels/train")
    focus_img_dir = Path("dataset/images/train_focus")
    focus_lbl_dir = Path("dataset/labels/train_focus")

    for directory in (focus_img_dir, focus_lbl_dir):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)

    created = 0
    missing_images = []

    for label_path in base_lbl_dir.glob("*.txt"):
        content = label_path.read_text().strip()
        if not content:
            continue

        lines = [line for line in content.splitlines() if line.strip()]
        if not any(line.split()[0] in FOCUS_CLASSES for line in lines):
            continue

        image_path = None
        for ext in (".png", ".jpg", ".jpeg", ".bmp"):
            candidate = base_img_dir / f"{label_path.stem}{ext}"
            if candidate.exists():
                image_path = candidate
                break

        if image_path is None:
            missing_images.append(label_path.stem)
            continue

        label_text = "\n".join(lines) + "\n"

        for idx in range(FOCUS_COPIES):
            suffix = f"_focus{idx}"
            dest_img = focus_img_dir / f"{label_path.stem}{suffix}{image_path.suffix}"
            dest_lbl = focus_lbl_dir / f"{label_path.stem}{suffix}.txt"
            shutil.copy2(image_path, dest_img)
            dest_lbl.write_text(label_text)
            created += 1

    print(f"Focus dataset 생성 완료: {created} 샘플")
    if missing_images:
        print(f"경고: 원본 이미지 누락 {len(missing_images)}건 (예: {missing_images[:5]})")


def main():
    prepare_focus_dataset()

    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        cfg="hyp.yaml",
        augment=True,
        project="runs/train",
        name="elevator_buttons_focus",
    )


if __name__ == "__main__":
    main()
