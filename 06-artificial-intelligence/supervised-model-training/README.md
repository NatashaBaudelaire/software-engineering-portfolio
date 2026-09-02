# Supervised Model Training Projects

This directory contains supervised learning projects using various neural network architectures for different classification and prediction tasks.

## Projects

### Cats vs Dogs Classification
Image classification project using convolutional neural networks (CNN) to classify images of cats and dogs.

**Files:**
- `dataset.py`: Dataset loading and preprocessing
- `model.py`: CNN model architecture
- `train.py`: Training script
- `cat_and_dogs.h5`: Trained model weights

### Code Autocomplete LSTM
Code completion system using Long Short-Term Memory (LSTM) networks for predicting code completions.

**Files:**
- `dataset.py`: Code dataset preparation and tokenization
- `model.py`: LSTM model architecture
- `train.py`: Training script with data collection
- `predict.py`: Inference script for code completion

### Image Classifier CNN
General image classification using convolutional neural networks for multi-class image classification.

**Files:**
- `dataset.py`: Image dataset loading
- `model.py`: CNN model architecture
- `train.py`: Training script
- `predict.py`: Prediction script for new images

## Prerequisites

- Python 3.7+
- TensorFlow/Keras
- NumPy
- Matplotlib
- Pillow (for image processing)

## How to Use

### Training a Model

```bash
# Navigate to the specific project directory
cd cats-vs-dogs-classifier

# Train the model
python train.py
```

### Making Predictions

```bash
# For image classification
python predict.py --image path/to/image.jpg

# For code autocomplete
python predict.py --code "def my_function"
```

## Model Files

- `.h5` files contain trained model weights
- Models can be loaded using `tf.keras.models.load_model()`
- Ensure you have the same model architecture when loading weights

## Dataset Requirements

- Images should be organized in subdirectories by class
- Code files should be plain text `.py` files
- Ensure datasets are properly split into train/validation/test sets

## Performance Tips

- Use GPU acceleration for faster training
- Adjust batch size based on available memory
- Monitor training/validation loss to prevent overfitting
- Use data augmentation for image classification tasks
