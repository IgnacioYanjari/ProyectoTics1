/*
  Web client

 This sketch connects to a website (http://www.google.com)
 using an Arduino Wiznet Ethernet shield.

 Circuit:
 * Ethernet shield attached to pins 10, 11, 12, 13

 created 18 Dec 2009
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe, based on work by Adrian McEwen

 */

//Configuración Del Sensor Creado
int ThermistorPin = 0;
int Vo;
float R1 = 10000;
float logR2, R2, T;
float Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;

// Configuración sensor Ph

#define SensorPin A2            //pH meter Analog output to Arduino Analog Input 2
#define Offset 0.00            //deviation compensate
#define LED 13
#define samplingIntervalph 20
#define printIntervalph 100
#define ArrayLenth  40    //times of collection
int pHArray[ArrayLenth];   //Store the average value of the sensor feedback
int pHArrayIndex=0;

// Configuración sensor Electroconductividad

#include <OneWire.h>

#define StartConvert 0
#define ReadTemperature 1

const byte numReadings = 20;     //the number of sample times
byte ECsensorPin = A1;  //EC Meter analog output,pin on analog 1
byte DS18B20_Pin = 2; //DS18B20 signal, pin on digital 2
unsigned int AnalogSampleInterval=25,printIntervalec=500,tempSampleInterval=1000;  //analog sample interval;serial print interval;temperature sample interval
unsigned int readings[numReadings];      // the readings from the analog input
byte index = 0;                  // the index of the current reading
unsigned long AnalogValueTotal = 0;                  // the running total
unsigned int AnalogAverage = 0,averageVoltage=0;                // the average
unsigned long AnalogSampleTime,printTime,tempSampleTime;
float temperature,ECcurrent;

//Temperature chip i/o
OneWire ds(DS18B20_Pin);  // on digital pin 2

#include <SPI.h>
#include <Ethernet.h>

// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(74,125,232,128);  // numeric IP for Google (no DNS)
char server[] = "192.168.1.147";    // name address for Google (using DNS)

// Set the static IP address to use if the DHCP fails to assign
IPAddress ip(192,168,1,237);

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
EthernetClient client;

void setup() {

  //sensor Ph
  pinMode(LED,OUTPUT);

  //Sensor Electroconductividad

 // initialize all the readings to 0:
  for (byte thisReading = 0; thisReading < numReadings; thisReading++)
    readings[thisReading] = 0;
  TempProcess(StartConvert);   //let the DS18B20 start the convert
  AnalogSampleTime=millis();
  printTime=millis();
  tempSampleTime=millis();

  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // start the Ethernet connection:
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // try to congifure using IP address instead of DHCP:
    Ethernet.begin(mac, ip);
  }

  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.println("connecting...");




}

