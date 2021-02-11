# hie2mmdet


## Requirement

- ffmpeg

## step 1

Download the `HIE20.zip` file and unzip. You should have a folder named HIE20 with subfolders like this

```
HIE20
├── labels
└── videos
```

## step 2

Run 

```
bash ffmpeg_video2image_HIE20.sh
```

to generate jpg images from the videos. **You will need to change some path in the script.**

## step 3 (Optional)

Then run

```
python hie2mmdet.py
``` 

to generate json file for training in COCO format. Or you can simply use the json file in this repository. It should works the same as long as you handle the prefix in the later mmdetection configs correctly.


### Reference
- https://mmdetection.readthedocs.io/en/latest/tutorials/customize_dataset.html
