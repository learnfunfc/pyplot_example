
#include "DHT.h"
#define dhtPinA 2      //讀取DHT11 DataA


#define dhtType DHT11 //選用DHT11   

 

DHT dht_a(dhtPinA, dhtType); // Initialize DHT sensor


void setup() {
  Serial.begin(9600);//設定鮑率9600
  dht_a.begin();//啟動DHT
  
  
}

void loop() {
//  float ha = dht_a.readHumidity();//讀取濕度
  float ta = dht_a.readTemperature();//讀取攝氏溫度

  Serial.println(ta);
  
  //Serial.println(ha);
  Serial.flush();
  delay(500);//延時0.5秒

}
