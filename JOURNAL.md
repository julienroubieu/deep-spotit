# Project Journal

## 2020-03-20 Model 1

- Will attempt to detect cards, not symbols on them. This should make the problem simpler by identifying a single object instead of multiple ones.
- The common symbol between two cards will be extracted from our hardcoded CSV file.
- Current available data: 1905 picture files, 300x200 px.
- No detection/cropping of the card in the image (but maybe this is too many pixels).
- Will use TensorFlow ImageGenerator to augment data.
- Working with a 70/15/15 train/dev/test distribution.
- Small CNN, to compensate big images.