// 세그먼트 디지털 핀 2~8
int seg[7] = {2,3,4,5,6,7,8};

int num[10][7] = {
  {1,1,1,1,1,1,0}, //0
  {0,1,1,0,0,0,0}, //1
  {1,1,0,1,1,0,1}, //2
  {1,1,1,1,0,0,1}, //3
  {0,1,1,0,0,1,1}, //4
  {1,0,1,1,0,1,1}, //5
  {1,0,1,1,1,1,1}, //6
  {1,1,1,0,0,0,0}, //7
  {1,1,1,1,1,1,1}, //8
  {1,1,1,0,0,1,1}  //9
};

long n = 0;

void setup() {
  Serial.begin(9600);
  for(int i = 0; i < 7; i++){
    pinMode(seg[i],OUTPUT);
  }
}

void loop() {
  char ch;
  long input;
  
  if(Serial.available()){
    ch = Serial.read();
    if(ch == 'u'){
      input = Serial.parseInt();
      if(input > 0)
        n = input;
    }
  }
  for(int j = 0; j < 7; j++)
    digitalWrite(seg[j], num[n][j]);
  delay(500);
}
