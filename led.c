int main(void) {  
    // エラー回避
    if(wiringPiSetupGpio() == -1) return 1;

    // 17番ピンを出力(OUTPUT)に設定  
    pinMode(17, OUTPUT);

    for(int i=0; i<10; i++){
        digitalWrite(17, 0);
        delay(950);
        digitalWrite(17, 1);
        delay(50);
    }

    // 消灯を忘れずに！  
    digitalWrite(17, 0);

    return 0;
}