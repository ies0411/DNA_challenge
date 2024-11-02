#pragma once
#include <cuda.h>
#include <cuda_runtime_api.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <torch/extension.h>
#include <torch/serialize/tensor.h>

#include <vector>
float iou(py::array_t<float> input1, py::array_t<float> input2);
