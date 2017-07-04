Step to compile IOT-DSA/sdk-dslink-c and build sdk-dslink-c library and run example.

Building :

	//Install followinng package for compile
	sudo apt-get install git  
	sudo apt-get install cmake  // CMake v3.0+
	//Note: we required cmake version v3.0+ 
	//Check cmake version using command
      	cmake -version

Download sdk-dslink-c :

	1. cd Desktop
	2. git clone https://github.com/IOT-DSA/sdk-dslink-c.git
	
	
Modification :

	1. Compile sample code :
	
		// For compile and execute sample example change CMakeLists.txt
		cd Desktop/sdk-dslink-c/
		nano CMakeLists.txt 
		// find this line 
		option(DSLINK_BUILD_EXAMPLES "Whether to build the examples" OFF)
		//Change OFF to ON for build examples
		option(DSLINK_BUILD_EXAMPLES "Whether to build the examples" ON)
		//save CMakeLists.txt file
		ctrl + x ,Yes
		
	2. Set Broker : 
	
		// go to sdk folder and open dslink.c file
		cd Desktop/sdk-dslink-c/sdk/src/
		nano dslink.c 
		// set the brokerUrl with your brokerIP,our brokerip is https://172.21.3.191:8443 
		// find this line 
		brokerUrl = "http://127.0.0.1:8080/conn";
		//change with your broker url
		brokerUrl = "https://172.21.3.191:8443/conn";
		//save file
		ctrl + x, Yes
		
Complie sdk-dslink-c : 
	
	// Follow these step 
	cd Desktop/sdk-dslink-c/ 
	mkdir build
	cd build 
	cmake ..
	make

Run the sample responder example: 

	cd Desktop/sdk-dslink-c/build/
	./responder


