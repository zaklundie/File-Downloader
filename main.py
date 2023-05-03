import os
import requests
from tqdm import tqdm

# get the path to the Downloads folder
downloads_folder = os.path.expanduser('~/Downloads')

# prompt the user for the URL and the number of pages to download
url = input("Enter the URL of the first file: ")
file_type = url.split('.')[-1]
num_pages = int(input("Enter the number of pages to download: "))

# create a tqdm progress bar with the specified number of iterations
progress_bar = tqdm(total=num_pages)

# loop through page numbers
for i in range(1, num_pages+1):
    # generate the URL for the current page
    current_url = url.replace('.'+file_type, '-{}.{}'.format(str(i).zfill(3), file_type))

    # make a request to the current URL
    response = requests.get(current_url)

    # save the file to the Downloads folder
    file_name = f'file_{str(i).zfill(3)}.{file_type}'
    file_path = os.path.join(downloads_folder, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    # update the progress bar
    progress_bar.update(1)

print('All files downloaded successfully!')
