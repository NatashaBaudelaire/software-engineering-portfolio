# Artificial Intelligence and Machine Learning

This directory contains artificial intelligence and machine learning projects covering supervised learning, neural networks, and practical applications. These projects were completed as part of my learning journey in AI/ML development.

## Directory Structure

### 📁 supervised-model-training
Supervised learning projects using various neural network architectures.

#### cats-vs-dogs-classification
Image classification project using convolutional neural networks (CNN) to classify images of cats and dogs.

**Content:**
- CNN architecture design
- Image preprocessing and augmentation
- Model training and validation
- Performance evaluation
- Prediction implementation

#### code-autocomplete-lstm
Code completion system using Long Short-Term Memory (LSTM) networks.

**Content:**
- LSTM network architecture
- Text preprocessing for code
- Sequence modeling
- Training on code datasets
- Autocomplete prediction generation

#### image-classifier-cnn
General image classification using convolutional neural networks.

**Content:**
- CNN model architecture
- Multi-class image classification
- Data augmentation techniques
- Transfer learning implementation
- Model optimization

## Learning Objectives

These projects cover fundamental AI/ML concepts:

- **Supervised Learning**: Training models with labeled data
- **Neural Networks**: Understanding neural network architectures
- **Deep Learning**: Implementing deep learning models
- **Image Processing**: Computer vision techniques
- **Sequence Modeling**: Handling sequential data
- **Model Evaluation**: Performance metrics and validation
- **Transfer Learning**: Using pre-trained models
- **Data Augmentation**: Expanding training datasets

## Prerequisites

- Python 3.7 or higher
- GPU (recommended for deep learning)
- Deep learning frameworks (TensorFlow, PyTorch, or Keras)
- Data science libraries (pandas, numpy, matplotlib)

### Required Packages

```bash
# Install deep learning framework
pip install tensorflow

# Or for PyTorch
pip install torch torchvision

# Install data science libraries
pip install pandas numpy matplotlib seaborn scikit-learn

# Install image processing libraries
pip install pillow opencv-python

# Install Jupyter for notebook support
pip install jupyter notebook
```

## How to Use

### Setting Up the Environment

```bash
# Navigate to the project directory
cd supervised-model-training

# Create a virtual environment (recommended)
python -m venv ai_env

# Activate the virtual environment
# On Windows:
ai_env\Scripts\activate
# On macOS/Linux:
source ai_env/bin/activate

# Install required packages
pip install -r requirements.txt
```

### Running the Projects

#### Cats vs Dogs Classification

```bash
# Navigate to the project directory
cd cats-vs-dogs-classification

# Open Jupyter Notebook
jupyter notebook

# Open the training notebook and run cells sequentially
# Or run the training script directly
python train_model.py
```

#### Code Autocomplete LSTM

```bash
# Navigate to the project directory
cd code-autocomplete-lstm

# Prepare the code dataset
python prepare_data.py

# Train the LSTM model
python train_lstm.py

# Test the autocomplete
python test_autocomplete.py
```

#### Image Classifier CNN

```bash
# Navigate to the project directory
cd image-classifier-cnn

# Train the CNN model
python train_cnn.py

# Evaluate the model
python evaluate_model.py

# Make predictions on new images
python predict.py --image path/to/image.jpg
```

## Project Details

### Cats vs Dogs Classification
- **Architecture**: Convolutional Neural Network (CNN)
- **Input**: Image data (resized to fixed dimensions)
- **Output**: Binary classification (cat/dog)
- **Techniques**: Data augmentation, dropout, batch normalization
- **Evaluation**: Accuracy, loss curves, confusion matrix

### Code Autocomplete LSTM
- **Architecture**: Long Short-Term Memory (LSTM) network
- **Input**: Code sequences as text
- **Output**: Predicted next tokens/code
- **Techniques**: Tokenization, sequence padding, embedding
- **Evaluation**: Perplexity, prediction accuracy

### Image Classifier CNN
- **Architecture**: Convolutional Neural Network (CNN)
- **Input**: Image data for multiple classes
- **Output**: Multi-class classification
- **Techniques**: Transfer learning, data augmentation, fine-tuning
- **Evaluation**: Accuracy, precision, recall, F1-score

## Model Training Best Practices

- **Data Splitting**: Use train/validation/test splits
- **Data Augmentation**: Apply transformations to increase dataset diversity
- **Early Stopping**: Monitor validation loss to prevent overfitting
- **Learning Rate Scheduling**: Adjust learning rate during training
- **Model Checkpointing**: Save best models during training
- **Batch Processing**: Use appropriate batch sizes for your hardware

## Common Issues

### GPU Memory Issues
- Reduce batch size
- Use gradient accumulation
- Enable mixed precision training
- Clear GPU cache between runs

### Overfitting
- Increase training data
- Apply data augmentation
- Use dropout layers
- Implement early stopping
- Regularize the model

### Training Convergence
- Adjust learning rate
- Change optimizer
- Modify network architecture
- Check data quality
- Normalize input data

## Performance Optimization

- **Batch Size**: Experiment with different batch sizes
- **Learning Rate**: Use learning rate schedulers
- **Model Architecture**: Balance complexity and performance
- **Data Loading**: Use efficient data loaders
- **Mixed Precision**: Use FP16 for faster training

## Next Steps

After completing these projects, consider:
- Exploring unsupervised learning techniques
- Learning about reinforcement learning
- Studying natural language processing (NLP)
- Understanding generative models (GANs, VAEs)
- Exploring model deployment and serving
- Learning about MLOps and model lifecycle management

## Resources

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Keras Documentation](https://keras.io/)
- [Deep Learning Book](https://www.deeplearningbook.org/)
- [Coursera Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
