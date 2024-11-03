
# Lidar sensor, edge-infra 3D 객체탐지 challenge
Lidar dataset을 이용하여  3D 객체 탐지하는 [challenge](https://www.auto-dna.org/page/?M2_IDX=32625)의 솔루션.
최종 리더보드 기준 3rd place score

## 환경세팅
-  Docker
```bash
cd docker_script
./make_image.sh # 도커 이미지 생성
./run_image.sh # 컨테이너 생성

cd python setup.py develop
cd /home/{PATH TO DNA_CHALLENGE}
```

## Preparing Dataset
1. [Datasets](https://nanum.etri.re.kr/share/kimjy/3DMODInfraAIchallenge2024?lang=ko_KR)에서 lidar dataset(edge case)를 다운.
2. 폴더트리는 아래의 그림과 같아야함
<p align="left">
  <img src="./docs/folder_tree.png" alt="Preparing Dataset" width="200">
</p>

3. pkl파일로 변환
```bash
python -m pcdet.datasets.custom.custom_dataset create_custom_infos tools/cfgs/dataset_configs/custom_dataset.yaml ./datasets
```


## Train
1. baseline model tranining
(scratch부터 학습을 수행)

```bash
cd tools/
python train.py --cfg_file ./cfgs/my_models/pv_rcnn_plus_base.yaml --work_dir ../output/
```
2. 1번을 통해 학습된 baseline model을 augmentation을 적용하여 추가학습
(1번의 과정을 생략하고 싶다면 [링크](https://drive.google.com/file/d/1YNrV9DXIlgsJUywoe0oLVU-lYJe7dd01/view?usp=sharing)를 동해 weight를 다운받아서 실행)
```bash
cd tools/
python train.py --cfg_file ./cfgs/my_models/pv_rcnn_plus_augmentation.yaml --work_dir ../output/ -–ckpt ../weights/baseline.pth
```

## Test(Inference)
**Traning을 생략하고 바로 Test를 수행하고 싶으면 [링크](https://drive.google.com/file/d/1Nlw_Ip3TsGSa9p9LtPXl_SGK02ZjiwpZ/view?usp=sharing)를 통해 최종 weight다운로드**


```bash
cd tools
python test.py --cfg_file ./cfgs/my_models/pv_rcnn_plus_augmentation.yaml --ckpt ../weights/final.pth --work_dir ../results/ --data_path ../datasets/

```

## Log
Evaluation Hook을 이용한 매 epoch마다 validation set의 mAP 결과
![log](./docs/eval.png)


## Ref
openpcdet
```bash
@misc{openpcdet2020,
    title={OpenPCDet: An Open-source Toolbox for 3D Object Detection from Point Clouds},
    author={OpenPCDet Development Team},
    howpublished = {\url{https://github.com/open-mmlab/OpenPCDet}},
    year={2020}
}
```
