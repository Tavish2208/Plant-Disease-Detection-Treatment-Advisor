import torch
from torchvision import transforms
from PIL import Image
from .model import CNN_NeuralNet
from .utils import class_labels, treatment_suggestions

device = torch.device('cpu')
model = CNN_NeuralNet(3, len(class_labels))
model.load_state_dict(torch.load("models/plant_disease_model.pth", map_location=device))
model.eval()

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

def predict_disease(image_bytes):
    image = Image.open(image_bytes).convert('RGB')
    tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(tensor)
        _, predicted = torch.max(outputs, 1)

    prediction = class_labels[predicted.item()]
    treatment = treatment_suggestions.get(prediction, "No treatment available.")
    return prediction, treatment