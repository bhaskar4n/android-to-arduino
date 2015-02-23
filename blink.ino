const int ledPin = 13;
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  
}

// the loop function runs over and over again forever
void loop() {
   byte pinStatus;
  if(Serial.available()){
   pinStatus = Serial.read();
     if(pinStatus=='1')
     {
       digitalWrite(ledPin,HIGH);
       Serial.println("led on...");
     }  else if(pinStatus=='0'){
        digitalWrite(ledPin,LOW);
        Serial.println("led off...");
     }else{
        Serial.println("waiting for incomming command..."); 
     }
 
}

}
