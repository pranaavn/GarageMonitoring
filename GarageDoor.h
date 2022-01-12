//definitions
#define STATUS_LED                          12    // Green LED
#define AMBER_LED                           14    // Amber LED
#define WIFI_STA_TIMEOUT                    20000 // try to connect to wifi for x seconds

const char* CUST_SSID = "";  //  SSID of the network you want ESP to connect to
const char* PASS = ""; //  pass of the network you want ESP to connect to

const char* _ssid = "wi-pj-g2";
const char* _password = "srmedw32";
const char* _GMailServer = "";
const char* _mailUser = "";
const char* _mailPassword = "";


//IPAddress cloudServerIP(34,83,30,196);      // IP address
//IPAddress cloudServerIP(10,1,1,10);

// REST client does not take IPAddress so converting to const char
//String cloudServerIPstr = String(cloudServerIP[0])+'.'+String(cloudServerIP[1])+'.'+String(cloudServerIP[2])+'.'+String(cloudServerIP[3]); 


//char const* RESTServer = cloudServerIPstr.c_str(); 
//unsigned int RESTPort = 80;                 // port on REST server

// Constants
const char* FIRMWARE_VER = " GarageOS version 1.0.2";
const char* EXTERNAL_IP_ADDRESS = "34.83.31.33:80";
const char* EXTERNAL_ENDPOINT = "http://34.83.31.33:80/device";

// BLE scan structures for namespace/UUID filter
  const int noOfNamespaces = 10;  // no of namesaces or UUIDs to scan for
  
  struct scanFilter {
    uint8_t uuid[16];
    uint8_t uidNamespace[10];
  };
  
  static scanFilter scanOnly[noOfNamespaces];

// Function declarations

char* nrf_send_recv(char*, boolean return_resp = false);
void esp_hb_ticker_trigger();
void post_to_cloud();
void http_ota_update();
