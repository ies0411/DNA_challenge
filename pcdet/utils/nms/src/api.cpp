#include <cuda.h>
#include <cuda_runtime_api.h>
#include <torch/extension.h>
#include <torch/serialize/tensor.h>

#include <vector>

#include "nms.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("iou", &iou, "nms cpp");
}
