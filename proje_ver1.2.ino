#include <SPI.h>
#include <Ethernet.h>

// Arduino server MAC address
uint8_t mac[] = { 0x00, 0xAA, 0xBB, 0xCC, 0xDE, 0x02 };
// Arduino server IP address
//IPAddress ip(192, 168, 137, 3);
// Arduino server port
const int port = 23;
const int pin = 3;

//int LedPin1 = 6;
//int LedPin2 = 7;
//int LedPin3 = 8;
//int LedPin4 = 9;


// Ethernet server
EthernetServer server(port);

// For store command from client
String cmd;

void setup()
{


  Serial.begin(9600);

  DDRB |= B00000011;
  PORTB &= ~B00000011;
  DDRD |= B11000000;
  PORTD &= ~B11000000;


  // Ethernet server initialization
  Ethernet.begin(mac);
  delay(100);
  server.begin();
  delay(100);

  // Print Arduino server IP address to serial monitor
  Serial.print("Server IP Address: ");
  Serial.println(Ethernet.localIP());

}

void loop()
{


  EthernetClient client = server.available();

  if (client.available())
  {

    // Read char until new line
    char c = client.read();

    if (c != '\n')
    {
      // Add received char to string variable
      cmd += c;
    }
    else
    {
      // Print received command to serial monitor
      Serial.println("Command: " + cmd);

      // Process the received command
      processCommand(cmd);

      // Clear variable for receive next command
      cmd = "";
    }
  }

}

void processCommand(String cmd)
{
  if (cmd == "Q")
  {
    PORTB ^= 0x01;
    delay(100);
    Serial.println("Q state changed");
  }
  else if (cmd == "W")
  {
    PORTB ^= 0x02;
    delay(100);
    Serial.println("W state changed");
  }
  else if (cmd == "E")
  {
    PORTD ^= 0x40;
    delay(100);
    Serial.println("E state changed");
  }
  else if (cmd == "R")
  {
    PORTD ^= 0x80;
    delay(100);
    Serial.println("R state changed");
  }

}

