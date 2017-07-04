In "RpiDht_IotDsa-C" project we are interfacing DHT11 sensor with RaspberryPi and Publishing Tempreature and Humidity data on CicsoDSA.

So,In this Project we are linking two library "lwiringPi" for Raspberry GPIO and "lsdk_dslink_c.so" for CiscoDSA publish API.

For installing both library following below step :

PreRequrities :  
  
    1. To read the DHT11 sensor 
        sudo apt-get install wiringPi
    
    2. Install Libuv Package in raspberry pi,Raspberry pi have older version on libuv
        sudo apt-get install make automake libtool curl
        curl -sSL https://github.com/libuv/libuv/archive/v1.8.0.tar.gz | sudo tar zxfv - -C /usr/local/src
        cd /usr/local/src/libuv-1.8.0
        sudo sh autogen.sh
        sudo ./configure
        sudo make
        sudo make install
        sudo rm -rf /usr/local/src/libuv-1.8.0 && cd ~/
        sudo ldconfig
        
    3. To Publish data on CiscoDSA
         follow all step of file "Compile sdk-dslink-c.md" till Complitaion.
         // Follow these step 
          cd Desktop/sdk-dslink-c/ 
          mkdir build
          cd build 
          cmake ..
          make
          sudo make install
          

Compile "RpiDht_IotDsa-C" code : 
    
      1. mkdir build
      2. cmake ..
      3. make
      4../dhtCisco
      
 
Note : you can see the above node on CicsoDSA dataflow.html 
    
    for our case :
        https://172.21.3.191:8443/dataflow.html
        username :effAdmin
        password : root@123

