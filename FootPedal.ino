/* Four Button Foot Pedal by Jeff */

// Map the pin values to array
   int pinValues[] = 
       {  13, /* red  */ 
          11, /* grey */
          10, /* blue */ 
          12  /* purp */ };

// Debounce Time
   const long delayTime = 0;

// Time since last button press 
   unsigned long previousMillis = 0;

// List containing which buttons have been pressed
   int buttonMap[4];

void setup(){ 
  Serial.begin(9600); 
  setPinsToInput(buttonMap);  
}

void noInput(){ 
  printEmptyButtonMap();
}

void  loop(){ ( isDebounceUp() ) ?  mapInputsAndSendToSerial() : loop(); }

void mapInputsAndSendToSerial(){
  setLastTime();
  initPins(buttonMap);
  mapReadsToButtonMap( mapPinsToRead(pinValues) );
  
  ( noPresses(buttonMap) ) ?  noInput() : printArrToSerial(buttonMap);  

}
// Utility functions 
void setLastTime(){
  previousMillis = millis();
}
boolean isDebounceUp(){
  return millis() - previousMillis >= delayTime;
}
void mapReadsToButtonMap( int pinStates[] ){
  for( int pin = 0; pin < 4; pin++ ) { 
    if(pinStates[pin] == HIGH){ buttonMap[pin] = 1;}
  }
}
int *mapPinsToRead ( int pinValues[] ){
  int result[4];  
  for( int pin = 0; pin < 4; pin++ ) { 
      result[pin] = digitalRead(pinValues[pin]); 
   }
   return result;
}
void printEmptyButtonMap (){
  Serial.println(); 
  for ( int pin = 0; pin < 4; pin++ ) { Serial.print(0); }
}
void setPinsToInput ( int pins[] ){
  for ( int pin = 0; pin < 4; pin++ ) { pinMode( pins[pin] , INPUT ); }
}
void printArrToSerial ( int pins[] ){
  Serial.println();  
  for ( int pin = 0; pin < 4; pin++ ) { Serial.print(pins[pin]); }
}
void initPins ( int pins[] ){
  for ( int pin = 0; pin < 4; pin++ ) { pins[pin] = 0; }
}
boolean noPresses (int pins[]){
  return pins[0] == 0 && pins[1] == 0 && pins[2] == 0 && pins[3] == 0;
}
