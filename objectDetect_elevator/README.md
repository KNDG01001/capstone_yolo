객체인식을 이용한 엘리베이터 
====
특정 인물을 인식하여 거주하는 층으로 이동하는 엘리베이터 입니다.


데이터 학습
----
Yolo 알고리즘을 사용하였습니다. 
[Roboflow](https://roboflow.com/)

1. train, validation, test로 분류된 이미지 파일폴더를 업로드 합니다.
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/UploadDataSet.png" width = 500 height = 400>

2. 박스를 만들어 라벨링합니다.  
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/AnnotateDataSet.png" width = 500 height = 400>

3. 데이터셋을 생성합니다.
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/GenerateDataSet.png" width = 500 height = 400>
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/GenerateDataSet2.png" width = 500 height = 400>

4. 데이터셋을 추출합니다.
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/DataSetCode.png" width = 500 height = 400>
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/DataSetCode2.png" width = 500 height = 400>

5. 데이터 모듈을 만듭니다. <br> TrainDataSet.ipynb을 Google Colab에서 실행합니다.
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/TrainDataSet.png" width = 500 height = 400>

``` python
from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("class-raify").project("project_customdataset")
dataset = project.version(1).download("yolov8")
```

데이터셋 다운로드 코드를 사용합니다.

best.pt을 다운로드 합니다.


카메라
----
기능 단위로 모듈을 나누었습니다.  

카메라
-  프레임 단위로 학습하는 객체인식의 특징에 따라 프레임 하나를 가져오고 보여주는 기능이 있습니다.

DB
- SQL을 통해 쿼리문을 실행합니다.
객체인식을 통해 반환된 라벨을 함수의 매개변수로 하여 그에 맞는 결과를 반환합니다.

객체인식
- 프레임을 모델화합니다. 인식된 객체들의 클래스의 숫자나 이름을 반환합니다.

통신
- 엘리베이터 제어를 위한 시리얼 통신 모듈입니다.


엘리베이터
----
기본적인 엘리베이터 기능도 구현되야 한다고 생각했습니다. <br>
아래는 제가 생각하는 엘리베이터 알고리즘 입니다. 
아두이노 기준으로 작성하였습니다. 
<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/elevator.drawio.png" width = 500 >


객체인식 개선
----
멀티프로세싱과 멀티쓰레드를 통해  객체인식 속도를 개선하고자 하였습니다.

1. 프로세스 분할 : 이미지 입력, Yolo모델을 이용한 객체인식, 영상 출력
2. 모델링 된 프레임을 큐에 저장하여 다른 프로세스와 데이터를 공유하였습니다.

<img src = "https://raw.githubusercontent.com/TAEYOONEM/objectDetect_elevator/main/img/multiprocess.jpg" width = 500 height = 250>


