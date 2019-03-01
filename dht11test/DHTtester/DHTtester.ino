
#include "DHT.h"
#define dhtPinA 2      //讀取DHT11 DataA
#define dhtPinB 4      //讀取DHT11 DataB
#define dhtPinC 5      //讀取DHT11 DataC
#define dhtPinD 8      //讀取DHT11 DataD

#define dhtType DHT11 //選用DHT11   

 

DHT dht_a(dhtPinA, dhtType); // Initialize DHT sensor
DHT dht_b(dhtPinB, dhtType); // Initialize DHT sensor
DHT dht_c(dhtPinC, dhtType); // Initialize DHT sensor
DHT dht_d(dhtPinD, dhtType); // Initialize DHT sensor

void setup() {
  Serial.begin(9600);//設定鮑率9600
  dht_a.begin();//啟動DHT
  dht_b.begin();//啟動DHT
  dht_c.begin();//啟動DHT
  dht_d.begin();//啟動DHT
  
}

void loop() {
//  float ha = dht_a.readHumidity();//讀取濕度
  float ta = dht_a.readTemperature();//讀取攝氏溫度
//  float fa = dht_a.readTemperature(true);//讀取華氏溫度
//  
//  float hb = dht_b.readHumidity();//讀取濕度
  float tb = dht_b.readTemperature();//讀取攝氏溫度
//  float fb = dht_b.readTemperature(true);//讀取華氏溫度
//  
//  float hc = dht_c.readHumidity();//讀取濕度
  float tc = dht_c.readTemperature();//讀取攝氏溫度
//  float fc = dht_c.readTemperature(true);//讀取華氏溫度
//
//  float hd = dht_d.readHumidity();//讀取濕度
  float td = dht_d.readTemperature();//讀取攝氏溫度
//  float fd = dht_d.readTemperature(true);//讀取華氏溫度

//  if (isnan(ha) || isnan(ta) || isnan(fa)) {
//    Serial.println("無法從DHT傳感器讀取！");
//    return;
//  }
//  if (isnan(ta) ) {
//    Serial.println("無法從DHT傳感器讀取！");
//    return;
//  }
//  Serial.println("A sensor:");
//  Serial.print("濕度: ");
//  Serial.print(ha);
//  Serial.print("%\t");
//  Serial.print("攝氏溫度: ");
  Serial.print(ta);
  Serial.print(" ");
  
//  Serial.println("B sensor:");
//  Serial.print("濕度: ");
//  Serial.print(hb);
//  Serial.print("%\t");
//  Serial.print("攝氏溫度: ");
  Serial.print(tb);
  Serial.print(" ");
//
//  Serial.println("c sensor:");
//  Serial.print("濕度: ");
//  Serial.print(hc);
//  Serial.print("%\t");
//  Serial.print("攝氏溫度: ");
  Serial.print(tc);
  Serial.print(" ");
//
//  Serial.println("d sensor:");
//  Serial.print("濕度: ");
//  Serial.print(hd);
//  Serial.print("%\t");
//  Serial.print("攝氏溫度: ");
  Serial.println(td);

  delay(1000);//延時5秒

}
