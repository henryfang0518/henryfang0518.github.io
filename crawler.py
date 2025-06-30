import requests
# import json
from dotenv import load_dotenv
import os

# 載入 .env 檔案中的環境變數
load_dotenv()
# 從環境變數中讀取 Instagram Graph API 的 access token
access_token = os.getenv('ACCESS_TOKEN')
print(access_token)
user_id = '9832554246856561'
url = 'https://graph.instagram.com/v23.0/'+ user_id +'/media?access_token=' + access_token
print(url)
response = requests.get(url)

# 如果程式狀態回應是200，​那回應將會解析成json格式的數據，存在變數data中
if response.status_code == 200:
    data = response.json()
    #json.dumps將程式作用的對象(像是 字典、列表)進行格式化輸出
    # formatted_data = json.dumps(data, indent=4, sort_keys=True)
    postidList = [item.get('id') for item in data.get('data')]
 
    
# 如果不是狀態回應不是200，則印出狀態碼
else:
    print("壞了，根本就不能用啊，ERROR CODE:",response.status_code)

# 印出來​
print(postidList)
print(type(postidList))


# url2 = 'https://graph.instagram.com/v23.0/'+ postidList[0] +'?fields=caption,media_type,timestamp&access_token=' + access_token
# response2 = requests.get(url2)
# if response2.status_code == 200:
#     data2 = response2.json()
#     #json.dumps將程式作用的對象(像是 字典、列表)進行格式化輸出
#     # formatted_data = json.dumps(data, indent=4, sort_keys=True)
#     post = (data2.get('caption'), data2.get('media_type'), data2.get('timestamp'))
 
    
# # 如果不是狀態回應不是200，則印出狀態碼
# else:
#     print("壞了，根本就不能用啊，ERROR CODE:",response2.status_code)

# # 印出來​
# print(post)
# print(type(post))


# url3 = 'https://graph.instagram.com/v23.0/'+ postidList[0] +'/children?access_token=' + access_token

# response3 = requests.get(url3)

# # 如果程式狀態回應是200，​那回應將會解析成json格式的數據，存在變數data中
# if response3.status_code == 200:
#     data3 = response3.json()
#     #json.dumps將程式作用的對象(像是 字典、列表)進行格式化輸出
#     # formatted_data = json.dumps(data, indent=4, sort_keys=True)
#     photoIdList = [item.get('id') for item in data3.get('data')]
 
    
# # 如果不是狀態回應不是200，則印出狀態碼
# else:
#     print("壞了，根本就不能用啊，ERROR CODE:",response3.status_code)

# # 印出來​
# print(photoIdList)
# print(type(photoIdList))



# url4 = 'https://graph.instagram.com/v23.0/'+ photoIdList[0] +'?fields=media_type,media_url&access_token=' + access_token
# response4 = requests.get(url4)
# if response4.status_code == 200:
#     data4 = response4.json()
#     #json.dumps將程式作用的對象(像是 字典、列表)進行格式化輸出
#     # formatted_data = json.dumps(data, indent=4, sort_keys=True)
#     photo = (data4.get('media_url'), data4.get('media_type'))
 
    
# # 如果不是狀態回應不是200，則印出狀態碼
# else:
#     print("壞了，根本就不能用啊，ERROR CODE:",response4.status_code)

# 印出來​
# print(photo)
# print(type(photo))
# print('Hi, my name is', 'Henry')

def getPhoto(photoId):
    getPhotoUrl = 'https://graph.instagram.com/v23.0/'+ photoId +'?fields=media_type,media_url&access_token=' + access_token
    photoResponse = requests.get(getPhotoUrl)
    if photoResponse.status_code == 200:
        photo = photoResponse.json()
        return photo.get('media_url')

for postid in postidList:
    getPostUrl = 'https://graph.instagram.com/v23.0/'+ postid +'?fields=caption,media_type,timestamp&access_token=' + access_token
    getAlbumUrl = 'https://graph.instagram.com/v23.0/'+ postid +'/children?access_token=' + access_token
    postResponse = requests.get(getPostUrl)
    albumResponse = requests.get(getAlbumUrl)
    if postResponse.status_code == 200:
        post = postResponse.json()
        album = albumResponse.json()
        photoList = [getPhoto(item.get('id')) for item in album.get('data')]
        
        # path = 'src/content/posts/'+ postid +'.md'
        # f = open(path, 'w', encoding='utf-8')
        # f.write('---\n')
        # f.write('title: My First Blog Post\n')
        # f.write('published: '+ post.get('timestamp') +'\n')
        # f.write('description: This is the first post from crawler.\n')
        # f.write('category: Blog\n')
        # f.write('tags: [Foo, Bar]\n')
        # f.write('draft: false\n')
        # f.write('---\n')
        # f.write(post.get('caption')+'\n')
        # for photo in photoList:
        #     f.write('\n![image]('+ photo +')\n')
        # f.close()
        print(postid)
    else:
        print("壞了，根本就不能用啊，ERROR CODE:",postResponse.status_code)




