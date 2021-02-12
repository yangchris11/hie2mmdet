import json
import tqdm

import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--metadata', default='metadata.json')
    parser.add_argument('--outfile',  default='output.json')

    args = parser.parse_args()

    global_img_idx = 0
    global_anno_idx = 0

    metadata_file = args.metadata
    with open(metadata_file) as f:
        metadata = json.load(f)

    output_json = {
        'images': [],
        'annotations': [],
        'categories': [
            {'id': 1, 'name': 'person'},
        ]
    }

    for seq_idx in tqdm.tqdm(metadata.keys()):
        json_file = 'labels/train/track2&3/' + seq_idx + '.json'
        with open(json_file) as f:
            data = json.load(f)

        annolist = data['annolist']

        for i, anno in enumerate(annolist):

            image_name = anno['image'][0]['name']
            anno_info = anno['annorect']

            coco_img = {
                'file_name': seq_idx + '/' + image_name,
                'height': metadata[seq_idx]['height'],
                'width': metadata[seq_idx]['width'],
                'id': global_img_idx
            }
            output_json['images'].append(coco_img)

            for j in range(len(anno_info)):
                x1, x2 = anno_info[j]['x1'][0], anno_info[j]['x2'][0]
                y1, y2 = anno_info[j]['y1'][0], anno_info[j]['y2'][0]

                coco_anno = {
                    'image_id': global_img_idx,
                    'iscrowd': 0,
                    'area': (x2-x1) * (y2-y1),
                    'bbox': [x1, y1, x2-x1, y2-y1],
                    'category_id': 1,
                    'id': global_anno_idx
                }
                output_json['annotations'].append(coco_anno)

                global_anno_idx += 1

            global_img_idx += 1

    with open(args.outfile, 'w') as outfile:
        json.dump(output_json, outfile)


if __name__ == '__main__':
    main()