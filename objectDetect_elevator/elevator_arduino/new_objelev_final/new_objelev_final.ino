#define MAX_FLOOR_PLUSONE 6

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


String state = "STOP";
bool next_floors[MAX_FLOOR_PLUSONE][2];
int now_floor = 1;
int next_floor = 1;

void get_nextfloor(long input,bool updown);
void move_elevator();
void seg_nowfloor();

void setup() {
  Serial.begin(9600);

  for(int i = 0; i < 7; i++)
    pinMode(seg[i],OUTPUT);
  
  for(int i=1;i<MAX_FLOOR_PLUSONE;i++){
    for(int j=0;j<2;j++)
      next_floors[i][j] = false;
  }
  Serial.println("done");
}

void loop() {  
  long input;
  char ch; 
  
  if(Serial.available()){
    ch = Serial.read();
    input = Serial.parseInt();
    if(input > 0){
      if(ch == 'u'){
        get_nextfloor(input,true);
      }
      else if(ch == 'd'){
        get_nextfloor(input,false);
      }
    }
  }  
  delay(1000);
  move_elevator();
}

void get_nextfloor(long input,bool updown){
  // 정지일때 들어온 신호를 우선 처리
  if(state == "STOP"){
    next_floor = input;
    Serial.print("Next floor is ");
    Serial.println(next_floor);
  }
  
  next_floors[input][0] = true; // 목적지 업데이트  
  if(updown)
    next_floors[input][1] = true; // 업
  else if(!updown)
    next_floors[input][1] = false; // 다운
}

void seg_nowfloor(){
  for(int j = 0; j < 7; j++)
    digitalWrite(seg[j], num[now_floor][j]);
}

void move_elevator(){
  seg_nowfloor();
  if(now_floor<next_floor){
    state = "UP";
    now_floor ++;
    Serial.println(state);
    Serial.println(now_floor);
  }
  else if(now_floor>next_floor){
    state = "DOWN";
    now_floor --;
    Serial.println(state);
    Serial.println(now_floor);
  } 
  else if(now_floor == next_floor){ 
    if(state == "UP"){ 
      // 같은 방향이면 방문
      if(next_floors[next_floor][1]){ 
        next_floors[next_floor][0] = false;    
        Serial.print("OPEN : ");
        Serial.println(now_floor);
        Serial.println("What floor do you want to go");
        // 방문한 사람의 목적지 업데이트 
        while(true){
          if(Serial.available()){
            long input = Serial.parseInt();
            if(input == -1 )
              break;
            if(input > 0){
              get_nextfloor(input,true);     
              Serial.print("Input : ");
              Serial.println(next_floors[input][0]);
            }
          }
        }
      }
      // 같은 방향에 신호가 있는지 확인 / 있으면 다음 목적지
      for(int i=1;now_floor+i<MAX_FLOOR_PLUSONE;i++){
        if(next_floors[now_floor+i][0]){
          Serial.println("keep going");
          next_floor = now_floor+i;
          Serial.print("Next floor is ");
          Serial.println(next_floor);
          return;
        }
      } 
      // 반대 방향에 신호가 있는지 확인 / 있으면 다음 목적지
      for(int i=0; now_floor-i>0;i++){
        if(next_floors[now_floor-i][0]){
          Serial.println("Change direction");          
          state = "DOWN";
          Serial.print("Next floor is ");
          Serial.println(next_floor);
          next_floor = now_floor-i;
          return;
        }
      }
    }
    else if(state == "DOWN"){
      // 같은 방향이면 방문 
      if(!next_floors[next_floor][1]){ 
        next_floors[next_floor][0] = false;
        Serial.print("OPEN : ");
        Serial.println(now_floor);
        Serial.println("What floor do you want to go");
        // 방문한 사람의 목적지 업데이트 
        while(true){
          if(Serial.available()){
            long input = Serial.parseInt();
            if(input == -1 )
              break;
            if(input > 0){
              get_nextfloor(input,false);     
              Serial.print("Input : ");
              Serial.println(next_floors[input][0]);
            }
          }
        }      
      }
      // 같은 방향에 신호가 있는지 확인 / 있으면 다음 목적지      
      for(int i=1;now_floor-i>0;i++){
        if(next_floors[now_floor-i][0]){
          Serial.println("keep going");
          next_floor = now_floor-i;
          Serial.print("Next floor is");
          Serial.println(next_floor);
          return;
        }
      }
     // 반대 방향에 신호가 있는지 확인 / 있으면 다음 목적지
     for(int i=0; now_floor+i<MAX_FLOOR_PLUSONE;i++){
        if(next_floors[now_floor+i][0]){
          Serial.println("Change direction");          
          state = "UP";
          next_floor = now_floor+i;
          Serial.print("Next floor is ");
          Serial.println(next_floor);
          return;
        }
      }
    }
  // 목적지가 없으면 정지
  state = "STOP";
  }
}
