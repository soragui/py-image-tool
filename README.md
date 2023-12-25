
> Image composition tools using Python

## Start
Install pip:
```bash
pip install -r requirements.txt
```

## Example

#### Compose image horizontally:
```python
composite_images(image_paths, horizon_compose, margin=10, padding=10, direction='horizontal')
```

Result:
![horizon_img](images/horizon_compose.jpg)

#### Compose image vertically:
```python
composite_images(image_paths, vertica_compose, margin=10, padding=10, direction='vertical')
```

Result:

![vertica_img](images/vertica_compose.jpg)

## Usage
|params||
|---|----|
|image_list|List of image to compose|
|output_image|Image Path for compose result|
|margin|Image Margin|
|padding|Image Padding|
|alignment|Left or Center|
|direction|Compose direction Vertical or Horizon|