import turtle as tu
from svgpathtools import svg2paths2
from svg.path import parse_path

# Đường dẫn đến tệp SVG của bạn
svg_file_path = 'D:\\DangTranTanLuc\\python\\quocky.svg'

# Hàm để vẽ từng đường dẫn từ tệp SVG lên màn hình
def draw_svg_file(file_path):
    try:
        # Tải và phân tích cú pháp tệp SVG
        paths, attributes, svg_attributes = svg2paths2(file_path)

        # Thiết lập turtle
        tu.speed(0)
        tu.penup()

        # Vẽ từng đường dẫn
        for attr in attributes:
            if 'd' in attr:
                path = parse_path(attr['d'])

                # Di chuyển đến điểm bắt đầu của đường dẫn
                start_point = path.point(0)
                tu.goto(start_point.real, -start_point.imag)
                tu.pendown()

                # Vẽ đường dẫn
                for i in range(1, 101):  # Chia đường dẫn thành 100 đoạn
                    point = path.point(i / 100)
                    tu.goto(point.real, -point.imag)

                tu.penup()

        # Hoàn thành
        tu.done()

    except Exception as e:
        print(f"Lỗi khi đọc và vẽ tệp SVG: {str(e)}")

# Gọi hàm để vẽ tệp SVG
if __name__ == "__main__":
    draw_svg_file(svg_file_path)
