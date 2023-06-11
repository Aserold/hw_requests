import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": file_path
        }
        headers = {
            "Authorization" : token
        }
        response_get = requests.get(url, headers=headers, params=params)

        upload_url = response_get.json().get('href', '')
        with open(file_path, 'rb') as f:
            response_put = requests.put(upload_url, files={'file': f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Screenshot_20221125_071145.png'
    token = 'OAuth '
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)