void loop() {


  // Código Sensor Creado
  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  // Código Sensor Ph

  static unsigned long samplingTime = millis();
  static unsigned long printTime = millis();
  static float pHValue,voltage;
  if(millis()-samplingTime > samplingIntervalph)
  {
      pHArray[pHArrayIndex++]=analogRead(SensorPin);
      if(pHArrayIndex==ArrayLenth)pHArrayIndex=0;
      voltage = avergearray(pHArray, ArrayLenth)*5.0/1024;
      pHValue = 3.5*voltage+Offset;
      samplingTime=millis();
  }


  //Código Sensor Electroconductividad
   /*
   Every once in a while,sample the analog value and calculate the average.
  */

  if(millis()-AnalogSampleTime>=AnalogSampleInterval)
  {
    AnalogSampleTime=millis();
     // subtract the last reading:
    AnalogValueTotal = AnalogValueTotal - readings[index];
    // read from the sensor:
    readings[index] = analogRead(ECsensorPin);
    // add the reading to the total:
    AnalogValueTotal = AnalogValueTotal + readings[index];
    // advance to the next position in the array:
    index = index + 1;
    // if we're at the end of the array...
    if (index >= numReadings)
    // ...wrap around to the beginning:
    index = 0;
    // calculate the average:
    AnalogAverage = AnalogValueTotal / numReadings;
  }
  /*
   Every once in a while,MCU read the temperature from the DS18B20 and then let the DS18B20 start the convert.
   Attention:The interval between start the convert and read the temperature should be greater than 750 millisecond,or the temperature is not accurate!
  */
   if(millis()-tempSampleTime>=tempSampleInterval)
  {
    tempSampleTime=millis();
    temperature = TempProcess(ReadTemperature);  // read the current temperature from the  DS18B20
    TempProcess(StartConvert);                   //after the reading,start the convert for next reading

  }
  if(millis() - printTime > printIntervalph)   //Every 800 milliseconds, print a numerical, convert the state of the LED indicator
  {
    Serial.print("    pH value: ");
    Serial.print(pHValue,2);
    digitalWrite(LED,digitalRead(LED)^1);
    printTime=millis();
    averageVoltage=AnalogAverage*(float)5000/1024;
    //Serial.print("Analog value:"); -  Serial.print(AnalogAverage);  -  //analog average,from 0 to 1023 Serial.print("    Voltage:");
    //Serial.print(averageVoltage);  //millivolt average,from 0mv to 4995mV - //Serial.print("mV    ");
    Serial.print("  Temperatura: ");
    Serial.println(Tc);
    //Serial.print("temp:"); - //Serial.print(temperature);    //current temperature - //Serial.print("^C     EC:");
    float TempCoefficient=1.0+0.0185*(temperature-25.0);    //temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.0185*(fTP-25.0));
    float CoefficientVolatge=(float)averageVoltage/TempCoefficient;
    //if(CoefficientVolatge<150)Serial.println("No solution!");   //25^C 1413us/cm<-->about 216mv  if the voltage(compensate)<150,that is <1ms/cm,out of the range
    //else if(CoefficientVolatge>3300)Serial.println("Out of the range!");  //>20ms/cm,out of the range
    //else
    //{
      if(CoefficientVolatge<=448)ECcurrent=6.84*CoefficientVolatge-64.32;   //1ms/cm<EC<=3ms/cm
      else if(CoefficientVolatge<=1457)ECcurrent=6.98*CoefficientVolatge-127;  //3ms/cm<EC<=10ms/cm
      else ECcurrent=5.3*CoefficientVolatge+2278;                           //10ms/cm<EC<20ms/cm
      ECcurrent/=1000;    //convert us/cm to ms/cm
      Serial.print(" EC : ");
      if(ECcurrent >= 0 ){
      Serial.print(ECcurrent,2);  //two decimal
      Serial.println("ms/cm");
      }
      else{
        Serial.println("No Solution ");
      }

      if ( client.connect(server, 80) ) {
        Serial.println("connected");
        // Make a HTTP request:
        // client.println("GET /?temperatura=100 HTTP/1.1");

        if(ECcurrent >= 0 ){
          //client.printf("GET /?temperature=%s&ph=%s&ec=%s HTTP/1.1"), Tc , pHvalue , ECcurrent );
          client.print("GET /data?temperatura=");
          client.print(Tc);
          client.print("&ph=");
          client.print(pHValue);
          client.print(" HTTP/1.1");
          // Serial.print(ECcurrent,2);  //two decimal
          // Serial.println("ms/cm");
        }
        else{
          char ECcurrent2[ ] = "Valor inapropiado";
          client.print("GET /data?temperatura=");
          client.print(Tc);
          client.print("&ph=");
          client.print(pHValue);
          client.print(" HTTP/1.1");
          //client.print("GET /?temperatura=%s&ph=%s&ec=%s HTTP/1.1"), Tc , pHvalue , ECcurrent2 );

        }
        // client.println("Connection: close");
        client.println();
      }
      else{
        // if you didn't get a connection to the server:
        Serial.println("connection failed");
      }

    //}

  }

  // if ( client.connect(server, 80) ) {
  //   Serial.println("connected");
  //   // Make a HTTP request:
  //   client.println("GET /?temperatura=100 HTTP/1.1");
  //   // client.printf(""),values);
  //
  //   client.println("Host: 10.10.1.147");
  //   // client.println("Connection: close");
  //   client.println();
  // }
  // else{
  //   // if you didn't get a connection to the server:
  //   Serial.println("connection failed");
  // }



  if(client.connected()){
    client.stop(); //Disconnect from the server
  }
  delay(1000);
}


// Función Extra De Electroconductividad
/*
ch=0,let the DS18B20 start the convert;ch=1,MCU read the current temperature from the DS18B20.
*/
float TempProcess(bool ch)
{
  //returns the temperature from one DS18B20 in DEG Celsius
  static byte data[12];
  static byte addr[8];
  static float TemperatureSum;
  if(!ch){
          if ( !ds.search(addr)) {
              Serial.println("no more sensors on chain, reset search!");
              ds.reset_search();
              return 0;
          }
          if ( OneWire::crc8( addr, 7) != addr[7]) {
              Serial.println("CRC is not valid!");
              return 0;
          }
          if ( addr[0] != 0x10 && addr[0] != 0x28) {
              Serial.print("Device is not recognized!");
              return 0;
          }
          ds.reset();
          ds.select(addr);
          ds.write(0x44,1); // start conversion, with parasite power on at the end
  }
  else{
          byte present = ds.reset();
          ds.select(addr);
          ds.write(0xBE); // Read Scratchpad
          for (int i = 0; i < 9; i++) { // we need 9 bytes
            data[i] = ds.read();
          }
          ds.reset_search();
          byte MSB = data[1];
          byte LSB = data[0];
          float tempRead = ((MSB << 8) | LSB); //using two's compliment
          TemperatureSum = tempRead / 16;
    }
          return TemperatureSum;
}


//Función Extra Del Sensor de Ph
double avergearray(int* arr, int number){
  int i;
  int max,min;
  double avg;
  long amount=0;
  if(number<=0){
    Serial.println("Error number for the array to avraging!/n");
    return 0;
  }
  if(number<5){   //less than 5, calculated directly statistics
    for(i=0;i<number;i++){
      amount+=arr[i];
    }
    avg = amount/number;
    return avg;
  }else{
    if(arr[0]<arr[1]){
      min = arr[0];max=arr[1];
    }
    else{
      min=arr[1];max=arr[0];
    }
    for(i=2;i<number;i++){
      if(arr[i]<min){
        amount+=min;        //arr<min
        min=arr[i];
      }else {
        if(arr[i]>max){
          amount+=max;    //arr>max
          max=arr[i];
        }else{
          amount+=arr[i]; //min<=arr<=max
        }
      }//if
    }//for
    avg = (double)amount/(number-2);
  }//if
  return avg;
}
