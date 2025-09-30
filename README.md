# Deep Learning Model with CIFAR-10 Dataset, FastAPI and Client (Express)
This project is a better version of the EXPOTEC presentation at my university. FastAPI helps provide customer service, a big difference from the presentation that day. It was a good experience in my career.

### Prerequisites
To run this project is necessary:
 - **Python** : Programming Language, version 3.10.0.
 - **Node.js** : The software for initializing JS files on a server.
 - **node_modules** : Installed in the root of the project.
 - **Visual Studio Code** : IDE for compiling.
 - **virtualenv** :  Tool to create isolated Python environments.


### Installing
1. **Download and Import the Trained Model**
   - Click on the following link to view the template for download:  
      - [Deep Learning Trained Model](https://drive.google.com/drive/folders/1tdV7F4SxixymHosXs7g_cKSoghzT44HA?usp=sharing)  
   - Put the project_deep.h5 file into the model package.
2. **Install all Python modules in virtualenv**
   - Download virtualenv:  
      ```bash
      python -m pip install virtualenv
   - Create a virtual environment at the root of the project: 
      ```bash
      python -m venv .venv
   - Open CMD in Visual Studio, and download within the virtual environment: 
      ```bash
      python -m pip install -r requirements.txt
   - Run the FastAPi script (localed in the api package, fast-api-cifar10.py file): 
      ```bash
      uvicorn fast-api-cifar10:app --reload
3. **Install the necessary Node.js modules**
   - Initialize the project:  
      ```bash
      npm init -y
   - Install the required modules in the server package:
       ```bash
      npm install express axios multer
   - Run the client script (located in the client package, server.js file):
      ```bash
      node server.js
- (Optional) If you are interested in that project, you can see the first version located in the model package.
   - Model_Training.ipynb: First presentation of the code.
   - Model_Training.py: The script to generate the project_deep.h5 file.


## Usage
You can use this project as a learning tool or to familiarize yourself with this technology, especially for AI, in models like deep learning. Please do not use it for commercial gain.

## Acknowledgments
I created this and I am truly grateful for all the learning my teacher Pedro de Lima Salomon Benites taught me from the AI ​​course.
