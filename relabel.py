import os
import glob

def map_to_new_class(old_class_name):
    # 열기 버튼 관련 매핑
    open_keywords = ['open', 'text_open', 'text_door open', 'text_OPEN', 'text_DOOR OPEN']
    if any(keyword.lower() in old_class_name.lower() for keyword in open_keywords):
        return 0  # 'O' class
    
    # 닫기 버튼 관련 매핑
    close_keywords = ['close', 'text_close', 'text_door close', 'text_CLOSE', 'text_DOOR CLOSE']
    if any(keyword.lower() in old_class_name.lower() for keyword in close_keywords):
        return 1  # 'C' class
    
    # 숫자 버튼 매핑 (1-6)
    for i in range(1, 7):
        if str(i) == old_class_name or old_class_name.startswith(str(i) + 'F') or \
           old_class_name.startswith(str(i) + 'A') or old_class_name.startswith(str(i) + 'B'):
            return i + 1  # class 2-7 for numbers 1-6
    
    return None  # 매핑되지 않는 클래스

def process_label_file(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5:  # YOLO 형식: class x y w h
                old_class = int(parts[0])
                if old_class < len(class_names):  # 유효한 클래스 인덱스인 경우
                    new_class = map_to_new_class(class_names[old_class])
                    if new_class is not None:
                        parts[0] = str(new_class)
                        new_lines.append(' '.join(parts) + '\n')
        
        if new_lines:  # 새로운 라벨이 있는 경우에만 파일 저장
            with open(file_path, 'w') as f:
                f.writelines(new_lines)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

# 원본 클래스 이름 목록 (data.yaml에서 가져온 368개의 클래스 이름)
class_names = ['-', '-1', '-1M', '-2', '-3', '-4', '-5', '-7', '0', '1', '10', '11', '114', '117', '118', '119', '12', '12A', '12B', '12M', '13', '13A', '14', '15', '16', '17', '18', '18A', '19', '1A', '1B', '1E', '1F', '1R', '1U', '2', '20', '21', '22', '23', '23A', '24', '25', '26', '27', '27A', '28', '29', '2A', '2B', '2M', '2R', '2U', '3', '30', '31', '32', '33', '33A', '34', '35', '36', '37', '38', '39', '3A', '3B', '3F', '3M', '3N', '3R', '3S', '4', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4A', '4B', '5', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5A', '5B', '5P', '6', '60', '61', '62', '63', '65', '66', '67', '68', '69', '6M', '7', '8', '8A', '9', '9M', 'A', 'AA', 'AL', 'ALT', 'B', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'BC', 'BF', 'BR', 'C', 'CH', 'CL', 'CP', 'D', 'D0', 'DC', 'DH', 'DHB', 'DHF', 'DHR', 'DN', 'DO', 'DOR', 'E', 'EG', 'EN', 'EX', 'F', 'F1', 'FB', 'FF', 'G', 'G1', 'G2', 'GA', 'GF', 'GG', 'GR', 'H', 'HC', 'I', 'ID', 'IR', 'IU', 'J', 'K', 'K1', 'L', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'LB', 'LG', 'LG1', 'LG2', 'LGA', 'LL', 'LL2', 'LM', 'LP', 'LR', 'LS', 'M', 'M2', 'MC', 'MG', 'MZ', 'NS', 'O', 'P', 'P1', 'P10', 'P11', 'P12', 'P15', 'P1A', 'P1B', 'P2', 'P25', 'P2A', 'P2B', 'P3', 'P35', 'P3A', 'P3B', 'P4', 'P45', 'P4A', 'P5', 'P5A', 'P6', 'P6A', 'P7', 'P7A', 'P8', 'P8A', 'P9', 'P9A', 'PA', 'PB', 'PG', 'PH', 'PH1', 'PH2', 'PL', 'PL4', 'PT', 'R', 'REF', 'RF', 'RL', 'RR', 'RS', 'S', 'S1', 'S2', 'SB', 'SF', 'SL', 'SPA', 'ST', 'T', 'TF', 'TOR', 'U', 'U1', 'U2', 'UB', 'UG', 'UL', 'UM', 'UP', 'UT', 'V', 'alarm', 'blur', 'bt_keyhole', 'bt_switch', 'call', 'close', 'down', 'empty', 'fan', 'fire', 'hat', 'indicator', 'key', 'keyhole', 'led', 'light', 'open', 's', 's1', 's2', 's3', 'sE', 'sG', 'sGR', 'sL', 'sLL', 'sP', 'sP1', 'sPS', 'speaker', 'stop', 'switch', 'text', 'text_1-5', 'text_2-5', 'text_3-5', 'text_30-90', 'text_340m', 'text_345m', 'text_ALARM', 'text_CALL CANCEL', 'text_CALL', 'text_CLOSE DOOR', 'text_CLOSE', 'text_DOOR CLOSE', 'text_DOOR OPEN', 'text_DOWN', 'text_FAN', 'text_FULL', 'text_GROUND', 'text_HOLD', 'text_INUSE', 'text_LL1R', 'text_LL2R', 'text_MEZZ', 'text_Mez', 'text_OPEN DOOR', 'text_OPEN', 'text_PASS', 'text_STOP', 'text_alarm bell', 'text_alarm', 'text_attendant', 'text_bell', 'text_blur', 'text_bridge', 'text_bypass', 'text_call bell', 'text_call cancel', 'text_call lift', 'text_car here', 'text_close door', 'text_close', 'text_delay', 'text_door close', 'text_door ext', 'text_door open', 'text_doordelay', 'text_emege call', 'text_emerg bell', 'text_emerg call', 'text_emerg', 'text_emergency', 'text_fan', 'text_ground', 'text_help', 'text_hold', 'text_homing', 'text_in use', 'text_intercom', 'text_light', 'text_lobby', 'text_nostop', 'text_oepn', 'text_open door', 'text_open hold', 'text_open', 'text_overload', 'text_overloaded', 'text_overweight', 'text_pass', 'text_plaza', 'text_push', 'text_start', 'text_stop', 'text_street', 'unknown', 'up', 'updown']

# 데이터셋 폴더들
folders = ['train', 'valid', 'test']

# 각 폴더의 라벨 파일 처리
for folder in folders:
    label_path = os.path.join(os.getcwd(), folder, 'labels')
    if os.path.exists(label_path):
        label_files = glob.glob(os.path.join(label_path, '*.txt'))
        for label_file in label_files:
            process_label_file(label_file)
            print(f"Processed: {label_file}")