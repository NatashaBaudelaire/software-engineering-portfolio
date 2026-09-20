# Artificial Intelligence and Machine Learning

Study notes for the AI and machine learning course module.

> **Status note.** This module contains practice exercises (not part of the
> original coursework) and a set of course notes. The hands-on work for the
> course itself is available under
> [Data Science Projects](../../data-science/README.md), which covers
> exploratory data analysis, visualization and preprocessing using Python and
> Jupyter notebooks (for example, `traffic_accident_severity_detection.ipynb`
> and `diabetes.ipynb`). Those notebooks form the practical foundation that
> machine learning builds on. This file documents the module roadmap and the
> concepts covered in class.

## Practice Exercises

Self-study activities in [exercises](../exercises/04-h5-image-classification/README.md)
and related folders under [exercises/](../exercises/), focused on loading,
inspecting and using trained Keras/TensorFlow models stored in the HDF5-based
`.h5` format. These are **not** historical university assignments; they were
created to complement the portfolio.

## Module Roadmap

1. Foundations: supervised and unsupervised learning, training/validation/test
   splits, model evaluation metrics (accuracy, precision, recall, F1-score).
2. Classical machine learning: linear/logistic regression, decision trees,
   ensemble methods (random forests, gradient boosting).
3. Neural networks and deep learning: feed-forward networks, convolutional
   neural networks (CNNs) for image tasks, sequence models (RNNs/LSTMs).
4. Practical workflows: data preparation, model training, tuning and
   deployment (MLOps).

## Notes

- The [preprocessing and EDA notebooks](../../data-science/README.md)
  demonstrate the data preparation step that feeds into any ML pipeline:
  handling missing values, scaling, encoding and visualization.
- Recommended Python stack for future ML work: `scikit-learn`, `pandas`,
  `numpy`, `matplotlib` and a framework such as TensorFlow or PyTorch.

## Resources

- [scikit-learn Documentation](https://scikit-learn.org/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [PyTorch Documentation](https://pytorch.org/docs/)