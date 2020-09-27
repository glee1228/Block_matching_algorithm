# Block_matching_algorithm
Block matching algorithm based on Exhaustive Search and Three Step Search

<br/>

## Usage


### Extract frames from video
```python
python frame_extract.py
```

### Run block matching algorithm in anchor frame and reference frame  
```python
python main.py
```   
<br/>
<br/>

## Example

**Figure 1.** anchor frame (left) and reference frame (right)

previous frame(anchor frame) | current frame(reference frame) 
---- | ---- 
![prev_frame](https://github.com/glee1228/Block_matching_algorithm/blob/master/result/20200927171519/prev.png) | ![current_frame](https://github.com/glee1228/Block_matching_algorithm/blob/master/result/20200927171519/cur.png )


**Figure 2.** Block motion estimation Results
interpolated frame(predicted frame) | motion field
---- | ---- 
|![interpolated](https://github.com/glee1228/Block_matching_algorithm/blob/master/result/20200927171519/interpolated.png) | ![motion_vector](https://github.com/glee1228/Block_matching_algorithm/blob/master/result/20200927171519/mv_drawing.png)

<br/>

**Table 1.** PSNR and reference time according to Search Window and Search Method

Block size(pixel)	| Pixel accuracy	| Search range(pixel) |	Search method	 | PSNR(db) |	Inference Time(sec)
---- | ---- | ---- | ---- | ----  |----
8  |	1  |	±7	 | Exhaustive  | 	27.39182 | 	14.16
8  |	1  |	±7	 | Three step  |	25.90376 |	0.85
8 |	1 |	±15 |	Exhaustive | 	30.80127 |	43.62
8 |	1 |	±15	 |Three step | 	25.77847 |	0.93
8 |	1 |	±23	 |Exhaustive | 	32.8551 |	85.36
8 |	1 |	±23 |	Three step  |	25.46356 |	0.87

