# ColorSense

ColorSense is an image processing application that allows users to upload an image, apply a segmentation algorithm based on k-means clustering, and customize the color of each segment using RGB values. The result is a transformed image with a unique and personalized look.

## Features

- **Image Upload**: Users can easily upload their images through the user-friendly interface.

- **K-Means Segmentation**: The application utilizes the k-means clustering algorithm to segment the uploaded image into a specified number of clusters.

- **Color Customization**: Users can interactively customize the color of each segment by entering RGB values.

- **Preview**: A preview is provided to visualize the changes made to the image.

- **Dockerized**: The entire application is containerized using Docker, ensuring easy deployment and consistent behavior across different environments.
  
- **Kubernetes Provisioning**: For those interested in deploying the application on Kubernetes, instructions are provided in the [Kubernetes](#kubernetes) section.

## Prerequisites

Before running ColorSense, ensure you have the following dependencies installed:

- Docker
- Docker Compose

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/sanchi-t/ColorSense.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd colorsense
    ```

3. **Build and Run the Docker Containers:**

    ```bash
    docker-compose up --build
    ```

4. **Access the Application:**

    Open your web browser and go to [http://localhost:5000](http://localhost:5000) to use ColorSense.

## Kubernetes

If you are interested in deploying ColorSense on Kubernetes, follow the steps below:

1. **Apply Kubernetes Manifests:**

    ```bash
    cd kubernetes/
    ```

    ```bash
    kubectl apply -f kubernetes/
    ```

2. **Access the Application:**

    Once the pods are running, the application will be accessible. You can find the service details using:

    ```bash
    kubectl get svc colorsense-service
    ```

    Access the application using the provided `EXTERNAL-IP`.

## Usage

1. **Segmentation:**
   - Enter the number of segments for k-means clustering.
   
2. **Upload Image:**
   - Click on the "Upload" button to select and upload an image.


3. **Color Customization:**
   - For each segment, enter RGB values to customize the color.
   - Changes will be reflected after you click on detect object button.

4. **Save or Download:**
   - Once satisfied with the customization, save or download the transformed image by right-clicking it.

## Images

![brave_MPUnUfwsGs](https://github.com/sanchi-t/ColorSense/assets/98596642/05627854-6645-46e2-94eb-2fe94d68e3a2)
![brave_qZvbnggbQH](https://github.com/sanchi-t/ColorSense/assets/98596642/3ac03c4e-34dc-43d8-8a17-bff6c0988522)
![brave_6gFIHJ2sLJ](https://github.com/sanchi-t/ColorSense/assets/98596642/da9121f4-537e-4868-a08a-be9008345572)
![brave_2LO3VTzI9z](https://github.com/sanchi-t/ColorSense/assets/98596642/60e99281-4923-4f18-9c50-0881744e011b)
![brave_uSjozZkz1v](https://github.com/sanchi-t/ColorSense/assets/98596642/6c9052b4-9af3-4d0f-982f-a60f3723798c)


## Contributing

If you want to contribute to ColorSense, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.


## Acknowledgments

- The ColorSense project is built using Flask, k-means clustering, and Docker.

Feel free to customize this README according to your specific project details and needs.
