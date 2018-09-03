cmake_minimum_required(VERSION 3.12)
project(ComputerVision)

set(CMAKE_CXX_STANDARD 17)

set(PYTHON_FILES image-classification.py)
set(SOURCE_FILES main.cpp)

add_executable(ComputerVision main.cpp)