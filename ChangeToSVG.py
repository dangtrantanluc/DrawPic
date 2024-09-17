import cv2
import numpy as np
import svgwrite

def image_to_svg(image_path, svg_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize image if necessary
    scale_percent = 50  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    
    # Use Canny edge detection
    edges = cv2.Canny(resized, threshold1=50, threshold2=150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create an SVG drawing
    dwg = svgwrite.Drawing(svg_path, profile='tiny', size=(width, height))
    
    # Add contours to the drawing
    for contour in contours:
        # Convert each contour to a polygon
        points = [(int(point[0][0]), int(point[0][1])) for point in contour]
        dwg.add(dwg.polygon(points, fill='none', stroke='black'))
    
    # Save the SVG file
    dwg.save()

# Path to the input image
image_path = "D:\\DangTranTanLuc\\python\\ronaldo7.jpg"
# Path to save the output SVG file
svg_path = "D:\\DangTranTanLuc\\python\\siu.svg"

# Convert the image to SVG
image_to_svg(image_path, svg_path)

# import cv2
# import svgwrite

# def image_to_svg(image_path, svg_path):
#     try:
#         # Load the image
#         image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
#         if image is None:
#             raise ValueError(f"Unable to load image from {image_path}")
        
#         # Resize image if necessary
#         scale_percent = 50  # percent of original size
#         width = int(image.shape[1] * scale_percent / 100)
#         height = int(image.shape[0] * scale_percent / 100)
#         dim = (width, height)
#         resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        
#         # Use Canny edge detection
#         edges = cv2.Canny(resized, threshold1=50, threshold2=150)
        
#         # Find contours
#         contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
#         # Create an SVG drawing
#         dwg = svgwrite.Drawing(svg_path, profile='tiny', size=(width, height))
        
#         # Add contours to the drawing
#         for contour in contours:
#             # Convert each contour to a polygon
#             points = [(int(point[0][0]), int(point[0][1])) for point in contour]
#             dwg.add(dwg.polygon(points, fill='none', stroke='black'))
        
#         # Save the SVG file
#         dwg.save()
#         print(f"SVG file saved successfully to {svg_path}")
        
#     except Exception as e:
#         print(f"Error: {str(e)}")

# # Path to the input image
# image_path = r"D:\\DangTranTanLuc\\python\\ronaldo7.jpg"
# # Path to save the output SVG file
# svg_path = r"D:\\DangTranTanLuc\\python\\siu.svg"

# # Convert the image to SVG
# image_to_svg(image_path, svg_path)
