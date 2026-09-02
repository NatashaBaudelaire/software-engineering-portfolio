from dataset import load_data
from model import create_model


train_data, validation_data = load_data()

model = create_model()


model.fit(
    train_data,
    validation_data=validation_data,
    epochs=10
)


model.save(
    "models/cats_dogs_model.keras"
)


print("Training completed!")