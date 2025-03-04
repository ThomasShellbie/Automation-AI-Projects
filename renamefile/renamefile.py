import os
import datetime

def rename_files_with_timestamp(directory_path):
    """
    Tự động đổi tên tất cả các file trong thư mục bằng cách thêm timestamp (Automatically rename all files in a directory by adding timestamp)
    """
    try:
        # Lấy danh sách tất cả file trong thư mục (Get a list of all files in a directory)
        files = os.listdir(directory_path)
        
        # Lấy thời gian hiện tại (Get current time)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Đếm số file đã đổi tên (count files renamed number)
        count = 0
        
        # Duyệt qua từng file (Browse through each file)
        for filename in files:
            # Tạo đường dẫn đầy đủ đến file (create path to file)
            old_path = os.path.join(directory_path, filename)
            
            # Chỉ xử lý file, không xử lý thư mục (Only process files, not folders)
            if os.path.isfile(old_path):
                # Lấy phần mở rộng của file (take the file extension)
                file_extension = os.path.splitext(filename)[1]
                
                # Tạo tên mới với timestamp (create new name with timestamp)
                new_filename = f"file_{timestamp}_{count}{file_extension}"
                new_path = os.path.join(directory_path, new_filename)
                
                # Đổi tên file (rename the files)
                os.rename(old_path, new_path)
                count += 1
                print(f"Đã đổi tên: {filename} -> {new_filename}")
        
        print(f"\nHoàn tất! Đã đổi tên {count} file.")
        
    except Exception as e:
        print(f"Đã xảy ra lỗi: {str(e)}")

def main():
    # Đường dẫn thư mục cần xử lý (Directory path to process)
    directory = input("Nhập đường dẫn thư mục (nhấn Enter để dùng thư mục hiện tại): ").strip()
    
    # Nếu không nhập, dùng thư mục hiện tại (If not entered, use current directory)
    if not directory:
        directory = os.getcwd()
    
    # Kiểm tra thư mục có tồn tại không (Check if directory exists)
    if not os.path.exists(directory):
        print("Thư mục không tồn tại!")
        return
    
    print(f"Đang xử lý thư mục: {directory}")
    rename_files_with_timestamp(directory)

if __name__ == "__main__":
    main()