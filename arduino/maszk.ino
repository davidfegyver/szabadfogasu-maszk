char val;

int relay = 13; 

int green = 3;
int red = 2;
int buzzer = 5;
void setup()  
{  
    Serial.begin(9600);
    pinMode(relay, OUTPUT);  
    pinMode(green, OUTPUT); 
    pinMode(red, OUTPUT); 
    pinMode(buzzer, OUTPUT); 
}  
void loop() {
  if(Serial.available() > 0) {
    val = Serial.read();
        switch (val) 
    {  
        case '2':
              digitalWrite(relay, LOW);
              digitalWrite(green, LOW);
              digitalWrite(red, LOW);
              noTone(buzzer);
              break;
        case '1':  
        
            digitalWrite(relay, HIGH);
            digitalWrite(green, HIGH);
            digitalWrite(red, LOW);
            noTone(buzzer);
            break;  
        case '0':  
            digitalWrite(relay, LOW);
            digitalWrite(red, HIGH);
            digitalWrite(green, LOW);
            tone(buzzer,1000);
            break;  
    }  
  }

}
