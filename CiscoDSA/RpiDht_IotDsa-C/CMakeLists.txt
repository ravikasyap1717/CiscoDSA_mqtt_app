cmake_minimum_required(VERSION 3.0.0 FATAL_ERROR)
project(CiscoSdk-Sensor)


#include_directories("${CMAKE_CURRENT_LIST_DIR}/SDK_library/SDK_include")
#include_directories("${CMAKE_CURRENT_LIST_DIR}/SDK_library/private_include")
include_directories("${CMAKE_CURRENT_LIST_DIR}/include")

#LINK_DIRECTORIES(${CMAKE_CURRENT_LIST_DIR})

set(EXAMPLE_INR_DIR "${CMAKE_CURRENT_LIST_DIR}/include")
set(EXAMPLE_INR
     "${EXAMPLE_INR_DIR}/rng.h"
     "${EXAMPLE_INR_DIR}/dht11.h"
)

set(EXAMPLE_SRC_DIR "${CMAKE_CURRENT_LIST_DIR}/src")
set(EXAMPLE_SRC
    "${EXAMPLE_SRC_DIR}/main.c"
    "${EXAMPLE_SRC_DIR}/rng.c"
    "${EXAMPLE_SRC_DIR}/dht11.c"
)

add_executable(dhtCisco ${EXAMPLE_INR}  ${EXAMPLE_SRC} )


target_link_libraries(dhtCisco
sdk_dslink_c
wiringPi
)


set_property(TARGET dhtCisco PROPERTY C_STANDARD 99)
