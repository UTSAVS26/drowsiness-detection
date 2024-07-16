# 🚗😴 Drowsiness Detection Project

---

This project aims to develop various approaches for drowsiness detection using machine learning and deep learning techniques. The goal is to create a robust system that can accurately identify signs of drowsiness using images, with plans to extend to video footage and sensor data in the future.

---

## 📁 Project Structure

```
drowsiness-detection/
├── data/                       # 🗂️ Dataset and data management with DVC
│   ├── drowsiness/             # 📁 Original dataset directory
│   ├── processed/              # 🧹 Preprocessed data
│   └── data.yaml               # 📜 Data configuration file
├── models/                     # 🧠 Saved models
├── notebooks/                  # 📓 Jupyter notebooks for experimentation
├── src/                        # 📂 Source code
│   ├── data_preprocessing/     # 🧪 Data preprocessing scripts
│   ├── basic_ml/               # 📊 Basic ML algorithms
│   ├── deep_learning/          # 🤖 Deep learning models
│   ├── reinforcement_learning/ # 🎮 Reinforcement learning approaches
│   └── transfer_learning/      # 🚀 Transfer learning models
├── tests/                      # 🧪 Test scripts and data
├── .github/                    # 🛠️ GitHub workflows
│   ├── workflows/              # 📝 GitHub Actions workflows
│   │   ├── cml_train.yml       # 🚀 CML GitHub Action for training
├── .dvc/                       # ⚙️ DVC configuration
├── .gitignore                  # 🙈 Git ignore file
├── dvc.yaml                    # 📝 DVC pipeline configuration
├── params.yaml                 # 📐 Parameters for training
├── requirements.txt            # 📦 Python dependencies
└── README.md                   # 📄 Project documentation
```

---

## 🚀 Getting Started

### 🛠️ Prerequisites

- 🐍 Python 3.8+
- 🗃️ Git
- 💾 DVC
- 🖥️ GitHub account

### 🔧 Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/drowsiness-detection.git
   cd drowsiness-detection
   ```

2. **Install Python dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up DVC:**

   ```sh
   dvc init
   ```

4. **Pull data from DVC remote:**

   ```sh
   dvc pull
   ```

---

## 📊 Dataset

The dataset is organized into training, validation, and test sets, with subdirectories for 'Active' and 'Fatigue' states.

```
|- drowsiness
  |- test
    |- Active
    |- Fatigue
  |- train
    |- Active
    |- Fatigue
  |- val
    |- Active
    |- Fatigue
```

---

## 🧪 Data Preprocessing

Data preprocessing scripts are located in `src/data_preprocessing/`. Run the preprocessing step using DVC:

```sh
dvc repro preprocess
```

---

## 🏋️‍♂️ Training

### 🧩 Basic ML

Scripts for basic machine learning algorithms are located in `src/basic_ml/`. To train a basic ML model:

```sh
dvc repro train-basic-ml
```

### 🤖 Deep Learning

Deep learning models are implemented in `src/deep_learning/`. To train a deep learning model:

```sh
dvc repro train-deep-learning
```

### 🏆 Reinforcement Learning

Reinforcement learning approaches are in `src/reinforcement_learning/`. To train a reinforcement learning model:

```sh
dvc repro train-reinforcement-learning
```

### 🚀 Transfer Learning

Transfer learning models are in `src/transfer_learning/`. To train a transfer learning model:

```sh
dvc repro train-transfer-learning
```

---

## ⚙️ Parameters

Training parameters are specified in `params.yaml`:

```yaml
train:
  epochs: 10
  batch_size: 32
  learning_rate: 0.001
```

---

## 🌐 Continuous Machine Learning (CML)

The project uses GitHub Actions and CML for continuous integration and deployment. The workflow file is located in `.github/workflows/cml_train.yml`.

### 🤖 GitHub Actions Workflow (`.github/workflows/cml_train.yml`)

```yaml
name: CML Training

on: [push, pull_request]

jobs:
  train:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Setup DVC
      run: pip install dvc[all]

    - name: Pull data from DVC
      run: dvc pull

    - name: Train model
      run: |
        python src/<your_training_script>.py

    - name: Push data to DVC
      run: |
        dvc add models/
        dvc push
        git add models.dvc
        git commit -m "Trained model"
        git push
```

---

## 🚀 Usage

1. **Preprocess the data:**

   ```sh
   dvc repro preprocess
   ```

2. **Train the model:**

   ```sh
   dvc repro train
   ```

3. **Push data to DVC:**

   ```sh
   dvc push
   ```
   
---

## 🤝 Contributing

We welcome contributions! Please read our [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For any questions or suggestions, please contact us at [utsavsinghal26@gmail.com](mailto:utsavsinghal26@gmail.com).

---
