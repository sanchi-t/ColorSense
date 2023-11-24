# ColorSense

ColorSense is an image processing application that allows users to upload an image, apply a segmentation algorithm based on k-means clustering, and customize the color of each segment using RGB values. The result is a transformed image with a unique and personalized look.

## Features

- **Image Upload**: Users can easily upload their images through the user-friendly interface.

- **K-Means Segmentation**: The application utilizes the k-means clustering algorithm to segment the uploaded image into a specified number of clusters.

- **Color Customization**: Users can interactively customize the color of each segment by entering RGB values.

- **Preview**: A real-time preview is provided to visualize the changes made to the image.

- **Dockerized**: The entire application is containerized using Docker, ensuring easy deployment and consistent behavior across different environments.

## Prerequisites

Before running ColorSense, ensure you have the following dependencies installed:

- Docker
- Docker Compose

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/colorsense.git
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

![Alt text](brave_MPUnUfwsGs.png)
![Alt text](brave_qZvbnggbQH.png)
![Alt text](brave_6gFIHJ2sLJ.png)
![Alt text](brave_2LO3VTzI9z.png)
![Alt text](brave_uSjozZkz1v.png)

## Contributing

If you want to contribute to ColorSense, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The ColorSense project is built using Flask, k-means clustering, and Docker.
- Special thanks to the open-source community for their contributions.

Feel free to customize this README according to your specific project details and needs.
